from flask import Flask
from flask import render_template
from flask import request, redirect, url_for
import question, score

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/start')
def init():
    return redirect(url_for('questions', number=1, url_score=score.initSocre()))


@app.route('/questions', methods=['GET'])
def questions():
    question_number = request.args.get("number")
    url_score = request.args.get("url_score")
    return render_template("form.html", temple_dict=question.temple_dict[question_number], url_score=url_score)


@app.route('/answer', methods=['POST'])
def answer():
    questions_answer = request.form['answer']
    url_score = request.form["url_score"]
    question_id = request.form['id']
    new_questions_id = str(int(question_id) + 1)
    new_score = addScore(question_id, questions_answer, url_score)
    if int(new_questions_id) <= 5:
        return redirect(url_for('questions', number=new_questions_id, url_score=new_score))
    elif int(new_questions_id) == 6:
        curr_score = getScoreDict(new_score)
        func_with_lowest_score = getLowestScoreFunc(curr_score)
        if ('MD5' in func_with_lowest_score) or ('SHA1' in func_with_lowest_score):
            new_questions_id = '7'
        return redirect(url_for('questions', number=new_questions_id, url_score=new_score))
    return redirect(url_for("result", result_score = new_score, output_len=questions_answer))


@app.route('/result')
def result():
    result_score = request.args.get("result_score")
    output_len = request.args.get("output_len")
    score_rank = getScoreDict(result_score)
    chosen_func = []
    highest_score = score_rank[1]['score']
    for i in score_rank:
        if score_rank[i]['score'] == highest_score:
            chosen_func.append(score_rank[i]['func'])
    if (len(chosen_func) >= 2) and ('MD5' in chosen_func):
        chosen_func.remove('MD5')
    if (len(chosen_func) >= 2) and ('SHA1' in chosen_func):
        chosen_func.remove('SHA1')
    if 'MD5' in chosen_func:
        output_len = 128
    if 'SHA1' in chosen_func:
        output_len = 160
    return render_template("result.html", score_rank=score_rank, output_len=output_len, chosen_func=chosen_func)

def getScoreDict(score):
    res = {}
    s = score.split('-')
    unsorted_res = (('MD5',s[0]), ('SHA1',s[1]), ('SHA2',s[2]), ('SHA3',s[3]), ('BLAKE2',s[4]))
    sorted_res = sorted(unsorted_res, key=lambda x:int(x[1]), reverse=True)
    for i in range(len(sorted_res)):
        res[i+1] = {'func':sorted_res[i][0],'score':sorted_res[i][1]}
    return res

def getLowestScoreFunc(score):
    func = []
    lowest_score = score[len(score)]['score']
    for key, val in score.items():
        if val['score'] == lowest_score:
            func.append(val['func'])
    print(func)
    return func

def addScore(question_id, question_answer, url_score):
    return score.addScore(url_score, question.temple_dict[question_id][question_answer])


if __name__ == '__main__':
    app.run()

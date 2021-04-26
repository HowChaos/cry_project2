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
    new_score = addScore(question_id, questions_answer, url_score)
    new_questions_id = str(int(question_id) + 1)
    if int(new_questions_id) <= 5:
        return redirect(url_for('questions', number=new_questions_id, url_score=new_score))
    #elif int(new_questions_id) == 6:
    return redirect(url_for("result", result_score = new_score))


@app.route('/result')
def result():
    result_score = request.args.get("result_score")
    print(result_score)
    return "your final score is " + result_score + " but the suggestion should waiting for 400 years to return"



def addScore(question_id, question_answer, url_score):
    return score.addScore(url_score, question.temple_dict[question_id][question_answer])


if __name__ == '__main__':
    app.run()

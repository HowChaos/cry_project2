from flask import Flask
from flask import render_template
from flask import request, redirect
import question

app = Flask(__name__)


@app.route('/hello')
def hello_world():
    return "hello world"


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/questions', methods=['GET'])
def questions():
    question_number = request.args.get("number")
    return render_template("form.html", temple_dict=question.temple_dict[question_number])


@app.route('/answer', methods=['POST'])
def answer():
    questions_answer = request.form['answer']
    questions_id = str(int(request.form['id']) + 1)
    if questions_answer == 'B':
        return redirect('/questions?number='+questions_id)
    else:
        return "your answer is " + questions_answer + ",which is totally wrong!"


if __name__ == '__main__':
    app.run()

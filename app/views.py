from app import app

from flask import render_template, request, redirect, url_for

import uuid
import json

try:
    with open("records.json", "r") as infile:
        records = json.load(infile)

        # Store the data in a list variable
        records = list(records)
except:
    records = []

data = {}

questions = [
    "What is the name of your store?",
    "What is the balance left on your gift card?",
    "What price are you selling at?",
    "Which network would you like to receive funds at?",
    "What address do you want to receive funds at?",
    "What’s your email address?"
]

@app.route('/', methods=['GET', 'POST'])
def index():

    if request.method == 'GET':
        question_index = 0
        # Display the first question
        return render_template('survey.html', question=questions[0], question_index=question_index, questions=questions)
    
    elif request.method == 'POST':
        # Display the other questions
        answer = request.form['answer']
        question_index = int(request.form['question_index'])
        data[question_index] = answer
    
        if 'previous' in request.form and question_index > 0:
            prev_question = questions[question_index - 1]
            return render_template('survey.html', question=prev_question, question_index=question_index - 1, questions=questions)
        
        elif question_index < len(questions) - 1:
            next_question = questions[question_index + 1]
            return render_template('survey.html', question=next_question, question_index=question_index + 1, questions=questions)
        
        else:
            # Generating a unique ID for the record
            answer_id = str(uuid.uuid4())
            # Store the answers in a dictionary with the ID as the key
            data['id'] = answer_id
            records.append(dict(data))

            with open("records.json", "w") as outfile:
                json.dump(records, outfile)
    
            return render_template('summary.html')

@app.route('/results')
def results():
    try:
        with open("records.json", "r") as infile:
            records = json.load(infile)
            
    except:
        return '<p> No data available </p>'
    return render_template('results.html', records=records)

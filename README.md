# MoodlePy

Perfeito — vamos torná-lo mais leve e direto, mas ainda profissional.

---

# Moodle Quiz Helper 📝

## What is this?

This is a uniproject developed in Python to make creating quizzes in Moodle a lot less painful.

Instead of manually adding questions one by one through the Moodle interface, this tool:

* Reads questions from a CSV file
* Automatically fills in the Moodle form fields
* Sends the POST request to create the questions

Simple as that.

## Why?

If you’ve ever created a big quiz in Moodle, you know it’s repetitive and time-consuming. This project was built to:

* Save time
* Avoid copy-paste mistakes
* Upload multiple questions at once

## How it works

1. You prepare a CSV file with your questions.
2. The script reads and processes the file.
3. It fills in the required form inputs automatically.
4. It submits the form to Moodle.

No manual clicking required.

## CSV Structure

Each row in the CSV represents one question.

Typical fields include:

* Question name
* Question text
* Answer options
* Correct answer
* Feedback (optional)
* Question type

(Adjust this section to match your actual format.)

## Requirements

* Python 3
* Required libraries (e.g., `requests`)
* Access to a Moodle account with permission to create questions

## How to use

1. Prepare your CSV file.
2. Configure the Moodle URL and login details in the script.
3. Run the script.
4. Let it do the boring part for you.

## Notes

* If Moodle’s form structure changes, the script may need adjustments.
* This was developed for academic purposes.

---

Se quiseres, posso torná-lo ainda mais informal — ou mais técnico — dependendo do tipo de professor que tens.

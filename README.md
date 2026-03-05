# MoodlePy

MoodlePy is a small Python tool that converts quiz questions stored in a CSV file into a **Moodle-compatible XML quiz file**.

Instead of manually creating questions through the Moodle interface, you can prepare them in a spreadsheet and generate the XML file that Moodle can import directly.

## Why?

Creating quizzes directly in Moodle can be slow and repetitive, especially when dealing with many questions.

This project was built to:

* Create multiple Moodle questions quickly
* Avoid manual input errors
* Allow quizzes to be prepared using spreadsheets
* Generate a Moodle XML file automatically

## How it works

1. Questions are written in a CSV file.
2. The script reads and groups rows that belong to the same question.
3. It converts the data into the correct Moodle XML structure.
4. The resulting XML file can be imported into Moodle.

## CSV Structure

Each row in the CSV represents **one answer option** of a question.

Example:

```
id;type;dificultity;category;questiontext;answer;fraction
Q1;multichoice;facil;Funcoes;O que faz criar_ficheiro()?;Cria ficheiro;100
Q1;multichoice;facil;Funcoes;O que faz criar_ficheiro()?;Lê ficheiro;0
Q1;multichoice;facil;Funcoes;O que faz criar_ficheiro()?;Apaga ficheiro;0
Q2;truefalse;facil;Funcoes;A função open() pode criar ficheiro.;true;100
Q2;truefalse;facil;Funcoes;A função open() pode criar ficheiro.;false;-25
```

Fields:

* **id** – question identifier (used to group answers)
* **type** – question type (`multichoice`, `truefalse`, etc.)
* **difficulty** – question difficulty level
* **category** – Moodle category
* **questiontext** – text of the question
* **answer** – answer option
* **fraction** – score percentage for the answer

## Requirements

* Python 3
* Standard Python libraries (`csv`, `xml.etree.ElementTree`)

No external dependencies are required.

## How to use

1. Prepare a CSV file with your questions.
2. Place it in the project directory.
3. Run the script.

The program will generate a **Moodle-compatible XML file** containing the quiz questions.

This file can then be imported through Moodle's **Quiz → Import → Moodle XML format** option.

## Notes

* The CSV must follow the expected structure.
* Questions are grouped using the `id` field.
* This project was developed as a university assignment.

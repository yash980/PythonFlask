import re
from wtforms import SubmitField
from random import randint, choice
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def welcome_page():
    return render_template("start_page.html")


@app.route("/generate", methods=['POST', 'GET'])
def password_generator():
    if request.method == 'POST':
        raw_file = open("raw_text", 'r')
        read_file = raw_file.readlines()

        symbols = ['!', '@', '#', '$', '%', '&', '_']

        single_word = read_file[randint(0, 466543)]

        cleaned_word = single_word.strip("\n")

        rules = re.compile('\w+')
        final_word = rules.findall(cleaned_word.title())

        password = [str(randint(0, 99)), choice(symbols), "".join(final_word), str(randint(0, 999))]

        raw_file.close()

        final_password = "".join(set(password))
        generate_password = SubmitField("Generate Password")
        return render_template("generate.html", password=final_password)


if __name__ == "__main__":
    app.run(debug=True)

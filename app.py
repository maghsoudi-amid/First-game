
from flask import Flask, request, render_template_string
import random

app = Flask(__name__)
number = random.randint(1, 100)

@app.route('/', methods=['GET', 'POST'])
def guess():
    message = ''
    if request.method == 'POST':
        try:
            guess = int(request.form['guess'])
            if guess < number:
                message = 'برو بالاتر!'
            elif guess > number:
                message = 'بیا پایین‌تر!'
            else:
                message = 'آفرین! درست حدس زدی.'
        except ValueError:
            message = 'عدد معتبر وارد کن!'
    return render_template_string('''
        <h1>بازی حدس عدد</h1>
        <form method="post">
            <input name="guess" type="number" />
            <input type="submit" value="حدس بزن" />
        </form>
        <p>{{message}}</p>
    ''', message=message)

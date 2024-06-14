Python

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
  if request.method == 'POST':
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']

    # Перевірте дані форми
    if not name or not email or not message:
      return render_template('index.html', error='Будь ласка, заповніть всі поля.')

    # Обробіть дані форми
    # (Надішліть електронний лист, збережіть дані в базі даних тощо)

    return render_template('index.html', success='Ваше повідомлення успішно відправлено!')
  else:
    return render_template('index.html')

if __name__ == '__main__':
  app.run(debug=True)
from flask import Flask, render_template, request, redirect
import psycopg2

app = Flask(__name__)
conn = psycopg2.connect(database="service_db", user="postgres", password="1940", host="localhost", port="5432")

cursor = conn.cursor()


@app.route('/login/', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        if request.form.get('login'):
            username = request.form.get('username')
            password = request.form.get('password')

            if not username:
                return render_template('login.html', error="Логин не введён")
            if not password:
                return render_template('login.html', error="Пароль не введён")

            cursor.execute("SELECT * FROM service.users WHERE login=%s AND password=%s", (str(username), str(password)))
            records = list(cursor.fetchall())
            if not records:
                return render_template('login.html', error="Пользователя не существует")
            print(records)
            return render_template('account.html', full_name=records[0][1], login=username, password=password)

        elif request.form.get('registration'):
            return redirect('/registration/')
    return render_template('login.html')


@app.route('/registration/', methods=['POST', 'GET'])
def registration():
    if request.method == 'POST':
        name = request.form.get('name')
        log1n = request.form.get('login')
        password = request.form.get('password')
        if not name:
            return render_template('registration.html', error="Пожалуйста введите ФИ")
        if not log1n:
            return render_template('registration.html', error="Пожалуйста введите логин")
        if not password:
            return render_template('registration.html', error="Пожалуйста введите пароль")

        cursor.execute('INSERT INTO service.users(full_name, login, password) VALUES (%s, %s, %s);',
                       (str(name), str(log1n), str(password)))

        conn.commit()
        return redirect('/login/')
    return render_template('registration.html')


if __name__ == '__main__':
    app.run(debug=True)

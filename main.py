import requests
import json
from flask import Flask
from datetime import datetime  # Для получения текущей даты

def get_valutes_list():
    url = 'https://www.cbr-xml-daily.ru/daily_json.js'
    response = requests.get(url)
    data = json.loads(response.text)
    valutes = list(data['Valute'].values())
    return valutes

app = Flask(__name__)

def create_html(valutes):
    current_date = datetime.now().strftime("%Y-%m-%d")  # Форматирование текущей даты
    text = f'<h1>Курс валют</h1>'
    text += f'<h2>Дата обновления: {current_date}</h2>'  # Добавляем дату как подзаголовок
    text += '<table border="1">'
    text += '<tr>'
    for _ in valutes[0]:
        text += f'<th><th>'
    text += '</tr>'
    for valute in valutes:
        text += '<tr>'
        for v in valute.values():
            text += f'<td>{v}</td>'
        text += '</tr>'

    text += '</table>'
    return text

@app.route("/")
def index():
    valutes = get_valutes_list()
    html = create_html(valutes)
    return html

if __name__ == "__main__":
    app.run()

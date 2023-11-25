from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from PIL import Image, ImageDraw
import os
import random
import base64
from io import BytesIO
import pickle
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

app = Flask(__name__, static_folder='dist')
CORS(app, resources={r"/*": {"origins": "*"}}, methods=['GET', 'POST', 'DELETE', 'PUT', 'OPTIONS'])

@app.route('/home')
def home():
    return send_from_directory(app.static_folder, 'index.html')

# Функция для сохранения изображений на сервере (заменить на свою)
def image_to_base64(img):
    buffered = BytesIO()
    img.save(buffered, format="PNG")
    return base64.b64encode(buffered.getvalue()).decode()

@app.route('/analyse', methods=['POST'])
def analyse():
    # Получение параметров из запроса
    data = request.json

    city = data.get('city', '')  # название города, второй аргумент - значение по умолчанию
    area = float(data.get('area', 0)) # площадь помещения
    temperature = data.get('temperature', '') # температура
    inflation = float(data.get('inflation', 0)) # инфляция
    taxes = float(data.get('taxes', 0)) # налог на имущество
    expenses = float(data.get('expenses', 0)) # объем затрат

    # код
    with open('dataframe.pkl', 'rb') as file:
        pred_df = pickle.load(file)

        pred_df['Город'] = city
            
        pred_df['Общая площадь'] = area
        pred_df['Общая площадь здания '] = area
        pred_df['Занято службами Банка России'] = area/1.28
        pred_df['Сдается Банком России в аренду'] = area/151

        pred_df['Капремонт, тыс. руб. 2017'] -= expenses/7
        pred_df['Капремонт, тыс. руб.  2018'] -=  expenses/7
        pred_df['Капремонт, тыс. руб.  2019'] -=  expenses/7
        pred_df['Капремонт, тыс. руб.  2020'] -=  expenses/7
        pred_df['Капремонт, тыс. руб.  2021'] -=  expenses/7
        pred_df['Капремонт, тыс. руб.  2022'] -=  expenses/7
        pred_df['Капремонт, тыс. руб.  2023'] -=  expenses/7

        pred_df['Налог'] = taxes

        pred_df['Инфляция ЦБ РФ'] = inflation

        pred_df['Температура'] += temperature
        pred_df['Анадырь'] += temperature
        pred_df['Билибино'] += temperature
        pred_df['Биробиджан'] += temperature
        pred_df['Благовещенск'] += temperature
        pred_df['Владивосток'] += temperature
        pred_df['Вольно-Надеждинское'] += temperature
        pred_df['Горные ключи'] += temperature
        pred_df['Ключи'] += temperature
        pred_df['Комсомольск-на-Амуре'] += temperature
        pred_df['Ленск'] += temperature
        pred_df['Магадан'] += temperature
        pred_df['Находка'] += temperature
        pred_df['Паратунка'] += temperature
        pred_df['Петропавловск-Камчатский'] += temperature
        pred_df['Покровск'] += temperature
        pred_df['Тында'] += temperature
        pred_df['Уссурийск'] += temperature
        pred_df['Усть-Камчатск'] += temperature
        pred_df['Усть-Нера'] += temperature
        pred_df['Усть-Омчуг'] += temperature
        pred_df['Хабаровск'] += temperature
        pred_df['Чурапча'] += temperature
        pred_df['Южно-Сахалинск'] += temperature
        pred_df['Якутск'] += temperature

        with open('model_el.pkl', 'rb') as file:
            loaded_model = pickle.load(file)

        y_pred_el = loaded_model.predict(pred_df)

        result_el = {
            '2022':y_pred_el[0:11].sum(),
            '2023':y_pred_el[12:23].sum(),
            '2024':y_pred_el[24:35].sum()
        }


        with open('model_teplo.pkl', 'rb') as file:
            loaded_model = pickle.load(file)

        y_pred_teplo = loaded_model.predict(pred_df)

        result_teplo = {
            '2022':y_pred_teplo[0:11].sum(),
            '2023':y_pred_teplo[12:23].sum(),
            '2024':y_pred_teplo[24:35].sum()
        }

        with open('model_gaz.pkl', 'rb') as file:
            loaded_model = pickle.load(file)

        y_pred_gaz = loaded_model.predict(pred_df)

        result_gaz = {
            '2022':y_pred_gaz[0:11].sum(),
            '2023':y_pred_gaz[12:23].sum(),
            '2024':y_pred_gaz[24:35].sum()
        }

        with open('model_voda.pkl', 'rb') as file:
            loaded_model = pickle.load(file)

        y_pred_voda = loaded_model.predict(pred_df)

        result_voda = {
            '2022':y_pred_voda[0:11].sum(),
            '2023':y_pred_voda[12:23].sum(),
            '2024':y_pred_voda[24:35].sum()
        }

        dates = pd.date_range(start='2022-01-01', end='2024-12-01', freq='MS')

        # Суммирование платежей для всех услуг за каждый месяц
        total_payments = y_pred_el + y_pred_teplo + y_pred_gaz + y_pred_voda

        # Проверка, что количество дат совпадает с размером массивов
        if len(dates) == len(y_pred_el) == len(y_pred_teplo) == len(y_pred_gaz) == len(y_pred_voda):
            # Построение графиков
            plt.figure(figsize=(12, 6))
            plt.plot(dates, y_pred_el, label='Электричество')
            plt.plot(dates, y_pred_teplo, label='Тепло')
            plt.plot(dates, y_pred_gaz, label='Газ')
            plt.plot(dates, y_pred_voda, label='Вода')
            plt.plot(dates, total_payments, label='Сумма', color='black', linestyle='--')

            # Настройка графика
            plt.title('Платежи за коммунальные услуги')
            plt.xlabel('Дата')
            plt.ylabel('Платежи')
            plt.legend()
            plt.grid(True)
            plt.savefig('utility_payments.png')
            image = Image.open('utility_payments.png')
        else:
            print("Количество дат и элементов в массивах не совпадает.")

        # Возвращение результата и URL изображений
        result = {
            'result_el': result_el,
            'result_teplo': result_teplo,
            'result_gaz': result_gaz,
            'result_voda': result_voda
        }

        images = [image_to_base64(image)]

        response = jsonify({"result": result, "images": images})
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

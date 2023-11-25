from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from PIL import Image, ImageDraw
import os
import random
import base64
from io import BytesIO
import pickle
import pandas as pd

app = Flask(__name__, static_folder='dist')
CORS(app, resources={r"/*": {"origins": "*"}}, methods=['GET', 'POST', 'DELETE', 'PUT', 'OPTIONS'])

@app.route('/assets/<path:filename>')
def serve_static(filename):
    return send_from_directory('path_to_your_build_folder/assets', filename)

@app.route('/home')
def home():
    return send_from_directory(app.static_folder, 'index.html')

# Функция для сохранения изображений на сервере (заменить на свою)
def image_to_base64(img):
    buffered = BytesIO()
    img.save(buffered, format="PNG")
    return base64.b64encode(buffered.getvalue()).decode()

# Функция для генерации случайного изображения
def create_random_image():
    img = Image.new('RGB', (100, 100), color=(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
    draw = ImageDraw.Draw(img)
    draw.text((10, 10), "Random Image", fill=(255, 255, 255))
    return img

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
    dates = pd.date_range(start='2022-01-01', end='2024-12-01', freq='MS')
    with open('dataframe.pkl', 'rb') as file:
        pred_df = pickle.load(file)

    # Убедитесь, что в pred_df достаточно строк для заполнения датами
    if len(pred_df) <= len(dates):
        # Присваивание дат в 'Дата проведения'
        pred_df['Дата проведения'] = dates[:len(pred_df)]

        # Обновление 'month' и 'year' на основе 'Дата проведения'
        pred_df['month'] = pred_df['Дата проведения'].dt.month
        pred_df['year'] = pred_df['Дата проведения'].dt.year
    else:
        print("Недостаточно дат для заполнения всех строк в pred_df")

    # Показываем первые строки для проверки
    pred_df['Общая площадь'] = area
    # Загрузка модели из файла
    with open('model.pkl', 'rb') as file:
        loaded_model = pickle.load(file)
    # pred_df.head()
    y_pred = loaded_model.predict(pred_df)

    # Все вычисления - заменить на реальные
    result = {
        '2022':y_pred[0:11].sum(),
        '2023':y_pred[12:23].sum(),
        '2024':y_pred[24:35].sum()
    }

    # Генерация изображений - заменить на реальные
    images = [image_to_base64(create_random_image()) for _ in range(2)]

    # Возвращение результата и URL изображений
    # return jsonify({"result": result, "images": images})
    response = jsonify({"result": result, "images": images})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

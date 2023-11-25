Деплой проекта - [Ссылка](http://84.201.139.219:5000/home)

🌟 Косатка-Analytics представляет: 🚀

💼 Революционное решение для прогнозирования коммунальных платежей!

Наша команда разработала инновационный инструмент, способный предсказывать коммунальные платежи, учитывая объемы вложений в ремонт зданий и влияние внешних факторов, включая климат, инфляцию и налоги.

🧠 Многоуровневый аналитический подход:

1. Морфологический анализ текста: Мы используем передовые технологии для нормализации каждого слова, что позволяет нам формировать единую и точную базу данных для последующего анализа.

2. Семантический анализ описаний ремонтных работ: Наш подход включает анализ текстовых описаний ремонтных работ, что позволяет выставлять оценки направления энергоэффективности и других ключевых параметров.

3. Обогащение данных: Мы расширили нашу базу данных дополнительной информацией для более точного и всестороннего прогнозирования.

4. Градиентный бустинг: Использование современной техники градиентного бустинга для создания эффективной и точной модели прогнозирования.

🌍 Адаптация к переменам: Наша модель умело адаптируется к изменяющимся экономическим и климатическим условиям, таким как инфляция и изменения климата.

🖥️ Интуитивное веб-приложение: Разработано для облегчения доступа и использования модели, позволяя пользователям легко взаимодействовать с нашим решением.

🔥 Косатка-Analytics: Ваш ключ к пониманию и прогнозированию коммунальных платежей! 🌊📊

## Пояснение к файлам в docs
- poisk.ipynb - объединение дата фреймов и разработка модели
- test.ipynb - анализ текстовой информации для определения класса
- text.ipynb - для обработки тестовой выборки

## Используемые библиотеки
### Стандартные библиотеки
import os

### Сторонние библиотеки
import catboost
from catboost import CatBoostClassifier, CatBoostRegressor, Pool
from catboost import cv
from catboost.eval.catboost_evaluation import *
from catboost.eval.evaluation_result import *
from catboost.utils import create_cd, get_roc_curve
import lightgbm as lgb
import matplotlib.pyplot as plt
from nltk import word_tokenize
import nltk
from nltk.corpus import stopwords, wordnet
from nltk.corpus import stopwords as nltk_stopwords
from nltk.probability import FreqDist
from nltk.stem import WordNetLemmatizer 
from pandarallel import pandarallel
import pandas as pd
from pytorch_transformers import BertTokenizer
import requests
import seaborn as sns
import shap
from sklearn import metrics
from sklearn.ensemble import IsolationForest, RandomForestRegressor
from sklearn.linear_model import LinearRegression, SGDRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, make_scorer
from sklearn.model_selection import KFold, train_test_split
from sklearn.model_selection import RandomizedSearchCV, GridSearchCV, cross_val_score
import sklearn
import torch
import transformers as ppb
from tqdm import tqdm
from wordcloud import WordCloud

### Модули Pytorch
from torch.utils.data import TensorDataset, DataLoader, RandomSampler, SequentialSampler

### Модули Keras
from keras_preprocessing.sequence import pad_sequences

### Статистические модули
from scipy.stats import probplot
from statsmodels.graphics.tsaplots import plot_acf
from statsmodels.stats.stattools import durbin_watson

### Pymorphy
from pymorphy2 import MorphAnalyzer

# Применение

```bash
#Установка
git clone https://github.com/GladR1/Passport_detection_app.git
cd <папка проекта>
python -m venv .venv
source .venv/bin/activate    # для Linux
# или
.venv\Scripts\activate       # для Windows
pip install -r requirements.txt
Установить последнюю версию tesseract (https://github.com/UB-Mannheim/tesseract/wiki)
скачать модели по ссылке https://disk.yandex.ru/d/AcxtV3xZl6-sGQ и положить их в папку \models

# Запуск
python run.py
    "Введите путь к 3 странице паспорта"
     foma.jpg (пример)
     "Обработка завершена. Результаты сохранены в папке processed_passports."
      

# Структура проекта
models/ — предобученные модели.
processed_passports/ — обработанные данные.
scripts/ — код детекции, обработки и OCR.
run.py — основной файл запуска.

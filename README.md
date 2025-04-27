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

# Запуск
python run.py

# Структура проекта
models/ — предобученные модели.
processed_passports/ — обработанные данные.
scripts/ — код детекции, обработки и OCR.
run.py — основной файл запуска.

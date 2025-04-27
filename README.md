Установка 
git clone <ссылка на репозиторий>
cd <папка проекта>
python -m venv .venv
source .venv/bin/activate (Linux)   # или .venv\Scripts\activate (Windows)
pip install -r requirements.txt

Запуск
python run.py

Структура проекта
models/ — предобученные модели.
processed_passports/ — обработанные данные.
scripts/ — код детекции, обработки и OCR.
run.py — основной файл запуска.

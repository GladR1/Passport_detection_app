from scripts.ocr import tesseract_ocr
from scripts.detector import detect_areas
from scripts.tools import (crop_xyxyn,
                    rotate_90_ccw,
                    draw_bboxes,
                    save_to_json,
                    find_last_slash_index)

import cv2
from pathlib import Path

def main():
    current_path = Path.cwd()  

    print("Введите путь к 3 странице паспорта")
    image_path = input()
    image = cv2.imread(image_path)

    s_id = find_last_slash_index(image_path)
    image_name = image_path[s_id + 1:-4]

    detected_hash_map = detect_areas(image)

    string_hash_map = {'Место рождения': "",
                        "Дата рождения":"",
                       "Пол":"",
                        "Имя":"",
                        "Фамилия":"",
                        "Серия и номер": "",
                        "Отчество":""}

    translation = {'birthplace':'Место рождения',
                    'date': "Дата рождения",
                    "gender": "Пол",
                    "names":"Имя",
                    "surname": "Фамилия",
                    "sn": "Серия и номер",
                    'patronymic': "Отчество"}

    for key in detected_hash_map:
        if key == "face":
            continue 
        croped_image = crop_xyxyn(image, detected_hash_map[key])
        if key == "sn":
            croped_image = rotate_90_ccw(croped_image)
        ocr_out = tesseract_ocr(image=croped_image)
        string_hash_map[translation[key]] = ocr_out

    drawn_image = draw_bboxes(image, detected_hash_map)

    for key in string_hash_map:
        if len(string_hash_map[key]) == 0:
            print(f"{key} в паспорте не обнаружено.")

    cv2.imwrite(current_path / "processed_passports" / "images" / f"{image_name}.png", drawn_image)
    save_to_json(string_hash_map, current_path / "processed_passports" / "data" / f"{image_name}.json")

    print("Обработка завершена. Результаты сохранены в папке processed_passports.")





from ultralytics import YOLO
import numpy as np
from pathlib import Path

current_path = Path.cwd()  

print(rf"{current_path}\models\passport_model.pt")
try: model = YOLO(rf"{current_path}\models\passport_model.pt")
except FileNotFoundError:
        raise FileNotFoundError(f"Ошибка: Модель passport_model в папке models не обнаружена!")

try: face_model = YOLO(rf"{current_path}\models\face_model.pt")
except FileNotFoundError:
        raise FileNotFoundError(f"Ошибка: Модель passport_model.pt в папке models не обнаружена!")

def detect_areas(image:np.ndarray) -> dict:
        """
        Обнаруживает области на изображении с помощью YOLOv11.
        args:
           image: numpy array изображения в формате (H, W, C) или (H, W).
        Returns:
           dict: Словарь, где ключи - классы, а значения - списки bbox в формате [x_center, y_center, width, height] (нормализованные).
        """
        pred = model(image,verbose = False)[0]
        face_pred = face_model(image,verbose = False)[0]

        conf = pred.boxes.conf.numpy()
        boxes_n = pred.boxes.xyxyn.numpy()[conf > 0.7]
        cls = pred.boxes.cls.numpy()[conf > 0.7]
        names = pred.names
        
        boxes_hash_map = {}
        for i, c in enumerate(cls):
            boxes_hash_map[names[c]] = boxes_n[i]

        cls = face_pred.boxes.cls.numpy()
        boxes_n_face = face_pred.boxes.xyxyn.numpy()[cls == 0]
        if len(boxes_n_face) == 0:
            raise ValueError("Ошибка: Лицо не обнаружено на изображении!")
        boxes_hash_map["face"] = boxes_n_face[0]

        return boxes_hash_map
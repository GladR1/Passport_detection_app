import numpy as np
import cv2
from pathlib import Path
import json 

def crop_xyxyn(image:np.ndarray, bbox_xyxyn: np.ndarray) -> np.ndarray:
    """
    Обрезает изображение по bounding box в формате xyxyn (нормализованные координаты).
    
    Args:
        image: Входное изображение (BGR или RGB).
        bbox_xyxyn (list/tuple): Bounding box в формате [x1, y1, x2, y2], где значения нормализованы [0, 1].
    
    Returns:
        numpy.ndarray: Вырезанный участок изображения.
    """
    h, w = image.shape[:2]

    x1, y1, x2, y2 = bbox_xyxyn
    x1 = int(x1 * w)
    y1 = int(y1 * h)
    x2 = int(x2 * w)
    y2 = int(y2 * h)

    cropped = image[y1:y2, x1:x2]

    return cropped

def rotate_90_ccw(image: np.ndarray) -> np.ndarray:
    """Поворачивает изображение на 90° против часовой стрелки.
    
    Args:
        image: numpy array изображения в формате (H, W, C) или (H, W).
    
    Returns:
        numpy.ndarray: Повёрнутый numpy array.
    """
    return np.rot90(image, k=1, axes=(0, 1))

def draw_bboxes(image, bbox_dict, color=(0, 255, 0), thickness=2, font_scale=0.6):
    """
    Рисует bounding boxes на изображении и подписывает их классы.
    
    Args:
        image (numpy.ndarray): Входное изображение (BGR или RGB).
        bbox_dict (dict): Словарь, где ключи - классы, а значения - списки bbox в формате [x_center, y_center, width, height] (нормализованные).
        color (tuple): Цвет bounding box (BGR). По умолчанию зеленый.
        thickness (int): Толщина линии.
        font_scale (float): Размер шрифта.
    
    Returns:
        numpy.ndarray: Изображение с нарисованными bounding boxes.
    """

    img = image.copy()
    h, w = img.shape[:2]
    
    for class_name, bbox in bbox_dict.items():

        x1, y1, x2, y2 = bbox
        x1 = int(x1 * w)
        y1 = int(y1 * h)
        x2 = int(x2 * w)
        y2 = int(y2 * h)

        cv2.rectangle(img, (x1, y1), (x2, y2), color, thickness)

        (text_w, text_h), _ = cv2.getTextSize(class_name, cv2.FONT_HERSHEY_SIMPLEX, font_scale, thickness)
        cv2.rectangle(img, (x1, y1 - text_h - 5), (x1 + text_w, y1), color, -1)  # Фон для текста
        cv2.putText(img, class_name, (x1, y1 - 5), cv2.FONT_HERSHEY_SIMPLEX, font_scale, (0, 0, 0), thickness)

    return img

def save_to_json(data, filename):
    try:
        with Path(filename).open('w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
    except Exception as e:
        print(f"Ошибка при сохранении: {e}")

def find_last_slash_index(path: str) -> int:
    """
    Находит последний индекс символа '/' или '\\' в строке.
    
    Args:
        path: Входная строка (обычно путь к файлу/директории)
    
    Returns:
        int | None: Индекс последнего слеша или None, если слешей нет
    """
    last_slash = max(path.rfind('/'), path.rfind('\\'))
    return last_slash if last_slash != -1 else None
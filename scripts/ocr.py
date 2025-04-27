from pytesseract import Output
import pytesseract
import cv2

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def tesseract_ocr(
    image: cv2.Mat,
    lang: str = 'rus',
    oem: int = 1,
    psm: int = 6):
    """
    Распознаёт текст на изображении с помощью Tesseract.

    Args:
        image: BGR-изображение (np.ndarray) из OpenCV.
        lang: код языка для Tesseract (по умолчанию 'rus').
        oem: OCR Engine Mode (0..3), 1 = LSTM only.
        psm: Page Segmentation Mode, 6 = Assume a single uniform block of text.
    Returns:
        Список кортежей (text, x, y, w, h, conf), где
        text — строка,
        x,y,w,h — координаты её bounding box,
        conf — confidence (0–100).
    """

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    _, th = cv2.threshold(gray, 0, 255,
                          cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    config = f'--oem {oem} --psm {psm}'

    data = pytesseract.image_to_data(
        th, lang=lang, config=config, output_type=Output.DICT
    )
    results_list = []
    n = len(data['text'])
    for i in range(n):
        txt = data['text'][i].strip()
        if not txt:
            continue
        results_list.append(txt)
    results = "".join(results_list)

    return results
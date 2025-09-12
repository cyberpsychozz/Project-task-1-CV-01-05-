import numpy as np      
import cv2 as cv        
from skimage import data

def finding_contours(imgray):
    # Применение детектора краёв Canny для выделения границ объектов на изображении
    edges = cv.Canny(imgray, 50, 150)

    ret, thresh = cv.threshold(edges, 127, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)

    # Создание ядра (структурирующего элемента) размером 3x3 для морфологических операций 
    kernel = np.ones((3,3), np.uint8)

    # Морфологическая операция "закрытие" (MORPH_CLOSE): сначала дилатация, потом эрозия
    # Это заполняет небольшие дыры внутри объектов и соединяет близкие компоненты на бинарном изображении
    thresh = cv.morphologyEx(thresh, cv.MORPH_CLOSE, kernel)

    # Поиск всех внешних контуров на бинарном изображении
    # Режим RETR_EXTERNAL — только внешние контуры; CHAIN_APPROX_SIMPLE — сжатие горизонтальных/вертикальных/диагональных сегментов
    contours, hierarchy = cv.findContours(thresh, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

    # Установка минимальной и максимальной площади контуров для фильтрации (монеты среднего размера)
    min_area = 200
    max_area = 5000
    filtered_contours = []

    for cnt in contours:
        area = cv.contourArea(cnt)  # Вычисление площади контура
        if min_area < area < max_area:  # Фильтрация: только контуры с площадью от 200 до 5000 пикселей
            filtered_contours.append(cnt)  # Добавление подходящего контура в список
    
    return filtered_contours

imgray = data.coins()
assert imgray is not None, "file could not be read, check with os.path.exists()"

contours = finding_contours(imgray)

# Отрисовка отфильтрованных контуров на оригинальном изображении (imgray)
# -1 — все контуры; цвет (0,255,0) — зелёный (BGR); толщина 3 пикселя
cv.drawContours(imgray, contours, -1, (0,255,0), 3)

cv.imwrite('res.png', imgray)

print(len(contours))
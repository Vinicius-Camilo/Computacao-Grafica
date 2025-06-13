import cv2
import numpy as np
from utils import preprocess_image, apply_watershed, filter_contours

def main():
    img, gray = preprocess_image('images/chocolates.jpg')
    _, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
    morph = cv2.morphologyEx(binary, cv2.MORPH_OPEN, kernel)
    markers = apply_watershed(img.copy(), morph)
    contours, _ = cv2.findContours(morph, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    filtered_contours = filter_contours(contours, min_area=100)
    object_count = 0
    for cnt in filtered_contours:
        object_count += 1
        cv2.drawContours(img, [cnt], -1, (0, 255, 0), 2)
    cv2.putText(img, f'Objetos detectados: {object_count}', (10, 30), 
                cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
    cv2.imwrite('images/mask.png', img)
    cv2.imshow("Resultado", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()

import cv2
import numpy as np
from utils import preprocess_image, apply_threshold, apply_watershed

def main():
    img, gray = preprocess_image('images/chocolates.jpg')
    binary = apply_threshold(gray)
    cv2.imshow("Máscara binarizada", binary)

    kernel_open = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (2, 2))
    kernel_close = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (30, 30))
    morph = cv2.morphologyEx(binary, cv2.MORPH_OPEN, kernel_open)
    morph = cv2.morphologyEx(morph, cv2.MORPH_CLOSE, kernel_close)
    cv2.imshow("Máscara após morfologia", morph)

    img_ws, markers = apply_watershed(img.copy(), morph)

    watershed_mask = np.zeros_like(gray)
    for label in np.unique(markers):
        if label <= 1:
            continue
        watershed_mask[markers == label] = 255
    cv2.imshow("Máscara Watershed", watershed_mask)

    object_count = 0
    for label in np.unique(markers):
        if label <= 1:
            continue
        mask = np.uint8(markers == label)
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        for cnt in contours:
            if cv2.contourArea(cnt) > 300:
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
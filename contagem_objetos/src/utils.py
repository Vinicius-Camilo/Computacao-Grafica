import cv2
import numpy as np

def preprocess_image(image_path):
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return img, gray

def apply_threshold(gray_image):
    """Aplicar a limiarização de Otsu invertida à imagem em tons de cinza."""
    _, binary = cv2.threshold(gray_image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    return binary

def remove_noise(binary_image):
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
    morph = cv2.morphologyEx(binary_image, cv2.MORPH_OPEN, kernel)
    return morph

def apply_watershed(img, mask):
    kernel = np.ones((3,3), np.uint8)
    sure_bg = cv2.dilate(mask, kernel, iterations=2)
    dist_transform = cv2.distanceTransform(mask, cv2.DIST_L2, 5)
    _, sure_fg = cv2.threshold(dist_transform, 0.1 * dist_transform.max(), 255, 0)
    sure_fg = np.uint8(sure_fg)
    unknown = cv2.subtract(sure_bg, sure_fg)
    _, markers = cv2.connectedComponents(sure_fg)
    markers = markers + 1
    markers[unknown == 255] = 0
    cv2.watershed(img, markers)
    img[markers == -1] = [0, 0, 255]
    return img, markers

def filter_contours(contours, min_area=100):
    filtered = [cnt for cnt in contours if cv2.contourArea(cnt) > min_area]
    return filtered

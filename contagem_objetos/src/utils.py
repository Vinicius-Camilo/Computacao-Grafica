import cv2
import numpy as np

def preprocess_image(image_path):
    """Carregue uma imagem e converta-a para tons de cinza."""
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return img, gray

def apply_threshold(gray_image):
    """Aplicar a limiarização de Otsu à imagem em tons de cinza."""
    _, binary = cv2.threshold(gray_image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    return binary

def remove_noise(binary_image):
    """Aplicar operações morfológicas para remover ruídos da imagem binária."""
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
    morph = cv2.morphologyEx(binary_image, cv2.MORPH_OPEN, kernel)
    return morph

def apply_watershed(img, mask):
    """Aplicar o algoritmo watershed para separar objetos sobrepostos."""
    dist_transform = cv2.distanceTransform(mask, cv2.DIST_L2, 5)
    _, sure_fg = cv2.threshold(dist_transform, 0.7 * dist_transform.max(), 255, 0)
    
    unknown = cv2.subtract(mask, sure_fg.astype(np.uint8))
    

    _, markers = cv2.connectedComponents(sure_fg.astype(np.uint8))
    markers = markers + 1  
    markers[unknown == 255] = 0 
    
    cv2.watershed(img, markers)
    img[markers == -1] = [0, 0, 255]  
    return img

def filter_contours(contours, min_area=100):
    """Filtrar contornos com base em uma área mínima."""
    filtered = [cnt for cnt in contours if cv2.contourArea(cnt) > min_area]
    return filtered

def draw_contours_and_count(img, contours):
    """Desenhe os contornos na imagem e retorne a contagem de objetos detectados."""
    count = len(contours)
    for cnt in contours:
        cv2.drawContours(img, [cnt], -1, (0, 255, 0), 2) 
    return count

def save_image(image, output_path):
    """Salve a imagem processada no caminho especificado."""
    cv2.imwrite(output_path, image)
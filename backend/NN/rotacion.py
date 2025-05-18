import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
import time

def estimate_rotation(pos):
    img_path_2 = "temp.png"
    img_path_1 = r"Data/malos/" + pos + ",0" + ".png"
    start_time = time.perf_counter()  # Inicio

    # Cargar imágenes en escala de grises
    img1 = cv2.imread(img_path_1, cv2.IMREAD_GRAYSCALE)
    img2 = cv2.imread(img_path_2, cv2.IMREAD_GRAYSCALE)

    if img1 is None or img2 is None:
        raise ValueError(f"No se pudo cargar una de las imágenes: {img_path_1} o {img_path_2}")

    orb = cv2.ORB_create(500)
    kp1, des1 = orb.detectAndCompute(img1, None)
    kp2, des2 = orb.detectAndCompute(img2, None)

    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
    matches = bf.match(des1, des2)
    matches = sorted(matches, key=lambda x: x.distance)[:50]

    pts1 = np.float32([kp1[m.queryIdx].pt for m in matches])
    pts2 = np.float32([kp2[m.trainIdx].pt for m in matches])

    matrix, inliers = cv2.estimateAffinePartial2D(pts1, pts2)
    if matrix is None:
        print("No se pudo estimar la transformación.")
        return None

    angle = np.arctan2(matrix[1, 0], matrix[0, 0]) * 180 / np.pi

    elapsed_time = time.perf_counter() - start_time  # Tiempo antes de mostrar

    print(f'Tiempo de procesamiento: {elapsed_time:.3f} segundos')
    return angle

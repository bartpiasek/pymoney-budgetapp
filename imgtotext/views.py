from django.shortcuts import render
import cv2 
import pytesseract
import numpy as np

def imagetotext():
    """
    converting upload image to string
    """
    img = cv2.imread('')

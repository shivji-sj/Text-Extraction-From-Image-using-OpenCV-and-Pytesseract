import cv2
import numpy as np
import pytesseract
from PIL import Image


class Text_Extraction():
    
    def show_image(self, path):
        try:
            x = path
        except Exception as e:
            print("Give your file path!!!")
        finally:
            pass

        return Image.open(path)
    
 
    def text_from_image(self, path):
        try:
            x = path
        except Exception as e:
            print("Give your file path!!!")
        finally:
            pass

        def extract_text(img):
            #Extracting the text
            text = pytesseract.image_to_string(img)
            for char in list("~`@#$%^&*()_-+=/'';[]{}"):
                text = text.replace(char,"")
                return text
            
        ###################################################### Read the given image
        img = cv2.imread(x)

        ###################################################### erosion
        e_kernel = np.ones((2,2), np.uint8)
        img = cv2.erode(img, e_kernel, iterations=1)
        
        ###################################################### Morphology
        #m_kernel=np.ones((5,5), np.uint8)
        #m_img = cv2.morphologyEx(img, cv2.MORPH_OPEN, m_kernel)
        
        
        ###################################################### Sharpening the image
        kernel = np.array([[0, -1, 0],
                       [-1, 5,-1],
                       [0, -1, 0]])
        sharp_img = cv2.filter2D(src=img, ddepth=-1, kernel=kernel)

        ###################################################### BGR TO GrayScale
        gray_img = cv2.cvtColor(sharp_img, cv2.COLOR_BGR2GRAY)
        
        ###################################################### Thresholding the image
        thresh_img = cv2.threshold(gray_img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
        
        ###################################################### Adaptive threshold
        ad_thresh_img = cv2.adaptiveThreshold(thresh_img, 255,
        cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 21, 18)
        
        ###################################################### Edge Detection using Canny Edge 
        #canny_img = cv2.Canny(thresh_img, 100,200)
        
        ###################################################### print the extracted text
        print(extract_text(ad_thresh_img))

        cv2.waitKey(2000)
        cv2.destroyAllWindows()

        
    def text_to_file(self, path):
        try:
            x = path
        except Exception as e:
            print("Give your file path!!!")
        finally:
            pass

        def extract_text(img):
            #Extracting the text
            text = pytesseract.image_to_string(img)
            for char in list("~`@#$%^&*()_-+=/'';[]{}"):
                text = text.replace(char,"")
                return text
            
        ###################################################### Read the given image
        img = cv2.imread(x)
        
        ###################################################### erosion
        e_kernel = np.ones((2,2), np.uint8)
        img = cv2.erode(img, e_kernel, iterations=1)
        
        ###################################################### Morphology
        #m_kernel=np.ones((5,5), np.uint8)
        #m_img = cv2.morphologyEx(img, cv2.MORPH_OPEN, m_kernel)
              
        ###################################################### Sharpening the image
        kernel = np.array([[0, -1, 0],
                       [-1, 5,-1],
                       [0, -1, 0]])
        sharp_img = cv2.filter2D(src=img, ddepth=-1, kernel=kernel)
       
        ###################################################### BGR TO GrayScale
        gray_img = cv2.cvtColor(sharp_img, cv2.COLOR_BGR2GRAY)

        ###################################################### Thresholding the image
        thresh_img = cv2.threshold(gray_img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
        
        ###################################################### Adaptive threshold
        ad_thresh_img = cv2.adaptiveThreshold(thresh_img, 255,
        cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 21, 18)
        
        ###################################################### Edge Detection using Canny Edge 
        #canny_img = cv2.Canny(thresh_img, 100,200)
               
        ###################################################### print the extracted text
        text = extract_text(ad_thresh_img)

        ###################################################### Converting to a file
        paragraph = text
        with open('example.txt', 'w') as file:
            file.write(paragraph)


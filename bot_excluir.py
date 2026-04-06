import pyautogui
import time
from PIL import Image

a=True

while a==True:
    try:
        # Use confidence to adjust how strict the match needs to be (0.0 to 1.0)
        image_location1 = pyautogui.locateCenterOnScreen("cam.png", confidence=0.6)
        
        point1_x, point1_y = image_location1.x, image_location1.y
        print(f"Image found at ({point1_x}, {point1_y}). Clicking there...")
        pyautogui.click(point1_x, point1_y)
        
        time.sleep(1)
        
        image_location2 = pyautogui.locateCenterOnScreen("excluir.png", confidence=0.9)

        point2_x, point2_y = image_location2.x, image_location2.y
        print(f"Image found at ({point2_x}, {point2_y}). Clicking there...")
        pyautogui.click(point2_x, point2_y)

        time.sleep(1)
        
        """
        image_location2 = pyautogui.locateCenterOnScreen("image2.png", confidence=0.9)

        point2_x, point2_y = image_location2.x, image_location2.y
        print(f"Image found at ({point2_x}, {point2_y}). Clicking there...")
        pyautogui.click(point2_x, point2_y)
        """
        
        time.sleep(1)

    except:
        print("CORRESPONDENCIAS FINALIZADAS")
        a=False
        print("Done!")
        break
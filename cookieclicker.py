import pyautogui
import time
import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"


class AutoCookieClicker:

    def __init__(self, cookie_image, cookie_number_image, grandma_image):
        self.cookie_image = cookie_image
        self.cookie_number_image = cookie_number_image
        self.grandma_image = grandma_image
        self.main()

    def click_cookie(self):
        """Move to the cookie's location, and begin clicking."""
        # Locate the cookie, and move the mouse over it
        cookie_location = pyautogui.locateOnScreen(self.cookie_image)
        pyautogui.moveTo(cookie_location)
        if cookie_location is not None:
            while True:
                for i in range(0, 1000):
                    pyautogui.click(interval=0)
                self.buy_grandma()

    def buy_grandma(self):
        buy_grandma_location = pyautogui.locateOnScreen(self.grandma_image)
        pyautogui.moveTo(buy_grandma_location)
        for i in range(1, 10):
            pyautogui.click()
        print("buy grandma")


    """Scrapped this section of code due to it only working around half of the time - feel free to have a go at fixing it yourself!"""
    # def get_current_cookies(self):
    #     """Find the number of cookies currently owned."""
    #
    #     # get the location of the cookie label
    #     cookie_label_location = pyautogui.locateOnScreen(self.cookie_number_image)
    #     print(cookie_label_location)
    #
    #     # create a tuple with modified x values to only get the number of cookies
    #     cookie_number_location = (cookie_label_location[0] - 20, cookie_label_location[1], cookie_label_location[2] - 105, cookie_label_location[3])
    #
    #     # take a screenshot of the region and save it to cookie_number.png
    #     pyautogui.screenshot("cookie_number.png", region=cookie_number_location)
    #
    #     self.image_to_number("cookie_number.png")
    #
    # def image_to_number(self, img_name):
    #     number = pytesseract.image_to_string(Image.open(img_name), config='--psm 6')
    #     print(number)

    def main(self):
        print("Please make sure the browser window is selected and visible within 5 seconds...")
        # time.sleep(5)
        self.click_cookie()


if __name__ == "__main__":
    AutoCookieClicker("images\\cookie_image.png", "images\\cookie_number_image.png", "images\\grandma_image.png")
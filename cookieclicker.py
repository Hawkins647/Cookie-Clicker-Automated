import pyautogui
import time
import pytesseract


pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"


class AutoCookieClicker:

    def __init__(self, cookie_image, cookie_number_image, grandma_image, farm_image, mine_image):
        self.cookie_image = cookie_image
        self.cookie_number_image = cookie_number_image
        self.grandma_image = grandma_image
        self.farm_image = farm_image
        self.mine_image = mine_image

        self.main()

    def click_cookie(self):
        """Move to the cookie's location, and begin clicking."""
        # Locate the cookie, and move the mouse over it
        cookie_location = pyautogui.locateOnScreen(self.cookie_image)
        pyautogui.moveTo(cookie_location)

        # main logic
        if cookie_location is not None:
            while True:
                for i in range(0, 105):
                    pyautogui.click()

                grandma_location = self.buy_grandma_location()
                self.move_click(grandma_location)

                pyautogui.moveTo(cookie_location)
                for i in range(0, 500):
                    pyautogui.click()
                self.move_click(grandma_location)

                pyautogui.moveTo(cookie_location)
                for i in range(0, 1005):
                    pyautogui.click()

                farm_location = self.buy_farm_location()
                self.move_click(farm_location)

                pyautogui.moveTo(cookie_location)
                for i in range(0, 1005):
                    pyautogui.click()

                self.move_click(farm_location)

                pyautogui.moveTo(cookie_location)
                for i in range(0, 2005):
                    pyautogui.click()

                self.move_click(farm_location)
                pyautogui.moveTo(cookie_location)
                for i in range(0, 10005):
                    pyautogui.click()

                mine_location = self.buy_mine_location()
                self.move_click(mine_location)


    def move_click(self, location):
        pyautogui.moveTo(location)
        for i in range(1, 10):
            pyautogui.click()

    def buy_grandma_location(self):
        grandma_location = pyautogui.locateOnScreen(self.grandma_image)
        return grandma_location

    def buy_mine_location(self):
        mine_location = pyautogui.locateOnScreen(self.mine_image)
        return mine_location

    def buy_farm_location(self):
        farm_location = pyautogui.locateOnScreen(self.farm_image)
        return farm_location


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
        print("Move the mouse into a corner of the screen to stop the program")
        time.sleep(5)
        self.click_cookie()


if __name__ == "__main__":
    AutoCookieClicker("images\\cookie_image.png", "images\\cookie_number_image.png", "images\\grandma_image.png", "images\\farm_image.png", "images\\mine_image.png")
import pyautogui
import time


class AutoCookieClicker:

    def __init__(self, cookie_image, cookie_number_image):
        self.cookie_image = cookie_image
        self.cookie_number_image = cookie_number_image
        self.main()

    def click_cookie(self):
        """Move to the cookie's location, and begin clicking."""
        cookie_location = pyautogui.locateOnScreen(self.cookie_image)
        pyautogui.moveTo(cookie_location)

    def get_current_cookies(self):
        """Find the number of cookies currently owned."""
        # get the location of the cookie label
        cookie_label_location = pyautogui.locateOnScreen(self.cookie_number_image)
        # create a tuple with modified x value to include the number of cookies
        cookie_number_location = (cookie_label_location[0] - 20, cookie_label_location[1], cookie_label_location[2], cookie_label_location[3])
        # take a screenshot of the region and save it to cookie_number.png
        pyautogui.screenshot("cookie_number.png", region=cookie_number_location)

        # TODO: get int value from img

    def main(self):
        print("Please make sure the browser window is selected and visible within 5 seconds...")
        time.sleep(5)
        self.click_cookie()


if __name__ == "__main__":
    AutoCookieClicker("images\\cookie_image.png", "images\\cookie_number_image.png")
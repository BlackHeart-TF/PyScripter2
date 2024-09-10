import cv2
import numpy as np
from PIL import Image as PILImage
from mss import mss

class Image:
    @staticmethod
    def match(template_path, bbox=None, threshold=0.8):
        """
        Matches the template image to the screen or a region defined by bbox.

        Args:
            template_path (str): Path to the image file to match.
            bbox (tuple): (left, top, width, height) bounding box for a specific region of the screen.
                         If None, the whole screen is used.
            threshold (float): The threshold for template matching (0.8 by default).

        Returns:
            tuple or None: Returns the top-left corner of the matched region (x, y) if found; otherwise None.
        """
        # Load the template image
        template = cv2.imread(template_path, 0)
        template_w, template_h = template.shape[::-1]

        # Capture the screen or region
        with mss() as sct:
            if bbox:
                screen = np.array(sct.grab({'left': bbox[0], 'top': bbox[1], 'width': bbox[2], 'height': bbox[3]}))
            else:
                screen = np.array(sct.grab(sct.monitors[1]))  # Capture the whole screen

        # Convert the screenshot to grayscale
        screen_gray = cv2.cvtColor(screen, cv2.COLOR_BGRA2GRAY)

        # Perform template matching
        res = cv2.matchTemplate(screen_gray, template, cv2.TM_CCOEFF_NORMED)
        loc = np.where(res >= threshold)

        # If a match is found, return the position
        if len(loc[0]) > 0:
            top_left = (loc[1][0], loc[0][0])
            return top_left
        else:
            return None

# # Example usage
# # This will match 'clip.jpg' on the entire screen or within a bounding box (x, y, width, height)
# result = Image.match('clip.jpg', bbox=(0, 0, 800, 600))  # Or use None to check the entire screen

# if result:
#     print(f"Image found at: {result}")
# else:
#     print("Image not found.")

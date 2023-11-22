from pathlib import Path
import cv2


def show_or_save_image(image, title, path=None, filename=None, save_image=True):
    if save_image and filename:
        full_path = Path(path).joinpath(filename)
        cv2.imwrite(str(full_path), image)
    else:
        cv2.imshow(title, image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

def find_images(folder_path):
    image_extensions = ['.jpg', '.jpeg', '.png', '.bmp', '.tiff']
    return [str(f) for f in Path(folder_path).glob('*') if f.suffix.lower() in image_extensions]

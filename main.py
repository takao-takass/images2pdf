from PIL import Image
import os

def create_pdf(image_folder):
    """
    Create a PDF file from a folder of images.
    """
    image_files = sorted([f for f in os.listdir(image_folder) if f.endswith('.jpg')])

    im1 = Image.open(os.path.join(image_folder, image_files[0])).convert('RGB')
    ims = [Image.open(os.path.join(image_folder, f)).convert('RGB') for f in image_files[1:]]

    im1.save('output.pdf', 'PDF', resolution=100.0, save_all=True, append_images=ims)

create_pdf('images')

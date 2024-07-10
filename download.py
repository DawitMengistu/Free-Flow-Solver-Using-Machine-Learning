import requests
from PIL import Image
from io import BytesIO
packNames = [""]
packLinks = [
    "",
    "",

]
names = ["55", "66-150", "77", "88", "99"]


def download_and_crop_image(image_url, crop_top, crop_bottom, save_path):
    # Download the image
    response = requests.get(image_url)
    if response.status_code == 200:
        image_data = response.content
        # Open the image
        image = Image.open(BytesIO(image_data))
        # Crop the image
        width, height = image.size
        cropped_image = image.crop(
            (0, crop_top, width, height - crop_bottom))
        # Save the cropped image
        cropped_image.save(save_path)
        print(f"Cropped image saved to {save_path}")
    else:
        print(f"Failed to download image. Status code: {
            response.status_code}")


folderIndex = 1
for i in range(0, 150):
    # if (i != 0 and i % 30 == 0):
    #     folderIndex += 1
    #     print("Here", folderIndex)
    # Example usage
    image_url = 'https://flowfreesolutions.com/solution-pictures/flow/6mania/flow-6mania-' + \
        str(i + 1) + '.png'
    crop_top = 128  # Number of pixels to crop from the top
    crop_bottom = 128  # Number of pixels to crop from the bottom
    save_path = 'data/' + names[folderIndex] + "/" + str(i) + '.jpg'
    # print(save_path, image_url)
    download_and_crop_image(image_url, crop_top, crop_bottom, save_path)

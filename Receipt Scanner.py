from PIL import Image
import pytesseract
import re

# Function to extract information from the receipt
def extract_receipt_info(image_path):
    try:
        # Load the image using Pillow
        image = Image.open(image_path)

        # Perform OCR on the image
        text = pytesseract.image_to_string(image)

        # Define regular expressions to match item names and prices
        item_name_pattern = r"[\w\s]+"
        price_pattern = r"\d+\.\d{2}"

        # Find item names and prices in the text using regular expressions
        item_names = re.findall(item_name_pattern, text)
        prices = re.findall(price_pattern, text)

        # Combine item names and prices into a dictionary
        items = dict(zip(item_names, prices))

        return items

    except Exception as e:
        return str(e)

# Usage example
if __name__ == "__main__":
    image_path = "your_receipt_image.png"  # Replace with the path to your receipt image
    receipt_info = extract_receipt_info(image_path)
    if isinstance(receipt_info, dict):
        for item, price in receipt_info.items():
            print(f"Item: {item}, Price: ${price}")
    else:
        print(f"Error: {receipt_info}")

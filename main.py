from PIL import Image, ImageDraw, ImageFont
import os
import pandas as pd

def replace_name_in_image(input_image_path, output_image_path, name):
    # Open the image file
    image = Image.open(input_image_path)
    
    # Initialize the drawing context
    draw = ImageDraw.Draw(image)
    
    # Define the font and size (ensure you have this font file and correct path)
    font_path = "font.otf"  # Example for Windows, use a common system font
    font_size = 90  # Adjust the size as needed
    try:
        font = ImageFont.truetype(font_path, font_size)
    except IOError:
        print("Font file not found. Please provide a valid font path.")
        return
    
    # Define the text color (in this case, it's gold)
    text_color = (183, 148, 69)  # RGB for gold-like color
    
    # Calculate the bounding box of the text to be added
    bbox = draw.textbbox((0, 0), name, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    
    # Calculate the position for centered text
    # Adjust y-coordinate based on where you want the text to appear
    position = ((image.width - text_width) // 2, 420)  # Adjust y-coordinate as needed
    
    # Draw the new name on the image
    draw.text(position, name, font=font, fill=text_color)
    
    # Save the modified image
    image.save(output_image_path)
    print(f"Image saved as {output_image_path}")

def create_invitation_image(name, email):
    input_image_path = 'invitation.jpg'
    output_dir = 'output_images'  # Make sure this directory exists
    output_image_path = os.path.join(output_dir, f"{email}.jpg")
    
    # Ensure the output directory exists
    os.makedirs(output_dir, exist_ok=True)
    
    replace_name_in_image(input_image_path, output_image_path, name)

def process_csv(csv_file_path):
    # Read the CSV file
    data = pd.read_csv(csv_file_path)
    
    # Iterate over each row in the CSV
    for index, row in data.iterrows():
        name = row['name']
        email = row['email']
        create_invitation_image(name, email)

# Example usage
csv_file_path = 'bce_079.csv'  # Path to the CSV file
process_csv(csv_file_path)

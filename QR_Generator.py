import qrcode
from PIL import Image

def generate_qr(text, version=1, box_size=10, border=4, fill_color='black', back_color='white', error_correction='L'):
    """
    Generates a QR code from the provided text or URL with customizable options.

    Parameters:
    text (str): The text or URL that you want to encode into a QR code.
    version (int): Version of the QR code (1 to 40). Default is 1 (21x21 matrix).
    box_size (int): The size of each individual box in the QR code (in pixels). Default is 10.
    border (int): The size of the border (in boxes). Default is 4.
    fill_color (str): The color of the QR code (foreground). Default is black.
    back_color (str): The background color of the QR code. Default is white.
    error_correction (str): The error correction level. Options are 'L', 'M', 'Q', 'H'. Default is 'L'.
    """

    # Map error correction level to QRCode constants
    error_correction_levels = {
        'L': qrcode.constants.ERROR_CORRECT_L,  # 7% of the data can be restored
        'M': qrcode.constants.ERROR_CORRECT_M,  # 15% of the data can be restored
        'Q': qrcode.constants.ERROR_CORRECT_Q,  # 25% of the data can be restored
        'H': qrcode.constants.ERROR_CORRECT_H   # 30% of the data can be restored
    }
    
    # Check if the provided error correction level is valid
    if error_correction not in error_correction_levels:
        print("Invalid error correction level. Defaulting to 'L'.")
        error_correction = 'L'
    
    # Create a QRCode object with user-defined parameters
    qr = qrcode.QRCode(
        version=version,
        error_correction=error_correction_levels[error_correction],
        box_size=box_size,
        border=border
    )
    
    # Add the provided text or URL to the QR code
    qr.add_data(text)
    qr.make(fit=True)
    
    # Generate the QR code image
    img = qr.make_image(fill=fill_color, back_color=back_color)
    
    # Save the generated QR code as a PNG image
    img.save("generated_qr_code.png")
    
    # Notify the user that the QR code has been generated
    print(f"QR Code generated and saved as 'generated_qr_code.png'.")

def get_user_input():
    """
    Prompts the user to input the QR code parameters from the console.
    """

    # Get user input for text or URL to encode
    text_input = input("Enter the text or URL to generate the QR code: ")

    # Get user input for QR code customization
    try:
        version = int(input("Enter the version (1-40, default 1): ") or 1)
        box_size = int(input("Enter the box size (default 10): ") or 10)
        border = int(input("Enter the border size (default 2): ") or 2)
        fill_color = input("Enter the fill color (default 'black'): ") or 'black'
        back_color = input("Enter the background color (default 'white'): ") or 'white'
        error_correction = input("Enter the error correction level (L, M, Q, H, default 'L'): ") or 'L'

    except ValueError:
        print("Invalid input. Default values will be used.")
        version = 1
        box_size = 10
        border = 4
        fill_color = 'black'
        back_color = 'white'
        error_correction = 'L'

    # Call the generate_qr function with the collected inputs
    generate_qr(text_input, version, box_size, border, fill_color, back_color, error_correction)
    
    input("Press Enter to exit...")

if __name__ == "__main__":
    # Run the user input function to get parameters and generate the QR code
    get_user_input()

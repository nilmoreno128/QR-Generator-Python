# **QR Generator**

This script allows you to generate QR codes from text or URLs, with the ability to:

✅ Customize the size and color of the QR code.  
✅ Save the generated QR code as an image file.  
✅ Generate QR codes from input provided directly in the console.  

## **Installation**  
- Download the [`QR_Generator.exe`](QR_Generator.exe) file.  
- Double-click `QR_Generator.exe` to start.  

## **Usage**  

Once you run the `QR_Generator.exe`, the following options will be available in the console

## **Example**
<details>
  <summary>Example</summary>
  ![QR](Media/generated_qr_code.png)
</details>

## **How the Script Work**
<details>
  <summary>📦 Requirements to Run in Python</summary>

  To run this script using Python, you need the following:

  ### **1️⃣ Install Python and pip**
  - **Python**  
    - Download it from [python.org](https://www.python.org/downloads/)  
    - Or install it directly from the **Microsoft Store** (search for "Python" in the Store)  
  - **pip** (Comes pre-installed with Python, but you can update it with:  
    ```sh
    python -m pip install --upgrade pip
    ```

  ### **2️⃣ Install Required Libraries**
  If you're running the script as a `.py`, install the following dependencies:

  ```sh
  pip install qrcode[pil]
  ```

  - **qrcode** → Library to generate the QR codes.
  - **Pillow** → Library for image manipulation (installed automatically with qrcode[pil]).

</details>

<details open>
  <summary>🔍 How the Script Works (Detailed Explanation)</summary>

  The script is designed to generate QR codes based on input text or URLs. Here's a breakdown of how the main parts of the code work:

  ### **1. Importing Libraries**
  ```python
  import qrcode
  from PIL import Image
  ```
  - The **qrcode** library is used to generate QR codes.
  - The **Pillow** library is used to save and manipulate the resulting image.

  ### **2. QR Code Generation Function**
  ```python
  def generate_qr_code(data, size=10, color="black"):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=size,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill=color, back_color="white")
    return img
  ```
  - Takes data (text or URL), size, and color as input.
  - Generates the QR code and returns it as an image.

  ### **3. Saving the Generated QR Code**
  ```python
      def save_qr_code(img, filename="qrcode.png"):
    img.save(filename)
    print(f"QR Code saved as {filename}")
  ```
  - Saves the generated QR code image to a file.

  ### **4. Main Execution**
  ```python
      if __name__ == "__main__":
    text = input("Enter the text or URL for the QR code: ")
    size = int(input("Enter the size of the QR code (default 10): ") or 10)
    color = input("Enter the color of the QR code (default black): ") or "black"

    qr_img = generate_qr_code(text, size, color)
    save_qr_code(qr_img)
  ```
  - Prompts the user for input (text, size, color).
  - Calls the function to generate and save the QR code.

</details>

## License  
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

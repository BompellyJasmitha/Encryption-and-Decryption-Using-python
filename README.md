Encryption and Decryption Project


## Overview
This project is a simple GUI application for encrypting and decrypting files using Python's Tkinter library. The application allows users to select image or audio files and apply a basic XOR encryption technique. Users can set a numeric key for the encryption and decryption processes.

# Features
    Encrypt and decrypt files using a user-defined key.
    Supports multiple file formats: JPEG, PNG, MP3, and MP4.
    User-friendly graphical interface built with Tkinter.

#   Prerequisites
To run this project, you need:
    Python 3.x installed on your system.
    Tkinter library (comes pre-installed with standard Python installations).

# Getting Started
1. Clone the Repository
        Clone this repository to your local machine using:
##      git clone <repository-url>

2. Navigate to the Project Directory
        Change to the project directory:
##      cd <project-directory>

3. Run the Application
        Run the application using Python:
##      python <filename>.py
        Replace <filename>.py with the name of your script file.

# How to Use the Application
1. Open the Application: When you run the script, a window will appear with the title "ENCRYPTION AND DECRYPTION".

2. Set Your Key: In the provided input field, enter a numeric key that will be used for encryption and decryption.

3. Encrypt a File:
    Click the "ENCRYPT" button.
    A file dialog will open. Select the file you want to encrypt.
    The file will be encrypted using the key you provided.

4. Decrypt a File:
    Click the "DECRYPT" button.
    A file dialog will open. Select the file you want to decrypt.
    The file will be decrypted using the same key.

5. Check Console Output: After each operation, a message will be printed in the console indicating the success of the encryption or decryption along with the file name and key used.

# Code Explanation
GUI Components: The GUI is built using Tkinter, with labels, buttons, and input fields to interact with the user.
File Dialogs: The filedialog module is used to open file dialogs for selecting files.
Encryption and Decryption: The XOR operation is applied to the bytes of the file using the provided key.

# Important Notes
Ensure the key entered is numeric; non-numeric keys will not be processed.
Use the same key for both encryption and decryption to successfully revert the file to its original state.
The application modifies the original file; it is recommended to keep a backup of your files before using the encryption/decryption features.

# License
This project is open-source and available under the MIT License.

# Acknowledgments
Thank you to the Python community for providing libraries like Tkinter that make GUI development easier.
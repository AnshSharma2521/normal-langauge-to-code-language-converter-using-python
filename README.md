# **Secret Language Converter**

This project is a Python-based secret language converter that allows users to encode and decode messages using a simple algorithm. The converter adds a layer of randomness and obfuscation to the original text, making it more difficult to decipher without the correct decoding method.

## **Features**

- **Encoding:** Converts a given input message into a "secret" language by adding random characters around the main content of the message.
- **Decoding:** Recovers the original message from the encoded text by stripping away the random characters.
- **Interactive:** The program allows users to continuously encode or decode messages until they choose to stop.

## **How It Works**

### **Encoding**
- The user is prompted to input a message.
- Random characters from the alphabet are selected and added to the message to create the encoded text.
- The encoded text is displayed, and the user can continue encoding more messages or stop the program.

### **Decoding**
- The user is prompted to input an encoded message.
- The program removes the random characters to reveal the original message.
- The decoded message is displayed, and the user can continue decoding more messages or stop the program.
### **Start**
- Enter 1 for code and Enter 0 for decode: 1
- Enter what you want to say: hello
- Encoded message: xyzhellonop

- Enter 1 for code and Enter 0 for decode: 0
- Enter word for decode: xyzhellonop
- Decoded message: hello


## **Getting Started**

### **Prerequisites**

- Python 3.x installed on your system.

### **Installation**

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/secret-language-converter.git

# **Author**
- Ansh Sharma


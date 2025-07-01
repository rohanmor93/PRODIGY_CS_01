def caesar_cipher(text, shift, mode='encrypt'):
    result = ''
    
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            offset = shift if mode == 'encrypt' else -shift
            result += chr((ord(char) - base + offset) % 26 + base)
        else:
            result += char  # Keep punctuation and spaces unchanged

    return result

def main():
    print("=== Caesar Cipher Tool ===")
    text = input("Enter the text: ")
    shift = int(input("Enter shift key (integer): "))
    mode = input("Encrypt or Decrypt? (e/d): ").strip().lower()
    
    if mode == 'd':
        result = caesar_cipher(text, shift, mode='decrypt')
    else:
        result = caesar_cipher(text, shift, mode='encrypt')

    print("\nResult:")
    print(result)

if __name__ == "__main__":
    main()

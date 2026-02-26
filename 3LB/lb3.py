from PIL import Image

def encode_lsb(image_path, secret_text, output_path):
    img = Image.open(image_path).convert('RGB')
    encoded = img.copy()
    width, height = img.size

    binary_message = ''.join(format(ord(c), '08b') for c in secret_text) + '1111111111111110'
    
    data_index = 0
    message_len = len(binary_message)
    
    pixels = encoded.load()
    
    for y in range(height):
        for x in range(width):
            if data_index < message_len:
                r, g, b = pixels[x, y]

                new_bit = int(binary_message[data_index])
                new_r = (r & ~1) | new_bit
                
                pixels[x, y] = (new_r, g, b)
                data_index += 1
            else:
                encoded.save(output_path, "PNG")
                return True
    return False

def decode_lsb(image_path):
    img = Image.open(image_path).convert('RGB')
    pixels = img.load()
    
    binary_data = ""
    for y in range(img.height):
        for x in range(img.width):
            r, g, b = pixels[x, y]
            binary_data += str(r & 1)

            if binary_data.endswith('1111111111111110'):
                clean_bin = binary_data[:-16]
                chars = [clean_bin[i:i+8] for i in range(0, len(clean_bin), 8)]
                return "".join(chr(int(b, 2)) for b in chars)
    return "Нічого не знайдено"

original = "input.png" 
output = "stego_result.png"
text = "Oleksandr Shovheniuk 06.04.2004"

if encode_lsb(original, text, output):
    print("Повідомлення зашифровано в файл stego_result.png")
    
    extracted = decode_lsb(output)
    print(f"Перевірка (дешифрування): {extracted}")
else:
    print("Помилка: занадто маленька картинка")
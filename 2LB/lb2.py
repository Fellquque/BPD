def calculate_caesar_key(dob_string):
    total = 0
    for char in dob_string:
        if char.isdigit():
            total += int(char)
    return total

def caesar_cipher(text, shift, decrypt=False):
    ukr_lower = 'абвгґдеєжзиіїйклмнопрстуфхцчшщьюя'
    ukr_upper = ukr_lower.upper()
    eng_lower = 'abcdefghijklmnopqrstuvwxyz'
    eng_upper = eng_lower.upper()
    
    if decrypt:
        shift = -shift
        
    result = ""
    for char in text:
        if char in ukr_lower:
            result += ukr_lower[(ukr_lower.index(char) + shift) % 33]
        elif char in ukr_upper:
            result += ukr_upper[(ukr_upper.index(char) + shift) % 33]
        elif char in eng_lower:
            result += eng_lower[(eng_lower.index(char) + shift) % 26]
        elif char in eng_upper:
            result += eng_upper[(eng_upper.index(char) + shift) % 26]
        else:
            result += char
    return result

def vigenere_cipher(text, key, decrypt=False):
    ukr_lower = 'абвгґдеєжзиіїйклмнопрстуфхцчшщьюя'
    ukr_upper = ukr_lower.upper()
    eng_lower = 'abcdefghijklmnopqrstuvwxyz'
    eng_upper = eng_lower.upper()
    
    result = ""
    key_index = 0
    key = key.lower()
    
    for char in text:
        shift = 0
        current_key_char = key[key_index % len(key)]
        if current_key_char in eng_lower:
            shift = eng_lower.index(current_key_char)
        elif current_key_char in ukr_lower:
            shift = ukr_lower.index(current_key_char)
            
        if decrypt:
            shift = -shift
            
        if char in ukr_lower:
            result += ukr_lower[(ukr_lower.index(char) + shift) % 33]
            key_index += 1
        elif char in ukr_upper:
            result += ukr_upper[(ukr_upper.index(char) + shift) % 33]
            key_index += 1
        elif char in eng_lower:
            result += eng_lower[(eng_lower.index(char) + shift) % 26]
            key_index += 1
        elif char in eng_upper:
            result += eng_upper[(eng_upper.index(char) + shift) % 26]
            key_index += 1
        else:
            result += char
    return result

def brute_force_caesar(encrypted_text):
    print("\n" + "="*50)
    print("Спроба взлому за допомогою brute force (Шифр Цезаря)")
    print("="*50)
    print(f"Аналіз шифротексту: '{encrypted_text}'\n")

    for shift in range(1, 34):
        attempt = caesar_cipher(encrypted_text, shift, decrypt=True)
        print(f"Спроба зсуву [k={shift:<2}]: {attempt}")
        
    print("="*50 + "\n")

def compare_ciphers(original_text, caesar_key, vigenere_key):
    print("\n=== Порівняльний аналіз шифрів ===")
 
    caesar_encrypted = caesar_cipher(original_text, caesar_key)
    vigenere_encrypted = vigenere_cipher(original_text, vigenere_key)
    
    print("--- Результати шифрування ---")
    print(f"Цезар (зсув {caesar_key}): '{caesar_encrypted}'")
    print(f"Віженер (ключ '{vigenere_key}'): '{vigenere_encrypted}'\n")

    brute_force_caesar(caesar_encrypted)


print("=== Програма для шифрування та криптоаналізу ===")

student_dob = "06.04.2004"
vigenere_word = "shovheniuk"
caesar_shift = calculate_caesar_key(student_dob)

print(f"Дата народження: {student_dob} -> Ключ Цезаря: {caesar_shift}")
print(f"Ключ Віженера: '{vigenere_word}'")

while True:
    test_text = input("\nВведіть текст (або 'вихід' для завершення): ")
    if test_text.lower() == 'вихід':
        break
    if not test_text.strip():
        continue
        
    compare_ciphers(test_text, caesar_shift, vigenere_word)
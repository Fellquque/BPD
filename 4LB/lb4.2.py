import hashlib

doc_name = "document.txt"
doc_content = "Цей документ містить офіційні результати Лабораторної роботи №4 студента Шовгенюка Олександра."

with open(doc_name, "w", encoding="utf-8") as f:
    f.write(doc_content)
print(f"Файл '{doc_name}' успішно створено.")

try:
    with open("private.key", "r") as f:
        private_key = int(f.read())
except FileNotFoundError:
    print("Помилка: Спочатку створіть ключі на Кроці 2!")
    exit()

with open(doc_name, "rb") as f:
    file_data = f.read()

file_hash_hex = hashlib.sha256(file_data).hexdigest()
file_hash = int(file_hash_hex[:8], 16) 
print(f"Хеш документа '{doc_name}': {file_hash}")

signature = file_hash ^ private_key

with open("signature.sig", "w") as sig_file:
    sig_file.write(str(signature))

print(f"Підпис успішно створено та збережено у 'signature.sig': {signature}")
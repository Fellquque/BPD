import hashlib

def get_file_hash(filename):
    with open(filename, "rb") as f:
        data = f.read()
    file_hash_hex = hashlib.sha256(data).hexdigest()
    return int(file_hash_hex[:8], 16)

with open("private.key", "r") as f:
    private_key = int(f.read())
with open("signature.sig", "r") as f:
    stored_signature = int(f.read())

print("=== ТЕСТУВАННЯ СИСТЕМИ ЗАХИСТУ ===")

print("\nЗміна вмісту документа...")
with open("document.txt", "a", encoding="utf-8") as f:
    f.write(" (змінено хакером)")

current_hash = get_file_hash("document.txt")
decrypted_hash = stored_signature ^ private_key

if decrypted_hash == current_hash:
    print("Результат: Підпис ДІЙСНИЙ")
else:
    print("Результат: Підпис ПІДРОБЛЕНИЙ (Документ було змінено!)")

print("\nСпроба використати випадковий підпис...")
fake_signature = 99999999

if (fake_signature ^ private_key) == current_hash:
    print("Результат: Підпис ДІЙСНИЙ")
else:
    print("Результат: Підпис ПІДРОБЛЕНИЙ (Ключ або підпис невірні!)")
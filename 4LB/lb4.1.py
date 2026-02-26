import hashlib

last_name = "Shovheniuk"
dob = "06042004"
secret_word = "aboba"

raw_private_data = f"{last_name}{dob}{secret_word}"
private_key_hash = hashlib.sha256(raw_private_data.encode()).hexdigest()
private_key = int(private_key_hash[:8], 16) 

public_key = (private_key * 7) % 1000007

with open("private.key", "w") as priv_file:
    priv_file.write(str(private_key))

with open("public.key", "w") as pub_file:
    pub_file.write(str(public_key))

print(f"Приватний ключ згенеровано: {private_key}")
print(f"Публічний ключ згенеровано: {public_key}")
print("Файли private.key та public.key створено успішно.")
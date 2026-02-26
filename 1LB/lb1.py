import re

def analyze_password(password, first_name, last_name, dob):
    score = 0
    recommendations = []
    personal_data_found = []

    password_lower = password.lower()
    first_name_lower = first_name.lower()
    last_name_lower = last_name.lower()

    dob_parts = dob.split('.')
    day, month, year = dob_parts[0], dob_parts[1], dob_parts[2]

    personal_strings = {
        "Ім'я": first_name_lower,
        "Прізвище": last_name_lower,
        "Рік народження": year,
        "День народження": day,
        "Місяць народження": month,
        "День і місяць": day + month
    }

    for key, val in personal_strings.items():
        if val in password_lower:
            personal_data_found.append(key)

    if len(password) >= 12:
        score += 4
    elif len(password) >= 8:
        score += 2
    else:
        recommendations.append("Збільште довжину пароля хоча б до 8-12 символів.")

    has_lower = bool(re.search(r'[a-zа-яіїєґ]', password_lower))
    has_upper = bool(re.search(r'[A-ZА-ЯІЇЄҐ]', password))
    has_digit = bool(re.search(r'\d', password))
    has_special = bool(re.search(r'[\W_]', password))

    if has_lower: score += 1
    else: recommendations.append("Додайте малі літери.")
    
    if has_upper: score += 2
    else: recommendations.append("Додайте великі літери.")
    
    if has_digit: score += 1
    else: recommendations.append("Додайте цифри.")
    
    if has_special: score += 2
    else: recommendations.append("Додайте спеціальні символи (наприклад: !, @, #, $, %).")

    if personal_data_found:
        penalty = len(personal_data_found) * 3
        score -= penalty
        recommendations.append(f"Уникайте використання особистих даних! Знайдено: {', '.join(personal_data_found)}.")

    score = max(1, min(10, score))

    print(f"\n--- Результат аналізу ---")
    print(f"Оцінка складності: {score}/10")
    
    if recommendations:
        print("Рекомендації для покращення:")
        for rec in recommendations:
            print(f" - {rec}")
    else:
        print("Чудовий пароль! Рекомендацій немає.")
    print("-" * 25 + "\n")


print("=== Аналізатор безпеки паролів ===")
print("Програма враховує ваші персональні дані для оцінки ризиків.")

student_first_name = "Oleksandr"
student_last_name = "Shovheniuk"
student_dob = "06.04.2004"

while True:
    user_password = input("Введіть пароль для перевірки (або напишіть 'вихід' для завершення): ")
    
    if user_password.lower() == 'вихід':
        print("Роботу завершено. Бережіть свої дані!")
        break
        
    if not user_password.strip():
        print("Пароль не може бути порожнім. Спробуйте ще раз.\n")
        continue

    analyze_password(user_password, student_first_name, student_last_name, student_dob)
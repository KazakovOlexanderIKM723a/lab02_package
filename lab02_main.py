# lab02_main.py (Версія для пакету)
# Основна програма для обробки показників системи "розумний будинок"

# ЗМІНЕНИЙ ІМПОРТ: підключаємо пакет sensors замість файлу stats_module
import sensors as sm 

def parse_input(input_str):
    """Перетворює введений рядок на список дійсних чисел (з перевіркою)."""
    try:
        # Розбиваємо рядок на елементи та конвертуємо у float
        data = [float(x) for x in input_str.split()]
        return data
    except ValueError:
        print("Помилка: введіть коректні числові дані, розділені пробілом.")
        return []

def create_data_dict(temp_list, hum_list, pres_list):
    """Формує словник даних з мітками часу."""
    data = {
        "temperature": {},
        "humidity": {},
        "pressure": {}
    }
    
    # Визначаємо кількість вимірів (беремо мінімальну довжину списків)
    count = min(len(temp_list), len(hum_list), len(pres_list))
    
    for i in range(count):
        key = f"T{i+1}"
        data["temperature"][key] = temp_list[i]
        data["humidity"][key] = hum_list[i]
        data["pressure"][key] = pres_list[i]
        
    return data

def process_measurements(title, data_dict, threshold):
    """Виводить таблицю та статистику для заданого виду даних."""
    if not data_dict:
        print(f"Немає даних для {title}")
        return

    # Виклик функції через пакет (sm.)
    sm.show_table(data_dict, title)
    
    # Обчислення статистики
    avg_val = sm.get_average(data_dict)
    min_val = sm.get_min(data_dict)
    max_val = sm.get_max(data_dict)
    med_val = sm.get_median(data_dict)
    
    print(f"Середнє значення: {avg_val:.2f}")
    print(f"Мінімум: {min_val}")
    print(f"Максимум: {max_val}")
    print(f"Медіана: {med_val}")
    
    # Пошук перепадів
    jumps = sm.find_jumps(data_dict, threshold)
    if jumps:
        # Формування рядка для виводу
        jump_str = ", ".join([f"між {j[0]} -> {j[1]} ({j[2]})" for j in jumps])
        print(f"Різкі перепади: {jump_str}")
    else:
        print("Різких перепадів не виявлено.")

def main():
    print("=== Обробка показів системи 'Розумний будинок' (Пакет) ===")

    # 1) Запит даних
    t_str = input("Введіть температури (°C): ")
    h_str = input("Введіть вологість (%): ")
    p_str = input("Введіть тиск (Па): ")

    # 2) Обробка введених рядків
    temp_list = parse_input(t_str)
    hum_list = parse_input(h_str)
    pres_list = parse_input(p_str)
    
    # Перевірка, чи є дані
    if not temp_list or not hum_list or not pres_list:
        print("Помилка даних. Програму зупинено.")
        return

    # 3) Створення словника
    full_data = create_data_dict(temp_list, hum_list, pres_list)

    # 4) Обробка та вивід результатів
    process_measurements("Temperature", full_data["temperature"], 7)
    process_measurements("Humidity", full_data["humidity"], 20)
    process_measurements("Pressure", full_data["pressure"], 5000)

if __name__ == "__main__":
    main()
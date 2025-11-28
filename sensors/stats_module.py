import statistics

def get_average(data_dict):
    """Повертає середнє значення."""
    if not data_dict:
        return None
    return statistics.mean(data_dict.values())

def get_min(data_dict):
    """Повертає мінімальне значення."""
    if not data_dict:
        return None
    return min(data_dict.values())

def get_max(data_dict):
    """Повертає максимальне значення."""
    if not data_dict:
        return None
    return max(data_dict.values())

def get_median(data_dict):
    """Повертає медіану."""
    if not data_dict:
        return None
    return statistics.median(data_dict.values())

def find_jumps(data_dict, threshold):
    """Знаходить різкі перепади між сусідніми значеннями."""
    jumps = []
    keys = list(data_dict.keys())
    values = list(data_dict.values())

    for i in range(len(values) - 1):
        diff = abs(values[i+1] - values[i])
        if diff > threshold:
            # Формат: (Мітка1, Мітка2, Різниця)
            jumps.append((keys[i], keys[i+1], round(diff, 2)))

    return jumps

def show_table(data_dict, title):
    """Виводить таблицю значень."""
    print(f"\n=== Таблиця показів: {title} ===")
    print(f"{'Мітка часу':<12} | {'Значення'}")
    print("-" * 25)
    for key, value in data_dict.items():
        print(f"{key:<12} {value}")
    print("-" * 25)

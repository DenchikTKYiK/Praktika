def what_to_wear(temperature, precipitation, heavy_precipitation):
    if temperature > 20 and temperature < 31:
        if precipitation:
            return "Футболку, шорты и зонт"
        return "Футболку и шорты"

    if temperature < 0:
        return "Пуховик"

    if precipitation:
        if heavy_precipitation:
            return "Пальто, непромокаемые сапоги и зонт"
        return "Пальто и дождевик"

    return "Пальто"


try:
    temperature = int(input("Введите температуру (в градусах): "))
except ValueError:
    print("Ошибка: введите числовое значение температуры.")
    exit()

precipitation_input = input("Есть ли осадки? (да/нет): ").strip().lower()
if precipitation_input == "да":
    precipitation = True
    heavy_precipitation_input = input("Осадки сильные? (да/нет): ").strip().lower()
    if heavy_precipitation_input == "да":
        heavy_precipitation = True
    else:
        heavy_precipitation = False
else:
    precipitation = False
    heavy_precipitation = False

result = what_to_wear(temperature, precipitation, heavy_precipitation)
print("Рекомендуемая одежда:", result)

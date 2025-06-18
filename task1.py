from pulp import LpMaximize, LpProblem, LpVariable, LpStatus, value, PULP_CBC_CMD

# Опис задачі: максимізувати виробництво лимонаду та фруктового соку, враховуючи обмеження на ресурси.
# Лимонад потребує: 2 од. води, 1 од. цукру, 1 од. лимонного соку.
# Фруктовий сік потребує: 2 од. фруктового пюре, 1 од. води.
# Обмеження: 100 од. води, 50 од. цукру, 30 од. лимонного соку, 40 од. фруктового пюре.

try:
    # Створюємо модель задачі на максимізацію
    model = LpProblem(name="drink-production", sense=LpMaximize)

    # Змінні рішення: цілочисельна кількість лимонаду (x) та фруктового соку (y)
    x = LpVariable(name="lemonade", lowBound=0, cat="Integer")
    y = LpVariable(name="fruit_juice", lowBound=0, cat="Integer")

    # Цільова функція: максимізувати загальну кількість напоїв
    model += x + y, "Total_Production"

    # Обмеження по ресурсах
    model += 2 * x + 1 * y <= 100, "Water_Constraint"  # Вода: 2 од. на лимонад, 1 од. на сік
    model += 1 * x <= 50, "Sugar_Constraint"  # Цукор: 1 од. на лимонад
    model += 1 * x <= 30, "Lemon_Juice_Constraint"  # Лимонний сік: 1 од. на лимонад
    model += 2 * y <= 40, "Fruit_Puree_Constraint"  # Фруктове пюре: 2 од. на сік

    # Розв’язання без виводу службових повідомлень
    status = model.solve(PULP_CBC_CMD(msg=False))

    # Перевірка і вивід результату
    if LpStatus[status] == "Optimal":
        lemonade = x.value()
        fruit_juice = y.value()
        total = value(model.objective)

        print(f"Кількість виробленого лимонаду: {int(lemonade)} одиниць")
        print(f"Кількість виробленого фруктового соку: {int(fruit_juice)} одиниць")
        print(f"Загальна кількість напоїв: {int(total)} одиниць\n")
        print("Використані ресурси:")
        print(f"  Вода: {int(2 * lemonade + fruit_juice)} з 100 одиниць")
        print(f"  Цукор: {int(lemonade)} з 50 одиниць")
        print(f"  Лимонний сік: {int(lemonade)} з 30 одиниць")
        print(f"  Фруктове пюре: {int(2 * fruit_juice)} з 40 одиниць")
    else:
        print(f"Задачу не вдалося розв’язати. Статус: {LpStatus[status]}")

except ImportError:
    print("Помилка: бібліотека PuLP не встановлена. Встановіть її командою: pip install pulp")
except Exception as e:
    print(f"Виникла помилка: {e}")
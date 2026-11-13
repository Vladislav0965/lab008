records = [
    {"title": "Брошюра о выставке", "category": "брошюры", "amount": 8},
    {"title": "Каталог продукции", "category": "каталоги", "amount": 24},
    {"title": "Инструкция по сборке", "category": "брошюры", "amount": 12},
    {"title": "Рекламный плакат A2", "category": "плакаты", "amount": 1},
    {"title": "Годовой отчёт", "category": "каталоги", "amount": 36},
    {"title": "Листовка-приглашение", "category": "брошюры", "amount": 2}]
def totals_by_category(records):
    totals = {}
    for record in records:
        category = record["category"]
        totals[category] = totals.get(category, 0) + record["amount"]
    return totals
def titles_in_category(records, category):
    return [record["title"] for record in records if record["category"] == category]
totals = totals_by_category(records)
print("Сводка по категориям:")
for category in sorted(totals):
    print(f"{category}: {totals[category]}")
user_category = input("Введите категорию: ").strip()
print(titles_in_category(records, user_category))
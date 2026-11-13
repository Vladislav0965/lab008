def record_demo():
    record = {"title": "Python", "hours": 12}
    record["hours"] = 16
    record["completed"] = False
    pair = (record["title"], record["hours"])
    course_title, course_hours = pair
    print("Курс:", course_title)
    print("Часов:", course_hours)
    print("Завершён:", record["completed"])
if __name__ == "__main__":
    record_demo()
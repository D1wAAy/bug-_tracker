bugs = [
    {"id": 1, "title": "Не работает вход",
     "severity": "high", "status": "open"},
    {"id": 2, "title": "Опечатка на главной странице",
     "severity": "low", "status": "closed"},
    {"id": 3, "title": "Не сохраняется расписание",
     "severity": "high", "status": "open"},
    {"id": 4, "title": "Неверный цвет кнопки",
     "severity": "medium", "status": "open"}
]
def find_bug(bugs, bug_id):
    for bug in bugs:
        if bug["id"] == bug_id:
            return bug
    return None
def filter_bugs(bugs, status, severity):
    status = status.strip().lower()
    severity = severity.strip().lower()
    result = []
    for bug in bugs:
        if bug["status"] == status and bug["severity"] == severity:
            result.append(bug)
    return result
def add_bug(bugs, title, severity):
    title = title.strip()
    severity = severity.strip().lower()
    if len(title) < 5 or severity not in ["low", "medium", "high"]:
        return None
    max_id = 0
    for bug in bugs:
        if bug["id"] > max_id:
            max_id = bug["id"]
    new_id = max_id + 1
    new_bug = {"id": new_id, "title": title,
               "severity": severity, "status": "open"}
    bugs.append(new_bug)
    return new_id
def change_status(bugs, bug_id, new_status):
    new_status = new_status.strip().lower()
    allowed = {
        "open": ["in_progress", "closed"],
        "in_progress": ["open"],
        "closed": ["open"],
    }
    if new_status not in allowed:
        return "invalid_status"
    bug = find_bug(bugs, bug_id)
    if bug is None:
        return "not_found"
    if new_status not in allowed[bug["status"]]:
        return "forbidden"
    bug["status"] = new_status
    return "updated"
def build_report(bugs):
    report = {
        "total": 0,
        "by_status": {"open": 0, "in_progress": 0, "closed": 0},
        "by_severity": {"low": 0, "medium": 0, "high": 0},
        "unresolved_high": 0,
    }
    for bug in bugs:
        report["total"] += 1
        report["by_status"][bug["status"]] += 1
        report["by_severity"][bug["severity"]] += 1
        if bug["severity"] == "high" and bug["status"] != "closed":
            report["unresolved_high"] += 1
    return report
def start_selected(bugs, ids):
    if len(ids) == 0:
        return False
    for bug_id in ids:
        if ids.count(bug_id) > 1:
            return False
        bug = find_bug(bugs, bug_id)
        if bug is None:
            return False
        if bug["status"] != "open":
            return False
    for bug_id in ids:
        bug = find_bug(bugs, bug_id)
        bug["status"] = "in_progress"
    return True
def read_id(text):
    text = text.strip()
    if text.isdigit() and int(text) > 0:
        return int(text)
    return None
while True:
    print()
    print("1. Показать все ошибки")
    print("2. Найти по ID")
    print("3. Отфильтровать")
    print("4. Добавить")
    print("5. Изменить статус")
    print("6. Показать отчёт")
    print("7. Назначить несколько ошибок в работу")
    print("0. Выход")
    choice = input("Команда: ").strip()
    if choice == "1":
        for bug in bugs:
            print(bug["id"], bug["title"], bug["severity"], bug["status"])
    elif choice == "2":
        bug_id = read_id(input("ID: "))
        if bug_id is None:
            print("ID должен быть положительным целым числом")
        else:
            bug = find_bug(bugs, bug_id)
            if bug is None:
                print("Ошибка с таким ID не найдена")
            else:
                print(bug["id"], bug["title"], bug["severity"], bug["status"])
    elif choice == "3":
        status = input("Статус: ")
        severity = input("Серьёзность: ")
        found = filter_bugs(bugs, status, severity)
        if len(found) == 0:
            print("Ничего не найдено")
        else:
            for bug in found:
                print(bug["id"], bug["title"], bug["severity"], bug["status"])
    elif choice == "4":
        title = input("Название: ")
        severity = input("Серьёзность (low/medium/high): ")
        new_id = add_bug(bugs, title, severity)
        if new_id is None:
            print("Данные неверны, ошибка не добавлена")
        else:
            print("Добавлена ошибка с ID", new_id)
    elif choice == "5":
        bug_id = read_id(input("ID: "))
        if bug_id is None:
            print("ID должен быть положительным целым числом")
        else:
            new_status = input("Новый статус (open/in_progress/closed): ")
            result = change_status(bugs, bug_id, new_status)
            if result == "updated":
                print("Статус изменён")
            elif result == "invalid_status":
                print("Неизвестный статус")
            elif result == "not_found":
                print("Ошибка с таким ID не найдена")
            elif result == "forbidden":
                print("Такой переход запрещён")
    elif choice == "6":
        report = build_report(bugs)
        print("Всего:", report["total"])
        print("По статусам:", report["by_status"])
        print("По серьёзности:", report["by_severity"])
        print("Нерешённых high:", report["unresolved_high"])
    elif choice == "7":
        parts = input("ID через пробел: ").split()
        ids = []
        correct = True
        for part in parts:
            bug_id = read_id(part)
            if bug_id is None:
                correct = False
            else:
                ids.append(bug_id)
        if not correct:
            print("Все ID должны быть положительными целыми числами")
        elif start_selected(bugs, ids):
            print("Выбранные ошибки переведены в работу")
        else:
            print("Отказ: данные не изменены")
    elif choice == "0":
        print("Выход")
        break
    else:
        print("Неизвестная команда")
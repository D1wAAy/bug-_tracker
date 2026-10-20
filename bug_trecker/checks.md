# Результаты проверок
Каждая проверка начиналась с нового исходного списка: ID 1 (high, open), 2 (low, closed), 3 (high, open), 4 (medium, open). Формат: вызов → ожидалось → получено — вывод.

## Функции
1. find_bug(bugs, 3) → «Не сохраняется расписание» → то же — пройдено
2. find_bug(bugs, 99) → None → None — пройдено
3. find_bug(bugs, 3) после bugs.reverse()` → запись ID 3 → запись ID 3 — пройдено
4. filter_bugs(bugs, " OPEN ", "High") → ID 1, 3 → [1, 3] — пройдено
5. filter_bugs(bugs, "waiting", "high") → [] → [] — пройдено
6. add_bug(bugs, " Не открывается профиль ", "HIGH") → 5, название очищено → 5, «Не открывается профиль» — пройдено
7. add_bug(bugs, "abcd", "low") (4 символа) → None, список не изменён → None, не изменён — пройдено
8. add_bug(bugs, "abcde", "low") (5 символов) → 5 → 5 — пройдено
9. add_bug(bugs, "Название", "urgent") → None, список не изменён → None, не изменён — пройдено
10. add_bug для записей с ID 1 и 4 → 5 → 5 — пройдено
11. add_bug([], "Новая запись", "low") → 1 → 1 — пройдено
12. change_status(bugs, 1, "in_progress") → updated → updated — пройдено
13. change_status(bugs, 1, "closed") → forbidden, данные не изменены → forbidden, не изменены — пройдено
14. change_status(bugs, 2, "open") → updated → updated — пройдено
15. change_status(bugs, 99, "open") → not_found → not_found — пройдено
16. change_status(bugs, 99, "bad") → invalid_status → invalid_status — пройдено
17. change_status(bugs, 1, "open") → forbidden → forbidden — пройдено
18. build_report(bugs)` → total 4; open 3, in_progress 0, closed 1; low 1, medium 1, high 2; unresolved_high 2 → совпало — пройдено
19. build_report([])` → все ключи, значения 0 → совпало — пройдено
20. start_selected(bugs, [1, 3]) → True, обе записи in_progress → то же — пройдено
21. start_selected(bugs, [1, 2]) → False, запись 1 остаётся open → то же — пройдено
22. start_selected(bugs, [1, 99]), [1, 1], [] → False, данные не изменены → то же — пройдено

## Меню
23. 2 → abc, -5, 0 → ошибка, программа работает → сообщение об ошибке — пройдено
24. 2 → 99 → запись не найдена → «Ошибка с таким ID не найдена.» — пройдено
25. 4 → abcd, low → отказ → сообщение об ошибке, запись не добавлена — пройдено
26. 5 → 1, closed → переход запрещён → «такой переход запрещён» — пройдено
27. 7 → 1 x; пустой ввод → отказ, данные не изменены → ошибка ввода; «Отказ: данные не изменены.» — пройдено
28. 4, 5, 7 (3 4), затем 6 → всего 5; open 1, in_progress 3, closed 1; high 3, unresolved_high 3 → совпало — пройдено
29. 9, затем 0 → «неизвестная команда», затем выход → совпало — пройдено

Итог: 29 проверок, все пройдены.
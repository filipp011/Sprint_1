# Исходные списки задач
new_tasks = ['task_001', 'task_011', 'task_007', 'task_015', 'task_005']
completed_tasks = ['task_002', 'task_012', 'task_006']

# 1. Переносим задачу task_005 из new_tasks в completed_tasks
completed_tasks.append('task_005'), new_tasks.remove('task_005')

# 2. Удаляем задачу task_007 из new_tasks
if 'task_007' in new_tasks:
    new_tasks.remove('task_007')

# 3. Выводим последнюю задачу из new_tasks, которая теперь имеет повышенный приоритет
if new_tasks:  # Проверка, что список new_tasks не пуст
    high_priority_task = new_tasks[-1]
    print(f"Следующая задача с повышенным приоритетом: {high_priority_task}")

# Выводим обновленные списки для проверки
print("Обновленный список новых задач:", new_tasks)
print("Список завершенных задач:", completed_tasks)
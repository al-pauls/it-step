import os


def create_lesson_folders(lesson_name, total_tasks=20, dz_tasks=2):
    file_content = """import pygame, sys, color, pg
from pygame.locals import *
"""

    if not os.path.exists(lesson_name):
        os.makedirs(lesson_name)
        print(f"Создана основная папка: {lesson_name}")

    # Создаем папки для основных заданий
    for i in range(1, total_tasks + 1):
        task_folder_name = f"#{i:02d}"
        full_path = os.path.join(lesson_name, task_folder_name)

        if not os.path.exists(full_path):
            os.makedirs(full_path)

        file_path = os.path.join(full_path, "_.py")
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(file_content)

    # Создаем папку dz и папки для домашних заданий (если dz_tasks > 0)
    if dz_tasks > 0:
        dz_root = os.path.join(lesson_name, "dz")
        for i in range(1, dz_tasks + 1):
            dz_task_name = f"#{i:02d}"
            dz_full_path = os.path.join(dz_root, dz_task_name)

            if not os.path.exists(dz_full_path):
                os.makedirs(dz_full_path)

            dz_file_path = os.path.join(dz_full_path, "_.py")
            with open(dz_file_path, "w", encoding="utf-8") as f:
                f.write(file_content)

    print(
        f"Успешно создано {total_tasks} папок для заданий и {dz_tasks} для ДЗ внутри '{lesson_name}'."
    )


# Пример использования:
lesson_num = input("Введите номер урока (например, 10): ").strip()

if lesson_num:
    folder_name = f"L{lesson_num}"

    tasks_input = input(
        "Сколько заданий на уроке? (Enter для 20 по умолчанию): "
    ).strip()
    dz_input = input(
        "Сколько заданий в домашнем задании? (Enter для 2 по умолчанию): "
    ).strip()

    total_tasks = int(tasks_input) if tasks_input.isdigit() else 20
    dz_tasks = int(dz_input) if dz_input.isdigit() else 2

    create_lesson_folders(folder_name, total_tasks, dz_tasks)

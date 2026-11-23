import os


def create_lesson_folders(lesson_name, total_tasks=20, dz_tasks=2):
    file_content = """import pygame, sys
from common import color
from common import pg
from pygame.locals import *
"""

    # Проверяем, существует ли уже папка для урока, если нет — создаем её
    if not os.path.exists(lesson_name):
        os.makedirs(lesson_name)
        print(f"Создана основная папка: {lesson_name}")

    # Создаем папки для основных заданий от 1 до total_tasks
    for i in range(1, total_tasks + 1):
        task_folder_name = f"#{i:02d}"
        full_path = os.path.join(lesson_name, task_folder_name)

        if not os.path.exists(full_path):
            os.makedirs(full_path)

        # Создаем файл _.py внутри папки задания
        file_path = os.path.join(full_path, "_.py")
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(file_content)

    # Создаем папку dz и папки для домашних заданий внутри неё
    dz_root = os.path.join(lesson_name, "dz")
    for i in range(1, dz_tasks + 1):
        dz_task_name = f"#{i:02d}"
        dz_full_path = os.path.join(dz_root, dz_task_name)

        if not os.path.exists(dz_full_path):
            os.makedirs(dz_full_path)

        # Создаем файл _.py внутри папки ДЗ
        dz_file_path = os.path.join(dz_full_path, "_.py")
        with open(dz_file_path, "w", encoding="utf-8") as f:
            f.write(file_content)

    print(
        f"Успешно создано {total_tasks} папок для заданий и {dz_tasks} для ДЗ внутри '{lesson_name}'."
    )


# Пример использования:
folder_input = input("Введите название папки урока (например, L10): ").strip()
if folder_input:
    create_lesson_folders(folder_input)

import csv
import os


def get_files(folder):
    names = os.listdir(folder)
    return [n for n in names if os.path.isfile(os.path.join(folder, n))]


def get_file_info(folder, files):
    result = []
    for name in files:
        size = os.path.getsize(os.path.join(folder, name))
        result.append((name, size))
    return result


def save_csv(rows, csv_path):
    with open(csv_path, "w", newline="", encoding="utf-8-sig") as f:
        writer = csv.writer(f, delimiter=";")
        writer.writerow(["Название", "Размер"])
        writer.writerows(rows)


def main():
    folder = input("Укажите путь: ").strip().strip('"')

    if not os.path.isdir(folder):
        print("Папка не найдена")
        input("Press Enter to exit")
        return

    files = get_files(folder)
    if not files:
        print("Папка пуста")
        input("Press Enter to exit")
        return

    rows = get_file_info(folder, files)

    print(f"\nНайдено файлов: {len(rows)}\n")
    for name, size in rows:
        print(f"{name:<50} {size:>12} байт")

    folder_name = os.path.basename(os.path.normpath(folder))
    csv_path = os.path.join(os.getcwd(), f"{folder_name}.csv")
    try:
        save_csv(rows, csv_path)
    except PermissionError:
        print("\nНе удалось записать файл")
        input("Press Enter to exit")
        return

    print(f"\nФайл сохранён: {csv_path}")
    input("Press Enter to exit")


if __name__ == "__main__":
    main()
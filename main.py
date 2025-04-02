from app.checker import LogsChecker


def main():
    while True:
        folder = input("Enter the path to the folder where you want to search for logs:\n")  # noqa: E501

        try:
            logs_checker = LogsChecker(folder)

        except Exception:
            print('Folder not exist!')

            continue

        extensions = input("Enter the required file extensions separated by space (for example: .txt .logs):\n").split()  # noqa: E501
        contents = input("Enter the contents of the files to be found separated by comma (for example: brut, monotone, green apple):\n").split(', ')  # noqa: E501

        print("Starting search of files... Please, wait...")

        scanned = logs_checker.scan_files(extensions)

        print(f"Files with extensions {extensions} found: {len(scanned)}")

        readed = logs_checker.read_files(scanned, contents)

        print(f"Readed files with matched contents: {len(readed)}")
        print("Starting removing...")

        logs_checker.remove_files(readed)

        print('All logs was removed!')


if __name__ == "__main__":
    main()

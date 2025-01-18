import os

def search_files(keyword, start_directory):
    results = []
    try:
        for root, dirs, files in os.walk(start_directory):
            for file in files:
                if keyword in file.lower():
                    results.append(os.path.join(root, file))
    except PermissionError:
        print("You do not have permission to access some directories.")
    return results

def another_search():
    value = input("Momo: Do you need any other file? (yes/no): ").lower()
    if value == "yes":
        return True
    else:
        print("Goodbye! See you next time!")
        return False

def intro():
    print("Hello! My name is Momo. I will be your chatbot assistant today.")
    print("Momo: You can look for specific files (such as pdf, Word docx, etc.) or look for files using keywords.")
    print("Momo: Really glad you're here!")

def chatbot_search():
    intro()

    while True:
        start_directory = input("Momo: Enter the directory to search in (or press Enter to search 'C:\\Users\\riyas'): ").strip()
        if not start_directory:
            start_directory = r"enter//your//default//directory"

        fileType = input("Momo: Are you specifically looking for a pdf/docx/csv/xl file? Enter the file type or enter None: ").strip().lower()
        if fileType == "none":
            file_type = None
            keyword = input("Momo: Got it. Will look for all types of files. Enter the file name or part of the filename (e.g. resume): ").lower()
        else:
            keyword = input(f"Momo: Got it. Searching for {fileType} files. Enter the file name or part of the filename (e.g. resume): ").lower()
            if fileType == "pdf":
                file_type = ".pdf"
            elif fileType == "docx":
                file_type = ".docx"
            elif fileType == "csv":
                file_type = ".csv"
            elif fileType in ["xl", "xls", "xlsx"]:
                file_type = ".xlsx"
            else:
                print(f"Momo: Sorry, I don't recognize the file type '{fileType}'. Searching all files instead.")
                file_type = None

        results = search_files(keyword, start_directory)

        if file_type:
            results = [file for file in results if file.endswith(file_type)]

        if results:
            print("Momo: Here are the files I found:")
            for result in results:
                print(result)
        else:
            print("Momo: No files found matching your search criteria.")

        if not another_search():
            break

chatbot_search()

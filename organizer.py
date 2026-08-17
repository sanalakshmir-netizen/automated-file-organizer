import os
import shutil

folder_path = "Downloads"

file_categories = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".txt", ".pdf", ".doc", ".docx"],
    "Audio": [".mp3", ".wav"],
    "Videos": [".mp4", ".mkv", ".avi"],
}


def organize_files():
    print("File Organizer Started!")

    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        if os.path.isfile(file_path):

            file_extension = os.path.splitext(filename)[1].lower()

            for category, extensions in file_categories.items():

                if file_extension in extensions:

                    category_folder = os.path.join(
                        folder_path, category
                    )

                    os.makedirs(category_folder, exist_ok=True)

                    shutil.move(
                        file_path,
                        os.path.join(category_folder, filename)
                    )

                    print(f"Moved: {filename} -> {category}")

                    break


if __name__ == "__main__":
    organize_files()
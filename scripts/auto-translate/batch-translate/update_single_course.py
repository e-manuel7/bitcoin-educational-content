import os
import sys
import shutil
import subprocess
from pathlib import Path
from functools import wraps
from typing import List, Callable, Any, Optional

def redirect_output_to_file(filepath: str) -> Callable:
    """Decorator to redirect function output to a file."""
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            original_stdout = sys.stdout
            with open(filepath, 'w') as f:
                sys.stdout = f
                result = func(*args, **kwargs)
            sys.stdout = original_stdout
            return result
        return wrapper
    return decorator

def get_supported_languages(courses_folder: str) -> List[str]:
    """Get list of supported languages from the specified course directory."""
    directory = f"../../../courses/{courses_folder}"
    supported_languages = []

    if os.path.exists(directory):
        for filename in os.listdir(directory):
            if filename.endswith(".md") and filename != "en.md":
                supported_languages.append(filename.split(".")[0])
    else:
        print(f"Directory {directory} does not exist.")

    return supported_languages

def content_exist(filenames: List[str], lang: str) -> bool:
    """Check if content exists for a specific language in given filenames."""
    return any(f.endswith(f"{lang}.md") or f.endswith(f"{lang}.yml") for f in filenames)

def create_txt_to_en_from(courses_folder: str, lang: str) -> None:
    """Create a list of files that need translation from given language to English."""
    base_dir = f"../../../courses/{courses_folder}"
    output_file = f"./translate-to-en/{lang}.txt"
    file_written = False

    with open(output_file, "w") as yml_file:
        for dirpath, dirnames, filenames in os.walk(base_dir):
            for filename in filenames:
                if filename.startswith(f"{lang}.") and not content_exist(filenames, 'en'): 
                    relative_path = os.path.relpath(Path(dirpath) / filename, start=".")
                    yml_file.write(f"{relative_path}\n")
                    file_written = True

    if not file_written:
        os.remove(output_file)
        print(f"No need to translate from {lang}")

def create_txt_from_en_to(courses_folder: str, lang: str) -> None:
    """Create a list of files that need translation from English to given language."""
    base_dir = f"../../../courses/{courses_folder}"
    output_file = f"./translate-from-en/{lang}.txt"
    file_written = False

    with open(output_file, "w") as yml_file:
        for dirpath, dirnames, filenames in os.walk(base_dir):
            for filename in filenames:
                if filename.startswith(f"en.") and not content_exist(filenames, lang): 
                    relative_path = os.path.relpath(Path(dirpath) / filename, start=".")
                    yml_file.write(f"{relative_path}\n")
                    file_written = True

    if not file_written:
        os.remove(output_file)
        print(f"No need to translate from en to {lang}")

def translate_file(input_file: str, target_lang: str) -> None:
    """Translate a single file using translation_controller."""
    try:
        command = ["python3", "../translation_controller.py", input_file, target_lang]
        subprocess.run(command, check=True)
        print(f"Translated {input_file} to {target_lang}")
    except subprocess.CalledProcessError as e:
        print(f"Error translating {input_file}: {e}")

def process_translation_list(list_file: str) -> None:
    """Process a list of files for translation."""
    if not os.path.exists(list_file):
        return

    with open(list_file, 'r') as f:
        files = f.readlines()
        
    for file_path in files:
        file_path = file_path.strip()
        if file_path:
            if list_file.startswith('./translate-to-en/'):
                translate_file(file_path, 'en')
            else:
                lang = Path(list_file).stem
                translate_file(file_path, lang)

def ensure_directory_exists(directory: str) -> None:
    """Create directory if it doesn't exist."""
    if not os.path.exists(directory):
        os.makedirs(directory)
        print(f"Created directory: {directory}")

def cleanup_temp_directories() -> None:
    """Remove temporary translation directories."""
    temp_dirs = ["./translate-to-en", "./translate-from-en"]
    for dir_path in temp_dirs:
        if os.path.exists(dir_path):
            shutil.rmtree(dir_path)
            print(f"Removed temporary directory: {dir_path}")

def main() -> None:
    """Execute the course translation workflow."""
    # Ask user which courses folder to focus on
    courses_folder = input("Enter the courses folder to focus on (e.g., btc101): ").strip()
    
    if not courses_folder:
        print("No courses folder specified. Exiting.")
        return

    languages = get_supported_languages(courses_folder)
    ensure_directory_exists("./translate-to-en")
    ensure_directory_exists("./translate-from-en")
    
    # First pass: translate all non-English content to English
    for lang in languages:
        create_txt_to_en_from(courses_folder, lang)
        to_en_list = f"./translate-to-en/{lang}.txt"
        if os.path.exists(to_en_list):
            print(f"\nProcessing translations from {lang} to English")
            process_translation_list(to_en_list)

    # Second pass: translate English content to other languages
    for lang in languages:
        create_txt_from_en_to(courses_folder, lang)
        from_en_list = f"./translate-from-en/{lang}.txt"
        if os.path.exists(from_en_list):
            print(f"\nProcessing translations from English to {lang}")
            process_translation_list(from_en_list)

    cleanup_temp_directories()
    print("Course translation process completed!")

if __name__ == "__main__":
    main()


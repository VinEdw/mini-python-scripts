# Folder Maker

import os

def make_folders_from_list(names: list[str]):
    parent_dir = os.getcwd()
    mode = 0o666
    for name in names:
        path = os.path.join(parent_dir, name)
        try:
            os.mkdir(path, mode)
            print(f"Directory '{name}' created")
        except OSError as error:
            print(error)

if __name__ == "__main__":
    import calendar
    # `calendar.month_name` gets names, while `calendar.month_abbr` gets abbreviations
    folder_names = [f"{i}-{month}" for i, month in enumerate(calendar.month_abbr)][1:]
    make_folders_from_list(folder_names)
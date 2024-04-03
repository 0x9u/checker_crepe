import subprocess
import random

PATH_EXAMPLE = "1511 crepe_stand"
PATH_PROGRAM = "INSERT_PATH_HERE"


RANDOM_NAMES = [
    "Aiden", "Brooke", "Callum", "Daisy", "Ethan", "Fiona", "Gavin", "Holly",
    "Isaac", "Jade", "Kai", "Lily", "Mason", "Nora", "Owen", "Paige", "Quinn",
    "Riley", "Seth", "Tara", "Umar", "Violet", "Wyatt", "Xena", "Yusuf", "Zoe",
    "Blake", "Chloe", "Dexter", "Eva", "Felix", "Grace", "Henry", "Isla",
    "Jack", "Kelsey", "Leo", "Mia", "Nolan", "Olivia", "Preston", "Quincy",
    "Rebecca", "Skye", "Tristan", "Una", "Victor", "Willow", "Xander", "Yara",
    "Zach", "April", "Brady", "Cora", "Dean", "Elsie", "Finley", "Gemma",
    "Harvey", "Ivy", "Joel", "Kara", "Landon", "Molly", "Noah", "Opal", "Piper",
    "Quinton", "Rosalie", "Sean", "Tessa", "Uriel", "Vanessa", "Wesley", "Xiomara",
    "Yael", "Zane", "Amber", "Bennett", "Cassie", "Dylan", "Ellie", "Freddie",
    "Georgia", "Hugo", "Irene", "Jasper", "Keira", "Logan", "Maya", "Nate", "Oscar"
]

TOTAL_MONTH_DAYS = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

SIGN_CREPES = ["custom", "matcha", "strawberry", "chocolate"]

MODES = ["a", "p", "c", "i", "s", "t", "b", "n", "d", ">", "<", "r", "R", "w", "m"]

class Marker:
    def __init__(self) -> None:
        field : str = input("How many threads (Default 25)? ")
        self.threads = int(field) if field.isnumeric() else 25
        field = input("How many lines before error (Default 100)? ")
        self.lines_before = int(field) if field.isnumeric() else 100
        field = input("How many lines after error (Default 100)? ")
        self.lines_after = int(field) if field.isnumeric() else 100
        field = input("How many commmands in total (Default 10000)? ")
        self.commands = int(field) if field.isnumeric() else 10000
        field = input("How many tests (Default 1000)? ")
        self.tests = int(field) if field.isnumeric() else 1000
    def create_test(self) -> str:
        command = ""
        year = random.randint(1583, 4000)
        month = random.randint(1,12)
        day = random.randint(1, TOTAL_MONTH_DAYS[month - 1])
        mode = random.choice(MODES)
        command += f"{year}-{month}-{day}\\n"
        for _ in range(self.commands):
            command += create_command()
        run_test(command)
    def create_command(self) -> str:
        command = ""
        crepe_type = random.choice(SIGN_CREPES)
        match crepe_type:
            case "a":
                mode = random.choice(SIGN_CREPES)
                command += f"{mode} {random.choice(RANDOM_NAMES)}"
                if mode == "custom":
                    command += f"{random.randint(0, 2)} {random.randint()}"

    def run_test(command: str) -> None:
        pass
    def run(self) -> None:

        


if __name__ == "__main__":


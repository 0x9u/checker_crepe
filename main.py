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

class GameState:
    def __init__(self, id) -> None:
        self.names = []
        self.position_crepes = {} # "Day" Int -> "Crepe Count" Int
        self.days = []

class Marker:
    def __init__(self) -> None:
        print("CREPE TESTER :)\n")
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
        self.games = {} # "Id" Int -> "GameState" GameState
    def create_test(self) -> str:
        command = ""
        year = random.randint(1583, 4000)
        month = random.randint(1,12)
        day = random.randint(1, TOTAL_MONTH_DAYS[month - 1])
        command += f"{year}-{month}-{day}\\n"
        for _ in range(self.commands):
            command += self.create_command()
        self.run_test(command)
    def add_arguments(self, mode : str) -> str:
        arguments = []
        match mode:
            case "a":
                crepe_type = random.choice(SIGN_CREPES)
                arguments.append(crepe_type)
                arguments.append(random.choice(RANDOM_NAMES))
                if crepe_type == "custom":
                    # Batter
                    arguments.append(random.randint(0, 2))
                    # Topping
                    arguments.append(random.randint(0, 3))
                    # Gluten Free
                    arguments.append(random.randint(0,1))
                    # Size
                    arguments.append(random.randint(10,39))
            case "p":
                pass
            case "c":
                pass
            case "i":
                # TODO: maybe keep track of the position cause
                # Majority might be wrong
                
                # Position
                arguments.append(random.choice(0, 50))
                crepe_type = random.choice(SIGN_CREPES)
                arguments.append(crepe_type)
                arguments.append(random.choice(RANDOM_NAMES))
                if crepe_type == "custom":
                    # Batter
                    arguments.append(random.randint(0, 2))
                    # Topping
                    arguments.append(random.randint(0, 3))
                    # Gluten Free
                    arguments.append(random.randint(0,1))
                    # Size
                    arguments.append(random.randint(10,39))
            case "s":
                pass
            case "C":
                # Position 0 - 25 to be less error prone
                arguments.append(random.choice(0, 25))
            case "t":
                pass
            case "b":
                arguments.append(random.choice(RANDOM_NAMES))
            case "n":
                year = random.randint(1583, 4000)
                month = random.randint(1,12)
                day = random.randint(1, TOTAL_MONTH_DAYS[month - 1])
                arguments.append(f"{year}-{month}-{day}")
            case "d":
                pass
            case ">":
                pass
            case "<":
                pass
            case "r":
                arguments.append(random.choice(0, 50))
            case "R":
                year = random.randint(1583, 4000)
                month = random.randint(1,12)
                day = random.randint(1, TOTAL_MONTH_DAYS[month - 1])
                arguments.append(f"{year}-{month}-{day}")
            case "w":
                pass
            case "m":
                pass

        return " ".join(arguments)
    def create_command(self) -> str:
        command = ""
        mode = random.choice(MODES)
        command += mode + " "
        command += self.add_arguments(mode)
        # Delimiter
        command += r"\n"

                    
                
            
        return command
    def run_test(command: str) -> None:
        pass
    def run(self) -> None:

        


if __name__ == "__main__":


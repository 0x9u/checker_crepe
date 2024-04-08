import subprocess
import random
import uuid
import os
from pathlib import Path

"""
Good luck guys.

btw insert ur path to ur program in path_program
e.g. ./crepe_stand
if this file is in same directory

TO RUN THIS DO
python3 main.py

feel free to modify
p.s. if you cant be bothered to copy and paste the code itself
then just import the class and inherit its properties
e.g. class Your_Own_marker(Marker)
where Marker is the super class
"""

"""
Note to self.

TODO:
- Purposely add incorrect commands
- Make it run compile command for file (WITH VALGRIND)
- Compare text with each other
- Find safe threading (to speed up the tasks)
- Make it run config - perhaps??
"""
PATH_EXAMPLE = "1511 crepe_stand"
PATH_PROGRAM = "INSERT_HERE"


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

class Colour:
    END = '\033[0m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'

    @classmethod
    def print_red(cls, text : str) -> None:
        print(f"{cls.RED}{text}{cls.END}")

    @classmethod
    def print_green(cls, text : str) -> None:
        print(f"{cls.GREEN}{text}{cls.END}")

    @classmethod
    def print_yellow(cls, text : str) -> None:
        print(f"{cls.YELLOW}{text}{cls.END}")

    @classmethod
    def print_blue(cls, text : str) -> None:
        print(f"{cls.BLUE}{text}{cls.END}")

    @classmethod
    def print_magenta(cls, text : str) -> None:
        print(f"{cls.MAGENTA}{text}{cls.END}")

    @classmethod
    def print_cyan(cls, text : str) -> None:
        print(f"{cls.CYAN}{text}{cls.END}")

    @classmethod
    def print_white(cls, text : str) -> None:
        print(f"{cls.WHITE}{text}{cls.END}")

class GameState:
    def __init__(self) -> None:
        self.names : list[str] = []
        self.position_crepes : dict[int,int] = {} # "Day" str -> "Crepe Count" Int
        self.days : list[str] = []
        self.current_day : int = 0

class Marker:
    def __init__(self) -> None:
        Colour.print_yellow("CREPE TESTER :)")
        Colour.print_green("TIP: Press <Enter> if you want to go default.")
        Colour.print_green(f"TIP: If you want to log this too do: {__file__.split('/')[-1]} > NAME_OF_FILE.txt\n")
        
        field : str = input("Test name? (Default Test) ")
        self.test_name : str = field if field != "" else "Test"
        
        #field = input("How many threads (WIP - Not Implemented) ? (Default 25)  ")
        #self.threads : int = int(field) if field.isnumeric() else 25
        
        # unused
        field = input("How many differences to show? (Default 3) ")
        self.differences : int = int(field) if field.isnumeric() else 3
        
        field = input("How many lines before error? (Default 100) ")
        self.lines_before : int = int(field) if field.isnumeric() else 100
        
        #field = input("How many lines after error? (Default 100) ")
        #self.lines_after : int = int(field) if field.isnumeric() else 100
        
        field = input("How many commmands in total? (Default 1000) ")
        self.commands : int = int(field) if field.isnumeric() else 1000
        
        field = input("Maximum time (seconds) for program to run? (Default 200) ")
        self.timeout : int = int(field) if field.isnumeric() else 200
        
        field = input("How many tests? (Default 1500) ")
        self.tests : int = int(field) if field.isnumeric() else 1500
        
        field = input("How much padding for output? (Default 50) ")
        self.padding : int = int(field) if field.isnumeric() else 50
        
        self.games : dict[str, GameState] = {} # "Id" Int -> "GameState" GameState
        
        self.success : int = 0
        self.failure : int = 0
    def create_test(self) -> None:
        id : str = str(uuid.uuid1())
        
        command : list[str] = []
        year : int = random.randint(1583, 4000)
        month : int = random.randint(1,12)
        day : int = random.randint(1, TOTAL_MONTH_DAYS[month - 1])
        
        self.games[id] = GameState()
        self.games[id].position_crepes[f"{year}-{month:02}-{day:02}"] = 0
        self.games[id].days.append(f"{year}-{month:02}-{day:02}")
        self.games[id].current_day = 0
        
        command.append(f"{year}-{month:02}-{day:02}")
        for _ in range(self.commands):
            command.append(self.create_command(id))
        del self.games[id]
        
        self.run_test(id, r"\n".join(command))
    def add_arguments(self, id : str, mode : str) -> str:
        arguments = []
        match mode:
            case "a":
                current_day : str = self.games[id].days[self.games[id].current_day]
                self.games[id].position_crepes[current_day] += 1
                crepe_type : str = random.choice(SIGN_CREPES)
                arguments.append(crepe_type)
                arguments.append(random.choice(RANDOM_NAMES))
                if crepe_type == "custom":
                    # Batter
                    arguments.append(str(random.randint(0, 2)))
                    # Topping
                    arguments.append(str(random.randint(0, 3)))
                    # Gluten Free
                    arguments.append(str(random.randint(0,1)))
                    # Size
                    arguments.append(str(random.randint(10,39)))
            case "p":
                pass
            case "c":
                pass
            case "i":
                current_day : str = self.games[id].days[self.games[id].current_day]
                max_position : int = self.games[id].position_crepes[current_day]
                arguments.append(str(random.randint(1, max_position) if max_position > 1 else random.randint(0,256)))
                crepe_type : str = random.choice(SIGN_CREPES)
                arguments.append(crepe_type)
                arguments.append(random.choice(RANDOM_NAMES))
                if crepe_type == "custom":
                    # Batter
                    arguments.append(str(random.randint(0, 2)))
                    # Topping
                    arguments.append(str(random.randint(0, 3)))
                    # Gluten Free
                    arguments.append(str(random.randint(0,1)))
                    # Size
                    arguments.append(str(random.randint(10,39)))
                
                self.games[id].position_crepes[current_day] += 1
            case "s":
                pass
            case "C":
                # Position 0 - 25 to be less error prone
                current_day : str = self.games[id].days[self.games[id].current_day]
                max_position : int = self.games[id].position_crepes[current_day]
                arguments.append(str(random.randint(1, max_position) if max_position > 1 else random.randint(0,256)))
            case "t":
                pass
            case "b":
                arguments.append(random.choice(RANDOM_NAMES))
            case "n":
                year : int = random.randint(1583, 4000)
                month : int = random.randint(1,12)
                day : int = random.randint(1, TOTAL_MONTH_DAYS[month - 1])
                new_date = f"{year}-{month:02}-{day:02}"
                arguments.append(new_date)
                
                self.games[id].days.append(new_date)
                self.games[id].position_crepes[new_date] = 0
                
                current_date = self.games[id].days[self.games[id].current_day]
                self.games[id].days.sort()
                self.games[id].current_day = self.games[id].days.index(current_date)
                
            case "d":
                pass
            case ">":
                self.games[id].current_day += 1;
                self.games[id].current_day %= len(self.games[id].days)
            case "<":
                self.games[id].current_day -= 1;
                self.games[id].current_day %= len(self.games[id].days)
            case "r":
                current_day : str = self.games[id].days[self.games[id].current_day]
                max_position : int = self.games[id].position_crepes[current_day]
                arguments.append(str(random.randint(0, max_position)))
            case "R":
                if random.randint(0,1) == 1:
                    max_year : int = int(self.games[id].days[-1].split("-")[0])
                    min_year : int = int(self.games[id].days[0].split("-")[0])
                else:
                    max_year : int = 9999
                    min_year : int = 1583
                year : int = random.randint(min_year, max_year)
                month : int = random.randint(1,12)
                day : int = random.randint(1, TOTAL_MONTH_DAYS[month - 1])
                date_remove = f"{year}-{month:02}-{day:02}"
                
                arguments.append(date_remove)
                
                if date_remove in self.games[id].days:
                    index = self.games[id].days.index(date_remove)
                    if index == self.games[id].current_day:
                        self.games[id].current_day += 1
                        self.games[id].current_day %= len(self.games[id].days)
                
                    del self.games[id].position_crepes[date_remove]
                    self.games[id].days.remove(date_remove)

                    if len(self.games[id].days) == 0:
                        self.games[id].current_day = 0
                        self.games[id].days.append("2024-01-01")
                        self.games[id].position_crepes["2024-01-01"] = 0
            case "w":
                pass
            case "m":
                pass
            case _:
                raise TypeError("Wtf this shouldn't be happening")

        return " ".join(arguments)
    def create_command(self, id : str) -> str:
        command = ""
        mode = random.choice(MODES)
        
        command += mode
        arguments = self.add_arguments(id, mode)
        if len(arguments) > 0:
            command += " "
        command += arguments
        return command
    def run_test(self, id : str, command: str) -> None:
        try:
            own_program = subprocess.Popen(f"echo \"{command}\" | {PATH_PROGRAM}", \
                                            stdout=subprocess.PIPE,
                                            stderr=subprocess.PIPE, \
                                            universal_newlines=True, \
                                            shell=True)
        except FileNotFoundError:
            Colour.print_red("You need to put your file path in PATH_PROGRAM")
            exit(1)
        sample_program = subprocess.Popen(f"echo \"{command}\" | {PATH_EXAMPLE}", \
                                            stdout=subprocess.PIPE, \
                                            stderr=subprocess.PIPE, \
                                            universal_newlines=True, \
                                            shell=True)
        
        try:
            own_result, own_error_txt = own_program.communicate(timeout=self.timeout)
            sample_result, sample_error_txt = sample_program.communicate(timeout=self.timeout)
        except subprocess.TimeoutExpired:
            own_program.kill()
            sample_program.kill()
            Colour.print_red("Timeout reached")
            self.failure += 1
            return
        
        print(f"Test ID: {id}")
        differences, diff_counter, own_lines, sample_lines = self.compare_texts(own_result, sample_result)
        
        if differences:
            Colour.print_red("Test Failed")
            
            
            first_diff_line_no = differences[0][0]
            start = max(0, first_diff_line_no - self.lines_before)
            if self.lines_before > 0:
                Colour.print_yellow(f"Here are the {self.lines_before} lines (or fewer) before the first difference:\n")
            
            Colour.print_yellow("Line")
            print(f"{'-'*6}+{'-'*(self.padding+2)}+{'-'*(self.padding+2)}")
            for i in range(start, first_diff_line_no - 1):
                print(f"{(i + 1):<5} | {own_lines[i]:<{self.padding+2}} | {sample_lines[i]:<{self.padding+2}}")
            
            Colour.print_yellow(f"\n{'Line':<5} | {'ACTUAL OUTPUT':<{self.padding}} | {'EXPECTED OUTPUT':<{self.padding}}")
            print(f"{'-'*6}+{'-'*(self.padding+2)}+{'-'*(self.padding+2)}")
            
            for line_num, own_line, sample_line in differences:
                print(f"{line_num:<5} - {own_line:<{self.padding+2}} + {sample_line:<{self.padding+2}}")
            
            print(f"\nTotal Differences: {diff_counter}")
            
            folder_path = f"{os.getcwd()}/Bulk Tests/{self.test_name}/{id}/"
            Colour.print_yellow(f"NOTE: Test is logged in folder {folder_path}\n")
            Colour.print_yellow(f"NOTE: You can copy and paste the command from Command.txt from said folder\n")
            
            if len(own_error_txt) > 0:
                Colour.print_red("Your program also returned an error:")
                Colour.print_red(own_error_txt)
            
            if len(sample_error_txt) > 0:
                Colour.print_red("Congrats you managed to break 1511 crepe_stand!!!:")
                Colour.print_red(sample_error_txt)
            
            parent_path = Path(folder_path)
            parent_path.mkdir(parents=True, exist_ok=True)
            
            own_result_path = Path(f"{folder_path}/Actual.txt")
            
            with own_result_path.open("w") as file:
                file.write(own_result)
                file.write(own_error_txt)
            
            sample_result_path = Path(f"{folder_path}/Expected.txt")
            
            with sample_result_path.open("w") as file:
                file.write(sample_result)
                file.write(sample_error_txt)
            
            command_path = Path(f"{folder_path}/Command.txt")
            
            with command_path.open("w") as file:
                file.write(f"echo -e \"{command}\" | {PATH_PROGRAM}")
            
            sample_result_path
            self.failure += 1
        else:
            Colour.print_green("Test Passed")
            self.success += 1
    def compare_texts(self, own_result : str, sample_result : str) -> tuple[list[tuple[int, str, str]], int, list[str], list[str]]:
        own_lines = own_result.splitlines()
        sample_lines = sample_result.splitlines()
        
        max_length = max(len(own_lines), len(sample_lines))
        
        differences : list[tuple[int, str, str]] = []
        
        last_diff_line = -2
        diff_counter = 0
        
        for i in range(max_length):
            own_line = own_lines[i] if i < len(own_lines) else ""
            sample_line = sample_lines[i] if i < len(sample_lines) else ""
            
            if own_line != sample_line:
                differences.append((i + 1, own_line, sample_line))
                if i != (last_diff_line + 1):
                    diff_counter += 1
                last_diff_line = i
            if diff_counter >= self.differences:
                break
        
        return differences, diff_counter, own_lines, sample_lines
    def run(self) -> None:
        try:
            for _ in range(self.tests):
                self.create_test()
        except KeyboardInterrupt:
            pass
        if self.failure > 0:
            Colour.print_red(f"Tests Failed: {self.failure}")
        if self.success > 0:
                Colour.print_green(f"Tests Passed: {self.success}")

if __name__ == "__main__":
    marker = Marker()
    marker.run()

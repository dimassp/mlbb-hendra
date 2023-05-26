import time
import sys
from os import system, name
users_json_path = r'D:\PROGRAMMING\python-3.10.0\hendra\MLBB\json\users.json'
last_login_json_path = r'D:\PROGRAMMING\python-3.10.0\hendra\MLBB\json\last_login_user.json'
heroes_json_dict =  r'D:\PROGRAMMING\python-3.10.0\hendra\MLBB\json\hero_atribut.json'
def clear_screen(sleeptime):
    if name == 'nt':
        time.sleep(sleeptime)
        _ = system('cls')
    else:
        time.sleep(sleeptime)
        _ = system('clear')

def write_per_character(text: str, delay: float, sleeptime: float):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    time.sleep(sleeptime)
    
def yes_no_question_func(text: str):
    yes_no_question = ""
    while yes_no_question.lower() != 'n' and yes_no_question.lower() != 'y':
        write_per_character(text, 0.03,0)
        yes_no_question = input("")
        if yes_no_question.lower() != 'n' and yes_no_question.lower() != 'y':
            write_per_character("Sorry,",0.03, 1.5)
            write_per_character(" your input doesn't seem quite right. Try again", 0.03, 1.5)
            clear_screen(0)
    return yes_no_question.lower()
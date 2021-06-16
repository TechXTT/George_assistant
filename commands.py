import socket

import ipify
import pyautogui
import pyttsx3
import speech_recognition as sr

r = sr.Recognizer()

def SpeakText(command):
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()

def perform_command(command):
    SpeakText('Doing ' +command)

def Calculate(num_1, operation, num_2):
    if operation == '+':
        result = num_1 + num_2
    elif operation == '-':
        result = num_1 - num_2
    elif operation == '*':
        result = num_1 * num_2
    elif operation == '/':
        result = num_1 / num_2
    else:
        SpeakText('Incorrect operation')
        exit
    SpeakText(result)

def get_ip(command):
    if command == 'local':
        hostname = socket.gethostname()
        local_ip = socket.gethostbyname(hostname)

        print(local_ip)
    if command == 'global':
        global_ip = ipify.get_ip()

        print(global_ip)

def open_program(program):
    win_button = pyautogui.locateOnScreen('win.png')
    pyautogui.click(win_button)
    pyautogui.write(program)
    SpeakText('Is this it')
    Answer = get_answer()
    if Answer == 'yes':
        pyautogui.press('enter')
    elif Answer == 'no':
        pyautogui.click(win_button)
        pyautogui.click(win_button)

def get_answer():
    while(1):
        try:
            with sr.Microphone(0) as source2:
                r.adjust_for_ambient_noise(source2, duration=1)

                audio2 = r.listen(source2)
                Answer = r.recognize_google(audio2)
                Answer = Answer.lower()
                if Answer == 'yes' or Answer == 'no':
                    return Answer
                else:
                    SpeakText('I did not hear that could you repeat')

        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))

        except sr.UnknownValueError:
            print("unknown error occured")
        
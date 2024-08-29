import speech_recognition as sr
import pyttsx3
import os
import sys
import subprocess

# Initialize the recognizer and the text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen_command():
    try:
        with sr.Microphone() as source:
            print("Listening...")
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)
            command = recognizer.recognize_google(audio)
            print(f"You said: {command}")
            return command.lower()
    except sr.UnknownValueError:
        print("Sorry, I did not understand that.")
        return ""
    except sr.RequestError:
        print("Could not request results; check your network connection.")
        return ""

def execute_command(command):
    if "open firefox" in command:
        os.system("firefox")

    elif "open chat" in command or "open chatGPT" in command:
        url = "https://chatgpt.com/"  # Replace with your desired URL
        subprocess.Popen([r"firefox", url])

    elif "open youtube" in command:
        url = "https://youtube.com/"  # Replace with your desired URL
        subprocess.Popen([r"firefox", url])

    elif "open reddit" in command:
        url = "https://reddit.com/"  # Replace with your desired URL
        subprocess.Popen([r"firefox", url])

    elif "update pac-man" in command or "update pacman" in command:
        command = 'sudo pacman -Syu'
        subprocess.run(["kitty", "-e", "sh", "-c", command])

    elif "update yay" in command:
        commands = 'yay -Syu'
        subprocess.run(["kitty", "-e", "sh", "-c", commands])

    elif "open github" in command or "opne git hub" in command:
        url = "https://github.com/"  # Replace with your desired URL
        subprocess.Popen([r"firefox", url])        

    elif "computer shut down" in command or "computer am gay" in command or "computer I am gay" in command:
        os.system("shutdown now")

    elif "computer restart" in command:
        os.system("reboot")

    elif "exit program" in command:
        speak("Closing the Program")
        sys.exit()

    else:
        speak("Command not recognized")

if __name__ == "__main__":
    while True:
        command = listen_command()
        if command:
            execute_command(command)
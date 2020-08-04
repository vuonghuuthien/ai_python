import speech_recognition

robot_ear = speech_recognition.Recognizer()
with speech_recognition.Microphone() as mic:
    print ("Robot: I'm Listening")
    audio = robot_ear.listen(mic)

try:
    you = robot_ear.recognize_google(audio)
except:
    you == ""

print("You: " + you)

robot_brain = ""
if you == "hello":
    robot_brain = "hello thomas"
elif you == "today":
    robot_brain = "saturday"
elif you == "":
    robot_brain = "I can't hear you, try again"
else :
    robot_brain = "I can updated"

print(robot_brain)

import pyttsx3

robot_mouth = pyttsx3.init()
robot_mouth.say(robot_brain)
robot_mouth.runAndWait()


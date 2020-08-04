import speech_recognition
import pyttsx3

robot_ear = speech_recognition.Recognizer()
robot_brain = ""
robot_mouth = pyttsx3.init()
you = ""

while True:
    with speech_recognition.Microphone() as mic:
        print ("Robot: I'm Listening")
        audio = robot_ear.listen(mic)
    print ("Robot: ...")
    try:
        you = robot_ear.recognize_google(audio)
    except:
        you = ""
    print ("You: " + you)
    if you == "hello":
        robot_brain = "hello thomas"
    elif you == "today":
        robot_brain = "saturday"
    elif you == "":
        robot_brain = "I can't hear you, try again"
    elif you == "bye":
        robot_brain = "Bye"
        print ("Robot: " + robot_brain)
        robot_mouth.say(robot_brain)
        robot_mouth.runAndWait()
        break
    else :
        robot_brain = "I need updated"

    print ("Robot: " + robot_brain)
    robot_mouth.say(robot_brain)
    robot_mouth.runAndWait()


import time
import datetime
import docx
import speech_recognition as sr

#****************User instruction for file selection***********************

print("""Please tell me, in which format would you like to save your speech :- 
                Press 1 :-  for MS Word Document 
                Press 2 :-  for Notepad Document""")
doc_type = int(input("Enter your option here :- "))

#************ CREATING UNIQUE FILE NAME for each run **************************
today = datetime.date.today()
current_time = time.strftime("%H:%M:%S", time.localtime())
current_date = today.strftime("%Y/%m/%d")
current_date = current_date.replace("/","_")
current_time = current_time.replace(":","")
unique_name = current_date+current_time
#------------------------------------------------------------------------------

r = sr.Recognizer()
with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source, duration=5)
    print("Let's Start Speaking......... ")
    audio_text = r.listen(source)
    print("Long pause, Considering you are done. thank you :) ")
    try:
        my_text = r.recognize_google(audio_text)
        if doc_type == 1:
            mydoc = docx.Document()
            mydoc.add_paragraph(my_text)
            create_Doc_file = "{}.docx".format(unique_name)
            mydoc.save(create_Doc_file)
        elif doc_type ==2:
            create_txt_file = "{}.txt".format(unique_name)
            with open(create_txt_file, "w") as mytxtfile:
                mytxtfile.write(my_text)
        else:
            print("Could not save your speech, wrong file type selected")
    except:
        print("Sorry, I did not get that")

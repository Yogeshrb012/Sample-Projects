import pyttsx3
import PyPDF2
#initialize the pyttsx3 module
text_to_speech = pyttsx3.init()

path = open('18CS52_CNS_Module_1_Notes.pdf', 'rb') #18CS52...is sample pdf
page_number = int(input("Enter which page do you want to convert into speech: "))

#read file using PdfFileReader() function
file = PyPDF2.PdfFileReader(path)
page = file.getPage(page_number)

#to extract text from specified page
text = page.extractText()

#convert text to speech
text_to_speech.say(text)
text_to_speech.runAndWait()

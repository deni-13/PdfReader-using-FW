import pyttsx3
import PyPDF2

hikaye= open("pdf-test.pdf","rb")

pdfoku=PyPDF2.PdfFileReader(hikaye)

engine= pyttsx3.init()
voices= engine.getProperty('voices')

engine.setProperty('voice',voices[0].id) #erkek 1 kadın sesi 0

for sayfano in range (0,pdfoku.numPages):
    sayfa=pdfoku.getPage(sayfano)
    yazi=sayfa.extractText()
    engine.say(yazi)
    engine.runAndWait()

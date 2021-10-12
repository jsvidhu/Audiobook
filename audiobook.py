import pyttsx3
import PyPDF2

book= open('sample.pdf','rb')
pdfread=PyPDF2.PdfFileReader(book)
pages = pdfread.numPages
print("The number of pages :",pages)
speaker = pyttsx3.init()
page = pdfread.getPage(10)
text = page.extractText()
speaker.say(text)
speaker.runAndWait()
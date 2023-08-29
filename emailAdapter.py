import glob
from pathlib import Path
from sendEmail import SendEmail

import subprocess

class EmailAdapter:
    def __init__(self):
        pass
    
    def mail(self):
        self.sendEmailMachine = SendEmail()
                
        address = input("Enter email address to send Email?")
        address.replace("\n", "")
        
        self.__displayOptions(address)
        
        print("Succssfully sent!!")
    
    def __displayOptions(self, emailAddress):
        while (True):
            print("Choose one PDF (relative path from Generated PDFS) to send from list below!!")
            filepaths = glob.glob("GeneratedPDFS/*.pdf")
            for index, file in enumerate(filepaths):
                filename = Path(file).stem
                print(str(index+1) + " " + filename)
            choosenPDF = input("")
            
            pdfpath = glob.glob("GeneratedPDFS/"+choosenPDF)
            if len(pdfpath) > 0:
                for file in pdfpath:
                    print(file)
                    # Run the other script
                    #subprocess.run(["python", "sendEmail.py", emailAddress, f"{file}.pdf"])
                    self.sendEmailMachine.email_send(emailAddress, f"{file}")
            break
        

    
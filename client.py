from emailAdapter import EmailAdapter
from fileType import FileType

import os

if __name__ == '__main__':
    
    decidedAction = 0
    
    playProgram = True
    
    while (playProgram):
        while (True):
            chooseAction = input("Enter your value: \nType 1 to send Generated PDFS or 2 to generate PDFS ")
            decidedAction = int(chooseAction)
            
            try:
                if (decidedAction == 1 or decidedAction == 2) :
                    break
                else:
                    print("Inappropiate action selected!!\n")        
            except:
                print("Inappropiate action selected!!\n")
        
        if (decidedAction == 1):
            emailAdapter = EmailAdapter()
            emailAdapter.mail()
        elif (decidedAction == 2):
            fileGenerator = FileType()
            
            methodDecision = input("Choose method. Type \"1\" for textfiles, \"2\" for csv files, otherwise excell files ")
            fileGenerator.chooseMethod(int(methodDecision))
            
            filePaths = input("Enter file path of method choosen ")
            fileGenerator.selectFiles(filePaths)
            
            fileGenerator.generateFiles()
        
        
        while (True):
            quit = input("Press 0 if you want to exit, any other number means to continue ")

            try:
                if (int(quit) == 0):
                    playProgram = False
                break
            except:
                pass
        
        if (not playProgram):
            break
        
        os.system('cls')
        
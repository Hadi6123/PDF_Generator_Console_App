from strategy import *

class FileType:
    
    __method = None
    
    def __init__(self):
        self.__method = TextStrategy()
    
    def chooseMethod(self, methodName):
        try:
            if (methodName == 1):
                print("Dealing with text files")
                self.__method = TextStrategy()
            elif (methodName == 2):
                print("Dealing with CSV files")
                self.__method = CSVStrategy()
            else:
                print("Dealing with Excell files")
                self.__method = ExcelStrategy()
        except:
            print("Dealing with Excell files")
            self.__method = ExcelStrategy()
    
    def selectFiles(self, path):
        self.__method.choose_file(path)
        
    def generateFiles(self):
        askName = input("Enter name of PDF to be generated!!  ")
        self.__method.generate(askName)
        print("Successfully Completed!!")
            
    
    
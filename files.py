from tkinter import StringVar

class settingsFile:
    def __init__(self):
        self.settings = [StringVar(),StringVar(),StringVar()]
        self.settings[0].set("en")
        self.settings[1].set("danger")
        self.settings[2].set("darkly")
    def saveFile(self):
        with open("settings.conf","w") as saves_file:
            saveData=""
            saveData = saveData + str(self.settings[0].get()) + ","
            saveData = saveData + str(self.settings[1].get()) + ","
            saveData = saveData + str(self.settings[2].get()) + ","
            #saveData = saveData + str(showLog.get()) + ","
            #saveData = saveData + str(autoConnect.get()) + ","
            saves_file.write(saveData[:-1])

        #messagebox.showinfo(lang.software_name,"You need to restart the\nsoftware for changes to apply.\n\nDu musst das Programm neustarten, damit\nänderenungen angewendet werden.")

    def loadFile(self):
        with open("settings.conf","r") as saves_file:
                saveData=saves_file.read().split(',')
                try:
                    self.settings[0].set(saveData[0])
                    self.settings[1].set(saveData[1])
                    self.settings[2].set(saveData[2])
                except:
                    pass
                #showLog.set(int(saveData[1]))
                #autoConnect.set(int(saveData[2]))

    def getSetting(self,id):
        return self.settings[id].get()

global file

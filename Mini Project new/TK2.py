from tkinter import *
import config
def main():
        root = Tk()
        global r
        r=StringVar(root,"4")
        gui = Window(root)
        gui.root.mainloop()
        
        return None

class Window:
        
        def __init__(self, root):
                self.root = root
                self.root.geometry('700x550')
                self.root.title("Diary")
                # Create textspace
                self.textspace = Text(self.root)
                self.textspace.grid(row=0, column = 0)
                # Create open and save buttons
                Button(self.root, text = "Save", command = self.writefile).grid(row=0, column = 1)
                #Button(self.root, text = "Open", command = self.openfile).grid(row=0, column = 2)
                self.openfile()
                Label(self.root, text = "Enter your mood today").grid(row=2, column = 0)
                Radiobutton(self.root,text="1",variable=r,value=1,command=self.moodsave).grid(row=3, column = 0)
                Radiobutton(self.root,text="2",variable=r,value=2,command=self.moodsave).grid(row=4, column = 0)
                Radiobutton(self.root,text="3",variable=r,value=3,command=self.moodsave).grid(row=5, column = 0)
                Radiobutton(self.root,text="4",variable=r,value=4,command=self.moodsave).grid(row=6, column = 0)
                Radiobutton(self.root,text="5",variable=r,value=5,command=self.moodsave).grid(row=7, column = 0)
                #self.pr="Your mood is "+str(r.get())
                pass
        def moodsave(self):
                self.pr="Your mood is "+ r.get()
        def writefile(self):
                #savegui = Tk()
                #savegui.geometry('560x50')
                filecontents = self.textspace.get(0.0, END)
                
                #def writefile():
                config.fname="svf/"+config.cuser+"-"+config.date + '.txt'
                with open(config.fname, 'w+') as file:
                        file.write(filecontents)
                        file.write("\n\n\n\n\n\n\n")
                        file.write(self.pr)
                                #Label(savegui,text=self.pr).grid(row=9,column=0)
                        file.close()
                        self.root.destroy()
                                #savegui.destroy()
                
                #Label(savegui, text = "File Name").grid(row=0, column = 0)
                #file_name = Entry(savegui, width = 40)
                #file_name.grid(row=0, column=1)
                
                #Button(savegui, text = "Save", command = writefile).grid(row=0, column = 1)
                
                
                
                return None
        def openfile(self):
                        try:
                                with open(config.fname, "r") as file:
                                        self.textspace.delete(0.0, END)
                                        self.textspace.insert(0.0, file.read())
                                        file.close()
                        except FileNotFoundError:
                                print("FILE NOT FOUND")
                        return None
        
        '''def openfile(self):
                opengui = Tk()
                opengui.geometry('560x50')
                def opennew():
                        try:
                                with open(file_name.get(), "r") as file:
                                        self.textspace.delete(0.0, END)
                                        self.textspace.insert(0.0, file.read())
                                        file.close()    
                                        opengui.destroy()
                        except FileNotFoundError:
                                file_name.delete(0.0, END)
                                file_name.insert(0.0, "FILE NOT FOUND. TRY ANOTHER")
                        
                        return None
                
                Label(opengui, text = "File Name along with extension").grid(row=0, column = 0)
                file_name = Entry(opengui, width = 40)
                file_name.grid(row=0, column=1)
                
                Button(opengui, text = "Open", command = opennew).grid(row=0, column = 2)
                return None'''
        
        
        pass

main()

from tkinter import Tk,BOTH,W,N,E,S,NW,NE,CENTER
from tkinter.ttk import Frame,Button,Label,Style
import tkinter as tk
import pprint

class Home(Frame):

    def __init__(self,data):
        self.data = data
        print(pprint.pprint(self.data))
        super().__init__()
        self.initUI()
        print('--------------------------------HAHAHAHAHAHA------------------------------------')
        try:
            with open('data.properties','r') as f:
                print(f.readlines())
        except:
            print('file error')
    
    def initUI(self):
        self.master.title("Home")
        self.pack(fill=BOTH,expand=False)
    
    def labelfont(self,family='times',size=15,weight=''):
        return (family,size,weight)
    
    def search(self,title,experience,pub,qualification):
        print(f'{title.get()} {experience.get()} {pub.get()} {qualification.get()}')
        match = []
        unMatch = []
        for user in self.data:
            us = user.get('personal_info','').get('headline','')
            publication = user.get('accomplishments','').get('publications','')
            educ = user.get('experiences','').get('education','')
            if str(title.get()).lower() in str(us).lower() and len(publication)>=int(pub.get()) and len([e for e in educ if str(qualification.get()).lower() in str(e.get('field_of_study')).lower() ])>0:
                match.append(str(user.get('personal_info',"Error 1").get('name',"Error 2"))+'.docx')
            else:
                unMatch.append(str(user.get('personal_info',"Error 1").get('name',"Error 2"))+'.docx')
        print(match)            

        

    def design(self,root):
        # text1 = tk.Label(root,text="Dashboard")
        # text1.place(anchor=NW)
        # text1.configure(bg='#00A2E5',fg='black')
        # text1.config(font=self.labelfont('times', 20, 'bold'))
        # text1.config(height=1,width=16)
        # b1 = Button(root, text = "Logout") 
        # b1.place(relx = 1, x =-2, y = 2, anchor = NE)
        # b2 = Button(root, text = "Search Resume") 
        # b2.place(relx = 1,x=-2,y=1, anchor = S)
        text2 = tk.Label(root,text="Resume for Fucality Position")
        text2.pack()
        title_var = tk.StringVar()
        title = tk.Entry(root,width=25 ,textvariable=title_var)
        title.config(font=self.labelfont('time',10,''))
        title.focus()
        title.pack()
        experience_var = tk.StringVar()
        experience = tk.Entry(root,width=25 ,textvariable=experience_var)
        experience.config(font=self.labelfont('time',10,''))
        experience.pack()
        publication_var = tk.StringVar()
        publication = tk.Entry(root,width=25 ,textvariable=publication_var)
        publication.config(font=self.labelfont('time',10,''))
        publication.pack()
        qualification_var = tk.StringVar()
        qualification = tk.Entry(root,width=25 ,textvariable=qualification_var)
        qualification.config(font=self.labelfont('time',10,''))
        qualification.pack()
        button = tk.Button(root,text="Search",command=lambda:self.search(title_var,experience_var,publication_var,qualification_var))
        button.configure(bg="#00A2F1",fg="black")
        button.config(height=2,width=15)
        button.pack()


def main(data):
    root = Tk()
    root.geometry("750x400+700+400")
    app = Home(data)
    root['bg']='#00A2E5'
    root.resizable(False,False)
    app.design(root)
    root.mainloop()

    
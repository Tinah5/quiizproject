#import MySQLdb

import mysql.connector
from tkinter import * #import all libraries of tkinter
from tkinter import messagebox
from tkinter import ttk
import random
import csv
######################################################

####First Window

class MainWindow:

    def __init__(self, mainWin):
        self.mainWin = mainWin
        self.mainWin.geometry("1000x600+0+0")
        self.mainWin.title("Welcome To Quizz App")
        self.mainWin.config(bg="white")

        f = Frame(self.mainWin, height=800, width=1000, bg="#F0E68C", relief="ridge", bd=10)
        f.propagate(0)
        f.pack()
        #insert photo into main window 
        self.mainphoto = PhotoImage(file="QMe2.png")
        frontimg = Label(f, image=self.mainphoto, bg="azure")
        frontimg.place(x=100, y=50)

        #self.mainTitle = Label(f, text="QUIZ ME", fg="Blue" ,bg="white", font=("Calibri",50, "bold")).place(
           # x=450, y=100)
        #self.mainTitle=label2(f, text="Online Quiz Application in Python Programming", fg="Blue" ,font=("Calibri", 30,"bold italic")).place(x=50, y=100)
        #fg - font color bg- backgroud color
        #call signup window
        self.sign = Button(f, text="Sign up", width=10, height=1, fg="#D68910", bg="white",
                           font=("Comic Sans MS",16, "bold"), command=self.c_reg)
        #call login window 
        self.login = Button(f, text="Login", width=10, height=1, fg="#D68910", bg="white",
                            font=("Comic Sans MS", 16, "bold"), command=self.c_login)
        self.sign.place(x=200, y=400)
        self.login.place(x=600, y=400)
        #self.sign.pack(ipadx=5,ipady=5)
    
        
#Sign up method
    def c_reg(self):
        self.newWindow = Toplevel(self.mainWin)
        self.newWindow.resizable(0, 0)
        self.app = Register(self.newWindow)
#login method
    def c_login(self):
        self.login = Toplevel(self.mainWin)
        self.login.resizable(0, 0)
        self.log = Login(self.login)


######################
#############   Sign In Window     ###########################
class Register:

    def __init__(self, mainWin):
        global mReg
        mReg = mainWin
        self.mainWin= mainWin
        self.mainWin.geometry("1000x600+0+0")
        self.mainWin.title("Sign up Window")
        self.mainWin.config(bg="white")
        global f1
        f1 = Frame(self.mainWin, height=800, width=1000, bg="#275DF8", relief="ridge", bd=20)
        f1.propagate(0)
        f1.pack()
        ################## Image#####################

        self.mainphoto1 = PhotoImage(file="QMesignin.png")
        frontimg = Label(f1, image=self.mainphoto1, bg="azure")
        frontimg.place(x=400, y=100)
        self.radio_var=IntVar()
        self.radio_var.set(2)

     

        self.mainTitle = Label(f1, text="Sign In", bg="white",fg="Blue",
                               font=("calibri", 30, "bold")).place(x=250, y=10)
        self.name = Label(f1, text="First Name  ", bg="white", font=("calibri", 16))
        self.lname = Label(f1, text="Last name  ", bg="white", font=("calibri", 16))
        self.email = Label(f1, text="Email      ", bg="white", font=("calibri", 16))
        self.uname = Label(f1, text="Username   ", bg="white", font=("calibri", 16))
        self.pw = Label(f1, text="Password      ", bg="white", font=("calibri", 16))
        self.utype=Label(f1,text="User Type     ", bg="white", font=("calibri", 16))
        self.rb1=Radiobutton(f1,text="Admin User", variable=self.radio_var, value=1,bg="white", font=("calibri", 16,"bold"))
        self.rb2=Radiobutton(f1,text="User      ", variable=self.radio_var, value=2,bg="white", font=("calibri", 16,"bold"))

        self.var = IntVar()
        

        self.tname = Entry(f1,width=30)
        self.tlname = Entry(f1, width=30)
        self.temail = Entry(f1, width=30)
        self.tuname = Entry(f1, width=30)
        self.tpw = Entry(f1, width=30, show="*")
        

        self.submit = Button(f1, text="Submit", width=12, height=1, fg="#D68910", bg="white",
                             font=("comic sans MS", 16, "bold"), command=self.c_submit)
        self.cancel = Button(f1, text="Cancel", width=12, height=1, fg="#D68910", bg="white",
                             font=("comic sans MS", 16, "bold"), command=self.c_cancel)

        self.checkB = Checkbutton(f1, text='Show Password', bg="lightsteelblue1", fg="navy",
                                  font=("comic sans MS", 12, "bold"), variable=self.var, onvalue=1,
                                  offvalue=0, command=self.Showpasswd)

        self.name.place(x=50, y=100)
        self.tname.place(x=200, y=100)
        self.lname.place(x=50, y=150)
        self.tlname.place(x=200, y=150)
        self.email.place(x=50, y=200)
        self.temail.place(x=200, y=200)
        self.uname.place(x=50, y=250)
        self.tuname.place(x=200, y=250)
        self.pw.place(x=50, y=300)
        self.tpw.place(x=200, y=300)
        self.utype.place(x=50,y=390)
        self.rb1.place(x=200,y=390)
        self.rb2.place(x=390,y=390)
        self.submit.place(x=200, y=500)
        self.cancel.place(x=500, y=500)
        self.checkB.place(x=195, y=330)

    def Showpasswd(self):
        if (self.var.get()):
            self.tpw.config(show="")
        else:
            self.tpw.config(show="*")  

    #check all the feilds are filled 
    def check(self, l1):
        ht = 50
        f = 0
        s = 0
        for i in range(5):
            ht = ht + 50
            if len(l1[i]) == 0:
                self.l = Label(f1, text="! You cannot leave this empty", fg='red', bg="azure")
                self.l.place(x=400, y=ht)
            else:
                self.l = Label(f1, text="! You cannot leave this empty", bg="azure", fg="azure")
                self.l.place(x=400, y=ht)
                f = f + 1
        if l1[2].find("@") == -1 and l1[2].find(".") == -1 and len(l1[2]) != 0:
            self.l = Label(f1, text="! Please enter a valid email id", bg="azure", fg="red")
            self.l.place(x=400, y=200)
            s = 1
        else:
            if (len(l1[2]) > 0):
                self.l = Label(f1, text="! Please enter a valid email id", bg="azure", fg="azure")
                self.l.place(x=400, y=200)
        if len(l1[4]) < 8 and len(l1[4]) != 0:
            self.l = Label(f1, text="! Password must atleast have 8 characters", bg="azure", fg="red")
            self.l.place(x=400, y=300)
        else:
            if (len(l1[4]) > 0):
                self.l = Label(f1, text="! Password must atleast have 8 characters", bg="azure", fg="azure")
                self.l.place(x=400, y=300)
        if (f == 5 and len(l1[4]) >= 8 and s == 0):
            return 1
        else:
            return 0

    def c_submit(self):
            
        #conn = mysql.connector.connect(host='localhost', database='quizdatabase', user='root', password='')
        conn = mysql.connector.connect(host='localhost', database='quizdatabase', user='root', password='mysql')
        cursor = conn.cursor()
        #get entry values for Sign up form
        name = self.tname.get()
        lname = self.tlname.get()
        email = self.temail.get()
        uname = self.tuname.get()
        pw = self.tpw.get()
        
        user=self.radio_var.get() # Admin user =1 , Normal User=2
        #print(user)
        #insert data from sign up form to a list  
        l1 = [name, lname, email, uname, pw,user]

        # checking the return value of check function (if all are filled return 1 else return 0)
        c = self.check(l1)
        
        if c == 1:
            #check whether there is a already taken similer username
            str = "select * from reg where uname='%s'"
            arg = (uname)
            
            cursor.execute(str % arg)
            row = cursor.fetchone()
            
            if row is not None:
                messagebox.showwarning("Error", "Username Already exist!")
                mReg.destroy()
            else:
                try:
                    s = "insert into reg(name,lname,email,uname,p,score,user) values('%s','%s','%s','%s','%s','%d','%d')"
                    #s = "insert into reg(name,lname,email,uname,p,score,user) values('qqq','aaa','ww@gmail.com','wwww','12345678','%d','%d')"
                    
                    
                    arg = (name, lname, email, uname, pw,0,user)
                    cursor.execute(s % arg)
                    conn.commit()
                    
                    #print("DEBUG: 1 ROW ADDED")
                    #clear entry fields 
                    self.tname.delete(0, 'end')
                    self.tlname.delete(0, 'end')
                    self.temail.delete(0, 'end')
                    self.tuname.delete(0, 'end')
                    self.tpw.delete(0, 'end')
                    self.radio_var.set(2)
                    #self.radio_var.set(2)
                    messagebox.showinfo("Success", "Registered Successfully!")
                    mReg.destroy()
                except:
                    conn.rollback()
        cursor.close()
        #mycursor.commit()
        conn.close()
#cancel method
    def c_cancel(self):
        mReg.destroy()

#login window 
class Login:

    def __init__(self, mainWin):
        global mLogin
        mLogin = mainWin
        self.mainWin = mainWin
        self.mainWin.geometry("1000x600+0+0")
        self.mainWin.config(bg="white")

        global f2
        f2 = Frame(self.mainWin, height=800, width=1000, bg="#275DF8", relief="ridge", bd=20)
        f2.propagate(0)
        f2.pack()
        
       


        self.mainphoto1 = PhotoImage(file="QMelogin.png")
        frontimg = Label(f2, image=self.mainphoto1, bg="azure")
        frontimg.place(x=350, y=20)
        self.radio_var=IntVar()
        self.radio_var.set(2)




                
        #self.SubTitle = Label(f2, text="Login", fg="Blue" ,font=("Calibri", 35, "bold")).place(
           # x=300, y=30)
        
        self.l1 = Label(f2, text="Enter Username: ", bg="white", font=("calibri", 14))
        self.e1 = Entry(f2, width=30)
        self.l2 = Label(f2, text="Enter Password: ", bg="white", font=("calibri", 14))
        self.e2 = Entry(f2, width=30, show="*")
        self.b1 = Button(f2, text="Login", width=10, height=1, fg="#D68910", bg="white",
                         font=("Comic sans MS", 16, "bold"), command=self.clicked)
        self.b2 = Button(f2, text="Cancel", width=10, height=1, fg="#D68910", bg="white",
                         font=("Comic sans MS", 16, "bold"), command=self.cancelLogin)

        self.var11 = IntVar()
        self.checkB = Checkbutton(f2, text='Show Password', bg="white", fg="black",
                                  font=("Comic sans MS", 12, "bold "), variable=self.var11, onvalue=1,
                                  offvalue=0, command=self.Showpasswd)

        #self.SubTitle.place(x=100

        self.l1.place(x=100, y=240)
        self.e1.place(x=325, y=250)
        self.l2.place(x=100, y=290)
        self.e2.place(x=325, y=300)
        self.b1.place(x=270, y=426)
        self.b2.place(x=570, y=426)
        self.checkB.place(x=325, y=340)

# display password method
    def Showpasswd(self):
        if (self.var11.get()):
            self.e2.config(show="")
        else:
            self.e2.config(show="*")
# cancelaction
    def cancelLogin(self):
        mLogin.destroy()
#when user click on the login button call the click method 
    def clicked(self):
        #conn = mysql.connector.connect(host='localhost', database='quizdatabase', user='root', password='')
        conn = mysql.connector.connect(host='localhost', database='quizdatabase', user='root', password='mysql')
        cursor = conn.cursor()
        u = self.e1.get()
        pw = self.e2.get()
        self.e1.delete(0, 200)
        self.e2.delete(0, 200)
        
        s = "select * from reg where uname='%s' and p='%s'"
        s1= "select user from reg where uname='%s' and p='%s'"
        
        arg = (u, pw)
        cursor.execute(s % arg)
        result = cursor.fetchall()
        if result:
            cursor.execute(s1%arg)
            result1=cursor.fetchone()#admin user or normal user value
            self.goinaccount(u,result1) # if valid user call goinaccount method
        else:
            messagebox.showerror("Error", "Invalid Username or Password, Try Again!")
            mLogin.destroy()
        cursor.close()
        conn.close()
#going to user account window
    def goinaccount(self, u,result1):
        
        rs=int(result1[0])
        self.accWindow = Toplevel(mLogin)
        self.accWindow.resizable(0, 0)
        # New window for Admin and user
        if rs==1:
            self.adminWindow=AdminWindow(self.accWindow)
        else:
            
            self.acWin = Account(self.accWindow, u)
class AdminWindow:
    def __init__(self,mainWin):
        global mAcc
        self.mainWin=mainWin
        mAcc = mainWin
        self.mainWin.geometry("1000x600+0+0")
        self.mainWin.title("Quiz Assign Window")
        self.mainWin.config(bg="#009FBF")
        f3 = Frame(mAcc, height=800, width=1000, bg="#275DF8", relief="ridge", bd=25)
        f3.propagate(0)
        f3.pack()


        self.mainphoto1 = PhotoImage(file="admin.png")
        frontimg = Label(f3, image=self.mainphoto1, bg="azure")
        frontimg.place(x=350, y=20)
        self.radio_var=IntVar()
        self.radio_var.set(2)




        
        self.startQuiz = Button(f3, text="Create Questions", width=15, height=2, fg="navy", bg="yellow",
                               font=("Calibri", 16, "bold"), command=self.AssignQuestions)
        #self.startQuiz.pack()
        self.startQuiz.place(x=400, y=350)
    def AssignQuestions(self):
        wb=open("Questionsnew1.csv",'r')
        sheet=csv.reader(wb)






        qn=[]
        for row in sheet:
            qn.append(row)
            #print(row)
            
        #sheet.close()

        db_connection = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="mysql",
        #passwd="",
        database="quizdatabase"

        )

        
        db_cursor = db_connection.cursor()
        db_cursor.execute("drop table if exists Questions")
        q = "create table questions(QID int, qstn text, opA text, opB text, opC text, opD text, ans int)"
        db_cursor.execute(q)
        #Code to add rows
        for i in qn:
           # i[0]=int(i[0])
            lst=i
            lst[0]=int(i[0])
            
            lst[6]=int(i[6])
            #print(lst[0],lst[6])
            
            #print(lst)
            q2 = "insert into questions(QID, qstn, opA, opB, opC, opD, ans) values('%d','%s','%s','%s','%s','%s','%d')"
            arg = (lst[0], lst[1], lst[2], lst[3], lst[4], lst[5], lst[6])
            
            db_cursor.execute(q2%arg)
            db_connection.commit()
        messagebox.showerror("Success", "Questions Assign Sucessfully")

        

        db_cursor.close()
        db_connection.close()

        
        

class Account:

    def __init__(self, mainWin, u ):
        global mAcc
        
        self.u = u
        self.mainWin = mainWin
        mAcc = mainWin
        self.mainWin.geometry("1000x600+0+0")
        self.mainWin.title("Quiz Start Window")
        self.mainWin.config(bg="#009FBF")
        f3 = Frame(mAcc, height=901, width=1001, bg="#275DF8", relief="ridge", bd=25)
        f3.propagate(0)
        f3.pack()
        #conn = mysql.connector.connect(host='localhost', database='quizdatabase', user='root', password='')
        conn = mysql.connector.connect(host='localhost', database='quizdatabase', user='root', password='mysql')
        cursor = conn.cursor()
        
        self.welcomepg = Label(f3, text="Welcome to QuizMe", fg="Blue" ,bg="white", font=("calibri", 35, "bold italic")).place(
            x=275, y=30)

        #inser photo into Account  window 
        self.userprof = PhotoImage(file='startquiz.png')
        frontimg = Label(f3, image=self.userprof, bg="white")
        frontimg.place(x=375, y=151)

        
         
        self.startQuiz = Button(f3, text="Start Quiz", width=16, height=1, fg="#D68910", bg="white",
                               font=("comic sans MS", 16, "bold"), command=self.goinside)
        self.startQuiz.place(x=245, y=401)
        self.logout = Button(f3, text="Logout", width=16, height=1, fg="#D68910", bg="white",
                             font=("comic sans MS", 16, "bold"), command=self.logout)
        self.logout.place(x=545, y=401)

#go to quiz start window

    def goinside(self):
        self.quizWindow = Toplevel(self.mainWin)
        self.quizWindow.resizable(0, 0)
        self.qw = Quiz(self.quizWindow, self.u)

    def logout(self):
        mAcc.destroy()


class Quiz:
    def __init__(self, mainWin, u):
        self.user = u
        global mQuiz
        mQuiz = mainWin
        self.mainWin = mainWin
        self.mainWin.geometry("1000x600+0+0")
        self.mainWin.title("E-Quiz")
        self.mainWin.config(bg="light steel blue1")
        global f1
        f = Frame(self.mainWin, height=800, width=1000, bg="#275DF8", relief="ridge", bd=20)
        #conn = mysql.connector.connect(host='localhost', database='quizdatabase', user='root', password='')
        conn = mysql.connector.connect(host='localhost', database='quizdatabase', user='root', password='mysql')
        
        cursor = conn.cursor()


        self.mainphoto1 = PhotoImage(file="QMe.png")
        frontimg = Label(f, image=self.mainphoto1, bg="azure")
        frontimg.place(x=50, y=400)
        self.radio_var=IntVar()
        self.radio_var.set(2)




        # take the questions,options and relavent answers to the lists 
        global l1, answerstemp
        global questions
        questions = []
        global options
        options = []
        global answers,correctAnswer
        answers = []
        answerstemp = []
        s1 = set() # empty set use to store the random question no
#####################
        correctAnswer=[]#use to store correct option for each question for display the question and answer at the end

        while len(s1) < 5:
            strQ = "" # empty variable taken to store the questions
            strA = "" #
            id = random.randint(1, 20)# select random question numbers
            s1.add(id)
            #print(s1)

        while len(s1) > 0:
            #get the randam question and append to the questions list
            s = "select qstn from questions where QID=%d" 
            id = s1.pop()
            arg = (id)
            cursor.execute(s % arg)
            strQ = strQ.join(list(cursor.fetchone()))
            questions.append(strQ)
            opts=[]

            #get the relavant options of each selected question and append to the options list
            s = "select opA,opB,opC,opD from questions where QID=%d"
            arg = (id)
            cursor.execute(s % arg)
            opts=list(cursor.fetchone())
            options.append(opts)
            

            #get the correct answer and store it in the correctAnswer list
            

            #get the correct answers of each selected question and append to the answerstepm list
            s = "select ans from questions where QID=%d"
            arg = (id)
            cursor.execute(s % arg)
            l = list(cursor.fetchone())
            answerstemp.append(l)
            ans=l[0]
            correctAnswer.append(opts[ans-1])
            

        mydict = {}#create dictionary to store each question and relavent options as key value pair
        for i in range(5):
            mydict[questions[i]] = options[i]
            #print(mydict)
            
        # append all answers into answers list  
        for i in range(len(answerstemp)):
            answers.append(answerstemp[i][0])
            #print(answers)


        print("Answers= ", answers)

        cursor.close()
        conn.close()
        
        l1 = {}
        for i in range(5):
            l1[i] = 0

        f.propagate(0)
        f.pack()
        self.qno = 0
        self.score1 = 0
        self.ques = self.create_q(f, self.qno)
        self.opts = self.create_options(f)
        self.display_q(self.qno)
        self.Back = Button(f, text="Back", width=16, height=1, fg="#D68910", bg="white",
                           font=("Comic Sans MS", 16, "bold"), command=self.back).place(x=270, y=400)
        self.Next = Button(f, text="Next", width=16, height=1, fg="#D68910", bg="white",
                           font=("Comic Sans MS", 16, "bold "), command=self.next).place(x=600, y=400)
        self.submit = Button(f, text="Submit", width=16, height=1, fg="#D68910", bg="white",
                             font=("Comic sans MS", 16, "bold "), command=self.Submit).place(x=400, y=500)

#geting questions from the questions list and display on the label   

    def create_q(self, mainWin, qno):
        qLabel = Label(mainWin, text=questions[qno], bg='#275DF8', font=("Segoe UI",16))
        qLabel.place(x=30, y=70)
        return qLabel
    
# placing options into radio buttons
    def create_options(self, mainWin):
        b_val = 0
        b = []
        ht = 85
        self.opt_selected = IntVar()
        while b_val < 4:
            btn = Radiobutton(mainWin, text="", variable=self.opt_selected, value=b_val + 1, bg='#275DF8',
                              font=("Segoe UI", 16))
            b.append(btn)
            ht = ht + 40
            btn.place(x=30, y=ht)
            b_val = b_val + 1
        return b

#display questions

    def display_q(self, qno):
        b_val = 0
        self.ques['text'] = str(qno + 1) + ". " + questions[qno]
        for op in options[qno]:
            self.opts[b_val]['text'] = op
            b_val = b_val + 1

#next method use to go up to 5th question and displing warning when try to go to next  
    def next(self):
        self.qno += 1

        if self.qno >= len(questions):
            self.qno -= 1
            messagebox.showwarning("Warning", "You are at the end.Press Submit to proceed")
        else:
            l1[self.qno - 1] = self.opt_selected.get()
            self.opt_selected.set(l1[(self.qno)])
            self.display_q(self.qno)

    def back(self):
        l1[self.qno] = self.opt_selected.get()
        self.qno -= 1
        if self.qno < 0:
            self.qno += 1
            messagebox.showerror("Error", "You are already in the start!!!")
        else:
            self.display_q(self.qno)
            c = l1[self.qno]
            self.opt_selected.set(c)

    def Submit(self):
        l1[self.qno] = self.opt_selected.get()
        x = 0
        y = True
        for i in range(5):
            if (l1[i] == 0):
                x += 1
        if (x > 0 and x != 1):
            y = messagebox.askyesno("Warning", "You have not attempted " + str(
                x) + " questions, Are you sure you want to submit?, You won't be able to make changes again")
        elif (x == 1):
            y = messagebox.askyesno("Warning", "You have not attempted " + str(
                x) + " question, Are you sure you want to submit?, You won't be able to make changes again")
        if (y == True or x == 0):
            s = 0
            for i in range(5):
                if (l1[i] == answerstemp[i][0]):
                    s = s + 1
            print("DEBUG: Score: ", s)
       # conn = mysql.connector.connect(host='localhost', database='quizdatabase', user='root', password='')
        conn = mysql.connector.connect(host='localhost', database='quizdatabase', user='root', password='mysql')

        cursor = conn.cursor()
        q = "update reg set score='%d' where uname= '%s'"
        arg = (s, self.user)
        cursor.execute(q % arg)
        conn.commit()
        cursor.close()
        conn.close()
#####################################################
        #Display Questions and the correct answer in the table with the total marks

                
        class showAnswerstable:

            def __init__(self,root):

                finalMarks=ttk.Treeview(root)
                finalMarks['columns'] = ('Question', 'Answer')
                questions.append("Total Marks")
                correctAnswer.append(str(s))
                #print(questions[10])
                #print(correctAnswer[10])
                


                finalMarks.column("#0", width=0,  stretch=YES)
                finalMarks.column("Question",anchor=W, width=380)
                finalMarks.column("Answer",anchor=W,width=180)

                finalMarks.heading("Question",text="Question",anchor=CENTER)
                finalMarks.heading("Answer",text="Answer",anchor=CENTER)
                                         
                # code for creating table
                for i in range(6):

                    finalMarks.insert(parent='',index='end',iid=i,text='',
                        values=(questions[i],correctAnswer[i]))
##                    if i==9:
##                        finalMarks.insert(parent='',index='end',iid=10,text='',
##                            values=('Total Marks',s) )
##            finalMarks.heading("Question",text="Total Marks",anchor=CENTER)
##            finalMarks.heading("Answer",text=str(s),anchor=CENTER)

                #print(s)
                
                finalMarks.pack()

        # create root window
        root = Tk()
        t = showAnswerstable(root)
        root.mainloop()

        
######################################################
        messagebox.showinfo("Score", "Your Score is: " + str(s) + "/05")
        mQuiz.destroy()
###########################################################


    

root = Tk()
root.resizable(0,0)
RegObj = MainWindow(root)
root.mainloop()

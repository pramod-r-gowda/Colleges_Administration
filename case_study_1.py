# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 11:45:02 2020

@author: home
"""
from tkinter import *
from tkinter import messagebox  
import csv
ol=[]
class Rect():
    def __init__(self):
        self.ans=0
    def setcollegeId(self,cid):
        self.collegeId=cid
    def setcollegeName(self,name):
        self.collegeName=name
    def setcourseType(self,ct):
        self.courseType=ct
    def setCity(self,city):
        self.cityName=city
    def setFees(self,fee):
        self.fees=fee
    def setpinCode(self,pc):
        self.pinCode=pc
    def getcollegeId(self):
        return self.collegeId
    def getcollegeName(self):
        return self.collegeName
    def getcourseType(self):
        return self.courseType
    def getCity(self):
        return self.cityName
    def getFees(self):
        return self.fees
    def getpinCode(self):
        return self.pinCode

def register():
    def getinfo():
        r=Rect()
        cid=t1.get("1.0","end-1c")
        r.setcollegeId(cid)
        #print(cid)
        cn=t2.get("1.0","end-1c")
        r.setcollegeName(cn)
        ct=t3.get("1.0","end-1c")
        r.setcourseType(ct)
        city=t4.get("1.0","end-1c")
        r.setCity(city)
        fees=t5.get("1.0","end-1c")
        r.setFees(fees)
        pc=t6.get("1.0","end-1c")
        r.setpinCode(pc) 
        ol.append(r) 
        #print(r.getcollegeName())
        t1.delete("1.0","end")
        t2.delete("1.0","end")
        t3.delete("1.0","end")
        t4.delete("1.0","end")
        t5.delete("1.0","end")
        t6.delete("1.0","end")
        messagebox.showinfo("Success","Added Successfully")
    r1=Tk()
    r1.title("New College Addition")
    r1.configure(background='gray')
    r1.columnconfigure(0, weight=1)
    w2=Label(r1,text="New College Addition Registration",fg="white",bg="black")
    w2.config(font=("Elephant", 20))
    w2.grid(row=2, column=0, columnspan=2, sticky="ew")
    a = Label(r1 ,text = "College Id").grid(row = 4,column = 0,padx=100,pady=10,sticky="w")
    b = Label(r1,text = "College Name").grid(row = 5,column = 0,padx=100,pady=10,sticky="w")
    c = Label(r1,text = "Course Type").grid(row = 6,column = 0,padx=100,pady=10,sticky="w")
    d = Label(r1,text = "City").grid(row = 7,column = 0,padx=100,pady=10,sticky="w")
    e=Label(r1,text = "Fees").grid(row = 8,column = 0,padx=100,pady=10,sticky="w")
    f=Label(r1,text = "Pincode").grid(row = 9,column = 0,padx=100,pady=10,sticky="w")
    t1 = Text(r1, height=1, width=40,bg="orange",fg="black")
    t1.grid(row=4, column=1, padx=100,pady=10)
    t2 = Text(r1, height=1, width=40,bg="orange",fg="black")
    t2.grid(row=5, column=1 , padx=100,pady=10)
    t3 = Text(r1, height=1, width=40,bg="orange",fg="black")
    t3.grid(row=6, column=1 ,padx=100,pady=10)
    t4 = Text(r1, height=1, width=40,bg="orange",fg="black")
    t4.grid(row=7, column=1 ,padx=100,pady=10)
    t5 = Text(r1, height=1, width=40,bg="orange",fg="black")
    t5.grid(row=8, column=1 ,padx=100,pady=10)
    t6 = Text(r1, height=1, width=40,bg="orange",fg="black")
    t6.grid(row=9, column=1 ,padx=100,pady=10)
    add = Button(r1, text="Add",bg="black",fg="white",command=getinfo,width=8,height=2)
    add.grid(row=10, column=0,padx=100,pady=10,sticky="w")
   
    r1.mainloop()

def display():
    ele=[]
    with open("colleges.csv","r") as csvfile:
        li=csv.reader(csvfile)
        #col.writerow(fields)
        for i in li:
            if i!=[]:
                ele.append(i)
    r2=Tk()
    r2.title("Mumbai Engineering Colleges")
    r2.configure(background='gray')
    r2.columnconfigure(0, weight=1)
    w3=Label(r2,text="Engineering Colleges in Mumbai",fg="white",bg="black")
    w3.config(font=("Elephant", 20))
    w3.grid(row=2, column=0, columnspan=2, sticky="ew")
    collegelist=[]
    for i in range(len(ele)):
        if ele[i][2].lower()=="engineering" and ele[i][3].lower()=="mumbai":
            collegelist.append(ele[i][1])
    k=4
    for i in range(len(collegelist)):
        Label(r2 ,text = collegelist[i] ).grid(row = k,column = 0,padx=100,pady=10,sticky="w")
        k+=1

def deleteCollege():
    def removeCollege():
        did=tid.get("1.0","end-1c")
        #print(did)
        lines=[]
        with open('colleges.csv', 'r') as readFile:
            reader = csv.reader(readFile)
            for row in reader:
                lines.append(row)
                for field in row:
                    if field == did:
                        lines.remove(row)
        with open('colleges.csv', 'w') as writeFile:
            writer = csv.writer(writeFile)
            writer.writerows(lines)
        tid.delete("1.0","end")
        messagebox.showinfo("Success","Removed Successfully")
    r3=Tk()
    r3.title("Removing a college from Database")
    r3.configure(background='gray')
    r3.columnconfigure(0, weight=1)
    w4=Label(r3,text="Removing Colleges from Database ",fg="white",bg="black")
    w4.config(font=("Elephant", 20))
    w4.grid(row=2, column=0, columnspan=2, sticky="ew")
    aid= Label(r3 ,text = "College Id").grid(row = 4,column = 0,padx=100,pady=10,sticky="w")
    tid= Text(r3, height=1, width=40,bg="orange",fg="black")
    tid.grid(row=4, column=1, padx=100,pady=10)
    dc = Button(r3, text="Remove",bg="black",fg="white",command=removeCollege,width=8,height=2)
    dc.grid(row=10, column=0,padx=100,pady=10,sticky="w")
    r3.mainloop()
root=Tk()
root.title("Case Study 1: College Addition/Removal Application")
root.configure(background='gray')
root.columnconfigure(0, weight=1)
w1 = Label(root, text="Case study on Python: College Addition/Removal Application", fg="white", bg="black")
w1.config(font=("Elephant", 25))
w1.grid(row=2, column=0, columnspan=2, sticky="ew")
rnc = Button(root, text="Register New College", bg="green",fg="yellow",command=register)
rnc.grid(row=3, column=0,padx=5,pady=5)

cim = Button(root, text="Engineering Colleges in Mumbai",bg="green",fg="yellow",command=display)
cim.grid(row=4, column=0,padx=5,pady=5)

rc = Button(root, text="Remove College", bg="green",fg="yellow",command=deleteCollege)
rc.grid(row=5, column=0,padx=5,pady=5)

root.mainloop()
res=[]
for i in range(len(ol)):
    res.append([ol[i].getcollegeId(),ol[i].getcollegeName(),ol[i].getcourseType(),ol[i].getCity(),ol[i].getFees(),ol[i].getpinCode()])
fields=['Id','Name','Type','City','Fees','Pincode']
with open("colleges.csv","a") as csvfile:
    col=csv.writer(csvfile)
    #col.writerow(fields)
    col.writerows(res)

#print(ele[0][3])
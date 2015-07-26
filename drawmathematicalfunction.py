from tkinter import *
from math import sqrt

class quad(Canvas):
        def __init__(self, master=None):
                Canvas.__init__(self, master, width=600, height=600, bg="light grey")
                self.enl()
        
        def enl(self):
                self.delete(ALL)
                # QUADRILLAGE FANTÔME
                for i in range(0, 600, 30):
                        self.create_line(i, 0, i, 600, fill="grey")

                for i in range(600, 0, -30):
                        self.create_line(0, i, 600, i, fill="grey")

                # AXES + CENTRE
                self.create_line(300, 0, 300, 600, width=1)
                self.create_line(0, 300, 600, 300, width=1)
                
                r = 2
                self.create_oval(300-r, 300-r, 300+r, 300+r, fill="black")

                # GRADUATION
                j = -9
                for i in range(0, 600, 30):
                        self.create_line(i, 297, i, 304)
                        if j <= 9:
                                if j == 0:
                                        self.create_text(305, 285, text=j, anchor=CENTER)
                                else:
                                        self.create_text(i+31, 285, text=j, anchor=CENTER)
                        j+=1

                j = -9
                for i in range(600, 0, -30):
                        self.create_line(297, i, 304, i)
                        if j <= 9:
                                if j != 0:
                                        self.create_text(289, i-31, text=j, anchor=CENTER)
                                j+=1


        def draw_1(self):
                self.m = frame.m1E.get()
                if self.m == "":
                        self.m = "0"
                        frame.m1E.insert(END, "0")
                self.p = frame.p1E.get()
                if self.p == "":
                        self.p = "0"
                        frame.p1E.insert(END, "0")

                prm = 1
                try:
                        self.m = eval(self.m)
                        self.p = eval(self.p)
                        
                except:
                        frame.m1E.delete(0, END)
                        frame.p1E.delete(0, END)
                        frame.m1E.insert(END, "Error")
                        frame.p1E.insert(END, "Error")
                        prm = 0

                if(prm == 1):
                        self.point = []
                        self.curve = []
                        for t in range(600):
                                x = t 
                                y = 600-(x * self.m)
                                self.point.append((x,y))
                                
                        dist = 300-self.point[300][1]
                        for it in self.point:
                                self.curve.append((it[0], it[1]+dist-(30*self.p)))
                        self.create_line(self.curve, fill="blue", smooth=1)

        def draw_2(self):
                self.a = frame.a2E.get()
                self.b = frame.b2E.get()
                self.c = frame.c2E.get()

                if self.a == "":
                        self.a = "0"
                        frame.a2E.insert(END, "0")
                if self.b == "":
                        self.b = "0"
                        frame.b2E.insert(END, "0")
                if self.b == "":
                        self.b = "0"
                        frame.b2E.insert(END, "0")

                prm = 1
                try:
                        self.a = eval(self.a)
                        self.b = eval(self.b)
                        self.c = eval(self.c)

                except:
                        frame.a2E.delete(0, END)
                        frame.b2E.delete(0, END)
                        frame.c2E.delete(0, END)
                        frame.a2E.insert(END, "Error")
                        frame.b2E.insert(END, "Error")
                        frame.c2E.insert(END, "Error")
                        prm = 0

                if(prm == 1):
                        self.point = []
                        for t in range(-300, 300):
                                x = t          
                                y = (((self.a*x)/30)**2 + (self.b*x)/30 + self.c)*30
                                
                                self.point.append((x+300,300-y))

                        self.create_line(self.point, fill="red")

        def draw_3(self):
                self.m = frame.m3E.get()
                self.a = frame.a3E.get()
                self.p = frame.p3E.get()

                if self.m == "":
                        self.m = "0"
                        frame.m3E.insert(END, "0")
                if self.p == "":
                        self.p = "0"
                        frame.p3E.insert(END, "0")
                if self.a == "":
                        self.a = "0"
                        frame.a3E.insert(END, "0")

                prm = 1
                try:
                        self.m = eval(self.m)
                        self.a = eval(self.a)
                        self.p = eval(self.p)

                except:
                        frame.m3E.delete(0, END)
                        frame.a3E.delete(0, END)
                        frame.p9E.delete(0, END)
                        frame.m3E.insert(END, "Error")
                        frame.a3E.insert(END, "Error")
                        frame.p9E.insert(END, "Error")
                        prm = 0

                if prm == 1:
                        self.point = []
                        for t in range(600):
                                if t >= 0:
                                        x = t
                                        y = (self.m)*sqrt((x)*30)+(self.p*30)

                                        self.point.append((x+300+(self.a)*30, 300-y))

                        self.create_line(self.point, fill="green")
                                
class valeurs(Frame):
        def __init__(self, master=None):
                Frame.__init__(self, master, width=600, height=200, bg="light grey")

                Label(self, text="Premier degré\nF(x) = m.x + p", bg="light grey").grid(row = 0, column=0, padx=20)
                Label(self, text="m :", bg="light grey").grid(row=1, column=0, padx=20, sticky=W, columnspan=3)
                Label(self, text="p  :", bg="light grey").grid(row=2, column=0, padx=20, sticky=W, columnspan=3)
                self.m1E = Entry(self, width=5)
                self.m1E.grid(row=1, column=0, pady=10, padx=35, sticky=E)
                self.m1E.insert(END, "0")
                self.p1E = Entry(self, width=5)
                self.p1E.grid(row=2, column=0, pady=10, padx=35, sticky=E)
                self.p1E.insert(END, "0")
                Button(self, text="Draw", command=can.draw_1).grid(row=4, column=0, pady=15, padx=20)

                Label(self, text="Second degré\nF(x) = a.x² + b.x + c", bg="light grey").grid(row = 0, column=1, padx=20)
                Label(self, text="a  :", bg="light grey").grid(row=1, column=1, padx=40, sticky=W, columnspan=3)
                Label(self, text="b  :", bg="light grey").grid(row=2, column=1, padx=40, sticky=W, columnspan=3)
                Label(self, text="c  :", bg="light grey").grid(row=3, column=1, padx=40, sticky=W, columnspan=3)
                self.a2E = Entry(self, width=5)
                self.a2E.grid(row=1, column=1, pady=10, padx=40, sticky=E)
                self.a2E.insert(END, "0")
                self.b2E = Entry(self, width=5)
                self.b2E.grid(row=2, column=1, pady=10, padx=40, sticky=E)
                self.b2E.insert(END, "0")
                self.c2E = Entry(self, width=5)
                self.c2E.grid(row=3, column=1, pady=10, padx=40, sticky=E)
                self.c2E.insert(END, "0")
                Button(self, text="Draw", command=can.draw_2).grid(row=4, column=1, pady=15, padx=20)

                Label(self, text="Racine carrée\nF(x) = m.V(x+a) + p", bg="light grey").grid(row = 0, column=2, padx=20)
                Label(self, text="m :", bg="light grey").grid(row=1, column=2, padx=35, sticky=W, columnspan=3)
                Label(self, text="a  :", bg="light grey").grid(row=2, column=2, padx=35, sticky=W, columnspan=3)
                Label(self, text="p  :", bg="light grey").grid(row=3, column=2, padx=35, sticky=W, columnspan=3)
                self.m3E = Entry(self, width=5)
                self.m3E.grid(row=1, column=2, pady=10, padx=40, sticky=E)
                self.m3E.insert(END, "0")
                self.a3E = Entry(self, width=5)
                self.a3E.grid(row=2, column=2, pady=10, padx=40, sticky=E)
                self.a3E.insert(END, "0")
                self.p3E = Entry(self, width=5)
                self.p3E.grid(row=3, column=2, pady=10, padx=40, sticky=E)
                self.p3E.insert(END, "0")
                Button(self, text="Draw", command=can.draw_3).grid(row=4, column=2, pady=15, padx=20)
        
if __name__ == "__main__":
        root = Tk()

        can = quad(root)
        Button(text="clear zone", command=can.enl).pack(padx=5, pady=5)
        can.pack(padx=5, pady=5)
        frame = valeurs(root)
        frame.pack(padx=5, pady=5)
        
        root.mainloop()
        

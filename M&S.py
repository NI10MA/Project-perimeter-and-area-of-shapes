import tkinter as tk
from tkinter import ttk
from PIL import Image,ImageTk 
from tkinter import messagebox,font

#------def_exit_program------------

def close_window():
    response=messagebox.askyesno("تایید خروج","آیا از خارج شدن اطمینان دارید؟")
    if response:
        win1.destroy()
    else:
        return

#------Defs_login&exit--------------
def logwin2():
    win1.withdraw()
    win2.deiconify()

def logwin3():
    win1.withdraw()
    win3.deiconify()

def logwin4():
    win1.withdraw()
    win4.deiconify()

def logwin5():
    win1.withdraw()
    win5.deiconify()

def logwin6():
    win1.withdraw()
    win6.deiconify()

def logwin7():
    win1.withdraw()
    win7.deiconify()

def logwin8():
    win8.withdraw()
    win9.deiconify()

def logwin9():
    win8.withdraw()
    win10.deiconify()

def logwin10():
    win8.withdraw()
    win11.deiconify()

def logwin11():
    win8.withdraw()
    win12.deiconify()

def logwin12():
    win8.withdraw()
    win13.deiconify()

def logwin13():
    win8.withdraw()
    win14.deiconify()

def showname():
    wintarah.deiconify()
    win1.withdraw()

def backshowname():
    wintarah.withdraw()
    win1.deiconify()
    

def back1():
    win1.deiconify()
    win2.withdraw()
    text_box1.delete(0, tk.END)
    javab1.config(text="")

def back2():
    win1.deiconify()
    win3.withdraw()
    text_box2.delete(0, tk.END)
    javab2.config(text="")

def back3():
    win1.deiconify()
    win4.withdraw()
    text_box3.delete(0, tk.END)
    javab3.config(text="")

def back4():
    win1.deiconify()
    win5.withdraw()
    text_box4.delete(0, tk.END)
    javab4.config(text="")

def back5():
    win1.deiconify()
    win6.withdraw()
    text_box5.delete(0, tk.END)
    javab5.config(text="")

def back6():
    win1.deiconify()
    win7.withdraw()
    text_box6.delete(0, tk.END)
    text_box7.delete(0, tk.END)
    javab6.config(text="")

def back7():
    win8.deiconify()
    win9.withdraw()
    text_box8.delete(0, tk.END)
    text_box9.delete(0, tk.END)
    text_box10.delete(0, tk.END)
    javab7.config(text="")

def back8():
    win8.deiconify()
    win10.withdraw()
    text_box11.delete(0, tk.END)
    text_box12.delete(0, tk.END)
    javab8.config(text="")
    
def back9():
    win8.deiconify()
    win11.withdraw()
    text_box13.delete(0, tk.END)
    text_box14.delete(0, tk.END)
    javab9.config(text="")

def back10():
    win8.deiconify()
    win12.withdraw()
    text_box15.delete(0, tk.END)
    text_box16.delete(0, tk.END)
    javab10.config(text="")

def back11():
    win8.deiconify()
    win13.withdraw()
    text_box17.delete(0, tk.END)
    text_box18.delete(0, tk.END)
    javab11.config(text="")

def back12():
    win8.deiconify()
    win14.withdraw()
    text_box19.delete(0, tk.END)
    text_box20.delete(0, tk.END)
    javab12.config(text="")

#-----Defs_reset----------
def reset1():
    text_box1.delete(0, tk.END)
    javab1.config(text="")

def reset2():
    text_box2.delete(0, tk.END)
    javab2.config(text="")

def reset3():
    text_box3.delete(0, tk.END)
    javab3.config(text="")

def reset4():
    text_box4.delete(0, tk.END)
    javab4.config(text="")

def reset5():
    text_box5.delete(0, tk.END)
    javab5.config(text="")

def reset6():
    text_box6.delete(0, tk.END)
    text_box7.delete(0, tk.END)
    javab6.config(text="")

def reset7():
    text_box8.delete(0, tk.END)
    text_box9.delete(0, tk.END)
    text_box10.delete(0, tk.END)
    javab7.config(text="")

def reset8():
    text_box11.delete(0, tk.END)
    text_box12.delete(0, tk.END)
    javab8.config(text="")

def reset9():
    text_box13.delete(0, tk.END)
    text_box14.delete(0, tk.END)
    javab9.config(text="")

def reset10():
    text_box15.delete(0, tk.END)
    text_box16.delete(0, tk.END)
    javab10.config(text="")

def reset11():
    text_box17.delete(0, tk.END)
    text_box18.delete(0, tk.END)
    javab11.config(text="")

def reset12():
    text_box19.delete(0, tk.END)
    text_box20.delete(0, tk.END)
    javab12.config(text="")

#-----Defs_mohasebeh-------
def mohit_dayereh():
    try:
        rmohit= float(text_box1.get())
        dayereh_mohit = 2 * 3.14159265359 * rmohit
        javab1.config(text=f"محیط دایره: {dayereh_mohit:.2f}")
    except ValueError:
        javab1.config(text="لطفاً یک عدد معتبر برای شعاع وارد کنید.")

def masahat_dayereh():
    try:
        rmasahat= float(text_box2.get())
        dayereh_masahat = 3.14159265359 * rmasahat *rmasahat
        javab2.config(text=f"مساحت دایره: {dayereh_masahat:.2f}")
    except ValueError:
        javab2.config(text="لطفاً یک عدد معتبر برای شعاع وارد کنید.")

def mohit_moraba():
    try:
        mmoraba= float(text_box3.get())
        moraba_mohit = mmoraba*4
        javab3.config(text=f"محیط مربع: {moraba_mohit:.2f}")
    except ValueError:
        javab3.config(text="لطفاً یک عدد معتبر برای ضلع وارد کنید.")

def masahat_moraba():
    try:
        mamoraba= float(text_box4.get())
        moraba_masahat = mamoraba*mamoraba
        javab4.config(text=f"مساحت مربع: {moraba_masahat:.2f}")
    except ValueError:
        javab4.config(text="لطفاً یک عدد معتبر برای ضلع وارد کنید.")

def mohit_lozi():
    try:
        mlozi= float(text_box5.get())
        lozi_mohit = mlozi*4
        javab5.config(text=f"محیط لوزی: {lozi_mohit:.2f}")
    except ValueError:
        javab5.config(text="لطفاً یک عدد معتبر برای ضلع وارد کنید.")

def masahat_lozi():
    try:
        qotrbig1lozi= float(text_box6.get())
        qotrsmalllozi= float(text_box7.get())
        lozi_masahat = (qotrbig1lozi*qotrsmalllozi/2)
        javab6.config(text=f"مساحت لوزی: {lozi_masahat:.1f}")
    except ValueError:
        javab6.config(text="لطفاً عدد معتبر برای قطرها وارد کنید.")

def mohit_mosalas():
    try:
        zelone= float(text_box8.get())
        zeltwo= float(text_box9.get())
        zelthree= float(text_box1.get())
        mohit_mosalas= zelone+zeltwo+zelthree
        javab7.config(text=f"محیط مثلث{mohit_mosalas:.1f}")
    except ValueError:
        javab7.config(text="لطفاً عدد معتبر برای اضلاع وارد کنید.")

def masahat_mosalas():
    try:
        ghaedeh_mosalas= float(text_box11.get())
        ertefa_mosalas= float(text_box12.get())
        masahat_mosalas= ghaedeh_mosalas*ertefa_mosalas/2
        javab8.config(text=f"مساحت مثلث{masahat_mosalas:.1f}")
    except ValueError:
        javab8.config(text="لطفاً عدد معتبر برای قاعده و ارتفاع وارد کنید.")

def mohit_mostatil():
    try:
        tol_mostatil= float(text_box13.get())
        arz_mostatil= float(text_box14.get())
        mohit_mostatil= (tol_mostatil+arz_mostatil)+2
        javab9.config(text=f"محیط مستطیل{mohit_mostatil:.1f}")
    except ValueError:
        javab9.config(text="لطفاً عدد معتبر برای طول و عرض وارد کنید.")
    

def masahat_mostatil():
    try:
        mostatil_tol= float(text_box15.get())
        mostatil_arz= float(text_box16.get())
        masahat_mostatil= mostatil_tol*mostatil_arz
        javab10.config(text=f"مساحت مستطیل{masahat_mostatil:.1f}")
    except ValueError:
        javab10.config(text="لطفاً عدد معتبر برای طول و عرض وارد کنید.")

def mohit_motavazilazla():
    try:
        zelmojaverone= float(text_box17.get())
        zelmojavertwo= float(text_box18.get())
        mohit_motavazilazla= (zelmojaverone+zelmojavertwo)*2
        javab11.config(text=f"محیط متوازی الاضلاع{mohit_motavazilazla:.1f}")
    except ValueError:
        javab11.config(text="لطفاً عدد معتبر برای اضلاع وارد کنید.")

def masahat_motavazilazla():
    try:
        ertefa_motavazilazla= float(text_box19.get())
        ghaedeh_motavazilazla= float(text_box20.get())
        masahat_motavazilazla= ghaedeh_motavazilazla*ertefa_motavazilazla
        javab12.config(text=f"مساحت متوازی الاضلاع{masahat_motavazilazla:.1f}")
    except ValueError:
        javab12.config(text="لطفاً عدد معتبر برای قاعده و ارتفاع وارد کنید.")

#------next_page & previous_page-------------------
def next_page():
    win1.withdraw()
    win8.deiconify()

def previous_page():
    win1.deiconify()
    win8.withdraw()

#------پنجره اصلی--------
#region
win1 = tk.Tk()
win1.title("محیط و مساحت")
win1.geometry("1024x800")
#-------canvas_win1------------
canvas=tk.Canvas(win1,width=1024,height=800)
canvas.pack()
Sazandeh=tk.Label(win1,text=":طراح",foreground="#cd2d0d",font=("B Nazanin",25),bg="#1ced38")
canvas.create_window(520,50,window=Sazandeh)
Sazandeh1=tk.Label(win1,text="نیما صدفی همدانی",foreground="#0e45ea",font=("B Nazanin",25),bg="#1ced38")
canvas.create_window(520,100,window=Sazandeh1)

#-------------------------
image1=Image.open("image14.png")
canvas_image1 = ImageTk.PhotoImage(image1.resize((1024, 800)))
canvas.create_image(512, 400, anchor="center", image=canvas_image1)
#-------شکل دایره----------
canvas.create_oval(50,50,330,330,outline="#fff",fill="#1cc",width=5)
#-------شکل لوزی-----------
canvas.create_polygon(874, 25,1024,175,874,325,724,175,outline="#fff",fill="#1cf", width=5)
#------شکل مربع------------
canvas.create_rectangle(50, 440,280, 620,outline="#fff",fill="#1fc",width=5)
#------buttons_page_one-----------

b1=tk.Button(win1,text="محیط دایره",bg="#1c2d6f",fg="white",width=12,height=2,command=logwin2)
canvas.create_window(400, 250, window=b1)

b2=tk.Button(win1,text="مساحت دایره",bg="#1c2d6f",fg="white",width=12,height=2,command=logwin3)
canvas.create_window(400, 300, window=b2)

b3=tk.Button(win1,text="محیط مربع",bg="#1c2d6f",fg="white",width=12,height=2,command=logwin4)
canvas.create_window(400, 570, window=b3)

b4=tk.Button(win1,text="مساحت مربع",bg="#1c2d6f",fg="white",width=12,height=2,command=logwin5)
canvas.create_window(400, 620, window=b4)

b5=tk.Button(win1,text="محیط لوزی",bg="#1c2d6f",fg="white",width=12,height=2,command=logwin6)
canvas.create_window(650, 250, window=b5)

b6=tk.Button(win1,text="مساحت لوزی",bg="#1c2d6f",fg="white",width=12,height=2,command=logwin7)
canvas.create_window(650, 300, window=b6)

#button next_page
b13=tk.Button(win1,text="صفحه بعد",bg="#1d4f2b",fg="white",width=15,height=3,command=next_page)
canvas.create_window(800,550, window=b13)

bname=tk.Button(win1,text="درباره سازنده",bg="red",fg="black",width=15,height=3,command=showname)
canvas.create_window(680,550,window=bname)

wintarah=tk.Toplevel(win1)
wintarah.withdraw()
wintarah.title("سازنده")
wintarah.geometry("550x550")
#---------------------------------------
canvas_wint=tk.Canvas(wintarah,width=550,height=550)
canvas_wint.pack()

imaget=Image.open("Name.jpg")
canvas_imaget = ImageTk.PhotoImage(imaget.resize((550, 550)))
canvas_wint.create_image(275,275, anchor="center", image=canvas_imaget)

Sazandeh=tk.Label(wintarah,text=":طراح",foreground="black",font=("B Nazanin",25),bg="#eedc12")
canvas_wint.create_window(275,270,window=Sazandeh)
Sazandeh1=tk.Label(wintarah,text="نیما صدفی همدانی",foreground="#0e45ea",font=("B Nazanin",25),bg="#fff")
canvas_wint.create_window(275,350,window=Sazandeh1)

Sazandeh_gmail=tk.Label(wintarah,text="Nima10.N10@gmail.com",foreground="#0e45ea",font=("B Nazanin",25),bg="#fff")
canvas_wint.create_window(275,420,window=Sazandeh_gmail)

backname=tk.Button(wintarah,text="بازگشت",bg="#eedc12",fg="black",width=15,height=3,command=backshowname)
canvas_wint.create_window(500,475,window=backname)
#endregion
#---------win2_dayereh---------------
#region
win2=tk.Toplevel(win1)
win2.withdraw()
win2.title("محیط دایره")
win2.geometry("550x550")
#-------canvas_win2------------
canvas_win2=tk.Canvas(win2,width=550,height=550)
canvas_win2.pack()

image2=Image.open("image3.png")
canvas_image2 = ImageTk.PhotoImage(image2.resize((550, 550)))
canvas_win2.create_image(275,275, anchor="center", image=canvas_image2)

label1=tk.Label(win2,text="لطفا اندازه شعاع خود را وارد کنید",foreground="blue",font=("B Nazanin",25),bg="#307b35")
canvas_win2.create_window(270,80,window=label1)


text_box1=tk.Entry(win2,width=25)
canvas_win2.create_window(270,130,window=text_box1)

m1=tk.Button(win2,text="محاسبه",bg="#021e3b",fg="white",width=12,height=2,command=mohit_dayereh)
canvas_win2.create_window(330,180, window=m1)

javab1=tk.Label(win2,text="",fg="lightgray",bg="#307b35",font=("B Nazanin",20))
canvas_win2.create_window(280,245,window=javab1)

v1=tk.Button(win2,text="ورودی جدید",bg="#021e3b",fg="white",width=12,height=2,command=reset1)
canvas_win2.create_window(230,180, window=v1)

b7=tk.Button(win2,text="بازگشت",bg="#307b35",fg="white",width=12,height=2,command=back1)
canvas_win2.create_window(450,430, window=b7)
#endregion
#--------win3_dayereh----------------
#region
win3=tk.Toplevel(win1)
win3.withdraw()
win3.title("مساحت دایره")
win3.geometry("550x550")
#-------canvas_win3------------
canvas_win3=tk.Canvas(win3,width=550,height=550)
canvas_win3.pack()

image3=Image.open("image4.png")
canvas_image3 = ImageTk.PhotoImage(image3.resize((550, 550)))
canvas_win3.create_image(275,275, anchor="center", image=canvas_image3)

label2=tk.Label(win3,text="لطفا اندازه شعاع خود را وارد کنید",foreground="blue",font=("B Nazanin",25),bg="#307b35")
canvas_win3.create_window(270,80,window=label2)

text_box2=tk.Entry(win3,width=25)
canvas_win3.create_window(270,130,window=text_box2)

m2=tk.Button(win3,text="محاسبه",bg="#021e3b",fg="white",width=12,height=2,command=masahat_dayereh)
canvas_win3.create_window(330,180, window=m2)

javab2=tk.Label(win3,text="",fg="lightgray",bg="#307b35",font=("B Nazanin",20))
canvas_win3.create_window(280,245,window=javab2)

v2=tk.Button(win3,text="ورودی جدید",bg="#021e3b",fg="white",width=12,height=2,command=reset2)
canvas_win3.create_window(230,180, window=v2)

b8=tk.Button(win3,text="بازگشت",bg="#307b35",fg="white",width=12,height=2,command=back2)
canvas_win3.create_window(450,430, window=b8)
#endregion
#-----win4_moraba-------------------
#region
win4=tk.Toplevel(win1)
win4.withdraw()
win4.title("محیط مربع")
win4.geometry("550x550")
#-------canvas_win4------------
canvas_win4=tk.Canvas(win4,width=550,height=550)
canvas_win4.pack()

image4=Image.open("image5.png")
canvas_image4 = ImageTk.PhotoImage(image4.resize((550, 550)))
canvas_win4.create_image(275,275, anchor="center", image=canvas_image4)


label3=tk.Label(win4,text="لطفا اندازه ضلع خود را وارد کنید",foreground="blue",font=("B Nazanin",25),bg="#307b35")
canvas_win4.create_window(270,80,window=label3)

text_box3=tk.Entry(win4,width=25)
canvas_win4.create_window(270,130,window=text_box3)

m3=tk.Button(win4,text="محاسبه",bg="#021e3b",fg="white",width=12,height=2,command=mohit_moraba)
canvas_win4.create_window(330,180, window=m3)

javab3=tk.Label(win4,text="",fg="lightgray",bg="#307b35",font=("B Nazanin",20))
canvas_win4.create_window(280,245,window=javab3)

v3=tk.Button(win4,text="ورودی جدید",bg="#021e3b",fg="white",width=12,height=2,command=reset3)
canvas_win4.create_window(230,180, window=v3)

b9=tk.Button(win4,text="بازگشت",bg="#307b35",fg="white",width=12,height=2,command=back3)
canvas_win4.create_window(450,430, window=b9)
#endregion
#-----win5_moraba--------------------
#region
win5=tk.Toplevel(win1)
win5.withdraw()
win5.title("مساحت مربع")
win5.geometry("550x550")
#-------canvas_win5------------
canvas_win5=tk.Canvas(win5,width=550,height=550)
canvas_win5.pack()

image5=Image.open("image6.png")
canvas_image5 = ImageTk.PhotoImage(image5.resize((550, 550)))
canvas_win5.create_image(275,275, anchor="center", image=canvas_image5)

label4=tk.Label(win5,text="لطفا اندازه ضلع خود را وارد کنید",foreground="blue",font=("B Nazanin",25),bg="#307b35")
canvas_win5.create_window(270,80,window=label4)

text_box4=tk.Entry(win5,width=25)
canvas_win5.create_window(270,130,window=text_box4)

m4=tk.Button(win5,text="محاسبه",bg="#021e3b",fg="white",width=12,height=2,command=masahat_moraba)
canvas_win5.create_window(330,180, window=m4)

javab4=tk.Label(win5,text="",fg="lightgray",bg="#307b35",font=("B Nazanin",20))
canvas_win5.create_window(280,245,window=javab4)

v4=tk.Button(win5,text="ورودی جدید",bg="#021e3b",fg="white",width=12,height=2,command=reset4)
canvas_win5.create_window(230,180, window=v4)

b10=tk.Button(win5,text="بازگشت",bg="#307b35",fg="white",width=12,height=2,command=back4)
canvas_win5.create_window(450,430, window=b10)
#endregion
#-----win6_lozi----------------------
#region
win6=tk.Toplevel(win1)
win6.withdraw()
win6.title("محیط لوزی")
win6.geometry("550x550")
#-------canvas_win6------------
canvas_win6=tk.Canvas(win6,width=550,height=550)
canvas_win6.pack()

image6=Image.open("image7.png")
canvas_image6 = ImageTk.PhotoImage(image6.resize((550, 550)))
canvas_win6.create_image(275,275, anchor="center", image=canvas_image6)

label5=tk.Label(win6,text="لطفا اندازه ضلع خود را وارد کنید",foreground="blue",font=("B Nazanin",25),bg="#19838a")
canvas_win6.create_window(270,80,window=label5)

text_box5=tk.Entry(win6,width=25)
canvas_win6.create_window(270,130,window=text_box5)

m5=tk.Button(win6,text="محاسبه",bg="#021e3b",fg="white",width=12,height=2,command=mohit_lozi)
canvas_win6.create_window(330,180, window=m5)

javab5=tk.Label(win6,text="",fg="lightgray",bg="#19838a",font=("B Nazanin",20))
canvas_win6.create_window(280,245,window=javab5)

v5=tk.Button(win6,text="ورودی جدید",bg="#021e3b",fg="white",width=12,height=2,command=reset5)
canvas_win6.create_window(230,180, window=v5)

b11=tk.Button(win6,text="بازگشت",bg="#eaed13",fg="black",width=12,height=2,command=back5)
canvas_win6.create_window(450,430, window=b11)
#endregion
#-----win7_lozi---------------------
#region
win7=tk.Toplevel(win1)
win7.withdraw()
win7.title("مساحت لوزی")
win7.geometry("550x550")
#-------canvas_win7------------
canvas_win7=tk.Canvas(win7,width=550,height=550)
canvas_win7.pack()

image7=Image.open("image8.png")
canvas_image7 = ImageTk.PhotoImage(image7.resize((550, 550)))
canvas_win7.create_image(275,275, anchor="center", image=canvas_image7)

label6=tk.Label(win7,text="لطفا اندازه قطر بزرگ را وارد کنید",foreground="#fff",font=("B Nazanin",25),bg="#1d4f2b")
canvas_win7.create_window(270,80,window=label6)

text_box6=tk.Entry(win7,width=25)
canvas_win7.create_window(270,130,window=text_box6)

label7=tk.Label(win7,text="لطفا اندازه قطر کوچک را وارد کنید",foreground="#fff",font=("B Nazanin",23),bg="#1d4f2b")
canvas_win7.create_window(270,180,window=label7)

text_box7=tk.Entry(win7,width=25)
canvas_win7.create_window(270,230,window=text_box7)

m6=tk.Button(win7,text="محاسبه",bg="#021e3b",fg="white",width=12,height=2,command=masahat_lozi)
canvas_win7.create_window(330,280, window=m6)

javab6=tk.Label(win7,text="",fg="lightgray",bg="#1d4f2b",font=("B Nazanin",20))
canvas_win7.create_window(280,350,window=javab6)

v6=tk.Button(win7,text="ورودی جدید",bg="#021e3b",fg="white",width=12,height=2,command=reset6)
canvas_win7.create_window(230,280, window=v6)

b12=tk.Button(win7,text="بازگشت",bg="#1d4f2b",fg="#fff",width=12,height=2,command=back6)
canvas_win7.create_window(450,430, window=b12)
#endregion
#---------Finish_page1-----------------------------

#--------Start_page2-------------------------------
#-------پنجره دوم برنامه-------------------------
#region
win8 = tk.Toplevel(win1)
win8.withdraw()
win8.title("محیط و مساحت")
win8.geometry("1024x800")
#-------canvas_win8------------
canvas_win8=tk.Canvas(win8,width=1024,height=800)
canvas_win8.pack()
#button previous_page
b14=tk.Button(win8,text="صفحه قبل",bg="#1d4f2b",fg="white",width=15,height=3,command=previous_page)
canvas_win8.create_window(800,550, window=b14)
#------------------------------
image8=Image.open("image2.png")
canvas_image8 = ImageTk.PhotoImage(image8.resize((1024, 800)))
canvas_win8.create_image(512, 400, anchor="center", image=canvas_image8)
#---------شکل مثلث----------
canvas_win8.create_polygon(130, 20, 280, 300, 20, 300, fill="#3498db", outline="#fff",width=5)
#---------شکل مستطیل--------
canvas_win8.create_rectangle(20, 420, 330, 580, fill="#2ecc71", outline="#fff",width=5)
#--------شکل متوازی الاضلاع-----
canvas_win8.create_polygon(700,50,1000,50,880,200,580,200,fill="#3498db", outline="#fff",width=5)
#------buttons_page_two-----------
b15=tk.Button(win8,text="محیط مثلث",bg="#1c2d6f",fg="white",width=12,height=2,command=logwin8)
canvas_win8.create_window(380, 240, window=b15)
b16=tk.Button(win8,text="مساحت مثلث",bg="#1c2d6f",fg="white",width=12,height=2,command=logwin9)
canvas_win8.create_window(380, 290, window=b16)
b17=tk.Button(win8,text="محیط مستطیل",bg="#1c2d6f",fg="white",width=12,height=2,command=logwin10)
canvas_win8.create_window(420, 500, window=b17)
b18=tk.Button(win8,text="مساحت مستطیل",bg="#1c2d6f",fg="white",width=12,height=2,command=logwin11)
canvas_win8.create_window(420, 550, window=b18)
b19=tk.Button(win8,text="محیط متوازی الاضلاع",bg="#1c2d6f",fg="white",width=15,height=2,command=logwin12)
canvas_win8.create_window(650, 260, window=b19)
b20=tk.Button(win8,text="مساحت متوازی الاضلاع",bg="#1c2d6f",fg="white",width=15,height=2,command=logwin13)
canvas_win8.create_window(780, 260, window=b20)
#endregion
#-------win9_mosalas-----------------
#region
win9=tk.Toplevel(win1)
win9.withdraw()
win9.title("محیط مثلث")
win9.geometry("550x550")
#-------canvas_win9------------
canvas_win9=tk.Canvas(win9,width=550,height=550)
canvas_win9.pack()

image9=Image.open("image9.png")
canvas_image9 = ImageTk.PhotoImage(image9.resize((550, 550)))
canvas_win9.create_image(275,275, anchor="center", image=canvas_image9)

label8=tk.Label(win9,text="لطفا اندازه ضلع اول را مشخص کنید",foreground="#fff",font=("B Nazanin",25),bg="#1d4f2b")
canvas_win9.create_window(270,80,window=label8)

text_box8=tk.Entry(win9,width=25)
canvas_win9.create_window(270,130,window=text_box8)

label9=tk.Label(win9,text="لطفا اندازه ضلع دوم را مشخص کنید",foreground="#fff",font=("B Nazanin",23),bg="#1d4f2b")
canvas_win9.create_window(270,180,window=label9)

text_box9=tk.Entry(win9,width=25)
canvas_win9.create_window(270,230,window=text_box9)

label10=tk.Label(win9,text="لطفا اندازه ضلع سوم را مشخص کنید",foreground="#fff",font=("B Nazanin",23),bg="#1d4f2b")
canvas_win9.create_window(270,280,window=label10)

text_box10=tk.Entry(win9,width=25)
canvas_win9.create_window(270,330,window=text_box10)


m7=tk.Button(win9,text="محاسبه",bg="#021e3b",fg="white",width=12,height=2,command=mohit_mosalas)
canvas_win9.create_window(330,380, window=m7)

javab7=tk.Label(win9,text="",fg="lightgray",bg="#1d4f2b",font=("B Nazanin",20))
canvas_win9.create_window(280,440,window=javab7)

v7=tk.Button(win9,text="ورودی جدید",bg="#021e3b",fg="white",width=12,height=2,command=reset7)
canvas_win9.create_window(230,380, window=v7)

b21=tk.Button(win9,text="بازگشت",bg="#1d4f2b",fg="#fff",width=12,height=2,command=back7)
canvas_win9.create_window(450,480, window=b21)
#endregion
#---------win10_mosalas------------------
#region
win10=tk.Toplevel(win1)
win10.withdraw()
win10.title("مساحت مثلث")
win10.geometry("550x550")
#-------canvas_win10------------
canvas_win10=tk.Canvas(win10,width=550,height=550)
canvas_win10.pack()

image10=Image.open("image11.png")
canvas_image10 = ImageTk.PhotoImage(image10.resize((550, 550)))
canvas_win10.create_image(275,275, anchor="center", image=canvas_image10)

label11=tk.Label(win10,text="لطفا اندازه ارتفاع را وارد کنید",foreground="#fff",font=("B Nazanin",25),bg="#0e45ea")
canvas_win10.create_window(270,80,window=label11)

text_box11=tk.Entry(win10,width=25)
canvas_win10.create_window(270,130,window=text_box11)

label12=tk.Label(win10,text="لطفا اندازه قاعده را مشخص کنید",foreground="#fff",font=("B Nazanin",23),bg="#0e45ea")
canvas_win10.create_window(270,180,window=label12)

text_box12=tk.Entry(win10,width=25)
canvas_win10.create_window(270,230,window=text_box12)

m8=tk.Button(win10,text="محاسبه",bg="#dc9b0d",fg="black",width=12,height=2,command=masahat_mosalas)
canvas_win10.create_window(330,280, window=m8)

javab8=tk.Label(win10,text="",fg="black",bg="#dc9b0d",font=("B Nazanin",20))
canvas_win10.create_window(280,330,window=javab8)

v8=tk.Button(win10,text="ورودی جدید",bg="#dc9b0d",fg="black",width=12,height=2,command=reset8)
canvas_win10.create_window(230,280, window=v8)

b22=tk.Button(win10,text="بازگشت",bg="#dc9b0d",fg="black",width=12,height=2,command=back8)
canvas_win10.create_window(450,400, window=b22)
#endregion
#---------win11_mostatil------------------
#region
win11=tk.Toplevel(win1)
win11.withdraw()
win11.title("محیط مستطیل")
win11.geometry("550x550")
#-------canvas_win11------------
canvas_win11=tk.Canvas(win11,width=550,height=550)
canvas_win11.pack()

image11=Image.open("image13.png")
canvas_image11 = ImageTk.PhotoImage(image11.resize((550, 550)))
canvas_win11.create_image(275,275, anchor="center", image=canvas_image11)

label13=tk.Label(win11,text="لطفا اندازه طول را وارد کنید",foreground="black",font=("B Nazanin",25),bg="#0ddc94")
canvas_win11.create_window(270,80,window=label13)

text_box13=tk.Entry(win11,width=25)
canvas_win11.create_window(270,130,window=text_box13)

label14=tk.Label(win11,text="لطفا اندازه عرض را وارد کنید",foreground="black",font=("B Nazanin",23),bg="#0ddc94")
canvas_win11.create_window(270,180,window=label14)

text_box14=tk.Entry(win11,width=25)
canvas_win11.create_window(270,230,window=text_box14)

m9=tk.Button(win11,text="محاسبه",bg="#09bbd2",fg="black",width=12,height=2,command=mohit_mostatil)
canvas_win11.create_window(330,280, window=m9)

javab9=tk.Label(win11,text="",fg="black",bg="#09bbd2",font=("B Nazanin",20))
canvas_win11.create_window(280,330,window=javab9)

v9=tk.Button(win11,text="ورودی جدید",bg="#09bbd2",fg="black",width=12,height=2,command=reset9)
canvas_win11.create_window(230,280, window=v9)

b23=tk.Button(win11,text="بازگشت",bg="#0ddc94",fg="black",width=12,height=2,command=back9)
canvas_win11.create_window(450,400, window=b23)
#endregion
#---------win12_mostatil------------------
#region
win12=tk.Toplevel(win1)
win12.withdraw()
win12.title("مساحت مستطیل")
win12.geometry("550x550")
#-------canvas_win12------------
canvas_win12=tk.Canvas(win12,width=550,height=550)
canvas_win12.pack()

image12=Image.open("image12.png")
canvas_image12 = ImageTk.PhotoImage(image12.resize((550, 550)))
canvas_win12.create_image(275,275, anchor="center", image=canvas_image12)

label15=tk.Label(win12,text="لطفا اندازه طول را وارد کنید",foreground="#fff",font=("B Nazanin",25),bg="#1d4f2b")
canvas_win12.create_window(270,80,window=label15)

text_box15=tk.Entry(win12,width=25)
canvas_win12.create_window(270,130,window=text_box15)

label16=tk.Label(win12,text="لطفا اندازه عرض را وارد کنید",foreground="#fff",font=("B Nazanin",23),bg="#1d4f2b")
canvas_win12.create_window(270,180,window=label16)

text_box16=tk.Entry(win12,width=25)
canvas_win12.create_window(270,230,window=text_box16)

m10=tk.Button(win12,text="محاسبه",bg="#021e3b",fg="white",width=12,height=2,command=masahat_mostatil)
canvas_win12.create_window(330,280, window=m10)

javab10=tk.Label(win12,text="",fg="lightgray",bg="#1d4f2b",font=("B Nazanin",20))
canvas_win12.create_window(280,330,window=javab10)

v10=tk.Button(win12,text="ورودی جدید",bg="#021e3b",fg="white",width=12,height=2,command=reset10)
canvas_win12.create_window(230,280, window=v10)

b24=tk.Button(win12,text="بازگشت",bg="#1d4f2b",fg="#fff",width=12,height=2,command=back10)
canvas_win12.create_window(450,400, window=b24)
#endregion
#-----win13_motavazilazla---------
#region
win13=tk.Toplevel(win1)
win13.withdraw()
win13.title("محیط متوازی الاضلاع")
win13.geometry("550x550")
#---------canvas_win13-------------
canvas_win13=tk.Canvas(win13,width=550,height=550)
canvas_win13.pack()

image13=Image.open("image15.png")
canvas_image13 = ImageTk.PhotoImage(image13.resize((550, 550)))
canvas_win13.create_image(275,275, anchor="center", image=canvas_image13)

label17=tk.Label(win13,text="لطفا اندازه ضلع اول(مجاور) را وارد کنید",foreground="black",font=("B Nazanin",25),bg="#d1d0ad")
canvas_win13.create_window(270,80,window=label17)

text_box17=tk.Entry(win13,width=25)
canvas_win13.create_window(270,130,window=text_box17)

label16=tk.Label(win13,text="لطفا اندازه ضلع دوم(مجاور)را وارد کنید",foreground="black",font=("B Nazanin",23),bg="#d1d0ad")
canvas_win13.create_window(270,180,window=label16)

text_box18=tk.Entry(win13,width=25)
canvas_win13.create_window(270,230,window=text_box18)

m11=tk.Button(win13,text="محاسبه",bg="#d1d0ad",fg="black",width=12,height=2,command=mohit_motavazilazla)
canvas_win13.create_window(330,280, window=m11)

javab11=tk.Label(win13,text="",fg="black",bg="#d1d0ad",font=("B Nazanin",20))
canvas_win13.create_window(280,330,window=javab11)

v11=tk.Button(win13,text="ورودی جدید",bg="#d1d0ad",fg="black",width=12,height=2,command=reset11)
canvas_win13.create_window(230,280, window=v11)

b25=tk.Button(win13,text="بازگشت",bg="#d1d0ad",fg="black",width=12,height=2,command=back11)
canvas_win13.create_window(450,400, window=b25)
#endregion
#------win14_motavazilazla--------
#region
win14=tk.Toplevel(win1)
win14.withdraw()
win14.title("مساحت متوازی الاضلاع")
win14.geometry("550x550")
#---canvas_win14---------------
canvas_win14=tk.Canvas(win14,width=550,height=550)
canvas_win14.pack()

image14=Image.open("image16.png")
canvas_image14 = ImageTk.PhotoImage(image14.resize((550, 550)))
canvas_win14.create_image(275,275, anchor="center", image=canvas_image14)

label17=tk.Label(win14,text="لطفا اندازه ارتفاع را وارد کنید",foreground="black",font=("B Nazanin",25),bg="#cde70b")
canvas_win14.create_window(270,80,window=label17)

text_box19=tk.Entry(win14,width=25)
canvas_win14.create_window(270,130,window=text_box19)

label18=tk.Label(win14,text="لطفا اندازه قاعده را وارد کنید",foreground="black",font=("B Nazanin",23),bg="#cde70b")
canvas_win14.create_window(270,180,window=label18)

text_box20=tk.Entry(win14,width=25)
canvas_win14.create_window(270,230,window=text_box20)

m12=tk.Button(win14,text="محاسبه",bg="#cde70b",fg="black",width=12,height=2,command=masahat_motavazilazla)
canvas_win14.create_window(330,280, window=m12)

javab12=tk.Label(win14,text="",fg="black",bg="#cde70b",font=("B Nazanin",20))
canvas_win14.create_window(280,330,window=javab12)

v12=tk.Button(win14,text="ورودی جدید",bg="#cde70b",fg="black",width=12,height=2,command=reset12)
canvas_win14.create_window(230,280, window=v12)

b26=tk.Button(win14,text="بازگشت",bg="#cde70b",fg="black",width=12,height=2,command=back12)
canvas_win14.create_window(450,400, window=b26)
#endregion
#--------Run_Program-----------------
#region
win1.resizable(False, False) 
win8.resizable(False, False) 
win1.protocol("WM_DELETE_WINDOW",close_window)
win8.protocol("WM_DELETE_WINDOW",close_window)
win1.mainloop()
#endregion
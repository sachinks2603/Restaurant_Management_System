from tkinter import *
from tkinter import filedialog,messagebox

import random
import time

# Functions
def roti():
    if var1.get()==1:
        quanRoti.config(state=NORMAL)
        quanRoti.delete(0,END)
        quanRoti.focus()
        
    else:
        quanRoti.config(state=DISABLED)
        e_roti.set('0')
        
def pt():
    if var2.get()==1:
        quanpt.config(state=NORMAL)
        quanpt.delete(0,END)
        quanpt.focus()
        
    else:
        quanpt.config(state=DISABLED)
        e_pt.set('0')
        
def dal():
    if var3.get()==1:
        quandal.config(state=NORMAL)
        quandal.delete(0,END)
        quandal.focus()
        
    else:
        quandal.config(state=DISABLED)
        e_dal.set('0')

def sev():
    if var4.get()==1:
        quansev.config(state=NORMAL)
        quansev.delete(0,END)
        quansev.focus()
        
    else:
        quansev.config(state=DISABLED)
        e_sev.set('0')
        
def kp():
    if var5.get()==1:
        quankp.config(state=NORMAL)
        quankp.delete(0,END)
        quankp.focus()
        
    else:
        quankp.config(state=DISABLED)
        e_kp.set('0')
        
def sp():
    if var6.get()==1:
        quansp.config(state=NORMAL)
        quansp.delete(0,END)
        quansp.focus()
        
    else:
        quansp.config(state=DISABLED)
        e_sp.set('0')
        
def lp():
    if var7.get()==1:
        quanlp.config(state=NORMAL)
        quanlp.delete(0,END)
        quanlp.focus()
        
    else:
        quanlp.config(state=DISABLED)
        e_lp.set('0')

def mk():
    if var8.get()==1:
        quanmk.config(state=NORMAL)
        quanmk.delete(0,END)
        quanmk.focus()
        
    else:
        quanmk.config(state=DISABLED)
        e_mk.set('0')
        
def pp():
    if var9.get()==1:
        quanpp.config(state=NORMAL)
        quanpp.delete(0,END)
        quanpp.focus()
        
    else:
        quanpp.config(state=DISABLED)
        e_pp.set('0')

def cof():
    if var10.get()==1:
        quancof.config(state=NORMAL)
        quancof.delete(0,END)
        quancof.focus()
        
    else:
        quancof.config(state=DISABLED)
        e_cof.set('0')
        
def tea():
    if var11.get()==1:
        quantea.config(state=NORMAL)
        quantea.delete(0,END)
        quantea.focus()
        
    else:
        quantea.config(state=DISABLED)
        e_tea.set('0')
        
def beer():
    if var12.get()==1:
        quanbeer.config(state=NORMAL)
        quanbeer.delete(0,END)
        quanbeer.focus()
        
    else:
        quanbeer.config(state=DISABLED)
        e_beer.set('0')

def cs():
    if var13.get()==1:
        quancs.config(state=NORMAL)
        quancs.delete(0,END)
        quancs.focus()
        
    else:
        quancs.config(state=DISABLED)
        e_cs.set('0')
        
def ms():
    if var14.get()==1:
        quanms.config(state=NORMAL)
        quanms.delete(0,END)
        quanms.focus()
        
    else:
        quanms.config(state=DISABLED)
        e_ms.set('0')
        
def shi():
    if var15.get()==1:
        quanshi.config(state=NORMAL)
        quanshi.delete(0,END)
        quanshi.focus()
        
    else:
        quanshi.config(state=DISABLED)
        e_shi.set('0')
        
def thand():
    if var16.get()==1:
        quanthand.config(state=NORMAL)
        quanthand.delete(0,END)
        quanthand.focus()
        
    else:
        quanthand.config(state=DISABLED)
        e_thand.set('0')

def milk():
    if var17.get()==1:
        quanmilk.config(state=NORMAL)
        quanmilk.delete(0,END)
        quanmilk.focus()
        
    else:
        quanmilk.config(state=DISABLED)
        e_milk.set('0')
        
def cha():
    if var18.get()==1:
        quancha.config(state=NORMAL)
        quancha.delete(0,END)
        quancha.focus()
        
    else:
        quancha.config(state=DISABLED)
        e_cha.set('0')

def oreo():
    if var19.get()==1:
        quanoreo.config(state=NORMAL)
        quanoreo.delete(0,END)
        quanoreo.focus()
        
    else:
        quanoreo.config(state=DISABLED)
        e_oreo.set('0')
        
def bf():
    if var20.get()==1:
        quanbf.config(state=NORMAL)
        quanbf.delete(0,END)
        quanbf.focus()
        
    else:
        quanbf.config(state=DISABLED)
        e_bf.set('0')
        
def straw():
    if var21.get()==1:
        quanstraw.config(state=NORMAL)
        quanstraw.delete(0,END)
        quanstraw.focus()
        
    else:
        quanstraw.config(state=DISABLED)
        e_straw.set('0')

def van():
    if var22.get()==1:
        quanvan.config(state=NORMAL)
        quanvan.delete(0,END)
        quanvan.focus()
        
    else:
        quanvan.config(state=DISABLED)
        e_van.set('0')
        
def choco():
    if var23.get()==1:
        quanchoco.config(state=NORMAL)
        quanchoco.delete(0,END)
        quanchoco.focus()
        
    else:
        quanchoco.config(state=DISABLED)
        e_choco.set('0')
        
def ic():
    if var24.get()==1:
        quanic.config(state=NORMAL)
        quanic.delete(0,END)
        quanic.focus()
        
    else:
        quanic.config(state=DISABLED)
        e_ic.set('0')
        
def sa():
    if var25.get()==1:
        quansa.config(state=NORMAL)
        quansa.delete(0,END)
        quansa.focus()
        
    else:
        quansa.config(state=DISABLED)
        e_sa.set('0')

def p2():
    if var26.get()==1:
        quanp2.config(state=NORMAL)
        quanp2.delete(0,END)
        quanp2.focus()
        
    else:
        quanp2.config(state=DISABLED)
        e_p2.set('0')
        
def pin():
    if var27.get()==1:
        quanpin.config(state=NORMAL)
        quanpin.delete(0,END)
        quanpin.focus()
        
    else:
        quanpin.config(state=DISABLED)
        e_pin.set('0')
        
def totalcost():
    item1=int(e_roti.get())*7
    item2=int(e_pt.get())*160
    item3=int(e_dal.get())*90
    item4=int(e_sev.get())*110
    item5=int(e_kp.get())*140
    item6=int(e_sp.get())*160
    item7=int(e_lp.get())*20
    item8=int(e_mk.get())*160
    item9=int(e_pp.get())*140
    
    item10 = int(e_cof.get())*40
    item11 = int(e_tea.get())*20
    item12 = int(e_beer.get())*800
    item13 = int(e_cs.get())*100
    item14 = int(e_ms.get())*80
    item15 = int(e_shi.get())*50
    item16 = int(e_thand.get())*50
    item17 = int(e_milk.get())*50
    item18 = int(e_cha.get())*25
    
    item19 = int(e_oreo.get())*400
    item20 = int(e_bf.get())*350
    item21 = int(e_straw.get())*300
    item22 = int(e_van.get())*300
    item23 = int(e_choco.get())*400
    item24 = int(e_ic.get())*400
    item25 = int(e_sa.get())*500
    item26 = int(e_p2.get())*450
    item27 = int(e_pin.get())*350
    
    totalfoodcost = item1+item2+item3+item4+item5+item6+item7+item8+item9
    totaldrinkcost = item10+item11+item12+item13+item14+item15+item16+item17+item18
    totalcakecost = item19+item20+item21+item22+item23+item24+item25+item26+item27
    
    subtotalcost = totalfoodcost+totaldrinkcost+totalcakecost
    servicetaxcost = 50
    if subtotalcost>=3000:
        servicetaxcost=0
    total = subtotalcost + servicetaxcost
    
    costoffoodvar.set(str(totalfoodcost)+' Rs.')
    costofdrinksvar.set(str(totaldrinkcost)+' Rs.')
    costofcakesvar.set(str(totalcakecost)+' Rs.')
    subtotalvar.set(str(subtotalcost)+'Rs.')
    servicetaxvar.set(f'{servicetaxcost} Rs.')
    totalcostvar.set(str(total)+' Rs.')
    
def getReceipt():
    global billno,date,totalfoodcost,totaldrinkcost,totalcakecost,subtotalcost,total,servicetaxcost
    textreceipt.delete(1.0,END)
    billno = random.randint(100,10000)
    date = time.strftime('%d-%m-%Y')
    textreceipt.insert(END,f"Receipt Ref: {billno}\t\t\t    Date: {date}\n")
    textreceipt.insert(END, "*"*61+'\n\n')
    textreceipt.insert(END, 'Items\t\t  Cost of Items\n')
    textreceipt.insert(END, "*"*61+'\n')
    totalfoodcost=0
    totaldrinkcost=0
    totalcakecost=0
    subtotalcost=0
    servicetaxcost=50
    if e_roti.get()!='0':
        item1=int(e_roti.get())*7
        totalfoodcost+=item1
        textreceipt.insert(END, f'Roti\t\t  {item1}\n')
    if e_pt.get()!='0':
        item1=int(e_pt.get())*160
        totalfoodcost+=item1
        textreceipt.insert(END, f'Panner Tikka\t\t  {item1}\n')
    if e_dal.get()!='0':
        item1=int(e_dal.get())*90
        totalfoodcost+=item1
        textreceipt.insert(END, f'Dal\t\t  {item1}\n')
    if e_sev.get()!='0':
        item1=int(e_sev.get())*110
        totalfoodcost+=item1
        textreceipt.insert(END, f'Sev Bhaji\t\t  {item1}\n')
    if e_kp.get()!='0':
        item1=int(e_kp.get())*140
        totalfoodcost+=item1
        textreceipt.insert(END, f'Khoa Panner\t\t  {item1}\n')
    if e_sp.get()!='0':
        item1=int(e_sp.get())*160
        totalfoodcost+=item1
        textreceipt.insert(END, f'Shahi Panner\t\t  {item1}\n')
    if e_lp.get()!='0':
        item1=int(e_lp.get())*20
        totalfoodcost+=item1
        textreceipt.insert(END, f'Laccha Parantha\t\t  {item1}\n')
    if e_mk.get()!='0':  
        item1=int(e_mk.get())*160
        totalfoodcost+=item1
        textreceipt.insert(END, f'Malai Kofta\t\t  {item1}\n')
    if e_pp.get()!='0':
        item1=int(e_pp.get())*140
        totalfoodcost+=item1
        textreceipt.insert(END, f'Palak Panner\t\t  {item1}\n')
    
    if e_cof.get()!='0':
        item1=int(e_cof.get())*40
        totaldrinkcost+=item1
        textreceipt.insert(END, f'Coffee\t\t  {item1}\n')
    if e_tea.get()!='0':
        item1=int(e_tea.get())*20
        totaldrinkcost+=item1
        textreceipt.insert(END, f'Tea\t\t  {item1}\n')
    if e_beer.get()!='0':
        item1=int(e_beer.get())*800
        totaldrinkcost+=item1
        textreceipt.insert(END, f'Beer\t\t  {item1}\n')
    if e_cs.get()!='0':
        item1=int(e_cs.get())*100
        totaldrinkcost+=item1
        textreceipt.insert(END, f'Chocolate Shake\t\t  {item1}\n')
    if e_ms.get()!='0':
        item1=int(e_ms.get())*80
        totaldrinkcost+=item1
        textreceipt.insert(END, f'Milk Shake\t\t  {item1}\n')
    if e_shi.get()!='0':
        item1=int(e_shi.get())*50
        totaldrinkcost+=item1
        textreceipt.insert(END, f'ShikanJi\t\t  {item1}\n')
    if e_thand.get()!='0':
        item1=int(e_thand.get())*50
        totaldrinkcost+=item1
        textreceipt.insert(END, f'Thandai\t\t  {item1}\n')
    if e_milk.get()!='0':  
        item1=int(e_milk.get())*50
        totaldrinkcost+=item1
        textreceipt.insert(END, f'Milk\t\t  {item1}\n')
    if e_cha.get()!='0':
        item1=int(e_cha.get())*25
        totaldrinkcost+=item1
        textreceipt.insert(END, f'Lassi\t\t  {item1}\n')
        
    if e_oreo.get()!='0':
        item1=int(e_oreo.get())*400
        totalcakecost+=item1
        textreceipt.insert(END, f'Oreo\t\t  {item1}\n')
    if e_bf.get()!='0':
        item1=int(e_bf.get())*350
        totalcakecost+=item1
        textreceipt.insert(END, f'Black Forest\t\t  {item1}\n')
    if e_straw.get()!='0':
        item1=int(e_straw.get())*300
        totalcakecost+=item1
        textreceipt.insert(END, f'Strawberry\t\t  {item1}\n')
    if e_van.get()!='0':
        item1=int(e_van.get())*300
        totalcakecost+=item1
        textreceipt.insert(END, f'Vanilla\t\t  {item1}\n')
    if e_choco.get()!='0':
        item1=int(e_choco.get())*400
        totalcakecost+=item1
        textreceipt.insert(END, f'Milk Shake\t\t  {item1}\n')
    if e_ic.get()!='0':
        item1=int(e_ic.get())*400
        totalcakecost+=item1
        textreceipt.insert(END, f'Ice Cream\t\t  {item1}\n')
    if e_sa.get()!='0':
        item1=int(e_sa.get())*500
        totalcakecost+=item1
        textreceipt.insert(END, f'Special Cake\t\t  {item1}\n')
    if e_p2.get()!='0':  
        item1=int(e_p2.get())*450
        totalcakecost+=item1
        textreceipt.insert(END, f'2 Pounds\t\t  {item1}\n')
    if e_pin.get()!='0':
        item1=int(e_pin.get())*350
        totalcakecost+=item1
        textreceipt.insert(END, f'Pinapple\t\t  {item1}\n')
    
    textreceipt.insert(END,"*"*61+'\n')
    subtotalcost+=totalcakecost+totaldrinkcost+totalfoodcost
    if subtotalcost>=3000:
        servicetaxcost=0
    total=subtotalcost+servicetaxcost
    if totalfoodcost>0:
        textreceipt.insert(END, f'Cost of Food\t\t  {totalfoodcost}\n')
    if totaldrinkcost>0:
        textreceipt.insert(END, f'Cost of Drinks\t\t  {totaldrinkcost}\n')
    if totalcakecost>0:
        textreceipt.insert(END, f'Cost of Cakes\t\t  {totalcakecost}\n')
    textreceipt.insert(END, f'Sub Total\t\t  {subtotalcost}\n')
    textreceipt.insert(END, f'Service Tax \t\t  {servicetaxcost}\n')
    textreceipt.insert(END, f'Total Amount\t\t  {total}\n')
    textreceipt.insert(END,"*"*61)
    
def save():
    url=filedialog.asksaveasfile(mode='w',defaultextension='.txt')
    bill_data=textreceipt.get(1.0,END)
    url.write(bill_data)
    url.close()
    messagebox.showinfo('Information','Bill is saved successfully')
    
def send():
    root2 = Toplevel()
    
    root2.title("SEND BILL")
    root2.geometry('485x620+50+50')
    root2.config(bg="red4")
    root.resizable(0,0)
    logoImage = PhotoImage(file="sender.png")
    lable = Label(root2,image=logoImage,bg='red4')
    lable.pack(pady=5)
    numberLabel  = Label(root2,text='Mobile Number',font=('arial',18,'underline'),fg='white',bg='red4')
    numberLabel.pack(pady=5)
    
    numberEntry=Entry(root2,font=('arial',18),bd=3)
    numberEntry.pack(pady=5)
    
    billLabel  = Label(root2,text='Bill Details',font=('arial',18,'underline'),fg='white',bg='red4')
    billLabel.pack(pady=5)
    
    textarea=Text(root2,font=('arial',12,'bold'),bd=3,width=42,height=14)
    textarea.pack(pady=5)
    
    textarea.insert(END,f"Receipt Ref: {billno}\t\t\t    Date: {date}\n\n")
    
    if totalfoodcost>0:
        textarea.insert(END, f'Cost of Food\t\t  {totalfoodcost}\n')
    if totaldrinkcost>0:
        textarea.insert(END, f'Cost of Drinks\t\t  {totaldrinkcost}\n')
    if totalcakecost>0:
        textarea.insert(END, f'Cost of Cakes\t\t  {totalcakecost}\n')
    textarea.insert(END, f'Sub Total\t\t  {subtotalcost}\n')
    textarea.insert(END, f'Service Tax \t\t  {servicetaxcost}\n')
    textarea.insert(END, f'Total Amount\t\t  {total}\n')
    
    sendButton = Button(root2,text='SEND',font=('arial',19,'bold'),fg='red4',bg='white',bd=5,relief=GROOVE,command='send_msg')
    sendButton.pack(pady=5)
    
    root2.mainloop()
    
def send_msg():
    pass
    
def reset():
    textreceipt.delete(1.0,END)
    costoffoodvar.set('')
    costofdrinksvar.set('')
    costofcakesvar.set('')
    subtotalvar.set('')
    servicetaxvar.set('')
    totalcostvar.set('')
    var1.set(0)
    var2.set(0)
    var3.set(0)
    var4.set(0)
    var5.set(0)
    var6.set(0)
    var7.set(0)
    var8.set(0)
    var9.set(0)
    var10.set(0)
    var11.set(0)
    var12.set(0)
    var13.set(0)
    var14.set(0)
    var15.set(0)
    var16.set(0)
    var17.set(0)
    var18.set(0)
    var19.set(0)
    var20.set(0)
    var21.set(0)
    var22.set(0)
    var23.set(0)
    var24.set(0)
    var25.set(0)
    var26.set(0)
    var27.set(0)
    quanRoti.config(state=DISABLED)
    quanbeer.config(state=DISABLED)
    quanbf.config(state=DISABLED)
    quancha.config(state=DISABLED)
    quanchoco.config(state=DISABLED)
    quancof.config(state=DISABLED)
    quancs.config(state=DISABLED)
    quandal.config(state=DISABLED)
    quanic.config(state=DISABLED)
    quankp.config(state=DISABLED)
    quanlp.config(state=DISABLED)
    quanmilk.config(state=DISABLED)
    quanmk.config(state=DISABLED)
    quanms.config(state=DISABLED)
    quanoreo.config(state=DISABLED)
    quanp2.config(state=DISABLED)
    quanpt.config(state=DISABLED)
    quanpp.config(state=DISABLED)
    quanpin.config(state=DISABLED)
    quansa.config(state=DISABLED)
    quansev.config(state=DISABLED)
    quansp.config(state=DISABLED)
    quanshi.config(state=DISABLED)
    quanstraw.config(state=DISABLED)
    quantea.config(state=DISABLED)
    quanthand.config(state=DISABLED)
    quanvan.config(state=DISABLED)
    e_roti.set('0')
    e_beer.set('0')
    e_bf.set('0')
    e_cha.set('0')
    e_choco.set('0')
    e_cof.set('0')
    e_cs.set('0')
    e_dal.set('0')
    e_ic.set('0')
    e_kp.set('0')
    e_lp.set('0')
    e_milk.set('0')
    e_mk.set('0')
    e_ms.set('0')
    e_oreo.set('0')
    e_p2.set('0')
    e_pt.set('0')
    e_pp.set('0')
    e_pin.set('0')
    e_sa.set('0')
    e_sp.set('0')
    e_sev.set('0')
    e_straw.set('0')
    e_tea.set('0')
    e_thand.set('0')
    e_van.set('0')
    e_shi.set('0')


    
root=Tk()

root.geometry('1050x650+0+0')
root.resizable(0,0)
root.config(bg='#333')
root.title('Restaurant Management System')
topFrame=Frame(root,bd=10,relief=FLAT,bg='#333')
# For the Top Most Frame
topFrame.pack(side=TOP)
labelTitle=Label(topFrame,text='Restaurant Bill System',font=('arial',40,'bold'),bg='#333',fg='#a7c221',bd=10)
labelTitle.grid(row=0,column=0)

# For the Left Menu Frame
menuFrame=Frame(root,bd=7,relief=RIDGE,bg='#333')
menuFrame.pack(side=LEFT)

# For the cost menu that is at bottom
costFrame=Frame(menuFrame,bd=4,relief=FLAT,bg='#333')
costFrame.pack(side=BOTTOM)

# For the Food menu that is inside menu frame and also labelled and in left
foodFrame=LabelFrame(menuFrame,text='Foods',font=('arial',17,'bold'),bd=4,relief=RIDGE,fg='red')
foodFrame.pack(side=LEFT)

# For the Drink menu that is inside menu frame and also labelled and next to food
drinkFrame=LabelFrame(menuFrame,text='Drinks',font=('arial',17,'bold'),bd=4,relief=RIDGE,fg='red')
drinkFrame.pack(side=LEFT)

# For the Cake menu that is inside menu frame and also labelled and next to cake
cakeFrame=LabelFrame(menuFrame,text='Cakes',font=('arial',17,'bold'),bd=4,relief=RIDGE,fg='red')
cakeFrame.pack(side=LEFT)

# For Right Frame
rightFrame=Frame(root,bd=12,relief=RIDGE,bg='#333')
rightFrame.pack(side=RIGHT)

# For the calculator Area
calculatorFrame=Frame(rightFrame,bd=1,relief=RIDGE,bg='#333')
calculatorFrame.pack()

# For the receipt Area
receiptFrame=Frame(rightFrame,bd=4,relief=RIDGE,bg='#333')
receiptFrame.pack()

# For the button Area
buttonFrame=Frame(rightFrame,bd=4,relief=RIDGE,bg='#000')
buttonFrame.pack()

# Variable Section
var1=IntVar()
var2=IntVar()
var3=IntVar()
var4=IntVar()
var5=IntVar()
var6=IntVar()
var7=IntVar()
var8=IntVar()
var9=IntVar()
var10=IntVar()
var11=IntVar()
var12=IntVar()
var13=IntVar()
var14=IntVar()
var15=IntVar()
var16=IntVar()
var17=IntVar()
var18=IntVar()
var19=IntVar()
var20=IntVar()
var21=IntVar()
var22=IntVar()
var23=IntVar()
var24=IntVar()
var25=IntVar()
var26=IntVar()
var27=IntVar()

# variable for foods
e_roti=StringVar()      #7
e_pt=StringVar()        #160
e_dal=StringVar()       #90
e_sev=StringVar()       #110
e_kp=StringVar()        #140
e_sp=StringVar()        #160
e_lp=StringVar()        #20 
e_mk=StringVar()        #160
e_pp=StringVar()        #140    

#variable for drinks

e_cof=StringVar()       #40
e_tea=StringVar()       #20
e_beer=StringVar()      #800
e_cs=StringVar()        #100
e_ms=StringVar()        #80 
e_shi=StringVar()       #50
e_thand=StringVar()     #50
e_milk=StringVar()      #50
e_cha=StringVar()       #25

#variable for cakes

e_oreo=StringVar()      #400
e_bf=StringVar()        #350
e_straw=StringVar()     #300
e_van=StringVar()       #300
e_choco=StringVar()     #400
e_ic=StringVar()        #400
e_sa=StringVar()        #500
e_p2=StringVar()        #450
e_pin=StringVar()       #350

# variable of cost Section
costoffoodvar=StringVar()
costofdrinksvar=StringVar()
costofcakesvar=StringVar()
subtotalvar=StringVar()
servicetaxvar=StringVar()
totalcostvar=StringVar()


# set variable for foods
e_roti.set('0')
e_pt.set('0')
e_dal.set('0')
e_sev.set('0')
e_kp.set('0')
e_sp.set('0')
e_lp.set('0')
e_mk.set('0')
e_pp.set('0')

#set variable for drinks

e_cof.set('0')
e_tea.set('0')
e_beer.set('0')
e_cs.set('0')
e_ms.set('0')
e_shi.set('0')
e_thand.set('0')
e_milk.set('0')
e_cha.set('0')

#set variable for cakes

e_oreo.set('0')
e_bf.set('0')
e_straw.set('0')
e_van.set('0')
e_choco.set('0')
e_ic.set('0')
e_sa.set('0')
e_p2.set('0')
e_pin.set('0')

# Food Section
roti=Checkbutton(foodFrame,text='Roti',font=('arial',16,'bold'),onvalue=1,offvalue=0,variable=var1,command=roti)
roti.grid(row=0,column=0,sticky=W)
paneer_tikka=Checkbutton(foodFrame,text='Paneer Tikka',font=('arial',16,'bold'),onvalue=1,offvalue=0,variable=var2,command=pt)
paneer_tikka.grid(row=1,column=0,sticky=W)
dal=Checkbutton(foodFrame,text='Dal',font=('arial',16,'bold'),onvalue=1,offvalue=0,variable=var3,command=dal)
dal.grid(row=2,column=0,sticky=W)
sev=Checkbutton(foodFrame,text='Sev Bhaji',font=('arial',16,'bold'),onvalue=1,offvalue=0,variable=var4,command=sev)
sev.grid(row=3,column=0,sticky=W)
khopan=Checkbutton(foodFrame,text='Khoa Paneer',font=('arial',16,'bold'),onvalue=1,offvalue=0,variable=var5,command=kp)
khopan.grid(row=4,column=0,sticky=W)
shpan=Checkbutton(foodFrame,text='Shai Paneer',font=('arial',16,'bold'),onvalue=1,offvalue=0,variable=var6,command=sp)
shpan.grid(row=5,column=0,sticky=W)
lachha=Checkbutton(foodFrame,text='Lachha Parantha',font=('arial',16,'bold'),onvalue=1,offvalue=0,variable=var7,command=lp)
lachha.grid(row=6,column=0,sticky=W)
malai=Checkbutton(foodFrame,text='Malai Kofta',font=('arial',16,'bold'),onvalue=1,offvalue=0,variable=var8,command=mk)
malai.grid(row=7,column=0,sticky=W)
palakpan=Checkbutton(foodFrame,text='Palak Paneer',font=('arial',16,'bold'),onvalue=1,offvalue=0,variable=var9,command=pp)
palakpan.grid(row=8,column=0,sticky=W)

# Entry Fields For Food
quanRoti=Entry(foodFrame,font=('arial',12,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_roti)
quanRoti.grid(row=0,column=1)
quanpt=Entry(foodFrame,font=('arial',12,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_pt)
quanpt.grid(row=1,column=1)
quandal=Entry(foodFrame,font=('arial',12,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_dal)
quandal.grid(row=2,column=1)
quansev=Entry(foodFrame,font=('arial',12,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_sev)
quansev.grid(row=3,column=1)
quankp=Entry(foodFrame,font=('arial',12,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_kp)
quankp.grid(row=4,column=1)
quansp=Entry(foodFrame,font=('arial',12,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_sp)
quansp.grid(row=5,column=1)
quanlp=Entry(foodFrame,font=('arial',12,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_lp)
quanlp.grid(row=6,column=1)
quanmk=Entry(foodFrame,font=('arial',12,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_mk)
quanmk.grid(row=7,column=1)
quanpp=Entry(foodFrame,font=('arial',12,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_pp)
quanpp.grid(row=8,column=1)

## Drinks Section
coffee=Checkbutton(drinkFrame,text='Coffee',font=('arial',16,'bold'),onvalue=1,offvalue=0,variable=var10,command=cof)
coffee.grid(row=0,column=0,sticky=W)
tea=Checkbutton(drinkFrame,text='Tea',font=('arial',16,'bold'),onvalue=1,offvalue=0,variable=var11,command=tea)
tea.grid(row=1,column=0,sticky=W)
beer=Checkbutton(drinkFrame,text='Beer',font=('arial',16,'bold'),onvalue=1,offvalue=0,variable=var12,command=beer)
beer.grid(row=2,column=0,sticky=W)
cs=Checkbutton(drinkFrame,text='Chocolate Shake',font=('arial',16,'bold'),onvalue=1,offvalue=0,variable=var13,command=cs)
cs.grid(row=3,column=0,sticky=W)
ms=Checkbutton(drinkFrame,text='Milk Shake',font=('arial',16,'bold'),onvalue=1,offvalue=0,variable=var14,command=ms)
ms.grid(row=4,column=0,sticky=W)
shikanji=Checkbutton(drinkFrame,text='ShikanJi',font=('arial',16,'bold'),onvalue=1,offvalue=0,variable=var15,command=shi)
shikanji.grid(row=5,column=0,sticky=W)
thandai=Checkbutton(drinkFrame,text='Thandai',font=('arial',16,'bold'),onvalue=1,offvalue=0,variable=var16,command=thand)
thandai.grid(row=6,column=0,sticky=W)
Milk=Checkbutton(drinkFrame,text='Milk',font=('arial',16,'bold'),onvalue=1,offvalue=0,variable=var17,command=milk)
Milk.grid(row=7,column=0,sticky=W)
chach=Checkbutton(drinkFrame,text='Lassi',font=('arial',16,'bold'),onvalue=1,offvalue=0,variable=var18,command=cha)
chach.grid(row=8,column=0,sticky=W)

# Entry Fields For Drinks
quancof=Entry(drinkFrame,font=('arial',12,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_cof)
quancof.grid(row=0,column=1)
quantea=Entry(drinkFrame,font=('arial',12,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_tea)
quantea.grid(row=1,column=1)
quanbeer=Entry(drinkFrame,font=('arial',12,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_beer)
quanbeer.grid(row=2,column=1)
quancs=Entry(drinkFrame,font=('arial',12,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_cs)
quancs.grid(row=3,column=1)
quanms=Entry(drinkFrame,font=('arial',12,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_ms)
quanms.grid(row=4,column=1)
quanshi=Entry(drinkFrame,font=('arial',12,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_shi)
quanshi.grid(row=5,column=1)
quanthand=Entry(drinkFrame,font=('arial',12,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_thand)
quanthand.grid(row=6,column=1)
quanmilk=Entry(drinkFrame,font=('arial',12,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_milk)
quanmilk.grid(row=7,column=1)
quancha=Entry(drinkFrame,font=('arial',12,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_cha)
quancha.grid(row=8,column=1)

## Cakes Section
Oreo=Checkbutton(cakeFrame,text='Oreo',font=('arial',16,'bold'),onvalue=1,offvalue=0,variable=var19,command=oreo)
Oreo.grid(row=0,column=0,sticky=W)
Black_Forest=Checkbutton(cakeFrame,text='Black Forest',font=('arial',16,'bold'),onvalue=1,offvalue=0,variable=var20,command=bf)
Black_Forest.grid(row=1,column=0,sticky=W)
strawberry=Checkbutton(cakeFrame,text='Strawberry',font=('arial',16,'bold'),onvalue=1,offvalue=0,variable=var21,command=straw)
strawberry.grid(row=2,column=0,sticky=W)
vanila=Checkbutton(cakeFrame,text='Vanilla',font=('arial',16,'bold'),onvalue=1,offvalue=0,variable=var22,command=van)
vanila.grid(row=3,column=0,sticky=W)
chocolate=Checkbutton(cakeFrame,text='Chocolate',font=('arial',16,'bold'),onvalue=1,offvalue=0,variable=var23,command=choco)
chocolate.grid(row=4,column=0,sticky=W)
ice_cream=Checkbutton(cakeFrame,text='Ice Cream',font=('arial',16,'bold'),onvalue=1,offvalue=0,variable=var24,command=ic)
ice_cream.grid(row=5,column=0,sticky=W)
Special_Abhi=Checkbutton(cakeFrame,text='Special Cake',font=('arial',16,'bold'),onvalue=1,offvalue=0,variable=var25,command=sa)
Special_Abhi.grid(row=6,column=0,sticky=W)
Pound2=Checkbutton(cakeFrame,text='2Pound',font=('arial',16,'bold'),onvalue=1,offvalue=0,variable=var26,command=p2)
Pound2.grid(row=7,column=0,sticky=W)
Pinapple=Checkbutton(cakeFrame,text='Pinapple',font=('arial',16,'bold'),onvalue=1,offvalue=0,variable=var27,command=pin)
Pinapple.grid(row=8,column=0,sticky=W)

# Entry Fields For Cakes
quanoreo=Entry(cakeFrame,font=('arial',12,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_oreo)
quanoreo.grid(row=0,column=1)
quanbf=Entry(cakeFrame,font=('arial',12,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_bf)
quanbf.grid(row=1,column=1)
quanstraw=Entry(cakeFrame,font=('arial',12,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_straw)
quanstraw.grid(row=2,column=1)
quanvan=Entry(cakeFrame,font=('arial',12,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_van)
quanvan.grid(row=3,column=1)
quanchoco=Entry(cakeFrame,font=('arial',12,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_choco)
quanchoco.grid(row=4,column=1)
quanic=Entry(cakeFrame,font=('arial',12,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_ic)
quanic.grid(row=5,column=1)
quansa=Entry(cakeFrame,font=('arial',12,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_sa)
quansa.grid(row=6,column=1)
quanp2=Entry(cakeFrame,font=('arial',12,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_p2)
quanp2.grid(row=7,column=1)
quanpin=Entry(cakeFrame,font=('arial',12,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_pin)
quanpin.grid(row=8,column=1)

## Cost label and Entry
costLabelToFood = Label(costFrame,text="Cost of Food",bd=4,font=('arial',17,'bold'),bg='#333',fg='white',padx=37,pady=10)
costLabelToFood.grid(row=0,column=0)

textcostofFood = Entry(costFrame,font=('arial',17,'bold'),bd=6,width=14,state='readonly',textvariable=costoffoodvar)
textcostofFood.grid(row=0,column=1)

costLabelToDrinks = Label(costFrame,text="Cost of Drinks",font=('arial',17,'bold'),bg='#333',fg='white',padx=37,pady=10)
costLabelToDrinks.grid(row=1,column=0)

textcostofDrinks = Entry(costFrame,font=('arial',17,'bold'),bd=6,width=14,state='readonly',textvariable=costofdrinksvar)
textcostofDrinks.grid(row=1,column=1)

costLabelToCakes = Label(costFrame,text="Cost of Cakes",font=('arial',17,'bold'),bg='#333',fg='white',padx=37,pady=10)
costLabelToCakes.grid(row=2,column=0)

textcostofCakes = Entry(costFrame,font=('arial',17,'bold'),bd=6,width=14,state='readonly',textvariable=costofcakesvar)
textcostofCakes.grid(row=2,column=1)

costLabelToSubTotal = Label(costFrame,text="Sub Total",font=('arial',17,'bold'),bg='#333',fg='white',padx=37,pady=10)
costLabelToSubTotal.grid(row=0,column=2)

textcostofSubTotal = Entry(costFrame,font=('arial',17,'bold'),bd=6,width=14,state='readonly',textvariable=subtotalvar)
textcostofSubTotal.grid(row=0,column=3)

costLabelToServiceTax = Label(costFrame,text="Service Tax",font=('arial',17,'bold'),bg='#333',fg='white',padx=37,pady=10)
costLabelToServiceTax.grid(row=1,column=2)

textcostofServiceTax = Entry(costFrame,font=('arial',17,'bold'),bd=6,width=14,state='readonly',textvariable=servicetaxvar)
textcostofServiceTax.grid(row=1,column=3)

costLabelToTotal = Label(costFrame,text="Total Cost",font=('arial',17,'bold'),bg='#333',fg='white',padx=37,pady=10)
costLabelToTotal.grid(row=2,column=2)

textcostofTotal = Entry(costFrame,font=('arial',17,'bold'),bd=6,width=14,state='readonly',textvariable=totalcostvar)
textcostofTotal.grid(row=2,column=3)

# Buttons
buttonTotal=Button(buttonFrame,text='Total',font=('aria',14,'bold'),bg='#333',fg='black',padx=5 , \
                    command = totalcost)
buttonTotal.grid(row=0,column=0)

buttonReceipt=Button(buttonFrame,text='Receipt',font=('aria',14,'bold'),bg='#333',fg='black',padx=5,command = getReceipt)
buttonReceipt.grid(row=0,column=1)

buttonSave=Button(buttonFrame,text='Save',font=('aria',14,'bold'),bg='#333',fg='black',padx=5,command=save)
buttonSave.grid(row=0,column=2)

buttonSend=Button(buttonFrame,text='Send',font=('aria',14,'bold'),bg='#333',fg='black',padx=5,command=send)
buttonSend.grid(row=0,column=3)

buttonReset=Button(buttonFrame,text='Reset',font=('aria',14,'bold'),bg='#333',fg='black',padx=5,command=reset)
buttonReset.grid(row=0,column=4)

# text area for receipt frame
textreceipt=Text(receiptFrame,font=('arial',12,'bold'),width=39,height=14.4)
textreceipt.grid(row=0,column=0)

# For calculator
operator=''
def buttonClick(numbers):
    global operator
    operator+=numbers
    calculatorField.delete(0,END)
    calculatorField.insert(END,operator)
    
def clear():
    global operator
    operator=''
    calculatorField.delete(0,END)

def answer():
    global operator
    ans=str(eval(operator))
    operator=ans
    calculatorField.delete(0,END)
    calculatorField.insert(END,ans)

calculatorField=Entry(calculatorFrame,font=('arial',14,'bold'),width=34)
calculatorField.grid(row=0,column=0,columnspan=4)

button7=Button(calculatorFrame,text='7',font=('arial',14,'bold'),fg='black',bg='#333',width=7,command=lambda:buttonClick('7'))
button7.grid(row=1,column=0)
button8=Button(calculatorFrame,text='8',font=('arial',14,'bold'),fg='black',bg='#333',width=7,command=lambda:buttonClick('8'))
button8.grid(row=1,column=1)
button9=Button(calculatorFrame,text='9',font=('arial',14,'bold'),fg='black',bg='#333',width=7,command=lambda:buttonClick('9'))
button9.grid(row=1,column=2)
buttonplus=Button(calculatorFrame,text='+',font=('arial',14,'bold'),fg='black',bg='#333',width=7,command=lambda:buttonClick('+'))
buttonplus.grid(row=1,column=3)

button4=Button(calculatorFrame,text='4',font=('arial',14,'bold'),fg='black',bg='#333',width=7,command=lambda:buttonClick('4'))
button4.grid(row=2,column=0)
button5=Button(calculatorFrame,text='5',font=('arial',14,'bold'),fg='black',bg='#333',width=7,command=lambda:buttonClick('5'))
button5.grid(row=2,column=1)
button6=Button(calculatorFrame,text='6',font=('arial',14,'bold'),fg='black',bg='#333',width=7,command=lambda:buttonClick('6'))
button6.grid(row=2,column=2)
buttonmin=Button(calculatorFrame,text='-',font=('arial',14,'bold'),fg='black',bg='#333',width=7,command=lambda:buttonClick('-'))
buttonmin.grid(row=2,column=3)

button1=Button(calculatorFrame,text='1',font=('arial',14,'bold'),fg='black',bg='#333',width=7,command=lambda:buttonClick('1'))
button1.grid(row=3,column=0)
button2=Button(calculatorFrame,text='2',font=('arial',14,'bold'),fg='black',bg='#333',width=7,command=lambda:buttonClick('2'))
button2.grid(row=3,column=1)
button3=Button(calculatorFrame,text='3',font=('arial',14,'bold'),fg='black',bg='#333',width=7,command=lambda:buttonClick('3'))
button3.grid(row=3,column=2)
buttonmul=Button(calculatorFrame,text='*',font=('arial',14,'bold'),fg='black',bg='#333',width=7,command=lambda:buttonClick('*'))
buttonmul.grid(row=3,column=3)

buttonans=Button(calculatorFrame,text='Ans',font=('arial',14,'bold'),fg='black',bg='#333',width=7,command=lambda:answer())
buttonans.grid(row=4,column=0)
buttonclear=Button(calculatorFrame,text='Clear',font=('arial',14,'bold'),fg='black',bg='#333',width=7,command=lambda:clear())
buttonclear.grid(row=4,column=1)
button0=Button(calculatorFrame,text='0',font=('arial',14,'bold'),fg='black',bg='#333',width=7,command=lambda:buttonClick('0'))
button0.grid(row=4,column=2)
buttondiv=Button(calculatorFrame,text='/',font=('arial',14,'bold'),fg='black',bg='#333',width=7,command=lambda:buttonClick('/'))
buttondiv.grid(row=4,column=3)

root.mainloop()
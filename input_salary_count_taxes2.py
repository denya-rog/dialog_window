#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 14:15:57 2017

@author: denya

This funktion takes csv file, and iterate thru every name in column "name".
Operator set salary, and programm calculate taxes
"""

from Tkinter import *
import pandas as pd

logWindowExists = False
reque=0

class LogWindow(Frame):
    """dialog window class"""
    def __init__(self, parent):
        
        Frame.__init__(self,parent)
        self.grid()
        global logWindowExists, root,reque
        logWindowExists = True
        self.create_widgets()
        self.parent = parent
        

    def create_widgets(self):
        """create 2 buttons"""
        
        self.label_file=Label(self, text="are you sure? ")
        self.label_file.grid(row=0, column=0, columnspan=3, sticky=N)
        
        self.button_yes =Button(self, text="yes")
        self.button_yes.grid(row=1, column=1, columnspan=3, sticky=W)
        self.button_yes["command"]=self.yes
        

        self.button_no =Button(self, text="no")
        self.button_no.grid(row=1, column=4, columnspan=3, sticky=E)
        self.button_no["command"]=self.no
    
    def yes(self):
        """when click, return 1 and close dialog"""
        global reque,logWindowExists
        reque=1
        logWindowExists = False
        self.parent.master.update_wind()
        self.master.destroy()
        #return reque
        
        
    def no(self):
        """when click, return 0 and close dialog"""
        global reque, logWindowExists
        
        logWindowExists = False
        reque=0
        self.master.destroy() 
        #return reque
#        self.master.quit()
        
        
        
        
        
class Application(Frame):
    """GUI APP with several buttons and labels"""
    global reque
    def __init__(self,master):
        """init
        ialisate Frame"""
        Frame.__init__(self,master)
        self.grid()
        self.create_widgets()
        self.dataF=pd.DataFrame
        self.counter=0
        
    def create_widgets(self):
        """create  buttons, entry, label and output"""
        
        self.label_file=Label(self, text="Type filename ")
        self.label_file.grid(row=0, column=0, columnspan=2, sticky=W)
        
        self.filename=Entry(self)
        self.filename.grid(row=0, column=3, columnspan=2, sticky=W)
        
        self.button_open =Button(self, text="open file")
        self.button_open.grid(row=0, column=5, columnspan=2, sticky=E)
        self.button_open["command"]=self.open_file
        
        
        
        self.label_name=Label(self, text="Name ")
        self.label_name.grid(row=1, column=0, columnspan=2, sticky=W)
        
        
        self.text_name=Text(self, width=10, height=1, wrap=WORD)
        self.text_name.grid(row=1, column=2, columnspan=2, sticky=W)
        
        
        self.label_salary=Label(self, text="salary ")
        self.label_salary.grid(row=2, column=0, columnspan=3, sticky=W)
        
        self.inp_salary=Entry(self)
        self.inp_salary.grid(row=2, column=2, columnspan=3, sticky=W)
        
        self.button_set =Button(self, text="set")
        self.button_set.grid(row=2, column=4, columnspan=3, sticky=E)
        self.button_set["command"]=self.set_salary
        
        
        self.button_up=Button(self, text="up")
        self.button_up.grid(row=3, column=0, columnspan=2, sticky=W)
        self.button_up["command"]=self.up
        
        self.button_down=Button(self, text="down")
        self.button_down.grid(row=4, column=0, columnspan=2, sticky=W)
        self.button_down["command"]=self.down
        
        
        self.button4=Button(self, text="click, to exit")
        self.button4.grid(row=12, column=4, columnspan=3, sticky=E)
        self.button4["command"]=self.out

#        self.button5=Button(self)
#        self.button5["text"]="wtf"
#        #self.button5["command"]=self.coun
#        self.button5.grid(row=5, column=2, columnspan=3, sticky=W)
        
        
        self.label_fed=Label(self, text="federal taxes")
        self.label_fed.grid(row=9, column=0, columnspan=2, sticky=W)
        
        self.label_st=Label(self, text="state taxes")
        self.label_st.grid(row=10, column=0, columnspan=2, sticky=W)
        
        self.label_t=Label(self, text='total')
        self.label_t.grid(row=11, column=0, columnspan=2, sticky=W)

        self.label_new=Label(self, text='seted salary 0')
        self.label_new.grid(row=8, column=0, columnspan=2, sticky=W)
        
        self.label_t_fed=Label(self, text="total federal taxes")
        self.label_t_fed.grid(row=12, column=0, columnspan=2, sticky=W)
        
        self.label_t_st=Label(self, text="total state taxes")
        self.label_t_st.grid(row=13, column=0, columnspan=2, sticky=W)
        
        
        
        self.label_100000=Label(self, text="earn more 100000")
        self.label_100000.grid(row=11, column=3, columnspan=3, sticky=W)
        
        self.label_50000=Label(self, text="earn more 50000, less 100000")
        self.label_50000.grid(row=10, column=3, columnspan=3, sticky=W)
        
        self.label_25000=Label(self, text="earn more 25000,less 50000")
        self.label_25000.grid(row=9, column=3, columnspan=3, sticky=W)

        self.label_0=Label(self, text='earn less 25000')
        self.label_0.grid(row=8, column=3, columnspan=3, sticky=W)
        
        
    def open_file(self):
        """open csv file"""
        import pandas as pd
        
        file_name=self.filename.get()
        try:
        
            data=pd.read_csv('{0}.csv'.format(file_name),delimiter =',') 
        except:
            raise NameError('name of csv File must be:  {0}.csv '.format(file_name))
            
        if 'salary' not in data.dtypes.index:
            data['salary']=0
        if 'federal_taxes' not in data.dtypes.index:
            data['federal_taxes']=0
        if 'state_taxes' not in data.dtypes.index:
            data['state_taxes']=0
        if 'total' not in data.dtypes.index:
            data['total']=0

        self.dataF=data
        
        self.text_name.insert(0.0,str(self.dataF.loc[self.counter,'name'])+'\n')
        self.label_fed['text']="federal taxes "+str(self.dataF.loc[self.counter,"federal_taxes"])
        self.label_st['text']="state_taxes "+str(self.dataF.loc[self.counter, "state_taxes"])
        self.label_t["text"]="total "+str(self.dataF.loc[self.counter,"total"])
        self.rewrite()

    def set_salary(self):
        """cet selary to employer,rise dialog window count taxes"""
        self.dataF.loc[self.counter,'salary']=int(self.inp_salary.get())
        self.dataF.loc[self.counter,'state_taxes']=self.dataF.loc[self.counter,'salary']*0.05

        if self.dataF.loc[self.counter,'salary']<100000:
            self.dataF.loc[self.counter,'federal_taxes']=self.dataF.loc[self.counter,'salary']*0.15
        else:
            self.dataF.loc[self.counter,'federal_taxes']=self.dataF.loc[self.counter,'salary']*0.2
        

        self.dataF.loc[self.counter,'total']=self.dataF.loc[self.counter,'federal_taxes']+self.dataF.loc[self.counter,'state_taxes']

        if not logWindowExists:
            self.logWindow = Toplevel(self)
            self.app = LogWindow(self.logWindow)
            self.logWindow.protocol("WM_DELETE_WINDOW",self.app.no)
            self.logWindow.protocol("WM_DELETE_WINDOW", self.app.yes)
            
        else:
            self.logWindow.deiconify()
         
  
    def rewrite(self):
        """rewrite most text of widgets in main window"""
        self.label_100000["text"]="earn more 100000 "+str(len(self.dataF[self.dataF['salary']>=100000]))
        self.label_50000["text"]="earn more 50000, less 100000 "+str(len(self.dataF[(self.dataF['salary']<100000)&(self.dataF['salary']>=50000)]))
        self.label_25000["text"]="earn more 25000, less 50000 "+str(len(self.dataF[(self.dataF['salary']<50000)&(self.dataF['salary']>=25000)]))
        self.label_0["text"]="earn  less 25000 "+str(len(self.dataF[self.dataF['salary']<25000]))
        
        self.label_t_fed["text"]="total federal taxes "+str(sum(self.dataF["federal_taxes"]))
        self.label_t_st["text"]="total state taxes "+str(sum(self.dataF["state_taxes"]))
        
        self.text_name.insert(0.0,str(self.dataF.loc[self.counter,'name'])+'\n')
        
        self.label_new["text"]="sated salary"+str(self.dataF.loc[self.counter,'salary'])
        self.label_fed["text"]='federal_taxes '+str(self.dataF.loc[self.counter,'federal_taxes'])
        self.label_st["text"]='state_taxes '+str(self.dataF.loc[self.counter,'state_taxes'])
        self.label_t["text"]="total "+str(self.dataF.loc[self.counter,'total'])
           
        root.update()
        
    def update_wind(self):
        """update main window"""
        if self.counter<len(self.dataF['salary'])-1:
            self.counter+=reque
        self.rewrite()

    def up(self):
        """go up in the dataFrame """ 
        if self.counter>0:
            self.counter-=1
        self.rewrite()    
#        
            
    def down(self):
        """go down in the dataFrame """ 
        if self.counter<len(self.dataF['salary'])-1:
            self.counter+=1
        self.rewrite()
     
        
    def out(self):
        """quit and save in csv"""
        filename=self.filename.get()
        self.dataF.to_csv("%s.csv"%(filename), cols=['salary','federal_taxes','state_taxes','total'])        
        
        
        self.quit()
        root.destroy()
        
    
    

root=Tk()
root.title("simple GUI")
root.geometry("450x300")
app=Application(root)
root.mainloop()
        


#def read_f(file_name):
#    import pandas as pd
#    try:
#        
#        data=pd.read_csv('{0}.csv'.format(file_name),delimiter ='\t') 
#    
#    except:
#
#        raise NameError('name of csv File must be:  {0}.csv '.format(file_name))
#    if 'salary' not in list(data):
#        data['salary']=0
#    data['federal_taxes']=0
#    data['state_taxes']=data['salary']*0.05
#    for i in range(data['federal_taxes']):
#        if data['salary'][i]>=100000:
#            data['federal_taxes'][i]=data['salary'][i]*0.2
#        else:
#            data['federal_taxes'][i]=data['salary'][i]*0.15
#    data['total']=data['state_taxes']+data['federal_taxes']
#    
        
    
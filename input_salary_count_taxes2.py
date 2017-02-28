#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 14:15:57 2017

@author: denya
"""

from Tkinter import *
import pandas as pd

logWindowExists = False
reque=0
class LogWindow(Frame):
    def __init__(self, parent):
        Frame.__init__(self,parent)
        self.grid()
        global logWindowExists, root,reque
        logWindowExists = True
        
        self.create_widgets()
        #self.parent = parent
        

    def create_widgets(self):
        """create 4 buttons, label and output"""
        
        self.label_file=Label(self, text="are you sure? ")
        self.label_file.grid(row=0, column=0, columnspan=3, sticky=N)
        
        self.button_yes =Button(self, text="yes")
        self.button_yes.grid(row=1, column=1, columnspan=3, sticky=W)
        self.button_yes["command"]=self.yes
        

        self.button_no =Button(self, text="no")
        self.button_no.grid(row=1, column=4, columnspan=3, sticky=E)
        self.button_no["command"]=self.no
    
    def yes(self):
        global reque
        reque=1
        logWindowExists = False

        self.master.destroy()
        return reque
        
    def no(self):
        global reque
        
        logWindowExists = False

        self.master.destroy() 
#        self.master.quit()
        return reque
        
        
        
        
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
        """create 4 buttons, label and output"""
        self.label_file=Label(self, text="Type filename ")
        self.label_file.grid(row=0, column=0, columnspan=3, sticky=W)
        
        self.filename=Entry(self)
        self.filename.grid(row=0, column=2, columnspan=3, sticky=W)
        
        self.button_open =Button(self, text="open file")
        self.button_open.grid(row=0, column=4, columnspan=3, sticky=E)
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
        self.button4.grid(row=5, column=4, columnspan=3, sticky=E)
        self.button4["command"]=self.out

        self.button5=Button(self)
        self.button5["text"]="wtf"
        self.button5["command"]=self.coun
        
        self.button5.grid(row=5, column=2, columnspan=3, sticky=W)
        
        
    def open_file(self):
        import pandas as pd
        
        file_name=self.filename.get()
        try:
        
            data=pd.read_csv('{0}.csv'.format(file_name),delimiter =',') 
        except:
            raise NameError('name of csv File must be:  {0}.csv '.format(file_name))
            
        if 'salary' not in data.dtypes.index:
            data['salary']=0

        data['federal_taxes']=0
        data['state_taxes']=data['salary']*0.05
        
        reach=data[data['salary']>=100000]
        poor=data[data['salary']<100000]
        reach['federal_taxes']=reach['salary']*0.2
        poor['federal_taxes']=poor['salary']*0.15
        data=poor.append(reach)
        
#        for i in range(len(data['federal_taxes'])):
#            if data['salary'][i]>=100000:
#                data['federal_taxes'][i]=data['salary'][i]*0.2
#            else:
#                data['federal_taxes'][i]=data['salary'][i]*0.15

        data['total']=data['state_taxes']+data['federal_taxes']
        self.dataF=data
        self.text_name.insert(0.0,str(self.dataF.loc[self.counter,'name'])+'\n')
#        self.label_name['text']=
#        self.text_name.insert(0.0,self.dataF[name][self.counter])

    def set_salary(self):
        self.dataF.loc[self.counter,'salary']=self.inp_salary.get()
#        self.dataF['salary'][self.counter]=self.inp_salary.get()
        if not logWindowExists:
            self.logWindow = Toplevel(self)
            self.app = LogWindow(self.logWindow)
            self.logWindow.protocol("WM_DELETE_WINDOW",self.app.no)
            self.logWindow.protocol("WM_DELETE_WINDOW", self.app.yes)
        else:
            self.logWindow.deiconify()
        if self.counter<len(self.dataF['salary'])-1:
            self.counter+=reque
        self.text_name.insert(0.0,str(self.dataF.loc[self.counter,'name'])+'\n')
            

    def up(self):
        if self.counter>0:
            self.counter-=1
        self.text_name.insert(0.0,str(self.dataF.loc[self.counter,'name'])+'\n')
        
            
    def down(self):
        if self.counter<len(self.dataF['salary'])-1:
            self.counter+=1
        else:
            pass
        self.text_name.insert(0.0,str(self.dataF.loc[self.counter,'name'])+'\n')
            
    def out(self):
        #write save csv
        self.quit()
        root.destroy()
        
    
    def coun(self):
        self.counter+=1
        self.button5["text"]="count="+str(self.counter)
    
    

root=Tk()
root.title("simple GUI")
root.geometry("400x300")
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
        
    
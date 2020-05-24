# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 13:04:08 2019

@author: ANSHUL
"""

from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from pathlib import Path

path = ''#Specifies the path here.

def read_file(path):    #Reads the file from the path
    return open(path,'r')

def sentence_tokenizer(file):   #to perform sentence tokenization
    text_here = file.read()
    # in my case, when it had '\n', I called it a new paragraph, 
    # like a collection of sentences
    paragraphs = [p for p in text_here.split('\n') if p]
    # and here, sent_tokenize each one of the paragraphs
    result = []
    for paragraph in paragraphs:
        result.append(sent_tokenize(paragraph))
    #print(result)
    return result

def produce_list(outer):
    res = []
    for o in outer:
        for s in o:
            res.append(s)
    return res

def annotate(sentence_list):
    encode_dict = {}
    i = 0
    for s in sentence_list:
        print(s)
        key = input('Sentiment:')
        encode_dict.update({i : key})
        i = i + 1
        print('\n')
    return encode_dict

def findPath(file_path):
    for j in range(0, len(file_path)):
        if file_path[j] == '\\':
            ind = j
    path = file_path[:ind]
    return path

def findFileName(file_path):
    for j in range(0, len(file_path)):
        if file_path[j] =="\\":
            ind = j
    file_name = file_path[ind+1:]
    return file_name

def getNumberWords(sentence_list):
    num = 0
    for s in sentence_list:
        c = word_tokenize(s)
        num = num + len(c)
    return num

def create_output(file_path_string, file_path, sentence_list, encode_dict, numb_words):
    
    file_name = file_path.name
    index = file_path_string.find(file_name)
    temp_path = file_path_string[:index]
    for j in range(0,len(file_name)):
        if file_name[j] == '.':
            ind = j
    file_name = file_name[:ind] + str('_annotated') + file_name[ind:]
    file_path_new = temp_path + file_name
    file_path = Path(file_path_new)
    file = open(file_path, 'w')
    i = 0
    for s in sentence_list:
        file.writelines(s + '\t\t' + encode_dict[i])
        file.write('\n')
        i = i + 1
    string = '[Sentence Length = '+str(len(sentence_list))+', Word Length = '+str(numb_words)+']'
    file.writelines(string)
    print('Succesfully annotated')
    print('Check the same path for the annotated file')
    
#path = input("Enter the path in which the file is located:\n")
#file_name = input('Enter the text file\'s name(along with extension):\n')
#file_path = path + '\\' + file_name
    
global file_path
file_path = ''
    
import os
import wx
 
wildcard = "Text files (*.txt)|*.txt|"\
            "All files (*.*)|*.*"
 
########################################################################
class MyForm(wx.Frame):
 
    #----------------------------------------------------------------------
    def __init__(self):
        wx.Frame.__init__(self, None, wx.ID_ANY,"File and Folder Dialogs Tutorial")
        self.panel = wx.Panel(self, wx.ID_ANY)
        self.currentDirectory = os.getcwd()
        # create the buttons and bindings
        self.openFileDlgBtn = wx.Button(self.panel, label="Browse for file")
        self.openFileDlgBtn.Bind(wx.EVT_BUTTON, self.onOpenFile)
        
        self.label = wx.StaticText(self.panel, label='File path selected', style=wx.ALIGN_CENTRE)
        self.button = wx.Button(self.panel, label="Okay")
        self.button.Bind(wx.EVT_BUTTON, self.OnButton)
        
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(self.openFileDlgBtn, 0, wx.EXPAND|wx.BOTTOM, 20)
        self.sizer.Add(self.label, 0, wx.EXPAND|wx.BOTTOM, 20)
        self.sizer.Add(self.button)
        
        self.panel.SetSizerAndFit(self.sizer) 
        self.Show()
        
    def onOpenFile(self, event):
        """
        Create and show the Open FileDialog
        """
        dlg = wx.FileDialog(
            self, message="Choose a file",
            defaultDir=self.currentDirectory, 
            defaultFile="",
            wildcard=wildcard,
            style=wx.FD_OPEN | wx.FD_MULTIPLE | wx.FD_CHANGE_DIR
            )
        if dlg.ShowModal() == wx.ID_OK:
            paths = dlg.GetPaths()
            #print(type(paths))
            print ("You chose the following file(s):")
            for path in paths:
                print (path)
                self.label.SetLabel(path)
                global file_path
                file_path = path
                
                #print(type(path))
        dlg.Destroy()
        
    def OnButton(self, e):
        wx.CallAfter(frame.Close)
                
# Run the program
if __name__ == "__main__":
    app = wx.App(False)
    frame = MyForm()
    frame.Show()
    app.MainLoop()  
    del app


#file_path = '~/Documents/Cyber.txt'
#path = findPath(file_path)
#file_name = findFileName(file_path)
file_path_string = file_path
file_path = Path(file_path)
file = read_file(file_path)
outer_list = sentence_tokenizer(file)
sentence_list = produce_list(outer_list)
numb_words = getNumberWords(sentence_list)
encode_dict={}
file2 = read_file(file_path)
display_text = file2.read()
print(display_text)

class MainWindow(wx.Frame):
    i=0
    key1 = '[POS]'
    key2 = '[INT]'
    key3 = '[SMY]'
    key4 = '[YES]'
    lblList1 = ['Introduction','Related Work', 'Experiments', 'Results','Dataset','Methodology','Future Work','Writing and Composition','Others'] 
    
    def __init__(self, *args, **kwargs):
        wx.Frame.__init__(self, *args, **kwargs)
        self.panel = wx.Panel(self)
        #self.label = wx.StaticText(self.panel, label=sentence_list[0], style=wx.ALIGN_LEFT)
        #font = wx.Font(12, wx.DECORATIVE, wx.ITALIC, wx.NORMAL)
        #self.label.SetFont(font)
        self.label = wx.TextCtrl(self.panel, style = wx.TE_MULTILINE | wx.TE_READONLY | wx.TE_RICH)
        self.label.SetValue(sentence_list[0])
        font = wx.Font(12, wx.DECORATIVE, wx.ITALIC, wx.NORMAL)
        self.label.SetFont(font)

        self.button = wx.Button(self.panel, label="Next")
        self.button.Bind(wx.EVT_BUTTON, self.OnButton)
        
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        #self.sizer.Add(self.label, 1)
        
        self.docDisplay = wx.TextCtrl(self.panel, style = wx.TE_MULTILINE | wx.TE_READONLY | wx.TE_RICH)
        self.horizontalAlign = wx.BoxSizer(wx.HORIZONTAL)
        self.docDisplay.SetValue(display_text)
        font1 = wx.Font(12, wx.MODERN, wx.NORMAL, wx.NORMAL, False, u'Consolas')
        self.docDisplay.SetFont(font1)
        self.docDisplay.SetForegroundColour(wx.RED)
        
        self.horizontalAlign.Add(self.label, 1)
        self.horizontalAlign.Add(self.docDisplay, 1, wx.EXPAND|wx.LEFT, 0)
        
        self.sizer.Add(self.horizontalAlign, 0, wx.EXPAND|wx.BOTTOM, 20)
        #   List 0        
        lblList = ['Pos','Neg', 'Neu'] 
		  
        self.rbox = wx.RadioBox(self.panel,-1 ,label = 'Sentiment Layer', choices = lblList,majorDimension=1,style = wx.RA_SPECIFY_ROWS) 
        self.rbox.SetSelection(0)
        self.rbox.Bind(wx.EVT_RADIOBOX,self.onRadioBox) 
        
        self.check = wx.CheckBox(self.panel, label='Comments')
        self.check.Disable()
        self.Bind(wx.EVT_CHECKBOX, self.OnCheck, self.check)
        
        self.text = wx.TextCtrl(self.panel, style = wx.TE_MULTILINE)
        self.Bind(wx.EVT_TEXT, self.OnTypeText, self.text)
                
        self.versizer = wx.BoxSizer(wx.VERTICAL)
                        
        self.versizer.Add(self.rbox, 0)
        self.versizer.Add(self.check, 0)
        self.versizer.Add(self.text, 1)
        
        #List two  
        
        		  
        #self.rbox1 = wx.RadioBox(self.panel,-1 ,label = 'Choice list 2', choices = lblList1,majorDimension=1,style = wx.RA_SPECIFY_ROWS) 
        #self.rbox1.SetSelection(0)
        #self.rbox1.Bind(wx.EVT_RADIOBOX,self.onRadioBox1) 
        self.labelIn2 = wx.StaticText(self.panel, label='Section Aspect', style=wx.ALIGN_CENTRE)

        self.lstBox = wx.ListBox(self.panel,choices=self.lblList1,style =wx.LB_MULTIPLE,name = 'ListBoxHere')
        self.lstBox.Bind(wx.EVT_LISTBOX, self.onListButton)
        
        self.check1 = wx.CheckBox(self.panel, label='Comment')
        self.check1.Disable()
        self.Bind(wx.EVT_CHECKBOX, self.OnCheck1, self.check1)
        
        self.text1 = wx.TextCtrl(self.panel,style = wx.TE_MULTILINE)
        self.Bind(wx.EVT_TEXT, self.OnTypeText1, self.text1)
        
        self.versizer1 = wx.BoxSizer(wx.VERTICAL)
        self.versizer1.Add(self.labelIn2)
        self.versizer1.Add(self.lstBox)                
        #self.versizer1.Add(self.rbox1)
        self.versizer1.Add(self.check1)
        self.versizer1.Add(self.text1, 3)
        
       
        #List three  
        
        lblList2 = ['Summary','Suggestion', 'Deficit', 'Appreciation','Discussion','Question'] 
		  
        self.rbox2 = wx.RadioBox(self.panel,-1 ,label = 'Subjective Polarity', choices = lblList2, majorDimension=1,style = wx.RA_SPECIFY_ROWS) 
        self.rbox2.SetSelection(0)
        self.rbox2.Bind(wx.EVT_RADIOBOX,self.onRadioBox2) 
        
        self.check2 = wx.CheckBox(self.panel, label='Comments')
        self.check2.Disable()
        self.Bind(wx.EVT_CHECKBOX, self.OnCheck2, self.check2)
        
        self.text2 = wx.TextCtrl(self.panel, style = wx.TE_MULTILINE)
        self.Bind(wx.EVT_TEXT, self.OnTypeText2, self.text2)
        
        self.versizer2 = wx.BoxSizer(wx.VERTICAL)
        self.versizer2.Add(self.rbox2)
        self.versizer2.Add(self.check2)
        self.versizer2.Add(self.text2, 1)
        
        lblList3 = ['Yes', 'No'] 
		  
        self.rbox3 = wx.RadioBox(self.panel,-1 ,label = 'Is Major Comment', choices = lblList3, majorDimension=1,style = wx.RA_SPECIFY_ROWS) 
        self.rbox3.SetSelection(0)
        self.rbox3.Bind(wx.EVT_RADIOBOX,self.onRadioBox3) 
                
        self.hsizer = wx.BoxSizer(wx.HORIZONTAL)
        self.hsizer.Add(self.versizer, 0, wx.EXPAND|wx.RIGHT, 0)
        self.hsizer.Add(self.versizer1, 0, wx.EXPAND|wx.RIGHT, 0)
        self.hsizer.Add(self.versizer2, 0, wx.EXPAND|wx.RIGHT, 0)
        self.hsizer.Add(self.rbox3)
        
        self.sizer.Add(self.hsizer, 0)
        
        self.sizer.Add(self.button, 0)
        
        self.panel.SetSizerAndFit(self.sizer)  
        self.Show()

    def OnButton(self, e):    
        
        if(self.check.IsChecked()):
            print('In the on button check box is clicked')
            self.key1 = '[' + self.text.GetValue() + ']'
            
        if(self.check1.IsChecked()):
            print('In the on button check box 1 is clicked')
            self.key2 = '[' + self.text1.GetValue() + ']'
        else:
            if self.key2[len(self.key2)-2] == ' ':
                self.key2= self.key2[:len(self.key2)-3]
                self.key2 = self.key2 + ']'                       
           
        if(self.check2.IsChecked()):
            print('In the on button check box 2 is clicked')
            self.key3 = '[' + self.text2.GetValue() + ']'
        
            
        key = '[' + self.key1 + ', ' + self.key2 + ', ' + self.key3 + ', ' + self.key4 +']'   
        encode_dict.update({self.i:key})
        print(encode_dict)
        
        for i in range(0,len(self.lblList1)):
            self.lstBox.Deselect(i)
        
        self.i = self.i + 1
        self.check.Enable()
        self.check.SetValue(False)
        self.text.SetValue('')
        
        self.check1.Enable()
        self.check1.SetValue(False)
        self.text1.SetValue('')
        
        self.check2.Enable()
        self.check2.SetValue(False)
        self.text2.SetValue('')
        
        if(self.i < len(sentence_list)):
            self.label.SetValue(sentence_list[self.i])
        else:
            self.button.SetLabel('Finished')
            self.label.SetLabel('All sentences are done. Please exit the application')
            wx.CallAfter(win.Close)
        self.sizer.Layout()
        # self.panel.Layout()  #Either works
        
    # Methods fo list 1
    def onRadioBox(self, e):
        print (self.rbox.GetStringSelection(),' is clicked from Radio Box 1')
        self.key1 = '[' + (self.rbox.GetStringSelection()).upper() + ']' 
          
    def OnTypeText(self, event):
        if( len(self.text.GetValue()) > 0 ):
            self.check.Enable()
        else:
            self.check.Disable()
            
    def OnCheck(self, event):
        if( self.check.IsChecked() ):
            print(self.text.GetValue())
            
    #Methods for list 2
    
    def onListButton(self, e):
        lst = self.lstBox.GetSelections()
        print(self.lstBox.GetSelections())
        lstLabel = ['INT', 'RWK', 'EXP', 'RES', 'DAT', 'MET', 'FWK', 'WRC', 'OTH']
        self.key2 = '['
        for i in range(0,len(lst)):
            self.key2 = self.key2 + lstLabel[lst[i]] + ', '
        self.key2 = self.key2 + ']'
        print(self.key2)
        
    def OnTypeText1(self, event):
        if( len(self.text1.GetValue()) > 0 ):
            self.check1.Enable()
        else:
            self.check1.Disable()
            
    def OnCheck1(self, event):
        if( self.check1.IsChecked() ):
            print(self.text1.GetValue())
            
    # Methods for list 3
    def onRadioBox2(self, e):
        print (self.rbox2.GetStringSelection(),' is clicked from Radio Box 3')
        lst = ['SMY', 'SUG', 'DFT', 'APR', 'DSN', 'QUN']
        self.key3 = '['+ lst[self.rbox2.GetSelection()] +']'
        print(self.rbox2.GetSelection())
        
    def OnTypeText2(self, event):
        if( len(self.text2.GetValue()) > 0 ):
            self.check2.Enable()
        else:
            self.check2.Disable()
            
    def OnCheck2(self, event):
        if( self.check2.IsChecked() ):
            print(self.text2.GetValue())
            
    def onRadioBox3(self, e):
        print(self.rbox3.GetStringSelection(),' is clicked from radio box 4')
        self.key4 = '['+ (self.rbox3.GetStringSelection()).upper() + ']'
        
        
        
        
app = wx.App(False)
win = MainWindow(None)
win.Show()
app.MainLoop()
del app

print(encode_dict)
create_output(file_path_string, file_path, sentence_list, encode_dict, numb_words)

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QDialog, QFileDialog,  QCalendarWidget, QListWidget
import sys
import os
import json
from PyQt5.QtCore import QDate, QTime, QDateTime, Qt
import Core
import keyboard

Version = 'V3.0.1'

#Ideas:
    # multiple selection of boxes


class Box_MainWindow(object):
    def __init__(self, MainWindow):
        
        self.currentBut = 'A1'
        self.boxes = []
        self.SubjectDialog = None
        self.times_list = []
        self.Path = self.load_save_path()
        
        MainWindow.resize(900, 650)
        MainWindow.setWindowTitle("Box Saver Second Gen "+Version)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        
        self.init_tabs()
        self.init_mainW()         
        self.init_menu()
        self.init_actions()

        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.load_data_from_path()   
        self.show_times_to_dates()
        
#Init Methods

    def init_menu(self):
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menuFile = QtWidgets.QMenu(self.menubar)    
        self.menuFile.setTitle("File") 
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        MainWindow.setStatusBar(self.statusbar)
        self.actionNew_Boxsettings = QtWidgets.QAction(MainWindow)       
        self.actionLoad_Boxsettings = QtWidgets.QAction(MainWindow)
        self.actionSave_Boxsettings = QtWidgets.QAction(MainWindow)        
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.pushButton_3)
        self.actionNew_Boxsettings.setText("New Box")
        self.actionLoad_Boxsettings.setText("Load Boxes")
        self.actionSave_Boxsettings.setText("Save Boxes")         
        
        self.menuFile.addAction(self.actionNew_Boxsettings)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionLoad_Boxsettings)
        self.menuFile.addAction(self.actionSave_Boxsettings)
        self.menuFile.addSeparator()
        self.menubar.addAction(self.menuFile.menuAction())
        
    def init_mainW(self):
        
        self.pushButton_4 = QtWidgets.QPushButton(MainWindow)
        self.pushButton_4.setGeometry(QtCore.QRect(785, 95, 75, 23))
        self.pushButton_4.setText('Reset')
        self.pushButton_5 = QtWidgets.QPushButton(MainWindow)
        self.pushButton_5.setGeometry(QtCore.QRect(785, 35, 75, 23))
        self.pushButton_5.setText('Search')   
        self.pushButton_6 = QtWidgets.QPushButton(MainWindow)
        self.pushButton_6.setGeometry(QtCore.QRect(760, 35, 23, 23))
        self.pushButton_6.setText('X')           
        self.LineEdit_search = QtWidgets.QLineEdit(MainWindow)
        self.LineEdit_search.setGeometry(QtCore.QRect(627, 35, 130, 23))
        self.Label_Info = QtWidgets.QListWidget(MainWindow)
        self.Label_Info.setGeometry(QtCore.QRect(520, 520, 340, 100))
        
        self.pushButton_delete_info = QtWidgets.QPushButton(MainWindow)
        self.pushButton_delete_info.setGeometry(QtCore.QRect(460, 520, 50, 100))    
        self.pushButton_delete_info.setText('Reset\nInfos')
        
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(460, 100, 400, 500))
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        self.label.setText("Name:")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_2.setText("Des:")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        
        self.label_4 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_4.setText("Last Edit:")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_4)
        
        self.label_5 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_5.setText("")        
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.label_5)            
        
        self.lineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit)         
        
        self.textEdit = QtWidgets. QTextEdit(self.formLayoutWidget)
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.textEdit)
        
        self.label_6 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_6.setText("Created:")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_6)  
        
        self.label_7 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_7.setText("")        
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.label_7)   
        
        self.pushButton_refs = QtWidgets.QPushButton(MainWindow)
        self.pushButton_refs.setGeometry(QtCore.QRect(810, 355, 50, 20))    
        self.pushButton_refs.setText('Ref')        
        
    def init_tabs(self):
        
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 5, 450, 600))
        self.tab = QtWidgets.QWidget() 
        self.gridLayoutWidget = QtWidgets.QWidget(self.tab)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 420, 100))
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(10, 10, 10, 10)        
        self.label_name = QtWidgets.QLabel('Name:')
        self.gridLayout.addWidget(self.label_name, 0, 0, 1, 1)
        self.LineEdit_Newb = QtWidgets.QLineEdit(self.tab)
        self.gridLayout.addWidget(self.LineEdit_Newb, 0, 1, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.tab)
        self.pushButton.setText("Create Box")
        self.gridLayout.addWidget(self.pushButton, 0, 2, 1, 1)        
        self.cal = dateCalendar(self.tab)
        self.cal.setGeometry(QtCore.QRect(20, 110, 400, 300))       
        self.label_path = QtWidgets.QLabel('Current Path:')
        self.gridLayout.addWidget(self.label_path, 1, 0, 1, 1)
        self.LineEdit_path = QtWidgets.QLineEdit(self.tab)
        self.LineEdit_path.setText(self.Path)
        self.gridLayout.addWidget(self.LineEdit_path, 1, 1, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.tab)        
        self.gridLayout.addWidget(self.pushButton_2, 1, 2, 1, 1)
        self.pushButton_2.setText('Save Path')
        self.pushButton_3 = QtWidgets.QPushButton('Save')       
        self.tabWidget.addTab(self.tab, "")
        self.tabWidget.setCurrentIndex(0)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), "Welcome")
        self.ListWidget_date_display = QtWidgets.QListWidget(self.tab)
        self.ListWidget_date_display.setGeometry(QtCore.QRect(20, 425, 350, 130))
        self.jump_button = QtWidgets.QPushButton(self.tab)
        self.jump_button.setGeometry(QtCore.QRect(380, 425, 50, 50))
        self.jump_button.setText('Jump')
        
        self.rbutton_group= QtWidgets.QButtonGroup(self.tab)
        self.created_rbutton = QtWidgets.QRadioButton(self.tab)
        self.created_rbutton.setGeometry(QtCore.QRect(390, 480, 50, 50))
        self.created_rbutton.setText('C')
        self.rbutton_group.addButton(self.created_rbutton)
        self.lastedit_rbutton = QtWidgets.QRadioButton(self.tab)
        self.lastedit_rbutton.setGeometry(QtCore.QRect(390, 510, 50, 50))
        self.lastedit_rbutton.setText('L')          
        self.rbutton_group.addButton(self.lastedit_rbutton)
        self.lastedit_rbutton.setChecked(True)
        self.hit_refs = False
      
        
        
    def init_actions(self):
        
        self.actionNew_Boxsettings.triggered.connect(self.switch_to_first_tab)
        self.actionSave_Boxsettings.triggered.connect(self.save_boxes_to_path)
        self.actionLoad_Boxsettings.triggered.connect(self.load_data_from_path)
        self.pushButton.clicked.connect(self.create_new_box)
        self.pushButton_2.clicked.connect(self.def_save_path)
        self.pushButton_3.clicked.connect(self.save_single_box)
        self.pushButton_4.clicked.connect(self.reset_box_entries)
        self.pushButton_5.clicked.connect(self.search)
        self.pushButton_6.clicked.connect(self.reset_search)
        self.cal.selectionChanged.connect(self.show_times_to_dates)
        self.jump_button.clicked.connect(self.jump_to_box)
        self.pushButton_delete_info.clicked.connect(lambda: self.Label_Info.clear())
        self.created_rbutton.clicked.connect(self.create_lastedit_toggle)
        self.lastedit_rbutton.clicked.connect(self.create_lastedit_toggle)
        self.pushButton_refs.clicked.connect(self.hit_ref)
        
#End of init methods 
        
        
    def create_new_box(self):
        a = Box(self, self.LineEdit_Newb.text())
        self.LineEdit_Newb.setText('')
        name = self.save_boxes_to_path(a) # this is needed due to a bug in the saving
        a.removeTab()
        self.load_data_from_path(name)
        os.remove(name)
                
    def change_to_show(self, box):
        res = []
        for el in range(box.ListWidget_refs.count()):
            res.append(box.ListWidget_refs.item(el).text())
        return res

    def jump_to_box_refs(self):
        curr_box = self.boxes[self.tabWidget.currentIndex()-1]
        if curr_box.ListWidget_refs.currentRow() >= 0:
            jump = curr_box.ListWidget_refs.item(curr_box.ListWidget_refs.currentRow()).text()
            jump = jump.split('(')
            row_name = jump[0][:-1]
            box_name = jump[1][:-1].split(':')[0]            
            box_but = jump[1][:-1].split(':')[1]
            for el in self.boxes:
                if box_name == el.name:
                    self.tabWidget.setCurrentIndex(el.tabsm.indexOf(el.tab))
                    self.currentBut = box_but
                    self.button_push(el,box_but)  
                    
    def button_push(self, box, row):
        if self.hit_refs:
            self.hit_refs = False
            self.tabWidget.setCurrentIndex(self.ref_box.tabsm.indexOf(self.ref_box.tab))
            self.button_push(self.ref_box, self.ref_but)
            comp = self.ref_text
            if box.data.note_dict[row].name == '':
                name = '..'
            else:
                name = box.data.note_dict[row].name
            new_ref = '{} ({}:{})'.format(name,box.name,row)
            self.currentBut = self.ref_but
            self.textEdit.setText(comp+new_ref)
            self.ref_box.ListWidget_refs.addItem(new_ref)
            res = self.change_to_show(self.ref_box)
            desc = self.textEdit.toPlainText()
            for el in res:
                if len(res) > 0:
                    load = el
                    if el in desc:
                        seq = desc[desc.index(load):desc.index(load)+len(load)]
                        seq1 = desc[:desc.index(load)]
                        seq2 = desc[desc.index(load)+len(load):]
                        desc = seq1 + " <html><b style=color:blue>{} </b></html>".format(seq) + seq2  
            self.textEdit.setText(desc)
            self.ref_box.but_dict[self.ref_but].setStyleSheet("background-color: None")
            
        else:
            name, desc, ref, ladate, cdate, edited = box.data.note_dict[row].getData()
            gui_element = [self.lineEdit, self.textEdit,box.ListWidget_refs]
            self.currentBut = row
            curr_box = self.boxes[self.tabWidget.currentIndex()-1]
            curr_box.Label3.setText('Current Button: '+self.currentBut)           
            gui_element[0].setText(name)
            gui_element[2].clear()
            for el in ref:
                if el != []:
                    load = el.split('|')
                    load = '{} ({}:{})'.format(load[0],load[1],load[2])
                    if load not in [box.ListWidget_refs.item(i).text() for i in range(box.ListWidget_refs.count())]:
                        box.ListWidget_refs.addItem(load)
                    if load in desc:
                        seq = desc[desc.index(load):desc.index(load)+len(load)]
                        seq1 = desc[:desc.index(load)]
                        seq2 = desc[desc.index(load)+len(load):]
                        desc = seq1 + " <html><b style=color:blue>{}</b></html>".format(seq) + seq2   
            gui_element[1].setText(desc)
            self.label_5.setText(ladate)
            self.label_7.setText(cdate)
            for i in box.but_dict.values():
                i.setFlat(False)
            box.but_dict[row].setFlat(True)
            if box.but_dict[row].styleSheet() == "background-color: #87CEFA":
                        box.but_dict[row].setStyleSheet("background-color: #8D8282")
        
        
    def save_single_box(self):
        if len(self.boxes) != 0:    
            curr_box = self.boxes[self.tabWidget.currentIndex()-1]            
            time = QDateTime.currentDateTime().toString(Qt.ISODate)
            time = time[8:10]+ time[4:5] + time[5:8] + time[0:4] + time[10:]
            time = time.replace('T',' ')
            value = [self.lineEdit.text(), self.textEdit.toPlainText(),curr_box.ListWidget_refs, time]
            if not curr_box.data.note_dict[self.currentBut].edited:
                curr_box.data.note_dict[self.currentBut].setData(4, time)
            else:
                curr_box.data.note_dict[self.currentBut].edited = True
            for i in range(0,4):
                if i == 2:
                    for el in range(value[2].count()):
                        save = value[2].item(el).text().split('(')
                        save1 = save[1][:-1].split(':')  
                        curr_box.data.note_dict[self.currentBut].ref.append('{}|{}|{}'.format(save[0][:-1],save1[0],save1[1]))
                else:
                    curr_box.data.note_dict[self.currentBut].setData(i, value[i])            
            self.button_push(curr_box, self.currentBut)
            curr_box.but_dict[self.currentBut].setStyleSheet("background-color: #8D8282")
            self.Label_Info.addItem('The Box is saved!')
        
    
    def load_data_from_path(self, file = None):
        if file == None:
            try:
                # load in all boxes from the save path
                P = os.listdir(self.Path)
                for el in P:
                    with open(self.Path+'\\'+el, 'r') as loadfile:
                        data = json.load(loadfile)
                        dname = list(data.keys())[0]
                        a = Box(self, dname, data[dname])
                        for key, value in a.data.note_dict.items():
                            if value.edited:
                                a.but_dict[key].setStyleSheet("background-color: #8D8282")
                self.tabWidget.setCurrentIndex(0)
                self.Label_Info.addItem('The Boxes were loaded from your savepath.')
                
                
                self.times_list = []
                for b in self.boxes:
                    for key1, value1 in b.data.note_dict.items():
                        if value1.getData()[3] != '':
                            self.times_list.append([b.name +'\\'+ key1,value1.getData()[3][:10],value1.getData()[3][11:],value1.getData()[4][:10],value1.getData()[4][11:]])
                self.cal_dates_created = []
                self.cal_dates_lastedit = []
                for el in self.times_list:
                    temp = el[1].split('-')[::-1]
                    temp = [int(el) for el in temp]
                    self.cal_dates_lastedit.append(QtCore.QDate(temp[0],temp[1],temp[2]))
                    temp = el[3].split('-')[::-1]
                    temp = [int(el) for el in temp]
                    self.cal_dates_created.append(QtCore.QDate(temp[0],temp[1],temp[2])) 
                
                self.create_lastedit_toggle()
        
        
            
            except:
                self.cal_dates_created = []
                self.cal_dates_lastedit = []
                self.Label_Info.addItem("Error loading your boxes.")
                return None
        else:
            with open(file, 'r') as loadfile:
                data = json.load(loadfile)
                dname = list(data.keys())[0]
                a = Box(self, dname, data[dname])
                for key, value in a.data.note_dict.items():
                    if value.edited:
                        a.but_dict[key].setStyleSheet("background-color: #8D8282")
            self.tabWidget.setCurrentIndex(0)           
    
    def create_lastedit_toggle(self):
        if self.created_rbutton.isChecked():
            self.cal.selectDates(self.cal_dates_created)
        else:
            self.cal.selectDates(self.cal_dates_lastedit) 
        
        self.ListWidget_date_display.clear()
        
    def save_boxes_to_path(self, lim = None):
        '''Saves all current boxes to a json file in the savepath.
        '''
        if lim == False:
            for i in range(len(self.boxes)):
                for b in self.boxes:
                    with open(self.Path+'\\box_'+b.name+'.json','w') as savefile:
                        data = {b.name:{}}
                        for key, value in b.data.note_dict.items():
                            data[b.name][key] = value.getData()
                        json.dump(data, savefile, indent=2)
            self.Label_Info.addItem("Boxes are saved.")
        else:
            with open(self.Path+'\\box_'+lim.name+'.json','w') as savefile:
                data = {lim.name:{}}
                for key, value in lim.data.note_dict.items():
                    data[lim.name][key] = value.getData()
                json.dump(data, savefile, indent=2)  
            return self.Path+'\\box_'+lim.name+'.json'
                
    def switch_to_first_tab(self):
        self.tabWidget.setCurrentIndex(0)
        
    def def_save_path(self):
        if self.LineEdit_path.text() =='':
            self.Path = str(QFileDialog.getExistingDirectory())
            self.LineEdit_path.setText(self.Path)
        else:
            self.Path = self.LineEdit_path.text()
            
        with open('Path.json','w') as pfile:
            json.dump(self.Path, pfile)
        self.Label_Info.addItem("Savepath was set.")
            
            
    def load_save_path(self):
        try:
            with open('Path.json','r') as pfile:
                return json.load(pfile)
        except:
            return None
        
    def reset_box_entries(self):
        if len(self.boxes) != 0:
            curr_box = self.boxes[self.tabWidget.currentIndex()-1]
            curr_box.data.note_dict[self.currentBut].name = ''
            curr_box.data.note_dict[self.currentBut].des = ''
            curr_box.data.note_dict[self.currentBut].ref = []
            curr_box.data.note_dict[self.currentBut].ladate = None
            curr_box.data.note_dict[self.currentBut].cdate = 0 
            curr_box.data.note_dict[self.currentBut].edited = False
            curr_box.but_dict[self.currentBut].setStyleSheet("background-color: None")
            self.lineEdit.setText('')
            self.textEdit.setPlainText('')
            self.lineEdit_2.setText('')
            self.label_5.setText('')      
        self.Label_Info.addItem("Info for Button "+ self.currentBut+ " was reset.")
        
        
    def search(self):
        s = self.LineEdit_search.text()
        for box in self.boxes:
                for key, value in box.data.note_dict.items():
                    if s in value.name or s in value.ref or s in value.des:
                        box.but_dict[key].setStyleSheet("background-color: #87CEFA")
        self.Label_Info.addItem('"'+s+'" was found in the blue marked buttons!')
                        
    def reset_search(self):
        for box in self.boxes:
            for key, value in box.data.note_dict.items(): 
                if box.but_dict[key].styleSheet() == "background-color: #87CEFA":
                    box.but_dict[key].setStyleSheet("background-color: #8D8282")
        self.Label_Info.addItem('Search was reset!')
        self.LineEdit_search.setText('')
        
    def show_subject(self):
        if self.SubjectDialog == None:
            a = SubjectDialog(MainWindow)
            self.SubjectDialog = a
            self.SubjectDialog.move(1405,202)
            self.SubjectDialog.setWindowTitle('Advanced Search')
            self.SubjectDialog.show()
        else:
            self.SubjectDialog.show()
            self.Label_Info.addItem('You already have a search window open!')
        
    def show_times_to_dates(self):
        self.displayed_dates_lastedit = []
        self.displayed_dates_created = []
        inp = self.cal.selectedDate() # selected date
        self.ListWidget_date_display.clear() # clear ListWidget for dates
        if self.created_rbutton.isChecked():
            n = 3
        else:
            n = 1
        for value in self.times_list:
            if inp.toString('dd-MM-yyyy') == value[n]:
                if n == 1:
                    self.displayed_dates_lastedit.append(value)
                else:
                    self.displayed_dates_created.append(value)
                temp = value[0].split('\\')
                self.ListWidget_date_display.addItem('Box: {} Slot: {}   {}'.format(temp[0],temp[1], value[2]))        
                    
    def jump_to_box(self):
        '''Use a date to jump to the corresponding entry
        '''
        if self.created_rbutton.isChecked():
            self.curr_displayed_dates = self.displayed_dates_created
        else:
            self.curr_displayed_dates = self.displayed_dates_lastedit
        if self.ListWidget_date_display.currentRow() >= 0:
            jump = self.curr_displayed_dates[self.ListWidget_date_display.currentRow()]
            box_name = jump[0].split('\\')[0]
            box_but = jump[0].split('\\')[1]
            for el in self.boxes:
                if box_name == el.name:
                    self.tabWidget.setCurrentIndex(el.tabsm.indexOf(el.tab))
                    self.currentBut = box_but
                    self.button_push(el,box_but)  
                    
    def hit_ref(self):
        self.hit_refs = True
        self.ref_box = self.boxes[self.tabWidget.currentIndex()-1]
        self.ref_but = self.currentBut
        self.ref_box.but_dict[self.ref_but].setStyleSheet("background-color: #FF0000")
        self.ref_box.but_dict[self.ref_but].setFlat(False)    
        self.ref_text = self.textEdit.toPlainText()
        
    def print_notes(self):
        print(self.boxes[self.tabWidget.currentIndex()-1].data.note_dict[self.currentBut].getData())
                
                
class Box():
    
    def __init__(self, mW, name, Data = None):
        
        
        self.data = Core.box_data(name, Data)
        self.name = name
        self.main = mW
        self.main.boxes.append(self)
        self.tabsm = self.main.tabWidget
        self.tab = QtWidgets.QWidget()
        self.tabsm.addTab(self.tab, "")
        self.tabsm.setTabText(self.tabsm.count()-1, name[:5]+'..')
        
        self.gridLayoutWidget = QtWidgets.QWidget(self.tab)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 30, 390, 390))
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(10, 10, 10, 10)
        
        self.ListWidget_refs = QtWidgets.QListWidget(self.tab)
        self.ListWidget_refs.setGeometry(QtCore.QRect(20, 425, 350, 130))
        self.jump_button_refs = QtWidgets.QPushButton(self.tab)
        self.jump_button_refs.setGeometry(QtCore.QRect(380, 425, 50, 50))
        self.jump_button_refs.setText('Jump')              
        self.jump_button_refs.clicked.connect(self.main.jump_to_box_refs)
        
        self.Button_init()
        self.main.tabWidget.setCurrentIndex(self.tabsm.indexOf(self.tab))
        
        
        
    def Button_init(self):
        '''Creates 9x9 buttons on the new box tab.
        '''
        letters = ['A','B','C','D','E','F','G','H','I']
        self.but_dict = {}
        for a in range(9):
            for i in range(1,10):
                z = letters[a]+str(i)
                self.but_dict[z] = QtWidgets.QPushButton(self.tab)
                self.but_dict[z].setFixedSize(40,40)
                self.but_dict[z].setObjectName("pushButton_"+z)
                self.gridLayout.addWidget(self.but_dict[z], a, i, 1, 1) 
                self.but_dict[z].setText(z)
                self.but_dict[z].clicked.connect(lambda a=a, z=z: self.main.button_push(self, z))
        self.but_dict['A1'].setFlat(True)
        
        self.Close_Button = QtWidgets.QPushButton(self.tab)
        self.Close_Button.setGeometry(QtCore.QRect(425, -1, 20, 20))
        self.Close_Button.setText('x')
        self.Close_Button.clicked.connect(self.removeTab)
        
        self.Label1 = QtWidgets.QLabel('Full Name:', self.tab)
        self.Label1.setGeometry(QtCore.QRect(20, 10, 75, 23))
        self.Label2 = QtWidgets.QLabel(self.name, self.tab)
        self.Label2.setGeometry(QtCore.QRect(100, 10, 250, 23)) 
        self.Label3 = QtWidgets.QLabel(self.name, self.tab)
        self.Label3.setGeometry(QtCore.QRect(280, 10, 250, 23))  
        self.Label3.setText('Current Button: '+self.main.currentBut)
        
    def removeTab(self):
        '''Remove a box from you view field.
        '''
        self.main.boxes.pop(self.tabsm.indexOf(self.tab)-1)
        self.tabsm.removeTab(self.tabsm.indexOf(self.tab))
        
class dateCalendar(QtWidgets.QCalendarWidget):
    
    def __init__(self, parent = None, data = None):
        super(QCalendarWidget, self).__init__(parent)
        self.color = QtGui.QColor(self.palette().color(QtGui.QPalette.Highlight))
        self.color.setAlpha(150)
        self.dateList = []
            
    def paintCell(self, painter, rect, date):
        #calling original paintCell to draw the actual calendar
        QtWidgets.QCalendarWidget.paintCell(self, painter, rect, date)

        #highlight a particular date
        if date in self.dateList:
            painter.fillRect(rect, self.color)

    def selectDates(self, qdatesList):
        self.dateList = qdatesList
        #this redraws the calendar with your updated date list
        self.updateCells()
        
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Box_MainWindow(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
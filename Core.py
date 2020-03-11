import sys
import os
import json

class box_data():
    '''Data information of one box.    
    '''
    
    def __init__(self, name, boxData = None):
        self.mainname = name
        self.note_dict = {}
        letters = ['A','B','C','D','E','F','G','H','I']
        for a in range(9):
            for i in range(1,10):
                z = letters[a]+str(i)
                self.note_dict[z] = single_sample_data()
        if boxData != None:
            for key, value in boxData.items():
                self.note_dict[key].loadData(value)        
                            
        
class single_sample_data():
    ''' Single slot is the place where the data is stored in. Has the functions getData and setData.
    Data can be:
        name: name of the sample (String)
        des: description of the sample (String)
        ref: references to other samples (List)
        ladate: last access data of the sample (String)
        cdate : creation data of the sample (String)
        edited: whether sample is edited (Boolean)
    '''
    
    def __init__(self, name = '', des = '', ref = [], ladate='', cdate='', edit = False):
        self.name = name
        self.des = des
        self.ref = ref
        self.ladate = ladate
        self.cdate = cdate 
        self.edited = edit
    
    def getData(self):
        '''returns name, des, ref, ladate, cdate as a list'''
        return [self.name,self.des,self.ref,self.ladate,self.cdate, self.edited]
    
    def setData(self, num, value):
        '''changes the value of the number you entered:
        num 0: name
        num 1: des
        num 2: ref
        num 3: ladate
        num 4: cdate'''
        if num == 0:
            self.name = value
        elif num == 1:
            self.des = value
        elif num == 2:
            self.ref.append(value)
        elif num == 3:
            self.ladate = value
        elif num == 4:
            self.cdate = value
        elif num == 5:
            refs = self.ref
            self.ref = []
            self.ref.append(value)
        self.edited = True
        
    def set_refs(self, value):
        self.ref.append(value)
        
    def loadData(self, li):
        
        self.name = li[0]
        self.des = li[1]
        self.ref = li[2]
        self.ladate = li[3]
        self.cdate = li[4] 
        self.edited = li[5]
        
    def delete_one(self, value):
        i = 0
        while i < len(self.ref):
            if self.ref[i] == value:
                del self.ref[i]
            else:
                i += 1
    

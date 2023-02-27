import pandas as pd
import openpyxl

wb = openpyxl.load_workbook('D:/THANH PHƯƠNG/University/Python for DA/data.xlsx')

def checkUnnamed(cinDf):
  if 'unnamed' in cinDf.lower():
    return False
  return True

df = pd.read_excel('D:/THANH PHƯƠNG/University/Python for DA/data.xlsx', sheet_name='contacts',
                   skiprows= 6,
                   usecols = checkUnnamed)

# print whole sheet data
print(df)

#convert to dict
rawDict = df.to_dict()
rawDict

from time import strftime
from datetime import date
from datetime import datetime

class convertDict:
  headerList = []
  list1 = []
  formedDict = {}
  def __init__(self, rawDict):
    self.rawDict = rawDict
  def showEle(self):
    for i in self.rawDict:
      print(i)
  def convertList(self):
    for i in range(len(self.rawDict['STT'])):
      fullName = self.rawDict['Họ và tên'][i]
      sdt = '0' + str(self.rawDict['SĐT'][i])
      gender = self.rawDict['Giới tính'][i]
      birthPlace = self.rawDict['Nơi sinh'][i]
      birthDate = self.rawDict['Ngày sinh'][i]
      age = int()
      email = self.rawDict['email'][i]
      convertDict.formedDict[i] = {
          'Name':fullName,
          'Phone':sdt,
          'gender':gender,
          'Age':age,
          'birthPlace':birthPlace,
          'birthDate':birthDate,
          'email': email
      }
    return convertDict.formedDict
  def caculateAge(self):
    for i in range(len(self.rawDict['STT'])):
      #đổi ngày sinh sang dạng str để có strptime đổi dữa liệu dạng từ dạng timestamp sang dạng datetime
      birthDate = datetime.strptime(self.rawDict['Ngày sinh'][i].strftime('%m/%d/%Y'), '%m/%d/%Y')
      today = date.today()
      #incase birth in leap year so the number of days will less than whom not 1 day 
      #So that needed to compare the current day with the birth's
      age = today.year - birthDate.year - ((today.month, today.day) < (birthDate.month, birthDate.day))
      convertDict.formedDict[i]['Age'] = age
    return convertDict.formedDict
  def modifyDate(self):
    for i in range(len(self.rawDict['STT'])):
      #strftime dùng để định dạng lại mẫu ngày tháng mình muốn hiện
      formedDate = datetime.strptime(self.rawDict['Ngày sinh'][i].strftime('%m-%d-%Y'), '%m-%d-%Y').strftime('%d/%m/%Y')
      convertDict.formedDict[i]['birthDate'] = formedDate
  
    return convertDict.formedDict
  @classmethod
  def DicttiList(cls):
    index = 1
    for contact in cls.formedDict.values():
      row = [index] # Danh sách lưu các giá trị cần ghi cho mỗi hàng
      index += 1
      for value in contact.values():
        row.append(value)
      cls.list1.append(row)
    return cls.list1
  # def __repr__(self):
  #   return convertDict.formedDict

Dataa = convertDict(rawDict)
formedData = Dataa.convertList()
addAge = Dataa.caculateAge()
modifyingDate = Dataa.modifyDate()
cmm = Dataa.DicttiList()
cmm
# formedData.showEle()

#create save 
def save():
  wb.save('D:/THANH PHƯƠNG/University/Python for DA/data.xlsx')

#Create new sheet

def generateNew_sheet(sheetName = str, headersList = str, dataa = list):
  #Delete sheets from previous run
  number_of_sheets = len(wb.worksheets)
  for i in reversed(range(1, number_of_sheets)): # Xóa ngược từ sheet cuối về, tránh bị lỗi
    print(i)
    wb.remove_sheet(wb.worksheets[i])
  save()

  
  #create new sheet
  # newSheet = wb.create_sheet(sheetName)
  # save() 

  #import data
  ###c1: create brand new excel
  with pd.ExcelWriter('D:/THANH PHƯƠNG/University/Python for DA/data.xlsx', engine="openpyxl", mode="a") as writer:
    newSheet = pd.DataFrame(dataa).to_excel(writer,
                                                  sheet_name=sheetName,
                                                  header= headersList, 
                                                  index=False)
  # newSheet = df.to_excel('/content/ggdrive/MyDrive/Python For Data Analysis/Bài 08/data.xlsx', sheet_name=sheetName)
  #import headers 
  
  ###c2: append sheet to exsiting excel
  # FilePath = "/content/ggdrive/MyDrive/Python For Data Analysis/Bài 08/data.xlsx"
  # Generating the writer engine

  # Adding the DataFrames to the excel as a new sheet
  # newSheet = pd.DataFrame(dataa).to_excel(writer, sheet_name = sheetName)
  # save()





generateNew_sheet('dcmm',['STT','Họ và tên', 'Giới tính' , 'Tuổi', 'SĐT', 'Nơi sinh', 'Ngày sinh','email'], cmm)

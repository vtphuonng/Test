
inforDict = {
 0: {'Name': 'Hà Quang Tuấn',
  'Phone': '0937623590',
  'gender': 'Nam',
  'Age': 32,
  'birthPlace': 'Thái Bình',
  'birthDate': '05/01/1990',
  'email': 'tuanhq@gmail.com'},
 1: {'Name': 'Trần Hải Nam',
  'Phone': '0981344528',
  'gender': 'Nam',
  'Age': 31,
  'birthPlace': 'Hải Dương',
  'birthDate': '20/01/1991',
  'email': 'namth@gmail.com'},
 2: {'Name': 'Dương Trung Đức',
  'Phone': '0917613311',
  'gender': 'Nam',
  'birthPlace': 'Hà Nội',
  'birthDate': '25/05/1990',
  'email': 'ducdt@gmail.com'}
}

class generateDict:
 inforList = []
 row = []
 list1 = []
 def __init__(self, cinDict):
  self.cinDict = cinDict
 def convertedList(self):
  for contact in self.cinDict.values():
    row = [] # Danh sách lưu các giá trị cần ghi cho mỗi hàng
    for value in contact.values():
      row.append(value)
    self.list1.append(row)
  return self.list1


obj = generateDict(inforDict)
checkedDict = obj.convertedList()
print(checkedDict)


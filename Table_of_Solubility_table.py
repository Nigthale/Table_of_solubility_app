import sys
import PyQt6.QtWidgets
import PyQt6.QtGui
import PyQt6.QtCore
import math
from PyQt6 import uic


ID_solubility = ["Растворимый", "Малорастворимый", "Нерастворимый", "Такого соединения не существует", "Соединение реагируег с водой"]
ID_color = ["Цвет не важен","Прозрачный", "Жёлтый", "Голубой", "Чёрный", "Ржавый", "Белый"]
ID_Type = ["Раствор","Осадок","Газ", "Соединение реагируег с водой"]
Cation_list = [1, 1, 3, 2, 2, 2, 3, 2, 2, 3, 1, 1, 2, 2, 1, 1, 2, 2, 2, 2, 2]
Anion_list = [1, 1, 2, 1, 1, 1, 1, 1, 1, 3, 2, 2, 2, 2]
class Compound():
    def __init__(self, solubility, Type, color):
        self.solubility = solubility
        self.Type = Type
        self.color = color
table = []
for i in range(14):
    row = []
    for i in range(21):
        item = Compound(ID_solubility[0], ID_Type[0], ID_color[0])
        row.append(item)
    table.append(row)
   

global cation_var
global anion_var
cation_var = 1
anion_var = 0
#table[anion][cation]
#region Table
table[8][0] = Compound("Жидкость", "Вода", ID_color[0])
table[13][0] = Compound(ID_Type[1],ID_solubility[2], ID_color[6])
table[0][1] = Compound(ID_Type[1], ID_solubility[2], ID_color[2])
table[2][1] = Compound(ID_Type[1], ID_solubility[2], ID_color[2])
table[3][1] = Compound(ID_Type[1], ID_solubility[2], ID_color[6])
table[5][1] = Compound(ID_Type[1], ID_solubility[2], ID_color[2])
table[7][1] = Compound(ID_Type[1], ID_solubility[1], ID_color[2])
table[8][1] = Compound(ID_Type[3], ID_solubility[2], ID_color[5])
table[9][1] = Compound(ID_Type[1], ID_solubility[2], ID_color[2])
table[10][1] = Compound(ID_Type[1], ID_solubility[2], ID_color[4])
table[11][1] = Compound(ID_Type[1], ID_solubility[2], ID_color[6])
table[12][1] = Compound(ID_Type[1], ID_solubility[1], ID_color[6])
table[13][1] = Compound(ID_Type[1],ID_solubility[2], ID_color[2])
table[2][2] = Compound(ID_Type[3], ID_solubility[4], ID_color[6])
table[4][2] = Compound(ID_Type[1], ID_solubility[1], ID_color[6])
table[7][2] = Compound(ID_Type[3], ID_solubility[4], ID_color[2])
table[8][2] = Compound(ID_Type[1], ID_solubility[2], ID_color[6])
table[9][2] = Compound(ID_Type[1], ID_solubility[2], ID_color[6])
table[10][2] = Compound(ID_Type[3], ID_solubility[4], ID_color[6])
table[11][2] = Compound(ID_Type[3], ID_solubility[4], ID_color[6])
table[2][3] = Compound(ID_Type[1], ID_solubility[2], ID_color[6])
table[4][3] = Compound(ID_Type[1], ID_solubility[1], ID_color[6])
table[9][3] = Compound(ID_Type[1], ID_solubility[2], ID_color[6])
table[10][3] = Compound(ID_Type[3], ID_solubility[4], ID_color[6])
table[11][3] = Compound(ID_Type[1], ID_solubility[2], ID_color[6])
table[12][3] = Compound(ID_Type[1], ID_solubility[2], ID_color[6])
table[13][3] = Compound(ID_Type[1],ID_solubility[2], ID_color[6])
table[2][4] = Compound(ID_Type[1], ID_solubility[2], ID_color[6])
table[4][4] = Compound(ID_Type[1], ID_solubility[2], ID_color[6])
table[8][4] = Compound(ID_Type[1], ID_solubility[1], ID_color[6])
table[9][4] = Compound(ID_Type[1], ID_solubility[2], ID_color[6])
table[10][4] = Compound(ID_Type[3], ID_solubility[4], ID_color[6])
table[11][4] = Compound(ID_Type[1], ID_solubility[2], ID_color[6])
table[12][4] = Compound(ID_Type[1], ID_solubility[1], ID_color[6])
table[13][4] = Compound(ID_Type[1],ID_solubility[2], ID_color[6])
table[2][5] = Compound(ID_Type[1], ID_solubility[2], ID_color[5])
table[7][5] = Compound(ID_Type[1], ID_solubility[1], ID_color[5])
table[8][5] = Compound(ID_Type[1], ID_solubility[2], ID_color[3])
table[9][5] = Compound(ID_Type[1], ID_solubility[2], ID_color[3])
table[10][5] = Compound(ID_Type[1], ID_solubility[2], ID_color[4])
table[11][5] = Compound(ID_Type[1], ID_solubility[2], ID_color[5])
table[13][5] = Compound(ID_Type[1],ID_solubility[2], ID_color[6])
table[2][6] = Compound(ID_Type[1],ID_solubility[3], ID_color[0])
table[4][6] = Compound(ID_Type[1], ID_solubility[2], ID_color[3])
table[7][6] = Compound(ID_Type[1], ID_solubility[3], ID_color[0])
table[8][6] = Compound(ID_Type[1], ID_solubility[2], ID_color[2])
table[9][6] = Compound(ID_Type[1], ID_solubility[2], ID_color[4])
table[10][6] = Compound(ID_Type[1], ID_solubility[4], ID_color[4])
table[11][6] = Compound(ID_Type[1], ID_solubility[2], ID_color[5])
table[13][6] = Compound(ID_Type[1], ID_solubility[2], ID_color[0])
table[2][7] = Compound(ID_Type[1], ID_solubility[2], ID_color[3])
table[5][7] = Compound(ID_Type[3], ID_solubility[2], ID_color[0])
table[7][7] = Compound(ID_Type[3], ID_solubility[2], ID_color[0])
table[8][7] = Compound(ID_Type[1], ID_solubility[2], ID_color[3])
table[9][7] = Compound(ID_Type[1], ID_solubility[2], ID_color[3])
table[10][7] = Compound(ID_Type[1], ID_solubility[2], ID_color[4])
table[11][7] = Compound(ID_Type[3], ID_solubility[4], ID_color[0])
table[13][7] = Compound(ID_Type[1], ID_solubility[2], ID_color[3])
table[2][8] = Compound(ID_Type[1], ID_solubility[2], ID_color[2])
table[4][8] = Compound(ID_Type[1], ID_solubility[2], ID_color[6])
table[7][8] = Compound(ID_Type[1], ID_solubility[3], ID_color[0])
table[8][8] = Compound(ID_Type[1], ID_solubility[2], ID_color[4])
table[9][8] = Compound(ID_Type[1], ID_solubility[2], ID_color[6])
table[10][8] = Compound(ID_Type[1], ID_solubility[2], ID_color[4])
table[11][8] = Compound(ID_Type[1], ID_solubility[2], ID_color[4])
table[13][8] = Compound(ID_Type[1], ID_solubility[2], ID_color[4])
table[2][9] = Compound(ID_Type[1], ID_solubility[2], ID_color[2])
table[4][9] = Compound(ID_Type[1], ID_solubility[2], ID_color[2])
table[5][9] = Compound(ID_Type[1], ID_solubility[4], ID_color[4])
table[7][9] = Compound(ID_Type[1], ID_solubility[3], ID_color[0])
table[8][9] = Compound(ID_Type[1], ID_solubility[2], ID_color[4])
table[9][9] = Compound(ID_Type[1], ID_solubility[2], ID_color[2])
table[10][9] = Compound(ID_Type[1], ID_solubility[2], ID_color[2])
table[11][9] = Compound(ID_Type[1], ID_solubility[3], ID_color[0])
table[4][11] = Compound(ID_Type[1], ID_solubility[1], ID_color[6])
table[9][11] = Compound(ID_Type[1], ID_solubility[2], ID_color[6])
table[13][11] = Compound(ID_Type[1], ID_solubility[2], ID_color[6])
table[2][12] = Compound(ID_Type[1], ID_solubility[2], ID_color[6])
table[4][12] = Compound(ID_Type[1], ID_solubility[2], ID_color[6])
table[8][12] = Compound(ID_Type[1], ID_solubility[2], ID_color[6])
table[9][12] = Compound(ID_Type[1], ID_solubility[2], ID_color[6])
table[10][12] = Compound(ID_Type[1], ID_solubility[2], ID_color[6])
table[11][12] = Compound(ID_Type[1], ID_solubility[1], ID_color[6])
table[13][12] = Compound(ID_Type[1], ID_solubility[2], ID_color[6])
table[2][13] = Compound(ID_Type[1], ID_solubility[2], ID_color[5])
table[7][13] = Compound(ID_Type[1], ID_solubility[3], ID_color[0])
table[8][13] = Compound(ID_Type[1], ID_solubility[2], ID_color[6])
table[9][13] = Compound(ID_Type[1], ID_solubility[2], ID_color[6])
table[10][13] = Compound(ID_Type[1], ID_solubility[2], ID_color[5])
table[11][13] = Compound(ID_Type[1], ID_solubility[2], ID_color[5])
table[13][13] = Compound(ID_Type[1], ID_solubility[2], ID_color[6])
table[9][15] = Compound(ID_Type[1], ID_solubility[4], ID_color[6])
table[13][15] = Compound(ID_Type[1], ID_solubility[3], ID_color[6])
table[2][16] = Compound(ID_Type[1], ID_solubility[2], ID_color[2])
table[8][16] = Compound(ID_Type[1], ID_solubility[2], ID_color[2])
table[9][16] = Compound(ID_Type[1], ID_solubility[2], ID_color[2])
table[10][16] = Compound(ID_Type[1], ID_solubility[2], ID_color[4])
table[11][16] = Compound(ID_Type[1], ID_solubility[2], ID_color[4])
table[13][16] = Compound(ID_Type[1], ID_solubility[4], ID_color[2])
table[0][17] = Compound(ID_Type[1], ID_solubility[1], ID_color[6])
table[2][17] = Compound(ID_Type[1], ID_solubility[2], ID_color[6])
table[3][17] = Compound(ID_Type[1], ID_solubility[1], ID_color[6])
table[4][17] = Compound(ID_Type[1], ID_solubility[2], ID_color[6])
table[5][17] = Compound(ID_Type[1], ID_solubility[2], ID_color[2])
table[7][17] = Compound(ID_Type[1], ID_solubility[0], ID_color[6])
table[8][17] = Compound(ID_Type[1], ID_solubility[2], ID_color[6])
table[9][17] = Compound(ID_Type[1], ID_solubility[2], ID_color[6])
table[10][17] = Compound(ID_Type[1], ID_solubility[2], ID_color[4])
table[11][17] = Compound(ID_Type[1], ID_solubility[2], ID_color[6])
table[12][17] = Compound(ID_Type[1], ID_solubility[2], ID_color[6])
table[13][17] = Compound(ID_Type[1], ID_solubility[2], ID_color[6])
table[1][18] = Compound(ID_Type[1], ID_solubility[4], ID_color[6])
table[5][18] = Compound(ID_Type[1], ID_solubility[1], ID_color[2])
table[6][18] = Compound(ID_Type[1], ID_solubility[4], ID_color[6])
table[7][18] = Compound(ID_Type[1], ID_solubility[4], ID_color[6])
table[8][18] = Compound(ID_Type[1], ID_solubility[2], ID_color[6])
table[9][18] = Compound(ID_Type[1], ID_solubility[2], ID_color[6])
table[10][18] = Compound(ID_Type[1], ID_solubility[2], ID_color[5])
table[11][18] = Compound(ID_Type[1], ID_solubility[2], ID_color[6])
table[2][19] = Compound(ID_Type[1], ID_solubility[2], ID_color[6])
table[4][19] = Compound(ID_Type[1], ID_solubility[2], ID_color[6])
table[8][19] = Compound(ID_Type[1], ID_solubility[1], ID_color[6])
table[9][19] = Compound(ID_Type[1], ID_solubility[2], ID_color[6])
table[10][19] = Compound(ID_Type[1], ID_solubility[2], ID_color[6])
table[11][19] = Compound(ID_Type[1], ID_solubility[2], ID_color[6])
table[12][19] = Compound(ID_Type[1], ID_solubility[2], ID_color[6])
table[13][19] = Compound(ID_Type[1], ID_solubility[2], ID_color[6])
table[2][20] = Compound(ID_Type[1], ID_solubility[2], ID_color[6])
table[7][20] = Compound(ID_Type[1], ID_solubility[3], ID_color[0])
table[8][20] = Compound(ID_Type[1], ID_solubility[2], ID_color[6])
table[9][20] = Compound(ID_Type[1], ID_solubility[2], ID_color[6])
table[10][20] = Compound(ID_Type[1], ID_solubility[2], ID_color[6])
table[11][20] = Compound(ID_Type[1], ID_solubility[1], ID_color[6])
table[13][20] = Compound(ID_Type[1], ID_solubility[2], ID_color[5])
#endregion 

windowtable = PyQt6.QtWidgets.QApplication(sys.argv) 

def cation(x):
    globals()["cation_var"] = x
    pass
def anion(y):
    globals()["anion_var"] =  y
    pass
def lcm(divisor1, divisor2 ):
    lcm = (divisor1 * divisor2) // math.gcd(divisor1,divisor2)
    return lcm
    
class UI(PyQt6.QtWidgets.QMainWindow):
    def __init__(self):
        super(UI,self).__init__()
        uic.loadUi("GUI.ui", self)
        self.setWindowIcon(PyQt6.QtGui.QIcon("Icon.png"))
        self.Cbuttonlist = [self.C0, self.C1, self.C2, self.C3, self.C4, self.C5, self.C6, self.C7,
                          self.C8, self.C9, self.C10, self.C11, self.C12, self.C13, self.C14, self.C15,
                          self.C16, self.C17, self.C18, self.C19, self.C20,]
        self.Abuttonlist = [self.A0, self.A1, self.A2, self.A3, self.A4, self.A5, self.A6, self.A7,
                          self.A8, self.A9, self.A10, self.A11, self.A12, self.A13]
        #region buttons
        self.C0.clicked.connect(lambda:cation(0))
        self.C1.clicked.connect(lambda:cation(1))
        self.C2.clicked.connect(lambda:cation(2))
        self.C3.clicked.connect(lambda:cation(3))
        self.C4.clicked.connect(lambda:cation(4))
        self.C5.clicked.connect(lambda:cation(5))
        self.C6.clicked.connect(lambda:cation(6))
        self.C7.clicked.connect(lambda:cation(7))
        self.C8.clicked.connect(lambda:cation(8))
        self.C9.clicked.connect(lambda:cation(9))
        self.C10.clicked.connect(lambda:cation(10))
        self.C11.clicked.connect(lambda:cation(11))
        self.C12.clicked.connect(lambda:cation(12))
        self.C13.clicked.connect(lambda:cation(13))
        self.C14.clicked.connect(lambda:cation(14))
        self.C15.clicked.connect(lambda:cation(15))
        self.C16.clicked.connect(lambda:cation(16))
        self.C17.clicked.connect(lambda:cation(17))
        self.C18.clicked.connect(lambda:cation(18))
        self.C19.clicked.connect(lambda:cation(19))
        self.C20.clicked.connect(lambda:cation(20))
        self.A0.clicked.connect(lambda:anion(0))
        self.A1.clicked.connect(lambda:anion(1))
        self.A2.clicked.connect(lambda:anion(2))
        self.A3.clicked.connect(lambda:anion(3))
        self.A4.clicked.connect(lambda:anion(4))
        self.A5.clicked.connect(lambda:anion(5))
        self.A6.clicked.connect(lambda:anion(6))
        self.A7.clicked.connect(lambda:anion(7))
        self.A8.clicked.connect(lambda:anion(8))
        self.A9.clicked.connect(lambda:anion(9))
        self.A10.clicked.connect(lambda:anion(10))
        self.A11.clicked.connect(lambda:anion(11))
        self.A12.clicked.connect(lambda:anion(12))
        self.A13.clicked.connect(lambda:anion(13))
        #endregion 
        #region color

        self.timer = PyQt6.QtCore.QTimer(self)
        self.timer.timeout.connect(lambda:self.Solubility.setText(f"Растворимость: <br />{table[anion_var][cation_var].solubility}"))
        self.timer.timeout.connect(lambda:color())
        self.timer.timeout.connect(lambda:self.Result.setText(f"Результат: {compound(cation_var,anion_var)}"))
        self.timer.start(200)    
        def color():
             if table[anion_var][cation_var].color == "Жёлтый":
                    self.Color_Color.setPixmap(PyQt6.QtGui.QPixmap("squares/yellow.jpg"))
             elif table[anion_var][cation_var].color == "Белый":
                  self.Color_Color.setPixmap(PyQt6.QtGui.QPixmap("squares/white.jpg"))
             elif table[anion_var][cation_var].color == "Ржавый":
                  self.Color_Color.setPixmap(PyQt6.QtGui.QPixmap("squares/burnt_orange.jpg"))
             elif table[anion_var][cation_var].color == "Чёрный":
                  self.Color_Color.setPixmap(PyQt6.QtGui.QPixmap("squares/black.gif"))   
             elif table[anion_var][cation_var].color == "Голубой":
                 self.Color_Color.setPixmap(PyQt6.QtGui.QPixmap("squares/blue.jpg"))
             elif table[anion_var][cation_var].color == "Прозрачный":
                 self.Color_Color.setPixmap(PyQt6.QtGui.QPixmap("squares/arrow.png"))
             elif table[anion_var][cation_var].color == "Цвет не важен":
                    self.Color_Color.setPixmap(PyQt6.QtGui.QPixmap("squares/tsnv.png"))
        #endregion
        def compound(cation_var,anion_var):
            cation_number = (lcm(Cation_list[cation_var],Anion_list[anion_var])) // Cation_list[cation_var]
            anion_number = (lcm(Cation_list[cation_var],Anion_list[anion_var])) // Anion_list[anion_var]
        
            if cation_number == 1:
                cation_string = self.Cbuttonlist[cation_var].text()
            else:
               if len(self.Cbuttonlist[cation_var].text()) >= 3 :
                    cation_string = f"({self.Cbuttonlist[cation_var].text()})<small>{1 * cation_number}</small>"
               else:
                    cation_string = f"{self.Cbuttonlist[cation_var].text()}<small>{1 * cation_number}</small>"
            if anion_number == 1:
                anion_string = self.Abuttonlist[anion_var].text()
            else:
                if len(self.Abuttonlist[anion_var].text()) >= 3 or self.Abuttonlist[anion_var].text() == "OH":
                    anion_string = f"({self.Abuttonlist[anion_var].text()})<small>{1 * anion_number}</small>"
                else:
                    anion_string = f"{self.Abuttonlist[anion_var].text()}<small>{1 * anion_number}</small>"
            return f"{cation_string}{anion_string}"
        self.show()
        
            
mainwindow = UI()
windowtable.exec()

print(f"<h2>{table[anion_var][cation_var].solubility}, {table[anion_var][cation_var].Type}, {table[anion_var][cation_var].color}<h2>")
print(anion_var, cation_var)


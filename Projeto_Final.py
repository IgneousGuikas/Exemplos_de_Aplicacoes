import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *


class Dia():
    def __init__(self):
        self.tabDayContent = QGraphicsView()
        self.tabWeekContent = QListView()
        self.tabMonthContent = QGraphicsView()
        
    def addCompromisso(self):
        print()

class Semana():
    print()

class Calendario(QAbstractScrollArea):
    def __init__(self):
        super(Calendario, self).__init__()
        
        
        self.main_widget = QWidget()
        
        layout_ScrollArea = QVBoxLayout(self)
        layout_ScrollArea.addWidget(self.main_widget)
        self.setLayout(layout_ScrollArea)
        
        self.createLayoutMes()
        
        
    def createLayoutMes(self):
        layout_Mes = QGridLayout(self)
        
        today = QDate.currentDate()
        first = today.addDays( -(today.day()-1) )
        if first.dayOfWeek() <= 6:
            begin = first.addDays( -first.dayOfWeek() )
        else:
            begin = first
        
        
        
        for i in range(42):
            dia = Dia()
            dia.tabMonthContent.resize(50,50)
            
            content = QGraphicsScene()
            content.setSceneRect(QRectF(0,0, dia.tabMonthContent.width(), dia.tabMonthContent.height() ) )
            
            dia.tabMonthContent.setScene(content)
            
            if i <= 6:
                layout_Mes.addWidget(dia.tabMonthContent, 2,i,1,1)
                layout_Mes.addWidget(QLabel('{0}'.format(begin.day() ) ), 2,i,1,1)
            elif i > 6 and i <= 13:
                layout_Mes.addWidget(dia.tabMonthContent, 3,(i-7),1,1)
                layout_Mes.addWidget(QLabel('{0}'.format(begin.day() ) ), 3,(i-7),1,3)
            elif i > 13 and i <= 20:
                layout_Mes.addWidget(dia.tabMonthContent, 4,(i-14),1,1)
                layout_Mes.addWidget(QLabel('{0}'.format(begin.day() ) ), 4,(i-14),1,3)
            elif i > 20 and i <= 27:
                layout_Mes.addWidget(dia.tabMonthContent, 5,(i-21),1,1)
                layout_Mes.addWidget(QLabel('{0}'.format(begin.day() ) ), 5,(i-21),1,3)
            elif i > 27 and i <= 34:
                layout_Mes.addWidget(dia.tabMonthContent, 6,(i-28),1,1)
                layout_Mes.addWidget(QLabel('{0}'.format(begin.day() ) ), 6,(i-28),1,3)
            elif i > 34 and i <= 41:
                layout_Mes.addWidget(dia.tabMonthContent, 7, (i-35),1,1)
                layout_Mes.addWidget(QLabel('{0}'.format(begin.day() ) ), 7,(i-35),1,3)
            begin = begin.addDays(1)
        self.main_widget.setLayout(layout_Mes)
        

class Tabs(QTabWidget):
    def __init__(self):
        super(Tabs, self).__init__()
        
        self.tab1 = QWidget(self)
        self.tab2 = QWidget(self)
        self.tab3 = QWidget(self)
        
        
        self.calendario = Calendario()
        layout_tab1 = QVBoxLayout()
        layout_tab1.addWidget(self.calendario)
        self.tab1.setLayout(layout_tab1)
        
        
        
        self.addTab(self.tab1, 'Mês')
        self.addTab(self.tab2, 'Semana')
        self.addTab(self.tab3, 'Dia')

class BarOptions():
    def __init__(self):
        self.main_buttonIN = QPushButton('+')
        self.main_buttonOUT = QPushButton('Cancelar')
        self.buttonDiario = QPushButton('Diário')
        self.buttonSemanal = QPushButton('Semanal')
        self.buttonMensal = QPushButton('Mensal')
        self.buttonPersonalInfo = QPushButton('Informações\n Pessoais')
        

class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.resize(640,480)
        
        self.tabs = Tabs()
        self.buttons = BarOptions()
        
        
        layout_main = QGridLayout()
        layout_main.addWidget(self.buttons.main_buttonIN, 0,0,1,1)
        layout_main.addWidget(self.tabs, 0,1,2,1)
        self.setLayout(layout_main)
        
        
        
        self.buttons.main_buttonIN.clicked.connect(self.showOptions)
        
        
        
        
        self.resize(self.width(), self.height())
        self.centerOnScreen()
        
        
    def centerOnScreen(self):
        resolution = QDesktopWidget().screenGeometry()
        self.move( ( (resolution.width() / 2 ) - (self.width() / 2 ) ) , ( (resolution.height() / 2 ) - ( self.height() / 2 ) ) )
    
    def showOptions(self):
        self.buttons.main_buttonIN.hide()






if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    app.exec_()
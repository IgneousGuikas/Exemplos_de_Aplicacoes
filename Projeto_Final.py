import sys
from PyQt4 import QtGui, QtCore



class Main_Window(QtGui.QWidget):
    def __init__(self):
        super(Main_Window, self).__init__()
        
        self.tab1 = QtGui.QWidget() # Tab Meses
        self.tab2 = QtGui.QWidget() # Tab Semanas
        self.tab3 = QtGui.QWidget() # Tab Dias
        
        self.calendario = QtGui.QTableWidget(self)
        self.calendario.setRowCount(15)
        self.calendario.setColumnCount(7)
        self.calendario.setCellWidget(0,2,QtGui.QPushButton('Click', self))
        self.calendario.setSpan(0,2,3,1)
        self.calendario.setColumnWidth(1,100)
        
        layout_tab1 = QtGui.QVBoxLayout(self)
        layout_tab1.addWidget(self.calendario)
        self.tab1.setLayout(layout_tab1)
        
        
        
        layout_tab2 = QtGui.QGridLayout(self)
        ListView_semana1 = self.createDays()
        ListView_semana2 = self.createDays()
        x = 0
        for i in ListView_semana1:
            layout_tab2.addWidget(ListView_semana1[i],0,x,1,1)
            x += 1
        x = 0
        for i in ListView_semana2:
            layout_tab2.addWidget(ListView_semana2[i],1,x,1,1)
            x += 1
        self.tab2.setLayout(layout_tab2)
        
        
        
           
        
        
        
        self.tabs = QtGui.QTabWidget(self)
        self.tabs.addTab(self.tab1, 'Mês')
        self.tabs.addTab(self.tab2, 'Semana')
        
        
        
        
        
        
        
        
        layout_main = QtGui.QGridLayout(self)
        layout_main.addWidget(self.tabs,0,1,2,1)
        layout_main.addWidget(QtGui.QPushButton(),0,0,1,1)
        self.setLayout(layout_main)
        
        
        
        
        
        self.setGeometry(0,0,self.tab1.width(),self.tab1.height())
        self.centerOnScreen()
        
        print(self.tab1.size())
        
    def centerOnScreen(self):
        resolution = QtGui.QDesktopWidget().screenGeometry()
        self.move( ( (resolution.width() / 2 ) - (self.frameSize().width() / 2 ) ) , ( (resolution.height() / 2 ) - ( self.frameSize().height() / 2 ) ) )
    
    def createDays(self):
        today = QtCore.QDate.currentDate()
        dayOfWeek = today.dayOfWeek()
        semana1 = today.addDays(-dayOfWeek+1)
        
        dias = ['seg', 'ter', 'qua', 'qui', 'sex', 'sab', 'dom']        
        
        ListView_dias = dict()
        for i in range(1,8):
            ListView_dias['{0} {1}/{2}'.format(dias[i-1], semana1.day(), semana1.month())] = QtGui.QListView()
            semana1 = semana1.addDays(1)
        return ListView_dias



if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    win = Main_Window()
    win.show()
    app.exec_()
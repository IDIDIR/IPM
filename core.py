import sys                  # импорт библиотеки, необходимой для запуска
from PyQt5 import QtWidgets # импорт необходимого модуля для работы с графикой
import general              # импорт разработанной формы

class AlarmClock(QtWidgets.QMainWindow, general.Ui_Form):
    def __init__(self):
        super().__init__()  # необходимо для доступа к компонентам формы
        self.setupUi(self)  # инициализация дизайна (вызов функции с модуля формы)

def main():
   app = QtWidgets.QApplication(sys.argv)   # создание нового экземпляра приложения
   window = AlarmClock()    # создание экземпляра класса AlarmClock
   window.show()            # отображение окна
   app.exec_()              # запуск приложения

if __name__ == '__main__':  # запуск кода на выполнение
    main()
import sys
from ppg_runtime.application_context.${python_bindings} import ApplicationContext, PPGLifeCycle
from ${python_bindings}.QtWidgets import QMainWindow, QLabel

class MyApp(PPGLifeCycle, QMainWindow,):

    store = {}

    def __init__(self, appctxt):
        super().__init__(appctxt)

    def render_(self):
        label = QLabel('Hello World!', parent=self)

    def responsive_UI(self):
        self.setMinimumSize(640, 480)

if __name__ == '__main__':
    appctxt = ApplicationContext()
    window = MyApp(appctxt)
    window.show()
    exit_code = appctxt.app.exec()
    sys.exit(exit_code)
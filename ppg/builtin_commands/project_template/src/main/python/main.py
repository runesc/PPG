import sys
from ppg_runtime.application_context.${python_bindings} import ApplicationContext
from ppg_runtime.application_context import PPGStore, PPGLifeCycle
from ${python_bindings}.QtWidgets import QMainWindow, QLabel

class MyApp(PPGLifeCycle, QMainWindow, PPGStore):

    def __init__(self, appctxt):
        super().__init__(appctxt)

    def render_(self):
        QLabel('Hello World!', parent=self)

    def responsive_UI(self):
        self.setMinimumSize(640, 480)

if __name__ == '__main__':
    appctxt = ApplicationContext()
    window = MyApp(appctxt)
    window.show()
    # This fixes the issue with PySide2 that the exec function is not found
    exec_func = getattr(appctxt.app, 'exec', appctxt.app.exec_)
    sys.exit(exec_func())
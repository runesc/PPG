import sys
from ppg_runtime.application_context.${python_bindings} import ApplicationContext, LifeCycle
from ${python_bindings}.QtWidgets import QMainWindow, QLabel


class MyApp(LifeCycle, QMainWindow, ApplicationContext):

    def render_(self):
        label = QLabel('Hello World!', parent=self)

    def translate(self):
        self.resize(250, 150)

if __name__ == '__main__':
    appctxt = ApplicationContext()       # 1. Instantiate ApplicationContext
    window = MyApp()
    window.show()
    exit_code = appctxt.app.exec_()      # 2. Invoke appctxt.app.exec_()
    sys.exit(exit_code)
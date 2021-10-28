import sys
from ppg_runtime.application_context.${python_bindings} import ApplicationContext, PPGLifeCycle
from ${python_bindings}.QtWidgets import QMainWindow, QLabel


class MyApp(PPGLifeCycle, QMainWindow, ApplicationContext):

    store = {}

    def render_(self):
        label = QLabel('Hello World!', parent=self)

    def responsive_UI(self):
        self.resize(250, 150)

if __name__ == '__main__':
    appctxt = ApplicationContext()
    window = MyApp()
    window.show()
    exit_code = appctxt.app.exec()
    sys.exit(exit_code)
component_template = f"""
from ppg_runtime.application_context.$Binding import PPGLifeCycle
from $Binding.QtWidgets import $Widget

class $Name($Widget, PPGLifeCycle):
	def __init__(self, parent=None, **kwargs):
		super().__init__(parent=parent, objectName="$Name", **kwargs)
		self.parent = parent
		self.store = parent.store

"""
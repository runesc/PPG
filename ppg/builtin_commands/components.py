component_template = f"""
from ppg_runtime.application_context.$Binding import PPGLifeCycle
from ppg_runtime.application_context import PPGStore
from $Binding.QtWidgets import $Widget

class $Name($Widget, PPGLifeCycle, PPGStore):
	def __init__(self, *args, **kwargs):
		super().__init__(objectName="$Name", *args, **kwargs)
		self.subscribe_to_store(self)

	def update_store(self, store):
		# Handle Pydux store update here
		pass

"""
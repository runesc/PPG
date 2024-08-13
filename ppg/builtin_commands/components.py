component_template = f"""
from ppg_runtime.application_context import PPGStore, PPGLifeCycle, init_lifecycle
from $Binding.QtWidgets import $Widget

@init_lifecycle
class $Name($Widget, PPGLifeCycle, PPGStore):
	def __init__(self, *args, **kwargs):
		super().__init__(objectName="$Name", *args, **kwargs)
		self.subscribe_to_store(self)

	def render_(self):
		# Render the UI here
		pass

	def update_store(self, store):
		# Handle Pydux store update here
		pass

"""

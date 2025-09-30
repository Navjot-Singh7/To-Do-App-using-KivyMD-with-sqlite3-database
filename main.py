from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.dialog import MDDialog
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.metrics import dp
from kivymd.uix.list import ILeftBodyTouch, OneLineAvatarIconListItem
from kivymd.uix.selectioncontrol import MDCheckbox
import todo_database as db
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDRectangleFlatButton

Builder.load_string(""" 

<TaskWithCheckBox>:
	id: list_item
	IconRightWidget:
		icon: "delete"
		theme_icon_color: "Custom"
		icon_color: (1,0,0,1)
		on_release: root.show_confirm_dialog()
	RightCheckbox:
		id: check
		on_release: root.mark(self, check, list_item)

<content>:
	orientation: "vertical"
	size_hint_y: None
	height: "120dp"
	
	MDTextField:
		id : task_name
		hint_text: "Add Task"
	
	MDBoxLayout:
		orientation: "horizontal"
		spacing: "5dp"
		#md_bg_color: (1,1,1,1)
		
		MDRectangleFlatButton:
			text: "Add"
			size_hint_x: 1
			on_release: root.add_task()

<Mainscreen>:
	MDLabel:
		markup: True
		text: "[u]My Tasks[/u]"
		italic: True
		bold: True
		halign: "center"
		pos_hint:{ "center_y" : .95}
		font_size: "45sp"
		theme_text_color: "Custom"
		text_color: "white"
	
	MDScrollView:
		pos_hint: {"top": .9}
		#md_bg_color: (1,1,1,1)
		
		MDList:
			id: scroll
	
	MDIconButton:
		icon: "plus"
		theme_icon_color: "Custom"
		md_bg_color: self.theme_cls.primary_color
		pos_hint: {"center_x": .85 , "center_y": .07}
		icon_size: "35sp"
		on_release: root.add_task_window()

""")


class TaskWithCheckBox(OneLineAvatarIconListItem):

	def delete_item(self , instance):
		mainscreen = MDApp.get_running_app().root.get_screen("mainscreen")
		db.delete_tasks(self.text)
		self.parent.remove_widget(self)
		tasks = db.get_tasks()
		
		if tasks == []:
			label = MDLabel(text="No Tasks Yet!, Add one!",
											halign = "center",
											font_style= "H5",
											size_hint_y = None,
											height = "100sp",
											theme_text_color= "Hint")
			mainscreen.ids.scroll.add_widget(label)
		
		self.dialog.dismiss()
			

	def mark(self, instance,  check , list_item):
		if check.active == True:
			db.mark_task_as_complete(self.text)
		else:
			db.mark_task_as_incomplete(self.text)
		
	def show_confirm_dialog(self ):
			self.dialog = MDDialog(
									text= "Are you sure, you want to delete this task",
									title = "INFO",
									buttons= [
											MDRectangleFlatButton(text="CANCEL", theme_text_color="Custom", text_color=self.theme_cls.primary_color,  on_release= lambda x: self.dialog.dismiss()),
											MDRectangleFlatButton(text="DELETE", theme_text_color="Custom", text_color=self.theme_cls.primary_color,  on_release= self.delete_item)
											],)
			self.dialog.open()
			
	
class RightCheckbox(ILeftBodyTouch,  MDCheckbox):
	pass

class content(BoxLayout):
	def __init__(self, mainscreen, **kwargs):
		super().__init__(**kwargs)
		self.mainscreen = mainscreen
	
	def add_task(self):
		task  = db.get_tasks()

		if self.ids.task_name.text != "":
			
			for x in task:
				if self.ids.task_name.text in x:
					self.dialog_2 = MDDialog(text="You cannot Add same task again", buttons=[MDRectangleFlatButton(text="OK",on_release=lambda x:self.dialog_2.dismiss())])
					self.dialog_2.open()
					return
			
			for widget in self.mainscreen.ids.scroll.children[:]:
				if isinstance(widget, MDLabel) and widget.text == "No Tasks Yet!, Add one!":
					self.mainscreen.ids.scroll.remove_widget(widget)
					break
	
			self.task = TaskWithCheckBox(text=self.ids.task_name.text)
			self.mainscreen.ids.scroll.add_widget(self.task)
			db.add_task(str(self.ids.task_name.text), "0")
			self.ids.task_name.text = ""
			

class Mainscreen(Screen):
	
	def add_task_window(self):
		self.dialog = MDDialog(
								title = "Add Task",
								type = "custom",
								pos_hint = {"center_y": .55},
								content_cls = content(mainscreen=self))
		self.dialog.open()

class myapp(MDApp):
	
	def build(self):
		self.theme_cls.theme_style = "Dark"
		self.theme_cls.primary_palette = "DeepPurple"
		
		sm = ScreenManager()
		sm.add_widget(Mainscreen(name="mainscreen"))
		return sm
		
	def on_start(self):
		mainscreen = self.root.get_screen("mainscreen")
		db.create_database()
		tasks = db.get_tasks()
		
		if tasks == []:
			label = MDLabel(text="No Tasks Yet!, Add one!",
											halign = "center",
											font_style= "H5",
											size_hint_y = None,
											height = "100sp",
											theme_text_color= "Hint")
			mainscreen.ids.scroll.add_widget(label)
		
		for task in tasks:
			if task[1] == "1":
				task_widget = TaskWithCheckBox(text=task[0])
				task_widget.ids.check.active = True
				mainscreen.ids.scroll.add_widget(task_widget)
			else:
				task_widget = TaskWithCheckBox(text=task[0])
				mainscreen.ids.scroll.add_widget(task_widget)


myapp().run()

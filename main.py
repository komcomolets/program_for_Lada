from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty
from kivy.uix.button import Button


KV = """
MyBL:
	orientation: "vertical"
	size_hint: (0.95, 0.95)
	pos_hint: {"center_x": 0.5, "center_y":0.5}

	Label:
		font_size: "30sp"
		text: root.data_label
				
	
	Button:
		text: "Мои баллы"
		bold: True
		background_color:'#00FFCE'
		size_hint: (1,0.5)
		on_press: root.callback()

	Button:
		text: "Куда потратить?"
		bold: True
		background_color:'#00FFCE'
		size_hint: (1,0.5)
		on_press: root.callback2()

	Button:
		text: "Адреса фандоматов"
		bold: True
		background_color:'#00FFCE'
		size_hint: (1,0.5)
		on_press: root.callback3()

	Button:
		text: "О приложении"
		bold: True
		background_color:'#00FFCE'
		size_hint: (1,0.5)
		on_press: root.callback4()

"""

class MyBL(BoxLayout):

	data_label = StringProperty("Спасибо за использование фандомата")

	

	def callback(self):
		print("Мои баллы")
		

	def callback2(self):
		print("Куда потратить?")
		

	def callback3(self):
		print("Адреса фандоматов")
		

	def callback4(self):
		print("О приложении")
		

	



class MyApp(App):
	
	running = True
	
	def build(self):

		return Builder.load_string(KV)

	def on_stop(self):
		self.running = False

MyApp().run()

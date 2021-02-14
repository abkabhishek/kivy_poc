from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class ToDoCreate(GridLayout):

    def __init__(self, **kwargs):
        super(ToDoCreate, self).__init__(**kwargs)
        self.cols = 2
        self.add_widget(Label(text='Title'))
        self.todo_title = TextInput(multiline=True)
        self.add_widget(self.todo_title)
        
        self.add_widget(Label(text='Type'))
        self.todo_type = TextInput(multiline=False)
        self.add_widget(self.todo_type)

        self.add_widget(Label(text='Status'))
        self.todo_status = TextInput(multiline=False)
        self.add_widget(self.todo_status)

        self.add_widget(Label(text='ETA'))
        self.todo_eta = TextInput(multiline=False)
        self.add_widget(self.todo_eta)

        self.add_widget(Label(text='Deadline'))
        self.todo_deadline = TextInput(multiline=False)
        self.add_widget(self.todo_deadline)

        
        self.button_create = Button(text="Create")
        self.add_widget(self.button_create)




class ToDoApp(App):
    def build(self):
        return ToDoCreate()


if __name__ == '__main__':
    ToDoApp().run()
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty

from kivy.core.window import Window

Window.size = (500, 700)
button = ObjectProperty(None)


class MyLayout(Widget):
    pass

    def button_press(self, button):
        prior = self.ids.calc_input.text
        if prior == "0":
            self.ids.calc_input.text = ''
            self.ids.calc_input.text = f'{button}'

    def equals(self, button):

        prior = self.ids.calc_input.text

        self.ids.calc_input.text = f'{prior}{button}'

    def Clear(self):
        self.ids.calc_input.text = ""

    def equation(self, button):
        prior = self.ids.calc_input.text
        if "+" in prior:
            num_list = prior.split("+")
            ans = 0.0
            for number in num_list:
                ans = ans + float(number)
            self.ids.calc_input.text = str(ans)
        prior = self.ids.calc_input.text
        if "*" in prior:
            num_list = prior.split("*")
            ans = 1.0
            add1 = 0.0
            for number in num_list:
                ans = ans * float(number) + add1
            self.ids.calc_input.text = str(ans)
        prior = self.ids.calc_input.text
        if "-" in prior:
            num_list2 = prior.split("-")
            for number in num_list2:
                num1 = float(num_list2[0])
                num2 = float(num_list2[-1])
                add = 0.0
                ans = num1 - num2 + add
                if "." in prior:
                    self.ids.calc_input.text = f'{ans}'
                else:
                    self.ids.calc_input.text = f'{int(ans)}'

        prior = self.ids.calc_input.text
        if "/" in prior:
            num_list2 = prior.split("/")
            for number in num_list2:
                num1 = float(num_list2[0])
                num2 = float(num_list2[-1])
                ans = num1 / num2
                if num2 > num1:
                    self.ids.calc_input.text = f'{float(ans)}'
                else:
                    self.ids.calc_input.text = f'{int(ans)}'

    def dot(self):
        prior = self.ids.calc_input.text

        if ".." in prior:
            f'{prior.replace(".", "")}'

        else:
            prior = f'{prior}.'
            self.ids.calc_input.text = prior
        if "." not in prior:
            prior = f'{prior}.'
            self.ids.calc_input.text = prior


class MyApp(App):
    def build(self):
        return MyLayout()


MyApp().run()

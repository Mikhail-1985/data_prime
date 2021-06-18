import requests
import json

from secret_key import KEY

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.config import Config
# from kivy.uix.modalview import ModalView
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.relativelayout import RelativeLayout
# from kivy.uix.floatlayout import FloatLayout

Config.set('graphics', 'resizable', '0')
Config.set('graphics', 'width', '640')
Config.set('graphics', 'heigth', '480')

data = requests.get(KEY)
movie = data.text
movie_list = json.loads(movie)
movie_list_result = []
movie_list_overview = []
movie_list_lang = []
movie_list_popularity = []
movie_list_release_date = []


def movie_popular(movie_list_result):    
    
    for i in range(len(movie_list['results'])):
        movie_list_result.append(movie_list['results'][i]['original_title'])
        movie_list_overview.append(movie_list['results'][i]['overview'])
        movie_list_lang.append(movie_list['results'][i]['original_language'])
        movie_list_popularity.append(movie_list['results'][i]['popularity'])
        movie_list_release_date.append(movie_list['results'][i]['release_date'])


class MobileApp(App):
    bl = BoxLayout(orientation='vertical', padding=[20, 40])
    def build(self):
        bl = self.bl
        for i in range(len(movie_list['results'])):
            bl.add_widget(Button(text=movie_list_result[i], on_press=self.btn_press))
        return bl




    def btn_press(self, instance):
        # print(instance.text, instance)
        key = 0
        for i in range(len(movie_list['results'])):
            if movie_list_result[i] == instance.text:
                key = i
        content = Button(
            text=f'''
            Описание: {movie_list_overview[key]}\n
            Дата выхода: {movie_list_release_date[key]}\n
            Основной язык: {movie_list_lang[key]}\n
            Рейтинг популярности: {movie_list_popularity[key]}
            ''',
            font_size = 16,
            halign ='left',
            valign = 'middle',
            # shorten = True,
            split_str = '.',
            size_hint=(1, 1),
            # text_align = 'center',
            text_size = (500, 700)
        )
        popup = Popup(title=instance.text, content=content, auto_dismiss=False)
        content.bind(on_press=popup.dismiss)
        popup.open()
        


if __name__ == "__main__":
    movie_popular(movie_list_result)
    MobileApp().run()
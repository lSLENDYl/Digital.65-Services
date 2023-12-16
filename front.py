from kivy.app import App
from kivy.uix.label import Label 
from kivy.uix.floatlayout import FloatLayout  
from kivy.uix.scatter import Scatter 
from kivy.uix.textinput import TextInput 
from kivy.uix.boxlayout import BoxLayout 
class MainApp(App):
    def build(self):
        label = Label(text='Сервис Доп-образования',
                      size_hint=(.1, .5),
                      pos_hint={'center_x': .2, 'center_y': .9})
        

      
 
  
        b = BoxLayout(orientation ='vertical') 
  
        poisk = TextInput(font_size = 10, 
                      size_hint_y = None, 
                      height = 50) 
          
        f = FloatLayout() 
  
        s = Scatter() 
  
        l = Label(text ="поиск", 
                  font_size = 10) 
  
        f.add_widget(s) 
        s.add_widget(l) 
  
        b.add_widget(poisk) 
        b.add_widget(f) 
        spec = []
        with open(r'D:\System\Destktop\hakaton\data.txt','r', encoding='utf-8') as f:
            start = f.readlines()
            print(start)
            for i in start:
                timemas = i.split('<=>')
                spec.append([timemas[0],timemas[1],timemas[2],timemas[3],timemas[4],timemas[5],timemas[6][:-2]])

        def search(poisk, spec):               # поиск
            def __init__(self):
                searched = []       # найденные

                for i in spec:
                    timewords = i[0].split() #делим название по пробелу
                    for k in timewords:
                        k = str(k)
                        kol = 0
                        for r in range(len(poisk)): # поиск по буквам
                            try:
                                if k.index(poisk[r]) >= 0:
                                    if kol >= 1:
                                        if k[k.index(poisk[r-1]) + 1] == poisk[r]:
                                            kol += 1
                                    else: kol += 1
                            except: pass
                        if kol == len(poisk):
                            print(i[0]) #вывод найденого
                            searched.append(i)
                return searched
        poisk.bind(text = str(l.setter(search(poisk,spec))))
                
        return b,
 
if __name__ == '__main__':
    app = MainApp()
    app.run()
    app.exec_()
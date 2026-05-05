from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, SwapTransition
from kivy.properties import StringProperty, ObjectProperty
from kivy.core.window import Window
from kivy.uix.popup import Popup
from kivy.uix.relativelayout import RelativeLayout
import webbrowser
import pandas as pd

# Configuração da Janela
Window.fullscreen = 'auto'

# --- INTERFACE KV (Design Centralizado e Inteligente) ---
KV = """
<ImageButton@Button>:
    image_source: ""
    background_color: 0, 0, 51, 0
    canvas.before:
        Color:
            rgba: 1, 1, 1, 1
        Rectangle:
            pos: self.pos
            size: self.size
            source: self.image_source

<AnimalDetailScreen>:
    canvas.before:
        Rectangle:
            pos: self.pos
            size: self.size
            source: root.bg_image
    RelativeLayout:
        ImageButton:
            image_source: "btnwhatsapp.png"
            size_hint: 0.2, 0.15
            pos_hint: {"x": 0.42, "top": 0.35}
            on_release: root.open_link('https://web.whatsapp.com/')
        ImageButton:
            image_source: "btnvoltar.png"
            size_hint: 0.2, 0.15
            pos_hint: {"x": 0.42, "top": 0.20}
            on_release: root.manager.current = root.back_screen

<Interface>: # Tela de Início (Splash)
    canvas.before:
        Rectangle:
            pos: self.pos
            size: self.size
            source: "inicio.png"
    RelativeLayout:
        Button:
            background_color: 0, 0, 0, 0
            on_release: root.manager.current = 'login'

<LoginWindow>:
    email: email
    pwd: pwd
    canvas.before:
        Rectangle:
            pos: self.pos
            size: self.size
            source: "tela_login.png"
    RelativeLayout:
        TextInput:
            id: email
            hint_text: 'Informe seu E-mail'
            size_hint: 0.5, 0.05
            pos_hint: {"x": 0.27, "top": 0.68}
            multiline: False
        TextInput:
            id: pwd
            hint_text: 'Digite sua senha'
            password: True
            size_hint: 0.5, 0.05
            pos_hint: {"x": 0.27, "top": 0.62}
            multiline: False
        ImageButton:
            image_source: "btnlogin.png"
            size_hint: 0.2, 0.15
            pos_hint: {"x": 0.43, "top": 0.52}
            on_release: root.validate()
        ImageButton:
            image_source: "btnnovaconta.png"
            size_hint: 0.4, 0.15
            pos_hint: {"x" : 0.33, "top" : 0.40}
            on_release: root.manager.current = 'signup'
        ImageButton:
            image_source: "btnsite.png"
            size_hint: 0.2, 0.15
            pos_hint: {"x" : 0.43, "top" : 0.16}
            on_release: root.open_site()

<MenuScreen>: # Home
    canvas.before:
        Rectangle:
            pos: self.pos
            size: self.size
            source: "fundogato.png"
    RelativeLayout:
        ImageButton:
            image_source: "btnadotar.png"
            size_hint: 0.3, 0.2
            pos_hint: {"x" : 0.35, "top" : 0.85}
            on_release: root.manager.current = 'tipo_animal'
        ImageButton:
            image_source: "btndoar.png"
            size_hint: 0.3, 0.2
            pos_hint: {"x" : 0.35, "top" : 0.65}
            on_release: root.manager.current = 'doar_animal'
        ImageButton:
            image_source: "btncontribuir.png"
            size_hint: 0.3, 0.2
            pos_hint: {"x" : 0.35, "top" : 0.45}
            on_release: root.manager.current = 'contribuir'

<GridAnimaisScreen>:
    canvas.before:
        Rectangle:
            pos: self.pos
            size: self.size
            source: root.bg_source
    RelativeLayout:
        Button: # Pos 1
            background_color: 0,0,0,0
            size_hint: 0.2, 0.2
            pos_hint: {"x": 0.20, "top": 0.85}
            on_release: root.manager.current = root.prefix + '1'
        Button: # Pos 2
            background_color: 0,0,0,0
            size_hint: 0.2, 0.2
            pos_hint: {"x": 0.55, "top": 0.85}
            on_release: root.manager.current = root.prefix + '2'
        Button: # Pos 3
            background_color: 0,0,0,0
            size_hint: 0.2, 0.2
            pos_hint: {"x": 0.20, "top": 0.55}
            on_release: root.manager.current = root.prefix + '3'
        Button: # Pos 4
            background_color: 0,0,0,0
            size_hint: 0.2, 0.2
            pos_hint: {"x": 0.55, "top": 0.55}
            on_release: root.manager.current = root.prefix + '4'
        ImageButton:
            image_source: "btnvoltar.png"
            size_hint: 0.2, 0.15
            pos_hint: {"x": 0.40, "top": 0.25}
            on_release: root.manager.current = root.back_screen

# Popups Simplificados
<P>:
    Label:
        text: "E-mail NÃO existe."
<Q>:
    Label:
        text: "Usuário Inválido !!!"
<S>:
    Label:
        text: "Seja Bem vindo(a) !!!"
"""

# --- CLASSES LÓGICAS ---

class P(RelativeLayout): pass
class Q(RelativeLayout): pass
class S(RelativeLayout): pass

class AnimalDetailScreen(Screen):
    bg_image = StringProperty("")
    back_screen = StringProperty("")
    def open_link(self, url): webbrowser.open(url)

class Interface(Screen): pass

class LoginWindow(Screen):
    email = ObjectProperty(None)
    pwd = ObjectProperty(None)
    
    def validate(self):
        # Lógica simplificada: se preenchido, entra. 
        # Você pode reativar o Pandas aqui se o arquivo CSV existir.
        if self.email.text != "":
            Popup(title='Login', content=S(), size_hint=(None, None), size=(300, 300)).open()
            self.manager.current = 'home'
        else:
            Popup(title='Erro', content=Q(), size_hint=(None, None), size=(300, 300)).open()

    def open_site(self):
        webbrowser.open('https://site-ong-jorge-gabriels-projects.vercel.app/')

class MenuScreen(Screen): pass
class TipoAnimal(Screen): pass # Reutilize o KV que já tínhamos ou adicione aqui
class GridAnimaisScreen(Screen):
    bg_source = StringProperty("")
    prefix = StringProperty("")
    back_screen = StringProperty("")

class AdotaPo(App):
    def build(self):
        Builder.load_string(KV)
        # Importante: Carregar as telas de porte que faltavam no KV acima
        Builder.load_string("""
<TipoAnimal>:
    canvas.before:
        Rectangle:
            pos: self.pos
            size: self.size
            source: "tela_login.png"
    RelativeLayout:
        ImageButton:
            image_source: "btncachorro.png"
            size_hint: 0.3, 0.22
            pos_hint : {"x" : 0.35, "top" : 0.80}
            on_release: root.manager.current = 'dog_porte'
        ImageButton:
            image_source: "btngato.png"
            size_hint: 0.3, 0.2
            pos_hint : {"x" : 0.35, "top" : 0.60}
            on_release: root.manager.current = 'cat_porte'
        ImageButton:
            image_source: "btnvoltar.png"
            size_hint: 0.2, 0.15
            pos_hint : {"x" : 0.41, "top" : 0.30}
            on_release: root.manager.current = 'home'

<PorteSelection>:
    canvas.before:
        Rectangle:
            pos: self.pos
            size: self.size
            source: "fundo1.png"
    RelativeLayout:
        ImageButton:
            image_source: "btnpequeno.png"
            size_hint: 0.3, 0.2
            pos_hint : {"x" : 0.35, "top" : 0.90}
            on_release: root.manager.current = root.prefix + '_p'
        ImageButton:
            image_source: "btnmedio.png"
            size_hint: 0.3, 0.2
            pos_hint : {"x" : 0.35, "top" : 0.73}
            on_release: root.manager.current = root.prefix + '_m'
        ImageButton:
            image_source: "btngrande.png"
            size_hint: 0.3, 0.2
            pos_hint : {"x" : 0.36, "top" : 0.54}
            on_release: root.manager.current = root.prefix + '_g'
        ImageButton:
            image_source: "btnvoltar.png"
            size_hint: 0.2, 0.15
            pos_hint : {"x" : 0.40, "top" : 0.25}
            on_release: root.manager.current = 'tipo_animal'
        """)

        sm = ScreenManager(transition=SwapTransition())

        # 1. Telas de Sistema
        sm.add_widget(Interface(name='splash'))
        sm.add_widget(LoginWindow(name='login'))
        sm.add_widget(MenuScreen(name='home'))
        sm.add_widget(TipoAnimal(name='tipo_animal'))

        # 2. Telas de Seleção de Porte
        class PorteSelection(Screen): prefix = StringProperty("")
        sm.add_widget(PorteSelection(name='dog_porte', prefix='dog'))
        sm.add_widget(PorteSelection(name='cat_porte', prefix='cat'))

        # 3. Grids de Listagem (Todos os 6 caminhos)
        grids = [
            ('dog_p', 'fundocachorropequeno.png', 'dp', 'dog_porte'),
            ('dog_m', 'fundocachorromedio.png', 'dm', 'dog_porte'),
            ('dog_g', 'fundocachorrogrande.png', 'dg', 'dog_porte'),
            ('cat_p', 'fundogatopequeno.png', 'cp', 'cat_porte'),
            ('cat_m', 'fundogatomedio.png', 'cm', 'cat_porte'),
            ('cat_g', 'fundogatogrande.png', 'cg', 'cat_porte'),
        ]
        for name, bg, prefix, back in grids:
            sm.add_widget(GridAnimaisScreen(name=name, bg_source=bg, prefix=prefix, back_screen=back))

        # 4. MAPEAMENTO COMPLETO DE TODOS OS ANIMAIS DO SEU CÓDIGO
        # (ID da tela, Imagem correspondente, Tela de onde veio)
        pets = [
            # Cachorros Pequenos
            ('dp1', 'bobi.png', 'dog_p'), ('dp2', 'billy.png', 'dog_p'), 
            ('dp3', 'ster.png', 'dog_p'), ('dp4', 'duda.png', 'dog_p'),
            # Cachorros Médios
            ('dm1', 'victor.png', 'dog_m'), ('dm2', 'jon.png', 'dog_m'),
            ('dm3', 'henrique.png', 'dog_m'), ('dm4', 'jorge.png', 'dog_m'),
            # Cachorros Grandes
            ('dg1', 'jhey.png', 'dog_g'), ('dg2', 'anderson.png', 'dog_g'),
            ('dg3', 'thiago.png', 'dog_g'), ('dg4', 'azuos.png', 'dog_g'),
            # Gatos Pequenos
            ('cp1', 'brenna.png', 'cat_p'), ('cp2', 'jardson.png', 'cat_p'),
            ('cp3', 'belly.png', 'cat_p'), ('cp4', 'hemy.png', 'cat_p'),
            # Gatos Médios
            ('cm1', 'blade.png', 'cat_m'), ('cm2', 'jax.png', 'cat_m'),
            ('cm3', 'tai.png', 'cat_m'), ('cm4', 'bils.png', 'cat_m'),
            # Gatos Grandes
            ('cg1', 'jailsonmendes.png', 'cat_g'), ('cg2', 'bolla.png', 'cat_g'),
            ('cg3', 'wagner.png', 'cat_g'), ('cg4', 'diego.png', 'cat_g'),
        ]

        for screen_id, img, back_ref in pets:
            sm.add_widget(AnimalDetailScreen(name=screen_id, bg_image=img, back_screen=back_ref))

        return sm

if __name__ == "__main__":
    AdotaPo().run()

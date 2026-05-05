from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, SwapTransition
from kivy.properties import StringProperty
from kivy.core.window import Window
import webbrowser

# Configuração da Janela
Window.fullscreen = 'auto'

# --- INTERFACE KV (Design Centralizado) ---
KV = """
# Template para botões que usam imagens como fundo
<ImageButton@Button>:
    image_source: ""
    background_color: 0, 0, 0, 0
    canvas.before:
        Color:
            rgba: 1, 1, 1, 1
        Rectangle:
            pos: self.pos
            size: self.size
            source: self.image_source

# Modelo para as telas de detalhes dos animais (Bobi, Billy, etc)
<AnimalDetailScreen>:
    canvas.before:
        Rectangle:
            pos: self.pos
            size: self.size
            source: root.bg_image
    
    RelativeLayout:
        # Botão WhatsApp
        ImageButton:
            image_source: "btnwhatsapp.png"
            size_hint: 0.2, 0.15
            pos_hint: {"x": 0.42, "top": 0.35}
            on_release: root.open_link('https://web.whatsapp.com/')
            
        # Botão Voltar
        ImageButton:
            image_source: "btnvoltar.png"
            size_hint: 0.2, 0.15
            pos_hint: {"x": 0.42, "top": 0.20}
            on_release: root.manager.current = root.back_screen

# --- TELAS PRINCIPAIS ---

<LoginScreen>:
    canvas.before:
        Rectangle:
            pos: self.pos
            size: self.size
            source: "tela_login.png"
    RelativeLayout:
        TextInput:
            hint_text: 'E-mail'
            size_hint: 0.5, 0.05
            pos_hint: {"x": 0.27, "top": 0.68}
            multiline: False
        TextInput:
            hint_text: 'Senha'
            password: True
            size_hint: 0.5, 0.05
            pos_hint: {"x": 0.27, "top": 0.62}
            multiline: False
        ImageButton:
            image_source: "btnlogin.png"
            size_hint: 0.2, 0.15
            pos_hint: {"x": 0.43, "top": 0.52}
            on_release: root.manager.current = 'home'

<HomeScreen>:
    canvas.before:
        Rectangle:
            pos: self.pos
            size: self.size
            source: "fundogato.png"
    RelativeLayout:
        ImageButton:
            image_source: "btnadotar.png"
            size_hint: 0.3, 0.2
            pos_hint: {"x": 0.35, "top": 0.85}
            on_release: root.manager.current = 'tipo_animal'
        ImageButton:
            image_source: "btndoar.png"
            size_hint: 0.3, 0.2
            pos_hint: {"x": 0.35, "top": 0.65}
        ImageButton:
            image_source: "btncontribuir.png"
            size_hint: 0.3, 0.2
            pos_hint: {"x": 0.35, "top": 0.45}

<TipoAnimalScreen>:
    canvas.before:
        Rectangle:
            pos: self.pos
            size: self.size
            source: "tela_login.png"
    RelativeLayout:
        ImageButton:
            image_source: "btncachorro.png"
            size_hint: 0.3, 0.22
            pos_hint: {"x": 0.35, "top": 0.80}
            on_release: root.manager.current = 'porte_cachorro'
        ImageButton:
            image_source: "btngato.png"
            size_hint: 0.3, 0.2
            pos_hint: {"x": 0.35, "top": 0.60}
            on_release: root.manager.current = 'porte_gato'
        ImageButton:
            image_source: "btnvoltar.png"
            size_hint: 0.2, 0.15
            pos_hint: {"x": 0.41, "top": 0.30}
            on_release: root.manager.current = 'home'

<PorteSelectionScreen>:
    canvas.before:
        Rectangle:
            pos: self.pos
            size: self.size
            source: "fundo1.png"
    RelativeLayout:
        Label:
            text: "Qual porte?"
            font_size: 25
            pos_hint: {"center_x": .5, "top": .95}
        ImageButton:
            image_source: "btnpequeno.png"
            size_hint: 0.3, 0.2
            pos_hint: {"x": 0.35, "top": 0.90}
            on_release: root.manager.current = root.prefix + '_pequeno'
        ImageButton:
            image_source: "btnmedio.png"
            size_hint: 0.3, 0.2
            pos_hint: {"x": 0.35, "top": 0.73}
            on_release: root.manager.current = root.prefix + '_medio'
        ImageButton:
            image_source: "btngrande.png"
            size_hint: 0.3, 0.2
            pos_hint: {"x": 0.36, "top": 0.54}
            on_release: root.manager.current = root.prefix + '_grande'
        ImageButton:
            image_source: "btnvoltar.png"
            size_hint: 0.2, 0.15
            pos_hint: {"x": 0.40, "top": 0.25}
            on_release: root.manager.current = 'tipo_animal'

<GridAnimaisScreen>:
    canvas.before:
        Rectangle:
            pos: self.pos
            size: self.size
            source: root.bg_source
    RelativeLayout:
        # Exemplo de Grid simplificado para 4 botões invisíveis sobre a imagem de fundo
        Button:
            background_color: 0,0,0,0
            size_hint: 0.2, 0.2
            pos_hint: {"x": 0.2, "top": 0.85}
            on_release: root.manager.current = root.prefix + '1'
        Button:
            background_color: 0,0,0,0
            size_hint: 0.2, 0.2
            pos_hint: {"x": 0.55, "top": 0.85}
            on_release: root.manager.current = root.prefix + '2'
        Button:
            background_color: 0,0,0,0
            size_hint: 0.2, 0.2
            pos_hint: {"x": 0.2, "top": 0.55}
            on_release: root.manager.current = root.prefix + '3'
        Button:
            background_color: 0,0,0,0
            size_hint: 0.2, 0.2
            pos_hint: {"x": 0.55, "top": 0.55}
            on_release: root.manager.current = root.prefix + '4'
        ImageButton:
            image_source: "btnvoltar.png"
            size_hint: 0.2, 0.15
            pos_hint: {"x": 0.40, "top": 0.25}
            on_release: root.manager.current = root.back_screen
"""

# --- CLASSES DE LÓGICA ---

class LoginScreen(Screen): pass
class HomeScreen(Screen): pass
class TipoAnimalScreen(Screen): pass

class PorteSelectionScreen(Screen):
    prefix = StringProperty("") # 'dog' ou 'cat'

class GridAnimaisScreen(Screen):
    bg_source = StringProperty("")
    prefix = StringProperty("")
    back_screen = StringProperty("")

class AnimalDetailScreen(Screen):
    bg_image = StringProperty("")
    back_screen = StringProperty("")
    
    def open_link(self, url):
        webbrowser.open(url)

class AdotaPo(App):
    def build(self):
        Builder.load_string(KV)
        sm = ScreenManager(transition=SwapTransition())

        # 1. Telas Iniciais
        sm.add_widget(LoginScreen(name='login'))
        sm.add_widget(HomeScreen(name='home'))
        sm.add_widget(TipoAnimalScreen(name='tipo_animal'))

        # 2. Configuração de Portes
        sm.add_widget(PorteSelectionScreen(name='porte_cachorro', prefix='dog'))
        sm.add_widget(PorteSelectionScreen(name='porte_gato', prefix='cat'))

        # 3. Configuração de Grids (Listagem)
        grids = [
            ('dog_pequeno', 'fundocachorropequeno.png', 'dp', 'porte_cachorro'),
            ('dog_medio', 'fundocachorromedio.png', 'dm', 'porte_cachorro'),
            ('dog_grande', 'fundocachorrogrande.png', 'dg', 'porte_cachorro'),
            ('cat_pequeno', 'fundogatopequeno.png', 'cp', 'porte_gato'),
            ('cat_medio', 'fundogatomedio.png', 'cm', 'porte_gato'),
            ('cat_grande', 'fundogatogrande.png', 'cg', 'porte_gato'),
        ]
        for name, bg, prefix, back in grids:
            sm.add_widget(GridAnimaisScreen(name=name, bg_source=bg, prefix=prefix, back_screen=back))

        # 4. Geração Automática das Telas de Detalhes (Animais Individuais)
        # Formato: (Nome da Tela, Nome do Arquivo de Imagem, Tela de Origem)
        detalhes_animais = [
            ('dp1', 'bobi.png', 'dog_pequeno'), ('dp2', 'billy.png', 'dog_pequeno'),
            ('dm1', 'victor.png', 'dog_medio'), ('dm2', 'jon.png', 'dog_medio'),
            ('cp1', 'brenna.png', 'cat_pequeno'), ('cp2', 'jardson.png', 'cat_pequeno'),
            # Adicione todos os outros aqui seguindo o padrão...
        ]
        
        for name, img, back in detalhes_animais:
            sm.add_widget(AnimalDetailScreen(name=name, bg_image=img, back_screen=back))

        return sm

if __name__ == "__main__":
    AdotaPo().run()

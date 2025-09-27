from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.app import MDApp
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.label import MDLabel
from kivymd.uix.toolbar import MDTopAppBar
from kivymd.uix.navigationdrawer import MDNavigationLayout, MDNavigationDrawer, MDNavigationDrawerItem
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.textfield import MDTextField
from kivymd.uix.list import OneLineListItem

KV = '''
ScreenManager:
    HomeScreen:
    AboutScreen:
    FounderScreen:
    ServicesScreen:
    SuccessStoriesScreen:
    ContactScreen:
    InquiryFormScreen:

<HomeScreen>:
    name: 'home'
    MDBoxLayout:
        orientation: 'vertical'
        padding: 20
        spacing: 20
        md_bg_color: 0.5, 0, 0, 1  # Maroon theme

        MDTopAppBar:
            title: "Khalifa Designs International"
            elevation: 10
            left_action_items: [['menu', lambda x: nav_drawer.set_state('toggle')]]
            md_bg_color: 0.3, 0, 0, 1

        Image:
            source: 'KDIlogo.png'
            size_hint: (0.8, 0.4)  # Increased logo size
            allow_stretch: True
            pos_hint: {'center_x': 0.5}

        MDLabel:
            text: "Welcome to Khalifa Designs International"
            halign: 'center'
            font_style: 'H5'
            theme_text_color: 'Custom'
            text_color: 1, 1, 1, 1

        MDBoxLayout:
            orientation: 'vertical'
            size_hint_y: None
            height: self.minimum_height
            spacing: 15
            pos_hint: {'center_x': 0.5}

            MDRaisedButton:
                text: "About KDI"
                on_press: root.manager.current = 'about'
                size_hint_x: 0.6
                pos_hint: {'center_x': 0.5}

            MDRaisedButton:
                text: "Founder"
                on_press: root.manager.current = 'founder'
                size_hint_x: 0.6
                pos_hint: {'center_x': 0.5}

            MDRaisedButton:
                text: "Services"
                on_press: root.manager.current = 'services'
                size_hint_x: 0.6
                pos_hint: {'center_x': 0.5}

            MDRaisedButton:
                text: "Success Stories"
                on_press: root.manager.current = 'success'
                size_hint_x: 0.6
                pos_hint: {'center_x': 0.5}

            MDRaisedButton:
                text: "Contact Us"
                on_press: root.manager.current = 'contact'
                size_hint_x: 0.6
                pos_hint: {'center_x': 0.5}

            MDRaisedButton:
                text: "Inquiry Form"
                on_press: root.manager.current = 'inquiry'
                size_hint_x: 0.6
                pos_hint: {'center_x': 0.5}

<AboutScreen>:
    name: 'about'
    MDBoxLayout:
        orientation: 'vertical'
        padding: 20
        spacing: 20
        md_bg_color: 0.5, 0, 0, 1  # Maroon theme

        MDTopAppBar:
            title: "About KDI"
            left_action_items: [['arrow-left', lambda x: setattr(root.manager, 'current', 'home')]]
            md_bg_color: 0.3, 0, 0, 1

        MDLabel:
            text: "KDI is a global leader in design, IT solutions, and real estate management, specializing in AI-driven innovations."
            halign: 'center'
            theme_text_color: 'Custom'
            text_color: 1, 1, 1, 1

<FounderScreen>:
    name: 'founder'
    MDBoxLayout:
        orientation: 'vertical'
        padding: 20
        spacing: 20
        md_bg_color: 0.5, 0, 0, 1  # Maroon theme

        MDTopAppBar:
            title: "Founder"
            left_action_items: [['arrow-left', lambda x: setattr(root.manager, 'current', 'home')]]
            md_bg_color: 0.3, 0, 0, 1

        MDLabel:
            text: "Meet Dr. Istanbul Shahraz Khan, a global expert in AI, Data Science, Python, and Environmental Solutions."
            halign: 'center'
            theme_text_color: 'Custom'
            text_color: 1, 1, 1, 1

<ServicesScreen>:
    name: 'services'
    MDBoxLayout:
        orientation: 'vertical'
        padding: 20
        spacing: 20
        md_bg_color: 0.5, 0, 0, 1  # Maroon theme

        MDTopAppBar:
            title: "Services"
            left_action_items: [['arrow-left', lambda x: setattr(root.manager, 'current', 'home')]]
            md_bg_color: 0.3, 0, 0, 1

        MDLabel:
            text: "Our services include AI-driven solutions, IT consultancy, and real estate management."
            halign: 'center'
            theme_text_color: 'Custom'
            text_color: 1, 1, 1, 1

<SuccessStoriesScreen>:
    name: 'success'
    MDBoxLayout:
        orientation: 'vertical'
        padding: 20
        spacing: 20
        md_bg_color: 0.5, 0, 0, 1  # Maroon theme

        MDTopAppBar:
            title: "Success Stories"
            left_action_items: [['arrow-left', lambda x: setattr(root.manager, 'current', 'home')]]
            md_bg_color: 0.3, 0, 0, 1

        ScrollView:
            MDList:
                OneLineListItem:
                    text: "AI-Driven Pricing Model for Printing Business"
                OneLineListItem:
                    text: "Meta Business Suite Automation"
                OneLineListItem:
                    text: "Automated Business Report Generation"
                OneLineListItem:
                    text: "Enterprise Resource Planning Deployment"
                OneLineListItem:
                    text: "Social Media Strategy Optimization"
                OneLineListItem:
                    text: "Bioinformatics & Genetic Engineering Solutions"

<ContactScreen>:
    name: 'contact'
    MDBoxLayout:
        orientation: 'vertical'
        padding: 20
        spacing: 20
        md_bg_color: 0.5, 0, 0, 1  # Maroon theme

        MDTopAppBar:
            title: "Contact Us"
            left_action_items: [['arrow-left', lambda x: setattr(root.manager, 'current', 'home')]]
            md_bg_color: 0.3, 0, 0, 1

        MDLabel:
            text: "Reach us at: khalifadesignsinfo@gmail.com | +92-322-085-7477"
            halign: 'center'
            theme_text_color: 'Custom'
            text_color: 1, 1, 1, 1

<InquiryFormScreen>:
    name: 'inquiry'
    MDBoxLayout:
        orientation: 'vertical'
        padding: 20
        spacing: 20
        md_bg_color: 0.5, 0, 0, 1  # Maroon theme

        MDTopAppBar:
            title: "Inquiry Form"
            left_action_items: [['arrow-left', lambda x: setattr(root.manager, 'current', 'home')]]
            md_bg_color: 0.3, 0, 0, 1

        MDTextField:
            hint_text: "Your Name"
            size_hint_x: 0.8
            pos_hint: {'center_x': 0.5}

        MDTextField:
            hint_text: "Your Email"
            size_hint_x: 0.8
            pos_hint: {'center_x': 0.5}

        MDTextField:
            hint_text: "Your Message"
            size_hint_x: 0.8
            pos_hint: {'center_x': 0.5}
            multiline: True

        MDRaisedButton:
            text: "Submit"
            size_hint_x: 0.8
            pos_hint: {'center_x': 0.5}
            on_press: app.submit_inquiry()

<NavigationDrawer>:
    MDNavigationDrawer:
        id: nav_drawer
        MDBoxLayout:
            orientation: 'vertical'
            spacing: '8dp'
            padding: '8dp'

            MDLabel:
                text: "Menu"
                font_style: 'H6'
                size_hint_y: None
                height: self.texture_size[1]

            OneLineListItem:
                text: "Home"
                on_press: root.manager.current = 'home'; nav_drawer.set_state('close')

            OneLineListItem:
                text: "About"
                on_press: root.manager.current = 'about'; nav_drawer.set_state('close')

            OneLineListItem:
                text: "Founder"
                on_press: root.manager.current = 'founder'; nav_drawer.set_state('close')

            OneLineListItem:
                text: "Services"
                on_press: root.manager.current = 'services'; nav_drawer.set_state('close')

            OneLineListItem:
                text: "Success Stories"
                on_press: root.manager.current = 'success'; nav_drawer.set_state('close')

            OneLineListItem:
                text: "Contact Us"
                on_press: root.manager.current = 'contact'; nav_drawer.set_state('close')

            OneLineListItem:
                text: "Inquiry Form"
                on_press: root.manager.current = 'inquiry'; nav_drawer.set_state('close')
'''

class HomeScreen(Screen):
    pass

class AboutScreen(Screen):
    pass

class FounderScreen(Screen):
    pass

class ServicesScreen(Screen):
    pass

class SuccessStoriesScreen(Screen):
    pass

class ContactScreen(Screen):
    pass

class InquiryFormScreen(Screen):
    pass

class NavigationDrawer(MDNavigationLayout):
    pass

class KDIApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Red"
        return Builder.load_string(KV)

    def submit_inquiry(self):
        print("Inquiry submitted!")  # Replace with actual submission logic

if __name__ == "__main__":
    KDIApp().run()
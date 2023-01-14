from kivy.lang import Builder

from kivymd.app import MDApp

KV = '''
MDScreen:
    GridLayout:
        cols: 2
        padding: 20
        spacing: '10dp'

        MDSmartTile:
            radius: 24
            box_radius: [0, 0, 24, 24]
            box_color: 1, 1, 1, .2
            source: "images/tarsier-un-des-animaux-les-plus-etranges-scaled.webp"
            pos_hint: {"center_x": .5, "center_y": .5}
            size_hint: None, None
            size: "320dp", "320dp"

            MDIconButton:
                icon: "heart-outline"
                theme_icon_color: "Custom"
                icon_color: 1, 0, 0, 1
                pos_hint: {"center_y": .5}
                on_release: self.icon = "heart" if self.icon == "heart-outline" else "heart-outline"

            MDLabel:
                text: "MY text animal"
                bold: True
                color: 1, 1, 1, 1
        MDSmartTile:
            radius: 24
            box_radius: [0, 0, 24, 24]
            box_color: 1, 1, 1, .2
            source: "images/les-animaux-domestiques-sont-ils-doues-dintuition.webp"
            pos_hint: {"center_x": .5, "center_y": .5}
            size_hint: None, None
            size: "320dp", "320dp"

            MDIconButton:
                icon: "heart-outline"
                theme_icon_color: "Custom"
                icon_color: 1, 0, 0, 1
                pos_hint: {"center_y": .5}
                on_release: self.icon = "heart" if self.icon == "heart-outline" else "heart-outline"

            MDLabel:
                text: "Dog Cat"
                bold: True
                color: 1, 1, 1, 1
        
        
        MDSmartTile:
            radius: 24
            box_radius: [0, 0, 24, 24]
            lines: 2
            source: "images/870x489_gettyimages-1269313679.jpg"
            pos_hint: {"center_x": .5, "center_y": .5}
            size_hint: None, None
            size: "320dp", "320dp"

            MDIconButton:
                icon: "heart-outline"
                theme_icon_color: "Custom"
                icon_color: 1, 0, 0, 1
                pos_hint: {"center_y": .5}
                on_release: self.icon = "heart" if self.icon == "heart-outline" else "heart-outline"

            TwoLineListItem:
                text: "[color=#ffffff][b]My cats[/b][/color]"
                secondary_text: "[color=#808080][b]Julia and Julie[/b][/color]"
                pos_hint: {"center_y": .5}
                _no_ripple_effect: True

        MDSmartTile:
            radius: 24
            box_radius: [0, 0, 24, 24]
            box_color: 1, 1, 1, .2
            source: "images/870x489_gettyimages-1269313679.jpg"
            pos_hint: {"center_x": .5, "center_y": .5}
            size_hint: None, None
            size: "320dp", "320dp"
            overlap: False

            MDIconButton:
                icon: "heart-outline"
                theme_icon_color: "Custom"
                icon_color: 1, 0, 0, 1
                pos_hint: {"center_y": .5}
                on_release: self.icon = "heart" if self.icon == "heart-outline" else "heart-outline"

            TwoLineListItem:
                text: "[color=#000000][b]My cats[/b][/color]"
                secondary_text: "[color=#808080][b]Julia and Julie[/b][/color]"
                pos_hint: {"center_y": .5}
                _no_ripple_effect: True
               
'''


class MyApp(MDApp):
    def build(self):
        return Builder.load_string(KV)


MyApp().run()
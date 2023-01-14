from kivy.lang import Builder

from kivymd.app import MDApp

KV = '''
MDScrollView:

    MDList:

        # OneLineAvatarIconListItem:
        #     on_release: print("Click!")

        #     IconLeftWidget:
        #         icon: "github"

        # OneLineAvatarIconListItem:
        #     on_release: print("Click 2!")

        #     IconLeftWidget:
        #         icon: "gitlab"

        OneLineRightIconListItem:
            text: "Client: Sun Site: Bank"

            ImageRightWidget:
                source: "images/success-icon.png"
        OneLineRightIconListItem:
            text: "Client Hergy Site: Vodacom "

            ImageRightWidget:
                source: "images/check-png.webp"
        OneLineRightIconListItem:
            text: "Client David Site: Airtel"

            ImageRightWidget:
                source: "images/success.png"
'''


class Example(MDApp):
    def build(self):
        #self.theme_cls.theme_style = "Dark"
        return Builder.load_string(KV)


Example().run()
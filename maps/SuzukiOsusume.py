from maps.AbstractGakushoku import AbstractGakushoku
class SuzukiOsusume(AbstractGakushoku):

    def get_menu(self):
        return "アロハの100円朝食"
    
    def get_summary(self):
        return "安い、うまい、朝からコーヒーで目が覚める"
    
    def get_author(self):
        return "すずき"
from maps.AbstractGakushoku import AbstractGakushoku
class GakushokuSample(AbstractGakushoku):

    def get_menu(self):
        return "馬鹿坊の日替わりランチ"
    
    def get_summary(self):
        return "日替わりランチなので飽きずに美味しいご飯が食べられる。"
    
    def get_author(self):
        return "小林知輝"
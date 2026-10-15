from maps.AbstractGakushoku import AbstractGakushoku
class KoiwaOsusumeGakushoku(AbstractGakushoku):

    def get_menu(self):
        return "天丼"
    
    def get_summary(self):
        return "ボリュームもあり、コスパも良いです。"
    
    def get_author(self):
        return "小岩"
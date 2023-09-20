class Dokon :
    def __init__(self,sabzovotlar,mevalar,sut_mahsulotlar,gusht,quruq_mahsulotlar):
        self.sabzovotlar = sabzovotlar
        self.mevalar = mevalar 
        self.sut_mahsulotlar = sut_mahsulotlar
        self.gusht = gusht
        self.quruq_mahsulotlar = quruq_mahsulotlar          

class Sotuvchi :
    def __init__(self):
        self.sabzavotlar = {}
        self.mevala = {}
        self.sut_mahsulotlari = {}
        self.gushtlar = {}
        self.quruq_mahsulotla = {}

    def add_product(self,sabzovotlar,mevalar,sut_mahsulotlar,gusht,quruq_mahsulotlar):
        self.sabzavotlar.append(sabzovotlar)
        self.mevala.append(mevalar)
        self.sut_mahsulotlari.append(sut_mahsulotlar)
        self.gushtlar.append(gusht)
        self.quruq_mahsulotla.append(quruq_mahsulotlar)

    def get_product_input(self):
        while True:
            product_name = input ("Qaysi mahsulotni nomini kiritmoqchisiz (1)sabzavotlar,(2)mevalar,(3)sut_mahsuloti(4)gushtlar(5)quruq mahsulot")
            if product_name == '1':
                sabzavot_name = input("Sabzavot nomini kiriting: ")
                if sabzavot_name.lower() == 'exit':
                    break
                if sabzavot_name not in self.sabzavotlar:
                    self.sabzavotlar.append(sabzavot_name)
                    print(f"{sabzavot_name} bu mahsulot ruyxatga qo'shildi.")
                else:
                    print(f"{sabzavot_name} bu mahsulot ruyxatda bor")
            if product_name == '2':
                meva_name = input("Meva nomini kiriting")
                if meva_name.lower() == 'exit':
                    break
                if meva_name not in self.mevala:
                    self.mevala.append(meva_name)  
                    print(f"{meva_name} bu mahsulot ruyxatga qo'shildi.")
                else:
                    print(f"{meva_name} bu mahsulot ruyxatda bor")
sotuvchi = Sotuvchi()
sotuvchi.get_product_input



            
                    
                   

        






          
            

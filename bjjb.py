class Usuario:
    def __init__(self):
        self.nombre=[]
        self.edad=[]
        self.credencial=[]
        self.cantidad_libro=0
        self.libro=[]
    print('''
                BIENVENIDO
        biblioteca municipal de neiva
        
        ''')
    
    def login (self):
        
        self.nombre = input('''¿cual es su nombre?:
                        
                        ''')
        print("ingrese su edad")
        self.edad = int(input())
        self.credencial= input('''¿cuenta usted con la credencial de la biblioteca? (""si"")(""no""): 
                            
                            ''')
        self.cantidad_libro= input('''¿cuantos libros desea solicitar?: 
                                
                                ''')
        self.verDatos= input('''¿desea ver su datos para confirmarlos?: 
                            ''')
        
        if self.verDatos == "si":
            self.VerDatos()
            
        else :
            print ("ok")
        
        if self.edad <= 17:
            self.MenorEdad()
            self.login()
            
        
        if self.credencial== "no":
            self.NoCrendecial()
            self.login()
        
    def NoCrendecial(self):
        print("por favor solicite una credencial de la biblioteca en la secretaria de educacion!!!")

    def MenorEdad(self):
        print("USTES ES MENOR DE EDAD, VUELVA CUANDO CUMPLA SUS 18!!!")
        
    def VerDatos(self):
        print("\tsu nombre es: ",self.nombre)
        print("\tsu edad es: ",self.edad)  
        print("\t¿cuenta con credencial?",self.credencial)
        print("\tla cantidad de libros a solicitar es de: ",self.cantidad_libro) 
        
biblioteca= Usuario()
biblioteca.login()

class Libro(Usuario):
    
    def __init__(self):
        self.solicitar=0
        self.CleanCode= {"titulo" : "clean code", "autor" : " Robert C. Martin", "ISBN" : "-13. 978-8441532106","paginas":"464","editorial":"ANAYA MULTIMEDIA", "edicion": "19 de junio 2012", "lugar": "california- EE.UU."}
        self.CodeComplete={"titulo" : "Code Complete", "autor" : " Steve McConnell", "ISBN" : "9780735619678","paginas":"900","editorial":"Microsoft Press", "edicion": "19 de junio 2004", "lugar": "sidney- australia"}
        self.ThePragmaticProgrammer={"titulo" : "The Pragmatic Programmer", "autor" : "Andy Hunt y Dave Thomas", "ISBN" : "9780135957059.","paginas":"352","editorial":"Addison Wesley", "edicion": "20 de octubre de 1999", "lugar": "raleigh-EE.UU."}
        self.IntroduccionALosAlgoritmos={"titulo" : "Introduccion A Los Algoritmos", "autor" : "Thomas H. Cormen y Ronald Rivest", "ISBN" : "9789587786804","paginas":"1312","editorial":"PHI learning", "edicion": "14 de febrero de 1990", "lugar": "columbia- EE.UU."}
        self.ProgramacionEnGo={"titulo" : "Porgramacion en GO", "autor" : " Mario Macias Lloret", "ISBN" : "-13. 978-8441532106","paginas":"246","editorial":"ALPHAEDITORIAL MARCOMBO", "edicion": "15 de noviembre de 2020", "lugar": "madrid - españa"}
    
    
    def SolicitarLibro(self):
        self.solicitar= int(input('''¿que libro desea solicitar?
                            \t1. clean code
                            \t2. code complete
                            \t3.the pragmatic programmer
                            \t4. introduccion a los algoritmos
                            \t5. prpgramacion en go
                            \t6. desea pedir otro libro?                          
                            ingresar:'''))
        while True:
            if self.solicitar== 1:
                self.libroClean()
            elif self.solicitar== 2:
                self.libroCodeComplete()
            elif self.solicitar== 3:
                self.libroPragmatic()
            elif self.solicitar==4:
                self.libroAlgoritmos()
            elif self.solicitar==5:
                self.libroGo()
            elif self.solicitar==6:
                break
                
    
    def libroClean (self):
        print('''el libro clean code que usted solicita tiene la siguiente informacion: 
            ''')
        print("\tTITULO: ",self.CleanCode["titulo"])
        print("\tAUTOR: ",self.CleanCode["autor"])
        print("\tISBN: ",self.CleanCode["ISBN"])
        print("\tPAGINAS: ",self.CleanCode["paginas"])
        print("\tEDITORIAL: ",self.CleanCode["editorial"])
        print("\tEDICION: ",self.CleanCode["edicion"])
        print("\tLUGAR: ",self.CleanCode["lugar"])
        self.SolicitarLibro()
    
    def libroCodeComplete(self):
        print('''el libro clean code que usted solicita tiene la siguiente informacion: 
            ''')
        print("\tTITULO: ",self.CodeComplete["titulo"])
        print("\tAUTOR: ",self.CodeComplete["autor"])
        print("\tISBN: ",self.CodeComplete["ISBN"])
        print("\tPAGINAS: ",self.CodeComplete["paginas"])
        print("\tEDITORIAL: ",self.CodeComplete["editorial"])
        print("\tEDICION: ",self.CodeComplete["edicion"])
        print("\tLUGAR: ",self.CodeComplete["lugar"])
        self.SolicitarLibro()
    
    def libroPragmatic (self):
        print('''el libro clean code que usted solicita tiene la siguiente informacion: 
            ''')
        print("\tTITULO: ",self.ThePragmaticProgrammer["titulo"])
        print("\tAUTOR: ",self.ThePragmaticProgrammer["autor"])
        print("\tISBN: ",self.ThePragmaticProgrammer["ISBN"])
        print("\tPAGINAS: ",self.ThePragmaticProgrammer["paginas"])
        print("\tEDITORIAL: ",self.ThePragmaticProgrammer["editorial"])
        print("\tEDICION: ",self.ThePragmaticProgrammer["edicion"])
        print("\tLUGAR: ",self.ThePragmaticProgrammer["lugar"])
        self.SolicitarLibro()
    
    def libroAlgoritmos (self):
        print('''el libro clean code que usted solicita tiene la siguiente informacion: 
            ''')
        print("\tTITULO: ",self.IntroduccionALosAlgoritmos["titulo"])
        print("\tAUTOR: ",self.IntroduccionALosAlgoritmos["autor"])
        print("\tISBN: ",self.IntroduccionALosAlgoritmos["ISBN"])
        print("\tPAGINAS: ",self.IntroduccionALosAlgoritmos["paginas"])
        print("\tEDITORIAL: ",self.IntroduccionALosAlgoritmos["editorial"])
        print("\tEDICION: ",self.IntroduccionALosAlgoritmos["edicion"])
        print("\tLUGAR: ",self.IntroduccionALosAlgoritmos["lugar"])
        self.SolicitarLibro()
    
    def libroGo (self):
        print('''el libro clean code que usted solicita tiene la siguiente informacion: 
            ''')    
        print("\tTITULO: ",self.ProgramacionEnGo["titulo"])
        print("\tAUTOR: ",self.ProgramacionEnGo["autor"])
        print("\tISBN: ",self.ProgramacionEnGo["ISBN"])
        print("\tPAGINAS: ",self.ProgramacionEnGo["paginas"])
        print("\tEDITORIAL: ",self.ProgramacionEnGo["editorial"])
        print("\tEDICION: ",self.ProgramacionEnGo["edicion"])
        print("\tLUGAR: ",self.ProgramacionEnGo["lugar"])
        self.SolicitarLibro()


pedir = Libro()
pedir.SolicitarLibro()

class hijo(Libro):
    
    def mostrar(self):
        print("desea pedir otro libro")
        self.pedirlibro=input()
        print("numero de libro")
        self.numero=input()
        if self.solicitar == self.numero :
            print("este libro ya a sido pedido")
        else:
            print("libro ya prestado")
            
            
            
hija=hijo()
hija.mostrar()
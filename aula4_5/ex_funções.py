


def mostrar_imc(peso, altura):
    imc  = peso/altura ** 2
    print(imc)



def sistema():
    p = float(input('>>>'))
    a = float(input('>>>'))    
    mostrar_imc(p,a)    
    
sistema()
import math
def main():
    #escribe tu código abajo de esta línea
    x1=int(input('x1= '))
    y1=int(input('y1= '))
    x2=int(input('x2= '))
    y2=int(input('y2= '))
    d= float(math.sqrt((x2-x1)**2+(y2-y1)**2))
    d=round(d,2)
    print('distancia= '+str(d))
if __name__ == '__main__':
    main()
    #x1= 2
#y1= -4
#x2= 5
#y2= 3
#distancia= 7.62
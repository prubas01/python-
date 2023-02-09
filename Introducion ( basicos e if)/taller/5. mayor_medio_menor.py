print("\nidentificar el mayor menor o el del medio\n")

mayor= int
menor = int
medio= int
a = int(input("Digite el primer numero: "))
b = int(input("Digite el segundo numero: "))
c = int(input("Digite el tercer numero: "))



if ((a>b) & (b>c)):
    print("mayor ", a , " medio " , b , " menor " , c )
  
if ((a>c) & (c > b)):
    print("mayor ", a , " medio " , c , " menor " , b )
  
  
if ((b>a) & (a > c)):
    print("mayor ", b , " medio " , a , " menor " , c )
  
  
if ((b>c) & (c > a)):
    print("mayor ", b , " medio " , c , " menor " , a );  
  
  
if ((c>a) & (a > b)):
    print("mayor ", c , " medio " , a , " menor " , b );  
  
   
if ((c>b) & (b > a)):
    print("mayor ", c , " medio " , b , " menor " , a ); 
   






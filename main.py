A,B,C = input().split()
A = float(A)
B = float(B)
C = float(C)
at = (A * C) / 2
ac = (C**2) * 3.14159
aq = B**2
at2 = ((A + B) * C) / 2
ar = A * B
print('TRIANGULO: %.3f'%at)
print('CIRCULO: %.3f'%ac)
print('TRAPEZIO: %.3f'%at2)
print('QUADRADO: %.3f'%aq)
print('RETANGULO: %.3f'%ar)
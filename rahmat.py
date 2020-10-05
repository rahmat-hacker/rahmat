print('''
+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=
HI WELCOME TOP MY SCRIPT """""""""""""""""""""""""""""""

THIS IS CALAULATOR SCRIPT HAHAHAHAHAHAHAHAHAHA
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
========================================================
THIS SCRIPT MADE BY RAHMAT CYBER

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
_______________________________________________________

MY ID IN TELEGRAM = @RAHMATCYBER

*********************************************************
*********************************************************

MY TELEGRAM CHANNEL IS @RAHMAT786786786

&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

''')

def calculate():
    number1=int(input('enter number'))
    ch=input('''
+
-
*
**
/
''')
    number2=int(input('enter number'))
    if ch =='+':
        print(number1,'+',number2,'=',number1+number2)
    if ch =='-':
        print(number1,'-',number2,'=',number1-number2)
    if ch =='*':
        print(number1,'*',number2,'=',number1*number2)
    if ch =='**':
        print(number1,'**',number2,'=',number1**number2)
    if ch =='/':
        print(number1,'/',number2,'=',number1/number2)
calculate()
def again():
    g=int(input('''
1=continue:
2=exit:

'''))
    if g==1:
        calculate()
    if g==2:
        exit()
again()
   

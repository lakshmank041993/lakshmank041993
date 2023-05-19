# covert roman to interger

class Roman_to_interger:
    def convert(self, s :str):
        #define numeric values for roman numerals
        roman={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        number = 0
        for i in range(len(s)-1):
            if roman.get(s[i]) < roman.get(s[(i+1)]):                                                                            
               number -= roman.get(s[i])
            else:
               number += roman.get(s[i])
        return number+roman.get(s[-1])
 
    

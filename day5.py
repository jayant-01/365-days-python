#roman numbers to decimal in python

roamn_decimal={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}

def conversion(s):
    decimal = 0
    for i in range(len(s)-1):
      if roamn_decimal[s[i]] < roamn_decimal[s[i+1]]:
          decimal = decimal - roamn_decimal[s[i]]
      else:
          decimal = decimal + roamn_decimal[s[i]]
    decimal = decimal + roamn_decimal[s[-1]]
    return decimal


s=input()
print(conversion(s))




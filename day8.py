# Description: Write a program to convert temperature from Fahrenheit to Celsius degree and vice versa.

def f_c(num):
    return ((num - 32)/1.8)



def c_f(num):
    return ((num * 1.8) + 32)




if __name__ == '__main__':
    print(f_c(108),"celcius")
    print(c_f(30),"fahrenheit")
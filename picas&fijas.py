# check if 2 numbers have numbers in the same position if so count it as "fija" 
# if num2 contains numbers that are in num count it as "pica"

def check(num, num2):
    # check both have same length
    num = [str(i) for i in str(num)]
    num2 = [str(i) for i in str(num2)]

    if len(num) != len(num2):
        return "Los numeros no tienen la misma longitud"
    
    fijas = []
    picas = []  
    
    #fijas 
    for i in range(len(num)):
        if num[i] == num2[i]:
            fijas.append(num[i])
            num2[i] = "0"
            
    #picas
    for i in range(len(num)):
        if num2[i] != "0":
            picas.append(num2[i])        
    
    return {"fijas": fijas, "picas": picas}

print(check(1234, 1243))
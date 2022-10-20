def zadanie4(x):
    
    def sqrtIter(r):
        if func2(r):
            return r
        else:
            return sqrtIter(improve(r))
        
    def improve(r):
        return average(r, x/r)
    
    def average(x, y):
        return (x+y)/2
    
    def func2(r):
        if(abs(r**2-x)<0.001):
            return 1
        else:
            return 0
        
    return sqrtIter(1.0)
print(zadanie4(int(input("Введите число: "))))    

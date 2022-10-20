def zadanie2(lst):
    div2 = [ i for i in lst if i % 2 == 0]
    div3 = [ i for i in lst if i % 3 == 0]
    div5 = [ i for i in lst if i % 5 == 0]
    return div2, div3, div5
 
print(zadanie2([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]))

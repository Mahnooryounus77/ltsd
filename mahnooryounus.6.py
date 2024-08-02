
# Q:1
def Sum(list):
    return sum(list)
Numbers = [10,15,5,3,35,9]
print(Sum(Numbers))


# Q 2:
def smallest(Tuple):
    return min(Tuple)
Numbers = (20,5,12,3,23,50)
print(smallest(Numbers)) 

# Q 3:
def square_elements(numbers):
    square= set()  
    for number in numbers:
        square.add(number ** 2)  
    return square
Numbers = {9, 7, 3, 14,16}
x = square_elements(Numbers)
print(x) 


# Q 4:
def keys(KEY):
    return list(KEY.keys())
dict = {'NAME': 'SARA','COUNTRY': 'PAKISTAN', 'CITY': 'lAHORE'}
print(keys(dict))
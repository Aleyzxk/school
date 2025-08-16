

def binary_search(list, item):
    low = 0                 #bajo y alto mantienen un registro de en qué parte de la lista buscarás
    high = len(list)-1
    
    while low <= high:      #mientras no lo hayas reducido a un solo elemento
        mid = (low + high)//2   #observa el elemento del medio
        guess = list[mid]
        if guess == item: #encuentre el articulo
            return mid
        if guess > item: #la suposicion es demasiado alta
            return mid - 1
        else:           #la suposicion es demasiado baja
            low = mid + 1
    return None #el elemento no existe

my_list = [1, 2, 5, 7, 9]
            
            
print(binary_search(my_list, 3))  # =>  1
print(binary_search(my_list, -1)) # =>  none
    
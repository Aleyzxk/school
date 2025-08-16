def binary_search(ordered_list, term):
    index_of_first_element = 0
    index_of_last_element = size_of_list
    while index_of_first_element <= index_of_last_element:
        mid_point = (index_of_first_element + index_of_last_element)//2
        if ordered_list[mid_point] == term:
            return mid_point
        if term > ordered_list[mid_point]:
            index_of_first_element = mid_point +1
        else:
            index_of_last_element = mid_point - 1 
    if index_of_first_element > index_of_last_element:
        return None
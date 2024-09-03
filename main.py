from collections import Counter


my_tuple: tuple[int] = (99,)
##################################
my_tuple2: tuple[int] = (77, 88 ,99)
##################################
def tuple_len():
    print(len(77 , 88, 99))
##################################
def tuple_plus(x: int, y: int) -> tuple[int]:
    return (x + y)
print(tuple_plus(5,6))
##################################
def shared_tuple(x: tuple[list[int]],y: tuple[list[int]]) -> tuple[int]:
    shared_elements = []
    for list_x in x:
        if list_x in y:
            shared_elements.append(list_x)
    return tuple(shared_elements)

result = shared_tuple((1, 2, 3 ,4) , (3, 4, 5, 6))
print(result)
###################################
def unshared_elements(x: tuple[list[int]], y: tuple[list[int]]) -> tuple[int]:
    unshared_tuples = []
    for list_x in x:
        if list_x not in y:
            unshared_tuples.append(list_x)
    return tuple(unshared_tuples)
x = unshared_elements((1, 2, 3, 4,) , (3, 4, 5, 6,))
print(x)
####################################
def tuple_index(t: tuple[any], index: int):
    if 0 <= index <len(t):
        return t[index]
    else:
        return None

result = tuple_index((10, 20, 30, 40), 2)
print(result)
#####################################
def reversed_tuple(x: tuple[int]) -> tuple[int]:
    return x[::-1]
tuple_reversed = reversed_tuple((1, 2, 3, 4))
print(tuple_reversed)
#####################################
def count_divisors_in_tuple(n: int, t: tuple[int]) -> int:
    def find_divisors(num: int) -> set[int]:
        divisors = set()
        for i in range(1, num + 1):
            if num % i == 0:
                divisors.add(i)
        return divisors

    divisors = find_divisors(n)
    count = 0
    for element in t:
        if element in divisors:
            count += 1
    return count
print(count_divisors_in_tuple(500,(10 ,20, 30, 40)))
#####################################
def mul_tuple(t: tuple[int], m:int) -> tuple[int]:
    return (t * m)

print(mul_tuple((3, 4, 5,), 2))
#####################################
def my_enumerate_tuple_list(t: tuple[str]) -> tuple[tuple[int, str]]:
    return tuple((index, value) for index, value in enumerate(t))

result = my_enumerate_tuple_list(("Alon", "Ofir", "shilo"))
print(result)
#####################################
def statistic_tuple(t: tuple[int]) -> dict[str, int]:
    stats = {
        "max": max(t),
        "min": min(t),
        "amount of numbers": len(t),
        "sum": sum(t),
        "sorted": sorted(t),
        "frequency": dict(Counter(t))
    }
    return stats

result = statistic_tuple((10, 5, 20, 15))
print(result)
#####################################
def letters_tuple(l: tuple[str]) -> str:
    return ''.join(l)
result = letters_tuple(('H', 'e', 'l', 'l', 'o'))
print(result)
#####################################
def tuple_to_str(s: str) -> tuple[str]:
    return tuple(s)
result = tuple_to_str(("hello"))
print(result)
#####################################
def delete_num(t: tuple[int], num: int) -> tuple[int]:
    return tuple(x for x in t if x != num)

result = delete_num((10, 20, 30, 10, 40), 10)
print(result)
######################################
def tuple_without_duplicates(t: tuple[int]) -> tuple[int]:
    unique_list = []
    for item in t:
        if item not in unique_list:
            unique_list.append(item)
    return tuple(unique_list)


result = tuple_without_duplicates((10, 20, 10, 30, 40, 30, 40, 50, 60))
print(result)
########################################
def tuple_index(x: tuple[int], y: int) -> tuple[int]:
    indices = [i for i, value in enumerate(x) if value == y]
    return tuple(indices)

result = tuple_index((10, 20, 5, 5, 20, 3, 5, 10, 10, 3, 20), 10)
print(result)
########################################
def names_and_grades_tuple():
    names_tuple = []
    while True:
        name = input("Type in names, type 'done' to exit: ")
        if name.lower() == "done":
            break
        names_tuple.append(name)


    grades = []
    while True:
            grade = int(input("Type in grades, type '-999' to exit: "))
            if grade == -999:
                break
            grades.append(grade)

    names_grades = tuple(zip(names_tuple, grades))

    return names_grades


result = names_and_grades_tuple()
print(result)




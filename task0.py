from random import randint


def RList():
    RList = []
    for i in range(0, 30):
        RList.append(randint(-100, 100))
    return RList


def M_List(List):

    M_list = max(List)
    M_i = List.index(max(List))

    return M_list, M_i


def res_list(List):
    res_list = []
    for i in List:
        if i % 2 != 0:
            res_list.append(i)
    if len(res_list) == 0:
        return "no unpaired numbers"
    else:
        return res_list


List = RList()
print("initial random list :\n", List)
print("max num > ", M_List(List)[0], "\nposition of max num > ", M_List(List)[1]+1)

# isinstance() проверяет принадлежность объекта к определенному типу данных isinstance(объект,тип данных)
if isinstance(res_list(List), list):
    print("List of unpaired numbers sorted from highest to lowest :\n",
          sorted(res_list(List), reverse=True))
else:
    print(res_list(List))
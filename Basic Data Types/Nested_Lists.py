if __name__ == '__main__':
    score_list = []
    nested_list = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        score_list.append(score)
        nested_list.append([name,score])
      
    score_list.sort() 
    lowest = score_list[0]
    for element in score_list:
        if lowest < element:
            second_lowest = element
            break 

    name_list = []
    for item in nested_list: 
        if second_lowest == item[1]: 
            name_list.append(item[0]) 
    name_list.sort() 
    for name in name_list: 
        print(name) 

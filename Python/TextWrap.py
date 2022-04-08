

def wrap(string, max_width):
    resultStr = ""
    flag = 1
    for i in range(len(string)):
        if flag<=max_width:
            resultStr += string[i]
            flag +=1
        if flag == max_width:
            resultStr += "\n"
            flag = 1
            
    return resultStr
if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)


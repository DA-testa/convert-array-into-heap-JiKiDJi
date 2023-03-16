def build_heap(data):
    swaps = []
    l = len(data)
    i = int((l-3)/2)
    while (i>=0):
        if(data[2*i+1]>data[2*i+2]):
            min = 2*i+2
        else:
            min = 2*i+1
        if(data[min]<data[i]):
            swaps.append([i, min])
            data[min], data[i] = data[i], data[min]
            if(min*2+1<=l-1):
                i=min+1       
        i-=1

            
    print(data)
    return swaps


def main():
    
    # TODO : add input and corresponding checks
    # add another input for I or F 
    # first two tests are from keyboard, third test is from a file
    let = input()[0]
    if let == 'F' :
        text = input()
        if 'a' in text:
            return
        text = "tests/" + text
        print(text)
        with open(text) as file:
            n = int(file.readline())
            data = [int(i) for i in file.readline().split(' ')]          
    elif let == 'I' :
        n = int(input())
        data = [int(i) for i in input().split(' ')]
    else: 
        return

    # input from keyboard
    # n = int(input())
    # data = list(map(int, input().split()))

    # checks if lenght of data is the same as the said lenght
    assert len(data) == n

    # calls function to assess the data 
    # and give back all swaps
    swaps = build_heap(data)

    # TODO: output how many swaps were made, 
    # this number should be less than 4n (less than 4*len(data))


    # output all swaps
    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()

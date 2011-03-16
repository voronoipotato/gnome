def swap(x,y):
	a = x
	b = y
	x = b
	y = a
	return x, y

def gnome(array):
    pos = 1
    while(pos < array.__len__()):
        if(array[pos] >= array[pos-1]):
            pos = pos + 1 
        else:
            array[pos],array[pos-1] = swap(array[pos],array[pos-1])
            if (pos > 1):
                pos = pos - 1
            else:
                pos = pos + 1
    

def main():
    test = [0,3,4,2,1,4,8,10,20,30,24,17]
    print test
    gnome(test)
    print test
    

main()

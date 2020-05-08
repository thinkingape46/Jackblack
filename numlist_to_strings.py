'''Created this function to convert a list of integers into a list of strings'''
def numtostr_range():
    startrange = int(input("Please enter START number of the range:"))
    endrange = int(input("Please enter END number of the range:"))
    steprange = int(input("Please enter STEP of the range:"))
    numrange = list(range(startrange,endrange,steprange))
    result = [str(x) for x in numrange]
    print("Below is the list of strings:")
    print(result)
numtostr_range()
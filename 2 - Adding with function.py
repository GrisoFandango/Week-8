#creating a function that will add up 
#the number between a range given from
#the 2 arguments
def sum(r1,r2):
    result = 0
    #this loop will sum up all the 
    #number bewtween the 2 arguments
    for i in range(r1,r2):
        result += i
    return result

def main():
    print("Sum from 1 to 10 is",sum(1,10))
    print("Sum from 20 to 37 is",sum(20,37))
    print("Sum from 35 to 49 is",sum(35,49))

main()

    

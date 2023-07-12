
def find_best_user(file_path):
    name = " "
    max = 0
    first_Iteration = True    
    with open (file_path, 'r') as file:
        for eachline in file:
            if first_Iteration == True:
                first_Iteration = False
                continue
            line = eachline.replace("\n", " ")
            words = line.split(",")
            # print(words)
            # print(len(words))
            for i in range(1):
                value = int(words[5])
                print(value)
                if value > max:
                    max = value
                    name = words[0]
        print(name)
        return name
                
                

             
    
    
    
    pass #TODO


def test():
    result = find_best_user("users.txt")
    print(f"Congraatulations {result}! You have a lot of reward points, would you like to spend them?")

test()
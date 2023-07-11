
def find_best_user(file_path):
    name = " "
    max = 0
    
    with open (file_path, 'r') as file:
        for eachline in file:
            lines = file.readline()
            words = lines.split(",")
            print(words)
            
            for i in range(len(words)):
                print(words)
                
                if words[5] > max:
                    max = int(words[5])
                    #print(words[5])
                    name = words[0]
                return name
             
    
    
    
    pass #TODO


def test():
    result = find_best_user("users.txt")
    print(f"Congraatulations {result}! You have a lot of reward points, would you like to spend them?")

test()
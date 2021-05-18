from IPython.display import clear_output


def user_choice():
    clear_output()
    print("WELCOME TO AVERAGE CALCULATOR")
    
    lst=[]
    choice = input('Enter Number of Subjects:')
    
   
    while choice.isdigit() == False:
        
        
        choice = input('Enter Number of Subjects:')
    ujj=int(choice)
    
    for i in range(0,ujj):
           
            x=input(f"Enter the score for subject {i} ->")
            while x.isdigit() == False:
                x=input(f"Enter the score for subject {i} -> ")
                continue
                
            ks=int(x)
            lst.append(ks)
            

            
    print(f"The Average is {sum(lst)/len(lst)}")

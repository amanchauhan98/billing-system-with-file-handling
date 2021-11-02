# shivam enterprises :

if __name__ == '__main__' :
    print("------- SHIVAM ENTERPRISES--------")
    user_name = str(input("Enter your name here\n"))
    contact = int(input("Enter your Contact here\n"))
    print("Do you want to know the price of metal harding.")
    choice = str(input("yes/no\n"))
    if choice == "yes" :
        metal = {"Iron" : 35, "Steel" : 50, "Copper" : 60, "Others" : 80}
        print(metal)
        user_metal_choice = str(input("Enter the Metal which you want to go for Harding. \n"))
        if user_metal_choice == "Iron" :
            kg = int(input("Enter the weight of your metal. \n"))
            price = lambda kg : kg * 35
            gst = (price(kg)*20)/100
            print(f"Your net Balance is {price(kg)} and GST is {gst}. So the Total Balance is {price(kg)+gst}")
        elif user_metal_choice == "Steel" :
            kg = int(input("Enter the weight of your metal. \n"))
            price = lambda kg : kg * 50
            gst = (price(kg)*20)/100
            print(f"Your  Balance is {price(kg)} and GST is {gst}. So Total Balance is {price(kg)+gst}")
        elif user_metal_choice == "Copper" :
            kg = int(input("Enter the weight of your metal. \n"))
            price = lambda kg : kg * 60
            gst = (price(kg)*20)/100
            print(f"Your net Balance is {price(kg)} and GST is {gst}. So the Total Balance is {price(kg)+gst}")   
        elif user_metal_choice == "Others" or user_metal_choice == "Other" :
            kg = int(input("Enter the weight of your metal. \n"))
            price = lambda kg : kg * 80
            gst = (price(kg)*20)/100
            print(f"Your net Balance is {price(kg)} and GST is {gst}. So the Total Balance is {price(kg)+gst}") 
        else :
            print(f"Sorry! {user_name}, You Enter the wrong input.")    
            raise EOFError("Value Error Found!")   
    elif choice == "no" or choice == "No" :
        print(f"OK! {user_name}")

    with open("shivam_Ent.txt","a") as f:
        f.write(f"User name : {user_name}\n")
        f.write(f"User Contact : {str(contact)}\n")
        f.write(f"Metal choice : {user_metal_choice}\n")
        f.write(f"Weight : {str(kg)}\n") 
        f.write(f"Net Amount : {str(price(kg))}\n")
        f.write(f"GST : {str(gst)}\n")
        f.write(f"Total Amount : {str(price(kg)+gst)}\n")

                   

    with open("shivam_Ent.txt","r+") as g:
        for i in g:
            print(i)

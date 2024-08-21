class multifunction():
    
    def subfields():
        List=["Subfields in AI are", "Machine Learning", "Neural Networks", "Vision", "Robotics", "Speech Processing", "Natural Language Processing"]
        for i in List:
            print(i)

    def OddEven():
        num=int(input("Enter a number"))
        if(num%2==0):
            print(num,"is a Even number")
            result="Even number"
        else:
            print(num,"is a Odd number")
            result="Odd number"

    def Elegible():
        Gender=input("Your Gender:")
        Age=int(input("Your Age:"))
        
        if(Gender=="Male" and Age>=21):
            print("Eligible")
        elif(Gender=="Female" and Age>=18):
            print("Eligible")
        else:
            print("Not Eligible")

    def percentage():
        subject1=int(input("Subject1="))
        subject2=int(input("Subject2="))
        subject3=int(input("Subject3="))
        subject4=int(input("Subject4="))
        subject5=int(input("Subject5="))
        Total=(subject1+subject2+ subject3+ subject4+subject5)
        print("Total:",Total)
        mark="Total"
        Percentage=((subject1+subject2+ subject3+ subject4+subject5)/5)
        print("Percentage:",Percentage)
        mark="Percentage"

    def triangle():
        Height=int(input("Height:"))
        Breadth=int(input("Breadth:"))
        Area=(Height*Breadth)/2
        print("Area formula:(Height*Breadth)/2")
        print("Area of Triangle:",Area)
        measure="Area of Triangle"
        Height1=int(input("Height1:"))
        Height2=int(input("Height2:"))
        Breadth2=int(input("Breadth2:"))
        print("Perimeter formula:Height1+Height2+Breadth2")
        perimeter=(Height1+Height2+Breadth2)
        print("perimeter of Triangle:",perimeter)
        measure="perimeter of Triangle"

    



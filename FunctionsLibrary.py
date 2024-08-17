class mulptiplefunctions():
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
        Age=int(input("Your age:"))
        
        if(Age<23):
            print("NOT ELIGIBLE")
            cate="NOT ELIGIBLE"
        else:
            print("ELIGIBLE")
            cate="ELIGIBLE"

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

    def subfields():
        print("Subfields in AI are:")
        Subfield1=print("Machine Learning")
        subfield="Subfield1"
        Subfield2=print("Neural Networks")
        subfield="Subfield2"
        Subfield3=print("Vision")
        subfield="Subfield3"
        Subfield4=print("Robotics")
        subfield="Subfield4"
        Subfield5=print("Speech Processing")
        subfield="Subfield5"
        Subfield6=print("Natural Language Processing")
        subfield="Subfield6"
    
    
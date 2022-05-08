current_location=["pune"]
cab_type=["(1)Micro","(2)Mini","(3)Auto","(4)Prime"]
dropping_point=["Pune station"]
show_the_driver=["(a).Raj","(b)Aman","(c)Arjun","(d)Yash"]
price=["(i)700","(ii)600","(iii)750","(iv)800"]
mobile_number=[["1)9156730845"],["2)8729489676"],["3)8037164372"],["4)9024368423"]]
cab_details=[["1)White,HR28DQ55"],["2)Black,KL215 8924"],["3)Gray,JP14BN400"],["4)Red,MH02EM5685"]]
feedback=[["(A),i)Good ,ii)Responsible Driving ,iii)Im satisfied with his driving"],
          ["(B),i)I had excellent trip,ii)carteous and friendly,iii)excellent driving"],
          ["(C),i)good driver,ii)good service,iii)small auto"],
          ["(D),i)wonderful service and safe,ii)comfartable ,iii)top service excelient driving"]]
print("WELCOME TO OLA APP ")
location=input("enter your location")
i=0
while i<len(current_location):
    print(current_location[i])
    cab=input("see your cab type")
    if cab=="yes":
        print(cab_type)
        i+=1
    cabtype=input("choose your cab type")
    if cabtype=="prime":
        print( "yes available")
        dropping_point=input("enter your dropping point")
        if dropping_point=="pune station":
            print("yes")
            driver_name=input("see the driver name")
            j=0
            while j<len(show_the_driver):
                print(show_the_driver[j])
                j+=1
            show_the_driver=input("choose the driver name")
            if show_the_driver=="Yash":
                print("yes avilable")
                rupees=input("see the price")
                x=0
                while x<len(price):
                    print(price[x])
                    x+=1
                rate=(input("choose the price"))
                if rate=="800":
                    print("take your price")
                    number=input("see driver mobile number")
                    k=0
                    while k<len(mobile_number):
                        print(mobile_number[k])
                        k+=1
                    mobile_number=input("enter your mobile no")
                    if mobile_number=="4":
                        print("correct no")
                    cabinformation=input("see the cab information")
                    y=0
                    while y<len(cab_details):
                        print(cab_details[y])
                        y+=1
                    cabinformation1=input("choose the cab details")
                    if cabinformation1=="4":
                        print("correct information")
                        feedback=input("see your feedback")
                        z=0
                        while z<len(feedback):
                            print(feedback[z])
                            z=z+1
                        feedback1=input("enter your feedback")
                        if feedback1=="D":
                            print("good") 
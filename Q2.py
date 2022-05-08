question_list = ["1).How many continents are there?","2).What is the capital of India?","3).NG mei kaun se course padhaya jaata hai?"]
options_list = [["A.Four", "B.Nine", "C.Seven", "D.Eight"],["A.Chandigarh", "B.Bhopal", "C.Chennai", "D.Delhi"],["A.Software Engineering", "B.Counseling", "C.Tourism", "D.Agriculture"]]
solution_list = [3,4,1]
answer_list=[["3.seven ","4.Eight"],["3.chennai","4.delhi"],["1.software engineering","2.counseling"]]
print("kaun banega codepati(KBC)")
i=0
sum=0
count=0
while i<len(question_list):
    print(question_list[i])
    a=0
    b=i
    while a<=len(options_list):
        k=(options_list[i][a])
        print(a+1,k)
        a+=1
    num=input("do you want lifeline :")
    if num=="yes":
        print("accept")
        if count<1:
            print(answer_list[b])
            num1=int(input("enter the answer"))
            if num1==solution_list[i]:
                print("correct answer")
                sum+=100
                print("win",sum)
            else:
                print("incorrect answer")
                print("win",sum)
                break
            count+=1
        else:
            print("you are alredy use lifeline")
            num2=int(input("enter the answer"))
            if num2==solution_list[i]:
                print("correct your answer")
                sum+=100
                print("win",sum)
            else:
                print("wrong answer")
                print("win",sum)
                break
    else:
        num3=int(input("enter the answer"))
        if num3==solution_list[i]:
            print("correct your answer")
            sum+=100
            print("win",sum)
        else:
            print("wrong answer")
            print("win",sum)
            print("congragulations..you are participated in kbc game")           
            print("win",sum)
            print("thank you")
            break
    i+=1

    






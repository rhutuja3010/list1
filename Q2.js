question_list = ["1).How many continents are there?","2).What is the capital of India?","3).NG mei kaun se course padhaya jaata hai?"]
options_list = [["A.Four", "B.Nine", "C.Seven", "D.Eight"],["A.Chandigarh", "B.Bhopal", "C.Chennai", "D.Delhi"],["A.Software Engineering", "B.Counseling", "C.Tourism", "D.Agriculture"]]
solution_list = [3,4,1]
answer_list=[["3.seven ","4.Eight"],["3.chennai","4.delhi"],["1.software engineering","2.counseling"]]
let i=0;
let sum=0;
let count=0;
while (i<question_list.length){
    console.log(question_list[i])
    let a=0;
    let b=i;
    while(a<=options_list.length){
        k=(options_list[i][a])
        console.log(a+1,k)
        a++
    }
    let user=require("readline-sync")
    let lifeline=user.question(`do you want lifeline ("yes" or "no") :`)
    if (lifeline=="yes"){
        console.log("accept")
        if(count<1){
            console.log(answer_list[b])
            let answer1=user.question("enter the answer :")
            if (answer1==solution_list[i]){
                console.log("correct answer")
                sum+=100
                console.log("win",sum)
            }else{
                console.log("incorrect answer")
                console.log("win",sum)
                break
                

            }
            count+=1
        }else{
            console.log("you are alredy use lifeline")
            let answer2=user.question("enter the answer :")
            if (answer2==solution_list[i]){
                console.log("correct your answer")
                sum+=100
                console.log("win",sum)
                break
            }

        }
    }else{
        let answer3=user.question("enter the answer :")
        if (answer3==solution_list[i]){
            console.log("correct your answer")
            sum+=100
            console.log("win",sum)
        }else{
            console.log("wrong answer")
            console.log("win",sum)
            console.log("thank you")
            console.log("congragulations..you are participated in kbc game")
            break
        }
        i++

    }
}
// a=[[2,7,6],[9,5,1],[4,3,8]]
// print("matrix is......")
// for i in range (3):
//     for j in range(3):
//         print(a[i][j],end=" ")
//     print()
// sumd1=0
// sumd2=0
// for i in range(3):
//     for j in range(3):
//         if i==j:
//             sumd1=sumd1+a[i][j]
//         if i+j==3-1:
//             sumd2=sumd2+a[i][j]
// print(sumd1)
// print(sumd2)
// if sumd1!=sumd2:
//     f=1
// else:
//     for i in range(3):
//         sumr=0
//         sumc=0
//     for j in range(3):
//         sumr=sumr+a[i][j]
//         sumc=sumc+a[j][i]
//     if sumr!=sumd1:
//         f=1
//     elif sumc!=sumd1:
//         f=1
//     else:
//         f=0
// if f==0:
//     print("matrix is a magic sequare")
// else:
//     print("matrix is not a magic sequare")



let a=[[2,7,6],
       [9,5,1],
       [4,3,8]]
string=""
for (let i=0;i<3;i++){
    for (let j=0;j<3;j++){
        string+=a[i][j]

    }string+="\n"
}
console.log(string)
let sumd1=0
let sumd2=0
for (let i=0;i<3;i++){
    for (let j=0;j<3;j++){
        if (i==j){
            sumd1+=a[i][j]}
        if (i+j==3-1){
            sumd2+=a[i][j]
        }
        }
}
console.log(sumd1)
console.log(sumd2)
if (sumd1!=sumd2){
    let f=1
}else{
    for (let i=0;i<3;i++){
        sumr=0
        sumc=0

    for (let j=0;j<3;j++){
        sumr=sumr+a[i][j]
        sumc=sumc+a[j][i]
        if (sumr!=sumd1){
            f=1
        
        }else if (sumc!=sumd1){
            f=1
        }else{
            f=0
        }

    }
}
}if (f==0){
    console.log("this  is a magic squre")
}else{
    console.log("not magic squre")
}

























// let a=[[2,7,6],[9,5,1],[4,3,7]]
// string=""
// for (let i=0;i<3;i++){
//     for (let j=0;j<3;j++){
//         string+=a[i][j]

//     }string+="\n"
// }
// console.log(string)
// let sumd1=0
// let sumd2=0
// for (let i=0;i<3;i++){
//     for (let j=0;j<3;j++){
//         if (i==j){
//             sumd1+=a[i][j]}
//         if (i+j==3-1){
//             sumd2+=a[i][j]
//         }
//         }
// }
// console.log(sumd1)
// console.log(sumd2)
// if (sumd1!=sumd2){
//     let f=1
// }else{
//     for (let i=0;i<3;i++){
//         sumr=0
//         sumc=0

//     for (let j=0;j<3;j++){
//         sumr=sumr+a[i][j]
//         sumc=sumc+a[j][i]
//         if (sumr!=sumd1){
//             f=1
        
//         }else if (sumc!=sumd1){
//             f=1
//         }else{
//             f=0
//         }

//     }}
// }
// if (f==0){
//     console.log("this  is a magic squre")
// }else{
//     console.log("not magic squre")
// }



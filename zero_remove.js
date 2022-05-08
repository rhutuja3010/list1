// let a=[500,909,5506,300]
// let l=[]
// for (i of a){
//     let string=""
//     s=String(i)
//     for (j of s){
//         if (j!="0"){
//             string+=j
    
//         }
//     }
// l.push(Number(string))
// }
// console.log(l)


let a=[500,909,5506,300]
let l=[]
for (i of a){
    let string=""
    s=String(i)
    for (j of s){

        // console.log(j)
        string+=j
        string+="+"
        // console.log(string)
        l.push(Number(j))
        l.push("+")
        }
        // console.log(string)
        // console.log(j)
    // }
// l.push(Number(j))
}
console.log(l)





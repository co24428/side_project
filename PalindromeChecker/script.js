function checkPalindrome(){
    const textElem = document.getElementById("text-input");
    const text = preprocessing(textElem.value);
    if (text === ""){
        alert("Please input a value");
        return 0;
    }
    const lenOfText = text.length;
    const numberOfloop = Math.floor(lenOfText/2);
    let isPalindrome = true;
    const resultElem = document.getElementById("result");

    for (let i=0; i<numberOfloop; i++){
        if (text[i] === text[lenOfText - 1 - i]){
            isPalindrome = true;
        } else {
            isPalindrome = false;
            break;
        }
    }
    if (isPalindrome) {
        resultElem.innerText = `${text} is a palindrome`;
    } else {
        resultElem.innerText = `${text} is not a palindrome`;

    }
    textElem.value = "";
}
// TODO: Check punctuation: Check ASCII code...!
// _eye (A palindrome)
// A man, a plan, a canal. Panama (A palindrome)
// My age is 0, 0 si ega ym. (A palindrome)
// 0_0 (: /-\ :) 0-0 (A palindrome)
// five|\_/|four (Not a palindrome)
function preprocessing(str){
    // change to lowercase & remove black characters 
    return str.toLowerCase().split(' ').join('');
}

// document.addEventListener("DOMContentLoaded", (e)=>{

// })

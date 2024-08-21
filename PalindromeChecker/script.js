function checkPalindrome(){
    const textElem = document.getElementById("text-input");
    const text = preprocessing(textElem.value);
    const lenOfText = text.length;
    const numberOfloop = Math.floor(lenOfText/2);
    let isPalindrome = true;
    const resultElem = document.getElementsByClassName("result");

    for (let i=0; i<numberOfloop; i++){
        if (text[i] === text[lenOfText - 1 - i]){
            isPalindrome = true;
        } else {
            isPalindrome = false;
            break;
        }
    }
    resultElem[0].children[0].innerText = textElem.value;
    if (isPalindrome) {
        resultElem[0].children[1].innerText = "is a palindrome";
    } else {
        resultElem[0].children[1].innerText = "is not a palindrome";
    }
    textElem.value = "";
}

function preprocessing(str){
    // change to lowercase & remove black characters 
    return str.toLowerCase().split(' ').join('');
}

// document.addEventListener("DOMContentLoaded", (e)=>{

// })

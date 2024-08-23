function checkPalindrome(){
    const textElem = document.getElementById("text-input");
    const oriText = textElem.value;
    const text = preprocessing(oriText);
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
        resultElem.innerText = `${oriText} is a palindrome`;
    } else {
        resultElem.innerText = `${oriText} is not a palindrome`;

    }
    textElem.value = "";
}
// TODO: Check punctuation: 
// Check ASCII code: 0-9(48-57) & A-Z(65-90) & a-z(97-122)
// Regular Expression: regex
// _eye (A palindrome)
// A man, a plan, a canal. Panama (A palindrome)
// My age is 0, 0 si ega ym. (A palindrome)
// 0_0 (: /-\ :) 0-0 (A palindrome)
// five|\_/|four (Not a palindrome)
function preprocessing(str){
    let result;
    // change to alphanumeric
    result = str.replace(/[^a-z0-9]/gi, '');
    // change to lowercase
    result = result.toLowerCase();
    return result;
}

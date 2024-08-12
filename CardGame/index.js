const cardObjectDefinitions = [
    {id:1, imagePath:"./img/card-KingHearts.png"},
    {id:2, imagePath:"./img/card-JackClubs.png"},
    {id:3, imagePath:"./img/card-QueenDiamonds.png"},
    {id:4, imagePath:"./img/card-AceSpades.png"}
]
const cardBackImgPath = "./img/card-back-blue.png";

const cardContainerElem = document.querySelector(".card-container");

createCards();

function createCards(){
    cardObjectDefinitions.forEach((cardItem)=>{
        console.log(cardItem);
        createCard(cardItem);
    })
}

// create card html dinamically
function createCard(cardItem){
    // create div elements that make up a card
    const cardElem = document.createElement("div");
    const cardInnerElem = document.createElement("div");
    const cardFrontElem = document.createElement("div");
    const cardBackElem = document.createElement("div");

    // create front and back image elements for a card
    const cardFrontImg = createElement("img");
    const cardBackImg = createElement("img");

    // add class and id to card element
    addClassToElement(cardElem, "card");
    addIdToElement(cardElem, cardItem.id);

    // add class to inner card element
    addClassToElement(cardInnerElem, "card-inner");

    // add class to inner card element
    addClassToElement(cardFrontElem, "card-front");

    // add class to inner card element
    addClassToElement(cardBackElem, "card-back");

    // add src attribute and appropriate value to img element - back and front of card
    addSrcToImageElem(cardFrontImg, cardItem.imagePath);
    addSrcToImageElem(cardBackImg, cardBackImgPath);

    // assign class to image element of back and front of cards
    addClassToElement(cardFrontImg, "card-img");
    addClassToElement(cardBackImg, "card-img");

    // add back image element as child element to front and back card elements
    addChildElement(cardFrontElem, cardFrontImg);
    addChildElement(cardBackElem, cardBackImg);

    // add front and back cards element as child element to inner card element
    addChildElement(cardInnerElem, cardFrontElem);
    addChildElement(cardInnerElem, cardBackElem);

    // add inner card element as child element to card element
    addChildElement(cardElem, cardInnerElem);

    // add card element as child element to appropriate cell
    addCardToGridCell(cardElem)



}
function createElement(elemType){
    return document.createElement(elemType);
}
function addClassToElement(elem, className){
    elem.classList.add(className);
}
function addIdToElement(elem, id){
    elem.id = id;
}
function addSrcToImageElem(imgElem, src){
    imgElem.src = src;
}
function addChildElement(parentElem, childElem){
    parentElem.appendChild(childElem);
}

function addCardToGridCell(card){
    const cardPostionClassName = mapCardIdToGridCell(card);
    const cardPosElem = document.querySelector(cardPostionClassName);
    addChildElement(cardPosElem, card);
}
function mapCardIdToGridCell(card){
    if(card.id == 1){
        return ".card-pos-a"
    } else if(card.id == 2){
        return ".card-pos-b"
    } else if(card.id == 3){
        return ".card-pos-c"
    } else if(card.id == 4){
        return ".card-pos-d"
    }
}
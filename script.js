const words = ["PYTHON", "APPLE", "DREAM", "ENGINEER", "FOOTBALL"];

let word = "";
let guessed = [];
let lives = 6;

const wordBox = document.getElementById("word");
const message = document.getElementById("message");
const letters = document.getElementById("letters");
const livesBox = document.getElementById("lives");
const restart = document.getElementById("restart");

function startGame(){

word = words[Math.floor(Math.random()*words.length)];

guessed=[];

lives=6;

livesBox.innerText=lives;

message.innerText="Start Guessing...";

letters.innerHTML="";

displayWord();

createButtons();

}

function displayWord(){

let display="";

for(let letter of word){

if(guessed.includes(letter)){

display+=letter+" ";

}

else{

display+="_ ";

}

}

wordBox.innerText=display;

if(!display.includes("_")){

message.innerText="🎉 You Won!";

disableButtons();

}

}

function createButtons(){

for(let i=65;i<=90;i++){

const btn=document.createElement("button");

btn.innerText=String.fromCharCode(i);

btn.onclick=function(){

guess(btn.innerText);

btn.disabled=true;

};

letters.appendChild(btn);

}

}

function guess(letter){

if(word.includes(letter)){

guessed.push(letter);

}

else{

lives--;

livesBox.innerText=lives;

}

displayWord();

if(lives===0){

message.innerText="💀 Game Over! Word: "+word;

disableButtons();

}

}

function disableButtons(){

const all=document.querySelectorAll("#letters button");

all.forEach(btn=>btn.disabled=true);

}

restart.onclick=startGame;

startGame();
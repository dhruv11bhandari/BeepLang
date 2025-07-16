const morseDict = {
    'A': '.-',    'B': '-...',  'C': '-.-.',
    'D': '-..',   'E': '.',     'F': '..-.',
    'G': '--.',   'H': '....',  'I': '..',
    'J': '.---',  'K': '-.-',   'L': '.-..',
    'M': '--',    'N': '-.',    'O': '---',
    'P': '.--.',  'Q': '--.-',  'R': '.-.',
    'S': '...',   'T': '-',     'U': '..-',
    'V': '...-',  'W': '.--',   'X': '-..-',
    'Y': '-.--',  'Z': '--..',
    '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....',
    '7': '--...', '8': '---..', '9': '----.',
    '0': '-----', ' ': '/'
};

const inverseMorseDict = {};
for (let key in morseDict) {
    inverseMorseDict[morseDict[key]] = key;
}

function textToMorse() {
    const input = document.getElementById("inputText").value.toUpperCase();
    let result = "";
    for (let char of input) {
        if (morseDict[char]) {
            result += morseDict[char] + " ";
        } else {
            result += "? ";
        }
    }
    document.getElementById("outputText").value = result.trim();
}

function morseToText() {
    const input = document.getElementById("inputText").value.trim().split(" ");
    let result = "";
    for (let code of input) {
        if (inverseMorseDict[code]) {
            result += inverseMorseDict[code];
        } else if (code === "/") {
            result += " ";
        } else {
            result += "?";
        }
    }
    document.getElementById("outputText").value = result;
}
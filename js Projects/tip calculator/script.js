// Get global access to all inputs / divs here (you'll need them later 😘)
// bill input, tip input, number of people div, and per person total div
const billTotalInput = document.getElementById("billTotalInput")
const tipInput = document.getElementById("tipInput") // Corrected typo
const numberOfPeopleDiv = document.getElementById("numberOfPeople")
const perPersonTotalDiv = document.getElementById("perPersonTotal")

// Get number of people from number of people div
let numberOfPeople = Number(numberOfPeopleDiv.innerText) // Corrected number to Number
console.log(numberOfPeople)

// ** Calculate the total bill per person **
const calculateBill = () => {
    
    // get bill from user input & convert it into a number
    let bill = Number(billTotalInput.value) // Corrected number to Number
    
    // get the tip from user & convert it into a percentage (divide by 100)
    let tip = Number(tipInput.value) / 100 // Corrected number to Number
    
    // get the total tip amount
    let totalTip = bill * tip
    
    // calculate the total (tip amount + bill)
    let totalBill = totalTip + bill
    
    // calculate the per person total (total divided by number of people)
    let perPersonTotal = totalBill / numberOfPeople
  
    // update the perPersonTotal on DOM & show it to user
    perPersonTotalDiv.innerText = "$" + perPersonTotal.toFixed(2)
}

// ** Splits the bill between more people **
const increasePeople = () => {
    // increment the amount of people
    numberOfPeople += 1
  
    // update the DOM with the new number of people
    numberOfPeopleDiv.innerText = numberOfPeople
    
    // calculate the bill based on the new number of people
    calculateBill()
}

// ** Splits the bill between fewer people **
const decreasePeople = () => {
    // guard clause
    // if amount is 1 or less simply return
    // (a.k.a you can't decrease the number of people to 0 or negative!)
    if (numberOfPeople <= 1) {
        return
    } else {
        numberOfPeople -= 1
    }
  
    // update the DOM with the new number of people
    numberOfPeopleDiv.innerText = numberOfPeople
  
    // calculate the bill based on the new number of people
    calculateBill()
}

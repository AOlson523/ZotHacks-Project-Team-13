// Get the value of the name input from the form and update the greeting

// const greetingText = document.querySelector("#greeting");                   // get greeting element
// const inputElement = document.querySelector("#exampleFormControlInput1");   // get input element
// const btn = document.querySelector("#exampleFormBtn");                      // get the element with id = 'exampleFormBtn'
// btn.addEventListener('click', function() {                                  // add an event to the button: whenever the button is pressed, update the greeting name
//     greetingText.innerHTML = `Hello, ${inputElement.value}`;                // this is a templated string in Javscript! https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Template_literals 
// });

let club_category = 'math';

function gotclicked(type, button) {
    // let userInput = document.getElementById('input1').value;
    if (button.classList.contains('selected-button')) {
        button.classList.remove("selected-button")
    } else {
        button.classList.add("selected-button")

    }
    club_category = type;
    // alert(type)
    // }
    // function submit(type){
    // let userInput = document.getElementById('input1').value;

    // send user selection to backend, category
    document.getElementById('dispaly').innerHTML = '<h1 class="text">this is answer</h1>result, cub1, club2, club2';
}
var options = {
    valueNames: [ 'name', 'born' ],
    // Since there are no elements in the list, this will be used as template.
    item: '<li><h3 class="name"></h3><p class="born"></p></li>'
  };
  
  var values = [
    {
      name: 'Jonny Strömberg',
      born: 1986
    },
    {
      name: 'Jonas Arnklint',
      born: 1985
    },
    {
      name: 'Martina Elm',
      born: 1986
    }
  ];
  
  var userList = new List('body', options, values);
  
  userList.add({
    name: 'Gustaf Lindqvist',
    born: 1983
  });
  
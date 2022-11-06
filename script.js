// Get the value of the name input from the form and update the greeting

// const greetingText = document.querySelector("#greeting");                   // get greeting element
// const inputElement = document.querySelector("#exampleFormControlInput1");   // get input element
// const btn = document.querySelector("#exampleFormBtn");                      // get the element with id = 'exampleFormBtn'
// btn.addEventListener('click', function() {                                  // add an event to the button: whenever the button is pressed, update the greeting name
//     greetingText.innerHTML = `Hello, ${inputElement.value}`;                // this is a templated string in Javscript! https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Template_literals 
// });

let club_category = 'math';
filters = [];



var options = {
    // Since there are no elements in the list, this will be used as template.
    item: function (itemvalues) {
        if (itemvalues.bio == null) {
            itemvalues.bio = ''
        }
        return  `<li><h3 class="name"><a href="${itemvalues.website}">${itemvalues.name}</a></h3><p class="bio">${itemvalues.bio}</p></li>`
    }
  };
  
  var values = data;
  
var club_list = new List('body', options, values);

function filter_function(){
    club_list.filter(function(item) {
        if (item.values()['sub_type'] != null)
        {
            for (let i = 0; i < item.values()['sub_type'].length; i++)
            {
                if (filters.includes(item.values()['sub_type'][i]))
                {
                    return true
                }
            }
        }
        
        if (filters.includes(item.values()['main_type'])) {
           return true;
        } 
        else if (filters.length == 0)
        {
            return true;
        }
        else
        {
            return false;
        }
        });
}

function gotclicked(type, button) {
    if (button.classList.contains('selected-button')) {
        button.classList.remove("selected-button")
        filters = filters.filter(function(item){
            if (item != type)
            {
                return true;
            }
            else
            {
                return false;
            }
        })
        filter_function();

    } else {
        button.classList.add("selected-button")
        filters.push(type);
        filter_function();
    }
    club_category = type;

}
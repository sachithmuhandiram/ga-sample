function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

const csrftoken = getCookie('csrftoken');

document.addEventListener('DOMContentLoaded', function () {
    const myForm = document.getElementById('course_code');
    
    // Example: Add event listener to form
    myForm.addEventListener('change', function(event) {
        //event.preventDefault();
        const newCourseCode = event.target.value;
        if (newCourseCode.length > 0) {
            const parentForm = document.getElementById("dynamic-obj");
            // new form
            if (parentForm === null) {
                fetchACourse(newCourseCode);      
            } else {
                removeEarlierDynamic();
                fetchACourse(newCourseCode);
            }
        } // selected a new course code
                    // Add your dynamic functionality here
    });
});

function fetchACourse(newCourseCode) {
    
    fetch('get_course_meta_data', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': csrftoken // Include the CSRF token in the headers
                },
                body: JSON.stringify(newCourseCode)
            })
            .then(response => {
                if (!response.ok) {
                    throw new Error('Network response was not ok ' + response.statusText);
                }

                return response.json();
            })
            .then(data => { // function call with data 
                    console.log("data: ", data)
                    createActivityElement(data);
                })
            .catch(error => {
                console.error('Fetch error:', error);
            });
}

function createActivityElement(activity) {
   /*
    Need to get data from db for groups. and then dynamically load text area for groups box
   */
    var formDiv = document.createElement('div');
    formDiv.classList.add("form-group row");
    formDiv.id = "dynamic-obj"

    console.log("activity: ", activity)
    for (activity_name in activity) {

        // check whether activity has groups
        // python route to get groups
        
        var label = document.createElement('label');
        label.for = activity[activity_name];
        label.innerHTML = activity[activity_name];
        label.classList.add("col-sm-2 col-form-label");        
        formDiv.appendChild(label);
        
        var inputDiv = document.createElement('div');
        inputDiv.classList.add("col-sm-4");

        var input = document.createElement('input');
        input.type = "text";
        input.name = activity[activity_name];
        input.classList.add("form-control");
        input.value = "";
        inputDiv.appendChild(input);

        var br = document.createElement("br");
        formDiv.appendChild(inputDiv);
   
    }

    var parent_form = document.getElementById("define_course_activities");
    parent_form.appendChild(formDiv);
}

function removeEarlierDynamic() {
    const parentForm = document.getElementById("dynamic-obj");
    if (parentForm.value !== "") {
            document.getElementById("dynamic-obj").remove();

    }
}
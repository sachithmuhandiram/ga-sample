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
                    createActivityElement(data);
                })
            .catch(error => {
                console.error('Fetch error:', error);
            });
}

function createActivityElement(activity) {
   
    var formDiv = document.createElement('div');
    formDiv.classList.add("form-group");
    formDiv.id = "dynamic-obj"
    const secondSelect = document.createElement('select');
    secondSelect.classList.add("form-control");
    secondSelect.id = "test";
    formDiv.appendChild(secondSelect);

    var parent_form = document.getElementById("define_course_activities");
    parent_form.appendChild(formDiv);
}

function removeEarlierDynamic() {
    const parentForm = document.getElementById("dynamic-obj");
    if (parentForm.value !== "") {
        console.log("here")

            document.getElementById("dynamic-obj").remove();

    }
}
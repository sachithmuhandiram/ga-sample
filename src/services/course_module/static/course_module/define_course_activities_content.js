

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
    myForm.addEventListener('change', function (event) {
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

function fetchGroups(activity) {
    fetch('get_course_activity_has_group', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken // Include the CSRF token in the headers
        },
        body: JSON.stringify(activity)
    })
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok ' + response.statusText);
            }
            return response.json();
        })
        .then(data => {
            // Process the data received from the API
            console.log("Groups data: ", data);
            return data;

        })
        .catch(error => {
            console.error('Fetch error:', error);
        });
}

function createActivityElement(activity) {
    var formDiv = document.createElement('div');
    formDiv.classList.add("form-group");
    formDiv.id = "dynamic-obj";

    console.log("activity: ", activity);

    for (activity_name in activity) {
        var label = document.createElement('label');
        label.htmlFor = activity[activity_name];
        label.innerHTML = activity[activity_name];
        label.classList.add("col-form-label");
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

    var parentForm = document.getElementById("define_course_activities");
    parentForm.appendChild(formDiv);
}

function removeEarlierDynamic() {
    const parentForm = document.getElementById("dynamic-obj");
    if (parentForm.value !== "") {
        document.getElementById("dynamic-obj").remove();

    }
}
document.addEventListener('DOMContentLoaded', function() {
    const myForm = document.getElementById('course_code');
    
    // Example: Add event listener to form
    myForm.addEventListener('change', function(event) {
        event.preventDefault();
        const newCourseCode = event.target.value;
        if (newCourseCode.length > 0) {
            fetch(`get_course_meta_data?course_code=${encodeURIComponent(newCourseCode)}`, {
                method: 'GET',
                headers: {
                    'Content-Type': 'application/json'
                }
            })
                .then(response => {
                    if (!response.ok) {
                        throw new Error('Network response was not ok ' + response.statusText);
                    }
                    console.log("Data here");
                    return response.json();
                })
                .then(data => console.log(data))
                .catch(error => console.error('Error:', error));
                    }
                    // Add your dynamic functionality here
    });
});

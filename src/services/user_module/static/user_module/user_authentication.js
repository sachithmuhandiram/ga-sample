async function authenticateUser(event) {
    event.preventDefault(); // Prevent form from submitting normally

    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;
    const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;

    const response = await fetch('authenticate_user', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken
        },
        body: JSON.stringify({
            username: username,
            password: password,

        })
    });

    const data = await response.json();
    if (response.status === 200) {
        alert(data.message); // Authentication successful
        // Redirect to a new page or perform other actions
    } else if (response.status === 401) {
        warningBanner.style.display = 'block'; // Show the warning banner
        warningBanner.textContent = data.message;
    }
    else {
        alert(data.message); // Authentication failed
    }
}
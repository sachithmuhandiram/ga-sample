async function authenticateUser(event) {
    event.preventDefault(); // Prevent form from submitting normally

    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;
    const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
    const warningBanner = document.getElementById('warning-banner');

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

    // const responseText = await response.json();
    // console.log(responseText);

    try {
        if (response.status === 200) {
            // Authentication successful
            // Redirect to a new page or perform other actions
            warningBanner.style.display = 'none'; // Hide the warning banner
            console.log("User authenticated");
            window.location.href = '/user_module/home';
        } else if (response.status === 401) {
            // Authentication failed
            warningBanner.style.display = 'block'; // Show the warning banner
            warningBanner.textContent = 'Username / Password do not match. Please try again.';
        }
    } catch (error) {
        console.error('Error parsing JSON:', error);
        warningBanner.style.display = 'block'; // Show the warning banner
        warningBanner.textContent = 'Username / Password do not match. Please try again Error.';
    }
}
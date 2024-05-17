//import connectToMongoDB from './mongo_db.js';

async function searchForARecord(user_name) {
    try {
        // Connect to the database
        const db = await connectToMongoDB();

        // Perform database operations
        const collection = db.collection('sample_course');
        const result = await collection.findOne({ keyName: user_name });

        if (result) {
            console.log('Found document:', result);
        } else {
            console.log('No document found');
        }

        // Close the connection
        db.client.close();
    } catch (error) {
        console.error('Error occurred while performing database operation:', error);
    }
}

// Here we can not go for => function, as this has limited area of accesss
document.getElementById("submit_btn").addEventListener("click", function (e) {

    //alert("Hello");
    e.preventDefault();  
    const username = document.getElementById('exampleInputName').value;
    console.log(username)
    fetch(`/user_module/api/items/${username}/`)
        .then(response => response.json())
        .then(data => {
            const passwords = data.map(item => item.password);
            console.log(passwords[0])
        })
    .catch(error => console.error('Error:', error));

});


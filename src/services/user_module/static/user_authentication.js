import connectToMongoDB from './mongo_db.js';

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

   let userName = document.getElementById("exampleInputName").value;

    let password = searchForARecord(user_name);
    console.log(password);

});


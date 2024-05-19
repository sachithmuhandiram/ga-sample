import { MongoClient } from 'mongodb';
const url = 'mongodb://localhost:27017';
const dbName = 'sample_db';

// Function to establish a connection to MongoDB and return the database object
async function connectToMongoDB() {
    try {
        const client = new MongoClient(url, { useNewUrlParser: true, useUnifiedTopology: true });

        await client.connect();

        console.log('Connected successfully to server');
        
        return client.db(dbName);
    } catch (error) {
        console.error('Error occurred while connecting to MongoDB:', error);
        throw error; 
    }
}

export default connectToMongoDB;
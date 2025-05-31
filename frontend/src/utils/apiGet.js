import axios from 'axios';

const apiGet = axios.create({
    baseURL: 'http://127.0.0.1:8000',
});

export const fetchData = async () => {
    try {
        const response = await apiGet.get('/documents/1/generate_questions/');
        return response.data;
    }catch (error){
        console.log("Error fetching the data:", error);
    }
};
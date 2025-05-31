import axios from 'axios';

const apiGet = axios.create({
    baseURL: 'http://localhost:8000',
});

export const fetchData = async () => {
    try {
        const response = await apiGet.get('/chat/invoke/');
        return response.data;
    }catch (error){
        console.log("Error fetching the data:", error);
    }
};


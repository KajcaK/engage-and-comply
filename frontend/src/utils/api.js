import axios from 'axios';

const api = axios.create({
    baseURL: '', //add URL
});

export const fetchData = async () => {
    try {
        const response = await api.get('/REALURL'); //add URL
        return response.data;
    }catch (error){
        console.log("Error fetching the data:", error);
    }
};
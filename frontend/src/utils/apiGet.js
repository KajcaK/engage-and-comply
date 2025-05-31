import axios from 'axios';

const apiGet = axios.create({
    baseURL: '', //add URL
});

export const fetchData = async () => {
    try {
        const response = await apiGet.get('/REALURL'); //add URL
        return response.data;
    }catch (error){
        console.log("Error fetching the data:", error);
    }
};
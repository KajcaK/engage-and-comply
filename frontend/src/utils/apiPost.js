import axios from 'axios';

export const apiPost = axios.create({
    baseURL: 'http://localhost:8000/chat/invoke', //add URL
});

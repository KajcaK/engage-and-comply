import {useEffect, useState} from "react";
import {Card} from "react-bootstrap";
import axios from "axios";

const apiGet = axios.create({
    baseURL: 'http://localhost:8000',
});

export const fetchData = async () => {
    try {
        const response = await apiGet.get('/chat/invoke/');
        return response.data;
    } catch (error) {
        console.log('Error fetching the data:', error);
        return null;
    }
};

const ChatContainer = () => {
    const [inputValue, setInputValue] = useState("");
    const [inputMessage, setInputMessage] = useState("");
    const [responseData, setResponseData] = useState(null);

    const handleInputChange = (e) => {
        setInputValue(e.target.value);
    }

    useEffect(() => {
        const getData = async () => {
            const data = await fetchData();
            setResponseData(data);
        };

        getData();
    }, []);

    const handleSubmit = () => {
        console.log('Input value submitted:', inputValue);

        fetch('http://localhost:8000/chat/invoke', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            mode: 'no-cors',
            body: JSON.stringify({
                "input": {
                    "input": inputValue,
                    "history": []
                },
                "config": {
                    "configurable": {
                        "session_id": "user-session-001"
                    }
                }
            })
        })
            .then(response => response.json())
            .then(data => {
                console.log('Response for backend:', data);
            })
            .catch(error => {
                console.error('Error:', error);
            });
        setInputMessage(inputValue);
        setInputValue("");
    }

    const handleKeyDown = (e) => {
        if (e.key === "Enter") {
            handleSubmit();
        }
    }

    return (
        <div
            className="content-container d-flex flex-column justify-content-between content-wrapper overflow-scroll p-3">
            <div className="card w-100 h-100 mb-4 bg-transparent border-0 p-0">
                <div className="card-body p-0">
                    <div style={{
                        display: 'flex',
                        flexDirection: 'column',
                        gap: '1rem',
                        padding: '1rem',
                        height: '100%'
                    }}>

                        {/* Output */}
                        {responseData ? (
                            <div className="message-left-wrapper">
                                <Card className="message-left">
                                    <Card.Body style={{ background: '#d9d9d9' }}>
                                        {responseData.output}
                                    </Card.Body>
                                </Card>
                            </div>
                        ) : (
                            <p>Loading...</p>
                        )}

                        {/* Input */}
                        <div className="message-right-wrapper">
                            <Card className="message-right">
                                <Card.Body style={{background: 'rgba(128, 182, 99, 0.6)'}}>
                                    {inputMessage}
                                </Card.Body>
                            </Card>
                        </div>

                        <div className="loading-next-message">
                            <p>A.C.E. is typing...</p>
                        </div>

                    </div>
                </div>
            </div>
            <div className="d-flex">
                <input
                    type="text"
                    value={inputValue}
                    onChange={handleInputChange}
                    onKeyDown={handleKeyDown}
                    placeholder="Type your message here"
                    className="form-control glow-input"
                ></input>
                <button className="btn btn-dark btn-lg glow-button ms-2"
                        onClick={handleSubmit}
                >
                    Send
                </button>
            </div>
        </div>
    );
};

export default ChatContainer;
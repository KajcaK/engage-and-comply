import {useEffect, useState} from "react";
import {Card} from "react-bootstrap";

const ChatContainer = () => {
    const [inputValue, setInputValue] = useState("");
    const [responseData, setResponseData] = useState(null);

    const handleInputChange = (e) => {
        setInputValue(e.target.value);
    }

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
            .then(data => (setResponseData)(data.output.result))
            .catch(error => {
                console.log('Error:', error)
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
        <div className="content-container d-flex flex-column justify-content-between content-wrapper overflow-scroll">
            <div className="card w-100 h-100 mb-4">
                <div className="card-body">
                    <p>{responseData}</p>
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
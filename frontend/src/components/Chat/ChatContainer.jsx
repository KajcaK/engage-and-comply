import {useState} from "react";

const ChatContainer = () => {
    const [inputValue, setInputValue] = useState("");

    const handleInputChange = (e) => {
        setInputValue(e.target.value);
    }

    const handleSubmit = () => {
        console.log('Input value submitted:', inputValue);

        fetch('', { // API endpoint
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            mode: 'cors',
            body: JSON.stringify(inputValue.trim()) //If API expects JSON => JSON.stringify({ link: inputLink })
        })
            .then(response => response.json())
            .then(data => {
                console.log('Response from backend:', data);
            })
            .catch(error => {
                console.error('Error:', error);
            });

        setInputValue("");
    }

    const handleKeyDown = (e) => {
        if (e.key === "Enter") {
            handleSubmit();
        }
    }

    return (
        <div className="content-container d-flex flex-column justify-content-between content-wrapper">
            <div className="card w-100 h-100 mb-4">
                <div className="card-body">

                </div>
            </div>
            <div className="d-flex">
                <input
                       type="text"
                       value={inputValue}
                       onChange={handleInputChange}
                       onKeyDown={handleKeyDown}
                       placeholder="Type your message here"
                       className="form-control"
                ></input>
                <button className="btn btn-dark btn-lg ms-2"
                        onClick={handleSubmit}
                >
                    Send</button>
            </div>
        </div>
    );
};

export default ChatContainer;
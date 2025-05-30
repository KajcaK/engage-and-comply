import {useState} from "react";

const ChatContainer = () => {
    const [inputValue, setInputValue] = useState("");

    const handleInputChange = (e) => {
        setInputValue(e.target.value);
    }

    const handleSubmit = () => {
        setInputValue(inputValue);
        console.log('Input value submitted:', inputValue);
        setInputValue("");
    }

    const handleKeyDown = (e) => {
        if (e.key === "Enter") {
            handleSubmit();
        }
    }


    return (
        <div className="content-container d-flex flex-column justify-content-between">
            <div className="card w-100 h-100 mb-4">
                <div className="card-body">

                </div>
            </div>
            <div className="d-flex">
                <textarea
                       value={inputValue}
                       onChange={handleInputChange}
                       onKeyDown={handleKeyDown}
                       placeholder="Type here"
                       className="form-control"
                       rows="2"
                ></textarea>
                <button className="btn btn-dark btn-lg ms-2"
                        onClick={handleSubmit}
                >
                    Send</button>
            </div>
        </div>
    );
};

export default ChatContainer;
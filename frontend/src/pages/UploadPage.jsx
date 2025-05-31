import {useState} from "react";

const UploadPage = () => {
    const [inputLink, setInputLink] = useState("");

    const handleInputChange = (e) => {
        setInputLink(e.target.value);
    }

    const handleSubmit = () => {
        console.log('URL submited:', inputLink);

        fetch('', { // API endpoint
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            mode: 'cors',
            body: JSON.stringify(inputLink) //If API expects JSON => JSON.stringify({ link: inputLink })
        })
            .then(response => response.json())
            .then(data => {
                console.log('Response from backend:', data);
            })
            .catch(error => {
                console.error('Error:', error);
            });

        setInputLink("");
    }

    const handleKeyDown = (e) => {
        if (e.key === "Enter") {
            handleSubmit();
        }
    }

    return (
        <div className="d-flex flex-column justify-content-center align-items-center p-3">
            <div className="content-wrapper upload-content align-content-center">
                <div className="row text-center mb-5">
                    <h1 className="upload-title">Upload Link</h1>
                </div>
                <div className="row">
                    <div className="d-flex">
                        <input
                            type="url"
                            value={inputLink}
                            onChange={handleInputChange}
                            onKeyDown={handleKeyDown}
                            placeholder="Enter URL to file here"
                            className="form-control">
                        </input>
                        <button className="btn btn-dark btn-lg ms-2"
                                onClick={handleSubmit}
                        >
                            Submit
                        </button>
                    </div>
                </div>
            </div>
        </div>
    );
};

export default UploadPage
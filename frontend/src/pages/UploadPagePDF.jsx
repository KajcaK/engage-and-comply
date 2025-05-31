import {Button, Form} from "react-bootstrap";
import {useState} from "react";
import {apiPost} from "../utils/apiPost.js";

const UploadPagePDF = () => {

    const [selectedFile, setSelectedFile] = useState(null);

    const handleFileChange = (event) => {
        setSelectedFile(event.target.files[0]);

        const file = event.target.files[0];

        if (file) {
            const fileName = file.name;
            const extension = fileName.split('.').pop().toLowerCase();

            if (extension !== 'pdf') {
                alert('Please select a PDF file only.');
                event.target.value = null;
                return;
            }

            console.log('Valid file selected:', file);
        }
    };

    const handleUpload = async () => {
        if (!selectedFile) {
            alert("Please select a file first.");
            return;
        }

        const formData = new FormData();
        formData.append("file", selectedFile);
        console.log(formData)

        try {
            const response = await apiPost.post('/REALURL', formData);
            console.log('Success:', response.data);
        } catch (error) {
            console.error('Error uploading file:', error);
        }
    };

    return (
        <div className="d-flex flex-column justify-content-center align-items-center p-3 mt-5">
            <div className="content-wrapper upload-content align-content-center mt-5">
                <div className="row text-center mb-5">
                    <h1 className="upload-title">Upload File</h1>
                </div>
                <div className="row">
                    <Form.Group controlId="formFile" className="mb-3 ">
                        <Form.Label column={"sm"} className="text-light">Select PDF file</Form.Label>
                        <Form.Control
                            size="lg"
                            type="file"
                            required
                            onChange={handleFileChange}
                            className="glow-input"
                        />
                    </Form.Group>
                    <Button className="btn-dark mt-2 btn-lg glow-button" onClick={handleUpload}>Upload</Button>
                </div>
            </div>
        </div>
    );
};

export default UploadPagePDF
import NavBar from "../components/UI/NavBar.jsx";
import {Route, Routes} from "react-router";
import ChatPage from "../pages/ChatPage.jsx";
import UploadPageLink from "../pages/UploadPageLink.jsx";
import UploadPagePDF from "../pages/UploadPagePDF.jsx";

const AppLayout = () => (
    <div className="container-fluid m-0 p-0 vh-100">
        <div className="d-flex flex-column">
            <NavBar/>
            <div className="flex-grow-1">
                <Routes>
                    <Route path="/" element={<ChatPage />} />
                    <Route path="/upload-link" element={<UploadPageLink />} />
                    <Route path="/upload-pdf" element={<UploadPagePDF />} />
                </Routes>
            </div>
        </div>
    </div>
);

export default AppLayout;
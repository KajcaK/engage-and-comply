import StoryContainer from "../components/StoryContainer.jsx";
import ChatContainer from "../components/ChatContainer.jsx";

const AppLayout = () => (
    <div className="d-flex min-vh-100 bg-light justify-content-evenly align-items-center p-3 app-layout">
        <StoryContainer/>
        <ChatContainer/>
    </div>
);

export default AppLayout;
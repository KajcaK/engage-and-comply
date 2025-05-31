import StoryContainer from "../components/Chat/StoryContainer.jsx";
import ChatContainer from "../components/Chat/ChatContainer.jsx";

const ChatPage = () => (
    <div className="d-flex flex-column flex-lg-row justify-content-evenly align-items-center p-3 chat-wrapper overflow-hidden">
        <StoryContainer/>
        <ChatContainer/>
    </div>
);

export default ChatPage
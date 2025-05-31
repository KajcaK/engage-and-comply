import {useEffect, useState} from "react";

const StoryContainer = () => {

    const [input, setInput] = useState(null);

    useEffect(() => {
        fetch('/testQuestions.json')
            .then(response => response.json())
            .then(data => setInput(data.questions))
            .catch(error => console.error('Error loading JSON:', error));
    }, []);
    console.log(input)

    if (!input || !input.question || !input.answer) return <p>Loading...</p>;

    const questions = (
        <div>
            <p className="ms-2">{input.question}</p>
            <hr/>
            <ul>
                {input.answer
                    .split('\n')
                    .filter(line => line.trim() !== '')
                    .map((line, index) => (
                        <li className="mt-2" key={index}>{line}</li>
                    ))}
            </ul>
        </div>
    );
    console.log(input.answer)

    return (
        <div className="content-container content-wrapper overflow-scroll">
            <div className="card ">
                <div className="card-body ">
                    <div className="card-text text-center">
                        <div className="text-start">
                            {questions}
                        </div>
                    </div>
                </div>
            </div>
        </div>
    );
};

export default StoryContainer;
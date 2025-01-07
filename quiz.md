---
layout: post
title: Flocker Social Media Site
permalink: /quiz
menu: nav/home.html
---
<!DOCTYPE html>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>10-Question Quiz: Find Your Perfect Vacation</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            padding: 20px;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
        }
        .quiz-container {
            background-color: white;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            width: 100%;
            max-width: 600px;
        }
        .question {
            font-size: 18px;
            margin-bottom: 15px;
        }
        .options {
            list-style: none;
            padding: 0;
            margin-bottom: 20px;
        }
        .options li {
            margin: 10px 0;
        }
        .options input {
            margin-right: 10px;
        }
        button {
            background-color: #4CAF50;
            color: white;
            padding: 10px 15px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            display: block;
            width: 100%;
        }
        button:hover {
            background-color: #45a049;
        }
        .result {
            font-size: 20px;
            font-weight: bold;
            color: #333;
            display: none;
            text-align: center;
        }
    </style>
</head>
<body>
    <div class="quiz-container">
        <div id="quiz-content">
            <div class="question" id="question">Question text will go here</div>
            <ul class="options" id="options"></ul>
            <button id="next-button">Next</button>
        </div>
        <div class="result" id="result">
            <p>Your perfect vacation destination is:</p>
            <p id="destination"></p>
        </div>
    </div>


    <script>
        // Quiz Questions
        const quizQuestions = [
            { question: "What climate do you prefer?", options: ["Tropical", "Cold", "Moderate"] },
            { question: "What's your ideal activity?", options: ["Adventure", "Relaxation", "Culture", "Nature"] },
            { question: "What's your travel budget?", options: ["Low", "Medium", "High"] },
            { question: "Do you prefer solo travel or group travel?", options: ["Solo", "Group"] },
            { question: "What’s your preferred cuisine?", options: ["Seafood", "Street Food", "Fine Dining", "Vegetarian"] },
            { question: "Do you like visiting cities or rural areas?", options: ["Cities", "Rural"] },
            { question: "Do you enjoy water activities?", options: ["Yes", "No"] },
            { question: "How important is shopping for you?", options: ["Very Important", "Not Important"] },
            { question: "Do you enjoy wildlife and safaris?", options: ["Yes", "No"] },
            { question: "How long would you like your vacation to last?", options: ["A Weekend", "A Week", "Two Weeks", "A Month"] }
        ];


        // Current question index
        let currentQuestionIndex = 0;
        let answers = []; // Store user answers


        // DOM Elements
        const questionElement = document.getElementById("question");
        const optionsElement = document.getElementById("options");
        const nextButton = document.getElementById("next-button");
        const resultElement = document.getElementById("result");
        const destinationElement = document.getElementById("destination");


        // Load a question
        function loadQuestion() {
            // Clear previous options
            optionsElement.innerHTML = "";


            // Get current question
            const currentQuestion = quizQuestions[currentQuestionIndex];
            questionElement.textContent = currentQuestion.question;


            // Add options to the UI
            currentQuestion.options.forEach((option, index) => {
                const li = document.createElement("li");
                li.innerHTML = `<input type="radio" name="option" value="${option}" id="option${index}">
                                <label for="option${index}">${option}</label>`;
                optionsElement.appendChild(li);
            });
        }


        // Go to the next question
        nextButton.addEventListener("click", () => {
            // Get the selected answer
            const selectedOption = document.querySelector('input[name="option"]:checked');
            if (!selectedOption) {
                alert("Please select an option!");
                return;
            }


            // Store the selected answer
            answers.push(selectedOption.value);


            // Move to the next question
            currentQuestionIndex++;


            // Check if we've reached the end of the quiz
            if (currentQuestionIndex < quizQuestions.length) {
                loadQuestion();
            } else {
                showResult();
            }
        });


        // Show the final result
        function showResult() {
            // Hide the quiz content
            document.getElementById("quiz-content").style.display = "none";


            // Determine a result (simple logic for now)
            if (answers.includes("Tropical") && answers.includes("Relaxation")) {
                destinationElement.textContent = "Bali, Indonesia - Beaches, sunshine, and affordable luxury!";
            } else if (answers.includes("Cold") && answers.includes("Adventure")) {
                destinationElement.textContent = "Switzerland - Ski resorts and beautiful alpine views!";
            } else if (answers.includes("Moderate") && answers.includes("Culture")) {
                destinationElement.textContent = "Italy - Rich history, art, and delicious food!";
            } else if (answers.includes("Nature") && answers.includes("Wildlife")) {
                destinationElement.textContent = "South Africa - Stunning safaris and natural parks!";
            } else {
                destinationElement.textContent = "Your dream destination is waiting! Explore the world!";
            }


            // Show the result
            resultElement.style.display = "block";
        }


        // Load the first question
        loadQuestion();
    </script>

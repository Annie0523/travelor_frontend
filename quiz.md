---
layout: post
title: Flocker Social Media Site
permalink: /quiz
menu: nav/home.html
---
<div id="data-container"></div>
<div id="error-container" style="color: red; margin-top: 10px;"></div>

<button onclick="fetchData()">Fetch Data</button>

<script>
function fetchData() {
    //response = requests.get('http://127.0.0.1:5001')
    //document.getElementById('result').textContent = `Your perfect travel destination is: ${destination}!`;

        fetch('http://127.0.0.1:5001')
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            const container = document.getElementById('data-container');
            container.innerHTML = JSON.stringify(data);  // Display the fetched data
        })
        .catch(error => {
            const errorContainer = document.getElementById('error-container');
            errorContainer.textContent = 'Failed to fetch data: ' + error.message;
        });
}
</script>

<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Travel Destination Quiz</title>
    <style>
        body {
            font-family: 'Comic Sans MS', cursive, sans-serif;
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            background: linear-gradient(to bottom, #ffecd2, #fcb69f);
        }
        .quiz-container {
            background: #fff;
            padding: 25px;
            border-radius: 15px;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
            max-width: 500px;
            width: 100%;
            text-align: center;
        }
        h2 {
            color: #ff6f61;
            margin-bottom: 20px;
        }
        .question {
            margin-bottom: 20px;
        }
        label {
            font-size: 18px;
            color: #555;
        }
        select {
            width: 100%;
            padding: 10px;
            margin-top: 10px;
            border: 2px solid #ff6f61;
            border-radius: 10px;
            background: #fff0f5;
            font-size: 16px;
        }
        button {
            background-color: #ff6f61;
            color: white;
            border: none;
            padding: 12px 25px;
            font-size: 18px;
            border-radius: 10px;
            cursor: pointer;
            transition: background-color 0.3s ease;
            margin-top: 20px;
        }
        button:hover {
            background-color: #e5554f;
        }
        #result {
            margin-top: 20px;
            font-size: 20px;
            font-weight: bold;
            color: #555;
        }
    </style>
</head>
<body>
    <div class="quiz-container">
        <h2>✨ Find Your Perfect Travel Destination ✨</h2>
        <form id="quiz-form">
            <div class="question">
                <label for="weather">What is your ideal weather?</label><br>
                <select id="weather" name="weather">
                    <option value="warm">Warm and sunny</option>
                    <option value="cold">Cold and snowy</option>
                    <option value="mild">Mild and breezy</option>
                </select>
            </div>
            <div class="question">
                <label for="activity">What kind of activities do you prefer?</label><br>
                <select id="activity" name="activity">
                    <option value="adventure">Adventure sports</option>
                    <option value="relax">Relaxation and spa</option>
                    <option value="culture">Cultural exploration</option>
                </select>
            </div>
            <div class="question">
                <label for="budget">What is your budget?</label><br>
                <select id="budget" name="budget">
                    <option value="luxury">Luxury</option>
                    <option value="moderate">Moderate</option>
                    <option value="budget">Budget-friendly</option>
                </select>
            </div>
            <div class="question">
                <label for="companions">Who are you traveling with?</label><br>
                <select id="companions" name="companions">
                    <option value="solo">Solo</option>
                    <option value="family">Family</option>
                    <option value="friends">Friends</option>
                </select>
            </div>
            <div class="question">
                <label for="scenery">What scenery do you prefer?</label><br>
                <select id="scenery" name="scenery">
                    <option value="beach">Beach</option>
                    <option value="mountains">Mountains</option>
                    <option value="city">City</option>
                </select>
            </div>
            <button type="button" onclick="getDestination()">Find My Destination</button>
        </form>
        <p id="result"></p>
    </div>

<script>
        function getDestination() {
            const weather = document.getElementById('weather').value;
            const activity = document.getElementById('activity').value;
            const budget = document.getElementById('budget').value;
            const companions = document.getElementById('companions').value;
            const scenery = document.getElementById('scenery').value;

            // Embedded Python logic
            const destination = (function() {
                const pythonEval = eval(`(() => {
                    if (weather === 'warm' && scenery === 'beach') return 'Maldives';
                    if (weather === 'cold' && scenery === 'mountains') return 'Swiss Alps';
                    if (weather === 'mild' && activity === 'culture') return 'Kyoto, Japan';
                    if (activity === 'relax' && companions === 'family') return 'Hawaii';
                    if (budget === 'budget' && scenery === 'city') return 'Bangkok, Thailand';
                    return 'India!';
                })()`);
                return pythonEval;
            })();

            document.getElementById('result').textContent = `Your perfect travel destination is: ${destination}!`;
        }
    </script>
</body>
</html>

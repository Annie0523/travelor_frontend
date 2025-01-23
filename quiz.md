---
layout: post
title: Flocker Social Media Site
permalink: /quiz
menu: nav/home.html
---


<!-- Quiz Container -->
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
        <button type="button" id="findDestinationButton">Find My Destination</button>  
    </form>
    <p id="result"></p>
</div>


<div id="data-container" style="margin-top: 20px;"></div>
<div id="error-container" style="color: red; margin-top: 10px;"></div>
<button id="fetchButton" style="margin-top: 20px;">Get More Info About This Destination!</button>


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
    label {
        font-size: 18px;
        color: #555;
    }
    select, button {
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
        cursor: pointer;
        transition: background-color 0.3s ease;
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


<script>
    document.addEventListener('DOMContentLoaded', () => {
        // Function to fetch data for a destination
        async function fetchData(destination) {
            const container = document.getElementById('data-container');
            const errorContainer = document.getElementById('error-container');
            const apiLinks = {
                Maldives: 'http://127.0.0.1:8887/api/destinations/maldives',
                Cancun: 'http://127.0.0.1:8887/api/destinations/cancun',
                Japan: 'http://127.0.0.1:8887/api/destinations/japan',
                Hawaii: 'http://127.0.0.1:8887/api/destinations/hawaii',
            };


            try {
                const response = await fetch(apiLinks[destination]);
                if (!response.ok) {
                    throw new Error(`Error: ${response.status}`);
                }
                const data = await response.json();
                container.innerHTML = `Place: ${data.name}<br>Climate: ${data.Climate}<br>Description: ${data.Description}`;
                errorContainer.textContent = '';
            } catch (error) {
                errorContainer.textContent = `Failed to fetch data: ${error.message}`;
            }
        }


        // Function to determine the travel destination
        function findDestination() {
            const weather = document.getElementById('weather').value;
            const activity = document.getElementById('activity').value;
            const budget = document.getElementById('budget').value;
            const companions = document.getElementById('companions').value;
            const scenery = document.getElementById('scenery').value;


            const destinations = [];


            if (weather === 'warm' && scenery === 'beach') {
                destinations.push('Maldives');
            }
            if (weather === 'warm' && activity === 'adventure') {
                destinations.push('Cancun');
            }
            if (weather === 'mild' && activity === 'culture') {
                destinations.push('Japan');
            }
            if (weather === 'warm' && activity === 'relax') {
                destinations.push('Hawaii');
            }


            // Randomly select a destination from the matched options
            const destination = destinations.length
                ? destinations[Math.floor(Math.random() * destinations.length)]
                : 'Maldives'; // Default fallback


            document.getElementById('result').textContent = `Your perfect travel destination is: ${destination}!`;
            return destination;
        }


        // Add event listeners
        document.getElementById('findDestinationButton').addEventListener('click', () => {
            const selectedDestination = findDestination();
            fetchData(selectedDestination);
        });
    });
</script>
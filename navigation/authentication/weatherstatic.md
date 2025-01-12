---
layout: post
title: Weatherstatic
permalink: /weatherstatic
menu: nav/home.html
search_exclude: true
---

<style>
    #weather-data {
        display: none;
        position: absolute;
        background-color: #fff;
        border: 1px solid #ccc;
        padding: 10px;
        border-radius: 8px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
        z-index: 1000;
    }
    button {
        background-color: #4CAF50; /* Green */
        border: none;
        color: white;
        padding: 10px 20px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 14px;
        margin: 4px 2px;
        cursor: pointer;
        border-radius: 12px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
        transition: background-color 0.3s ease;
    }

    button:hover {
        background-color: #45a049;
    }

    #button-container {
        display: flex;
        flex-wrap: wrap;
        gap: 10px;
    }
</style>

<h1>Weather Information</h1>
<div id="button-container">
    <button id="sandiego-btn">San Diego</button>
    <button id="tokyo-btn">Tokyo</button>
    <button id="mumbai-btn">Mumbai</button>
    <button id="cairo-btn">Cairo</button>
    <button id="lagos-btn">Lagos</button>
    <button id="london-btn">London</button>
    <button id="paris-btn">Paris</button>
    <button id="newyorkcity-btn">New York City</button>
    <button id="mexicocity-btn">Mexico City</button>
    <button id="saopaulo-btn">Sao Paulo</button>
    <button id="buenosaires-btn">Buenos Aires</button>
</div>
<div id="weather-data"></div>

<script>
    /**
     * Fetch data from the backend API and display it.
     * 
     * @param {string} apiURL - The API endpoint to fetch data from.
     * @param {Event} event - The button click event for positioning the result.
     */
    async function fetchWeatherData(apiURL, event) {
        try {
            const response = await fetch(apiURL);

            if (response.ok) {
                const data = await response.json();

                // Display the data in the page
                const weatherDataDiv = document.getElementById('weather-data');
                weatherDataDiv.innerHTML = `
                    <h2>${data.name}</h2>
                    <p><strong>Temperature:</strong> ${data.temperature}°C</p>
                    <p><strong>Feels Like:</strong> ${data.feelslike}°C</p>
                    <p><strong>Humidity:</strong> ${data.humidity}%</p>
                    <p><strong>Pressure:</strong> ${data.pressure} hPa</p>
                    <p><strong>Wind Speed:</strong> ${data.windspeed} km/h</p>
                    <p><strong>Wind Direction:</strong> ${data.winddirection}</p>
                `;

                // Position the div under the clicked button
                const buttonRect = event.target.getBoundingClientRect();
                weatherDataDiv.style.position = 'absolute';
                weatherDataDiv.style.top = `${buttonRect.bottom + window.scrollY}px`;
                weatherDataDiv.style.left = `${buttonRect.left + window.scrollX}px`;
                weatherDataDiv.style.display = 'block'; // Make sure the div is visible
            } else {
                document.getElementById('weather-data').innerText = 
                    `Error: Could not fetch data (Status: ${response.status})`;
            }
        } catch (error) {
            document.getElementById('weather-data').innerText = `Error: ${error.message}`;
        }
    }

    // Add event listeners to the buttons
    const locations = [
        { id: 'sandiego-btn', url: 'http://127.0.0.1:5000/api/cities/sandiego' },
        { id: 'tokyo-btn', url: 'http://127.0.0.1:5000/api/cities/tokyo' },
        { id: 'mumbai-btn', url: 'http://127.0.0.1:5000/api/cities/mumbai' },
        { id: 'cairo-btn', url: 'http://127.0.0.1:5000/api/cities/cairo' },
        { id: 'lagos-btn', url: 'http://127.0.0.1:5000/api/cities/lagos' },
        { id: 'london-btn', url: 'http://127.0.0.1:5000/api/cities/london' },
        { id: 'paris-btn', url: 'http://127.0.0.1:5000/api/cities/paris' },
        { id: 'newyorkcity-btn', url: 'http://127.0.0.1:5000/api/cities/newyorkcity' },
        { id: 'mexicocity-btn', url: 'http://127.0.0.1:5000/api/cities/mexicocity' },
        { id: 'saopaulo-btn', url: 'http://127.0.0.1:5000/api/cities/saopaulo' },
        { id: 'buenosaires-btn', url: 'http://127.0.0.1:5000/api/cities/buenosaires' },
    ];

    locations.forEach(location => {
        document.getElementById(location.id).addEventListener('click', (event) => {
            fetchWeatherData(location.url, event);
        });
    });
</script>

---
layout: post
title: Landscapes
permalink: /landscape
menu: nav/home.html
search_exclude: true
---
<style>
        #landscape-data {
            display: none;
            position: absolute;
            background-color: #fff;
            border: 1px solid #ccc;
            padding: 10px;
            border-radius: 8px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
            z-index: 1000;
        }
    </style>

<button id="greatwall-btn">Show Great Wall Info</button>
<button id="deathvalley-btn">Show Death Valley Info</button>
<button id="zhangjiajie-btn">Show Zhang Jia Jie Info</button>
<div id="landscape-data"></div>

<script>
        /**
         * Fetch data from the backend API and display it.
         * 
         * @param {string} apiURL - The API endpoint to fetch data from.
         * @param {Event} event - The button click event for positioning the result.
         */
        async function fetchLandscapeData(apiURL, event) {
            try {
                const response = await fetch(apiURL);

                if (response.ok) {
                    const data = await response.json();

                    // Display the data in the page
                    const landscapeDataDiv = document.getElementById('landscape-data');
                    landscapeDataDiv.innerHTML = `
                        <h2>${data.name}</h2>
                        <p><strong>Location:</strong> ${data.location}</p>
                        <p><strong>Introduction:</strong> ${data.Introduction}</p>
                    `;

                    // Position the div under the clicked button
                    const buttonRect = event.target.getBoundingClientRect();
                    landscapeDataDiv.style.position = 'absolute';
                    landscapeDataDiv.style.top = `${buttonRect.bottom + window.scrollY}px`;
                    landscapeDataDiv.style.left = `${buttonRect.left + window.scrollX}px`;
                    landscapeDataDiv.style.display = 'block'; // Make sure the div is visible
                } else {
                    document.getElementById('landscape-data').innerText = 
                        `Error: Could not fetch data (Status: ${response.status})`;
                }
            } catch (error) {
                document.getElementById('landscape-data').innerText = `Error: ${error.message}`;
            }
        }

        // Add event listeners to the buttons
        document.getElementById('greatwall-btn').addEventListener('click', (event) => {
            fetchLandscapeData('http://127.0.0.1:8887/api/landscape/greatwall', event);
        });

        document.getElementById('deathvalley-btn').addEventListener('click', (event) => {
            fetchLandscapeData('http://127.0.0.1:8887/api/landscape/deathvalley', event);
        });
        document.getElementById('zhangjiajie-btn').addEventListener('click', (event) => {
            fetchLandscapeData('http://127.0.0.1:8887/api/landscape/zhangjiajie', event);
        });
    </script>
---
layout: post
title: Landscapes
permalink: /landscape
menu: nav/home.html
search_exclude: true
---
<style>
        .container {
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
            background-color: #fff;
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        }
        .landscape-item {
            margin-bottom: 20px;
        }
        .landscape-item h2 {
            margin: 0;
            color: #333;
        }
        .landscape-item p {
            margin: 5px 0;
        }
    </style>

<div class="container">
        <h1>Landscape Info Display</h1>
        <table id="demo" class="table">
            <thead>
                <tr>
                    <th>Name</th>
                    <th>Country</th>
                    <th>City</th>
                    <th>Description</th>
                </tr>
            </thead>
            <tbody id="result">
                <!-- JavaScript generated data -->
            </tbody>
        </table>
    </div>

<script>
        async function fetchLandscapes() {
            try {
                const response = await fetch('http://127.0.0.1:8887//api/landscapes'); 
                if (!response.ok) {
                    throw new Error('Failed to fetch landscapes: ' + response.statusText);
                }
                const landscapeData = await response.json();
                displayLandscapes(landscapeData);
            } catch (error) {
                console.error('Error fetching landscapes:', error);
            }
        }

        function displayLandscapes(landscapeData) {
            const resultContainer = document.getElementById('result');
            resultContainer.innerHTML = ''; // Clear previous content

         landscapeData.forEach(landscape => {
                const tr = document.createElement('tr');
                const name = document.createElement('td');
                const country = document.createElement('td');
                const city = document.createElement('td');
                const description = document.createElement('td');
                name.innerHTML = landscape.name; 
                country.innerHTML = landscape.country; 
                city.innerHTML = landscape.city; 
                description.innerHTML = landscape.description; 
                tr.appendChild(name);
                tr.appendChild(country);
                tr.appendChild(city);
                tr.appendChild(description);
                resultContainer.appendChild(tr);
            });
        }

        // Fetch and display landscapes when the page loads
        fetchLandscapes();
    </script>

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
        form {
            display: flex;
            flex-direction: column;
        }
        label, input, textarea, button {
            margin-bottom: 10px;
        }
        input, textarea {
            padding: 10px;
            border: 1px solid #ccc;
            border-radius: 5px;
            width: 100%;
            box-sizing: border-box;
        }
        button {
            background-color: #4CAF50;
            color: white;
            padding: 10px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            transition: background-color 0.3s ease;
        }
        button:hover {
            background-color: #45a049;
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

<script type="module">
    import config from './config.js';

    const pythonURI = config.API_BASE_URL;

    window.fetchLandscapes = async function() {
        try {
            const response = await fetch(`${pythonURI}/api/landscapes`);
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
    window.fetchLandscapes();
</script>

<div class="container">
        <h1>Add New Landscape</h1>
        <form id="landscapeForm">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required>
        <label for="country">Country:</label>
        <input type="text" id="country" name="country" required>
        <label for="city">City:</label>
        <input type="text" id="city" name="city" required>
        <label for="description">Description:</label>
        <textarea id="description" name="description" required></textarea>
        <button type="submit">Add Landscape</button>
        </form>
    </div>

<script>
        document.getElementById('landscapeForm').addEventListener('submit', async function(event) {
            event.preventDefault();

            const formData = {
                name: document.getElementById('name').value,
                country: document.getElementById('country').value,
                city: document.getElementById('city').value,
                description: document.getElementById('description').value
            };

            try {
                const response = await fetch(`${pythonURI}/api/landscapes`, {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify(formData)
                });

                if (response.ok) {
                    alert('Landscape added successfully!');
                    document.getElementById('landscapeForm').reset();
                } else {
                    alert('Failed to add landscape.');
                }
            } catch (error) {
                console.error('Error:', error);
                alert('An error occurred while adding the landscape.');
            }
        });
    </script>

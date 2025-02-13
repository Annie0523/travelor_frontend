---
layout: post
title: Recommended Vacation Spots!
permalink: /vacations
menu: nav/home.html
search_exclude: true
---

<style>
    body {
        font-family: 'Comic Sans MS', cursive, sans-serif;
        margin: 0;
        padding: 0;
        background-color: #ffe4e1; /* Light pinkish background for a cute vibe */
        color: #333;
    }

    .container {
        max-width: 1200px;
        margin: 20px auto;
        padding: 20px;
    }

    .earth-icon {
        width: 50px;
        height: 50px;
        background-color: #4CAF50; /* Green like the Earth */
        border-radius: 50%;
        margin: 0 auto 20px auto;
        display: flex;
        align-items: center;
        justify-content: center;
        color: white;
        font-size: 24px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    }

    .earth-icon::before {
        content: "🌍"; /* Earth emoji for a cute touch */
    }

    h1 {
        text-align: center;
        margin-bottom: 20px;
        color: #4CAF50;
    }

    .vacation-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
        gap: 20px;
    }

    .vacation-card {
        background-color: #fff;
        border-radius: 15px;
        box-shadow: 0 6px 12px rgba(0, 0, 0, 0.1);
        overflow: hidden;
        transition: transform 0.3s, box-shadow 0.3s;
        padding: 15px;
        text-align: center;
    }

    .vacation-card:hover {
        transform: scale(1.05);
        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
    }

    .vacation-card h2 {
        margin: 10px 0;
        padding: 10px;
        background-color: #87CEFA; /* Soft blue background */
        color: white;
        border-radius: 10px;
    }

    .vacation-card p {
        margin: 5px 0;
        font-size: 16px;
        color: #555;
    }

    .form-container {
        margin-top: 40px;
        padding: 20px;
        background-color: #fff;
        border-radius: 15px;
        box-shadow: 0 6px 12px rgba(0, 0, 0, 0.1);
    }

    form {
        display: grid;
        grid-template-columns: 1fr;
        gap: 15px;
    }

    label {
        font-weight: bold;
        font-size: 16px;
        color: #4CAF50;
    }

    input, textarea, button {
        padding: 10px;
        border: 2px solid #ccc;
        border-radius: 10px;
        font-size: 16px;
    }

    button {
        background-color: #FF69B4; /* Hot pink for a playful vibe */
        color: white;
        border: none;
        cursor: pointer;
        font-weight: bold;
        transition: all 0.3s ease;
    }

    button:hover {
        background-color: #FF1493; /* Darker pink for hover */
    }
</style>

<div class="container">
    <div class="earth-icon"></div>
    <h1>Explore Our Recommended Vacation Spots!</h1>
    <div class="vacation-grid" id="vacationGrid">
        <!-- JavaScript generated vacation cards -->
    </div>

    <div class="form-container">
        <h2>Add a New Vacation Spot</h2>
        <form id="vacationForm">
            <label for="name">Name:</label>
            <input type="text" id="name" name="name" required>
            <label for="climate">Climate:</label>
            <input type="text" id="climate" name="climate" required>
            <label for="country">Country:</label>
            <input type="text" id="country" name="country" required>
            <button type="submit">Add Vacation</button>
        </form>
    </div>
</div>

<script type="module">
    import {pythonURI, fetchOptions } from '{{site.baseurl}}/assets/js/api/config.js'
    const URL = pythonURI;
    async function fetchVacations() {
        try {
            const response = await fetch(`${URL}/api/vacations`, fetchOptions)
            if (!response.ok) {
                throw new Error('Failed to fetch vacations: ' + response.statusText);
            }
            const vacationData = await response.json();
            displayVacations(vacationData);
        } catch (error) {
            console.error('Error fetching vacations:', error);
        }
    }
    function displayVacations(vacations) {
        const vacationGrid = document.getElementById('vacationGrid');
        vacationGrid.innerHTML = '';
        vacations.forEach(vacation => {
            const card = document.createElement('div');
            card.className = 'vacation-card';
            card.innerHTML = `
                <h2>${vacation.name}</h2>
                <p><strong>Climate:</strong> ${vacation.climate}</p>
                <p><strong>Country:</strong> ${vacation.country}</p>
            `;
            vacationGrid.appendChild(card);
        });
    }
    document.getElementById('vacationForm').addEventListener('submit', async function(event) {
        event.preventDefault();
        const name = document.getElementById('name').value;
        const climate = document.getElementById('climate').value;
        const country = document.getElementById('country').value;
        try {
            const response = await fetch(`${URL}/api/vacations`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ name, climate, country })
            });
            if (!response.ok) {
                throw new Error('Failed to add vacation');
            }
            alert('Vacation added successfully!');
            document.getElementById('vacationForm').reset();
            fetchVacations();
        } catch (error) {
            console.error('Error:', error);
            alert('An error occurred while adding the vacation.');
        }
    });
    fetchVacations();
</script>



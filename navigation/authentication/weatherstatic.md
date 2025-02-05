---
layout: post
title: Weather Static
permalink: /weatherstatic
menu: nav/home.html
search_exclude: true
---
<!-- 
  Full updated frontend code for "Weather Static" page.
  Adds:
    - A Delete button for each row in the table.
    - Unit-append buttons ("°C", "%", "hPa") for temperature, feelslike, humidity, pressure.
-->

<style>
  /* Basic styling for the tabs and content */
  .tabs {
    margin-bottom: 10px;
  }
  .tab {
    display: inline-block;
    padding: 10px 15px;
    margin-right: 5px;
    background-color: #eee;
    cursor: pointer;
    border-radius: 4px 4px 0 0;
  }
  .tab.active {
    background-color: #ccc;
    font-weight: bold;
  }
  .content-section {
    border: 1px solid #ccc;
    border-top: none;
    padding: 15px;
    max-width: 800px; /* a bit wider to accommodate the table + form */
    margin-bottom: 30px;
  }
  .city-content {
    display: none;
  }
  .city-content.active {
    display: block;
  }

  /* Table styling */
  table {
    border-collapse: collapse;
    width: 100%;
    margin-top: 10px;
  }
  th, td {
    padding: 8px 12px;
    border: 1px solid #ccc;
    text-align: left;
  }
  th {
    background-color: #f5f5f5;
  }
  .delete-btn {
    cursor: pointer;
    padding: 4px 8px;
    color: #fff;
    background-color: #d9534f;
    border: none;
    border-radius: 4px;
  }

  /* Form styling */
  .weather-form {
    margin-top: 20px;
    border: 1px solid #ccc;
    padding: 15px;
  }
  .weather-form h3 {
    margin-top: 0;
  }
  .weather-form label {
    display: block;
    margin: 10px 0 5px;
  }
  .weather-form input[type="text"] {
    width: 70%;
    padding: 6px;
    margin-right: 6px;
    margin-bottom: 10px;
  }
  .weather-form button {
    padding: 6px 10px;
    cursor: pointer;
    margin-bottom: 10px;
  }
  .small-btn {
    padding: 6px;
    margin-right: 6px;
    background-color: #ccc;
    border: none;
    border-radius: 4px;
    cursor: pointer;
  }
</style>

<div id="weatherApp">
  <h1>Weather Data</h1>

  <!-- TABBED VIEW -->
  <div class="tabs" id="tabs"></div>
  <div class="content-section" id="contentSection"></div>

  <!-- DATA TABLE -->
  <div class="content-section" id="tableSection">
    <h2>All Weather Records</h2>
    <table id="weatherTable">
      <thead>
        <tr>
          <th>ID</th>
          <th>Name</th>
          <th>Temp</th>
          <th>Feels Like</th>
          <th>Humidity</th>
          <th>Pressure</th>
          <th>Wind Speed</th>
          <th>Wind Dir</th>
          <th>Actions</th>
        </tr>
      </thead>
      <tbody></tbody>
    </table>
  </div>

  <!-- NEW WEATHER FORM -->
  <div class="weather-form" id="weatherFormSection">
    <h3>Add New Weather</h3>

  <label for="w-name">City Name:</label>
    <input type="text" id="w-name" placeholder="e.g. Chicago" />

  <label for="w-temperature">Temperature:</label>
    <div>
      <input type="text" id="w-temperature" placeholder="e.g. 20°C" />
      <button class="small-btn" id="tempUnitBtn">°C</button>
    </div>

  <label for="w-feelslike">Feels Like:</label>
    <div>
      <input type="text" id="w-feelslike" placeholder="e.g. 19°C" />
      <button class="small-btn" id="feelsUnitBtn">°C</button>
    </div>

  <label for="w-humidity">Humidity:</label>
    <div>
      <input type="text" id="w-humidity" placeholder="e.g. 55%" />
      <button class="small-btn" id="humidUnitBtn">%</button>
    </div>

  <label for="w-pressure">Pressure:</label>
    <div>
      <input type="text" id="w-pressure" placeholder="e.g. 1012 hPa" />
      <button class="small-btn" id="pressureUnitBtn">hPa</button>
    </div>

  <label for="w-windspeed">Wind Speed:</label>
    <input type="text" id="w-windspeed" placeholder="e.g. 3.6 m/s" />

  <label for="w-winddirection">Wind Direction:</label>
    <input type="text" id="w-winddirection" placeholder="e.g. 300°" />

  <button id="addWeatherBtn">Add Weather</button>
  </div>
</div>

<script>
  // 1. Define pythonURI exactly as in your first script
  const pythonURI = (() => {
    if (location.hostname === "localhost") {
      return "http://localhost:8887";
    } else if (location.hostname === "127.0.0.1") {
      return "http://127.0.0.1:8887";
    } else {
      return "https://flask2025.nighthawkcodingsociety.com";
    }
  })();

  // We'll keep all data in memory:
  let allWeatherData = [];

  // ------------------ ON LOAD ------------------
  fetchDataFromBackend();

  // 2. FETCH DATA (adjust to use pythonURI)
  function fetchDataFromBackend() {
    fetch(`${pythonURI}/api/weathers`)
      .then((response) => {
        if (!response.ok) {
          throw new Error("Error fetching weather data");
        }
        return response.json();
      })
      .then((data) => {
        allWeatherData = data;
        createTabs(data);
        buildWeatherTable(data);
      })
      .catch((error) => {
        console.error("Error fetching weather data:", error);
      });
  }

  // 3. CREATE TABS
  function createTabs(weatherArray) {
    const tabsContainer = document.getElementById("tabs");
    const contentSection = document.getElementById("contentSection");

    // Clear old content
    tabsContainer.innerHTML = "";
    contentSection.innerHTML = "";

    let firstTab = true;

    weatherArray.forEach((weather) => {
      // Create the clickable tab
      const tabButton = document.createElement("div");
      tabButton.className = "tab";
      tabButton.textContent = weather.name;
      tabsContainer.appendChild(tabButton);

      // Create the city content div
      const cityContent = document.createElement("div");
      cityContent.className = "city-content";
      cityContent.innerHTML = `
        <h2>${weather.name}</h2>
        <p><strong>Temperature:</strong> ${weather.temperature}</p>
        <p><strong>Feels Like:</strong> ${weather.feelslike}</p>
        <p><strong>Humidity:</strong> ${weather.humidity}</p>
        <p><strong>Pressure:</strong> ${weather.pressure}</p>
        <p><strong>Wind Speed:</strong> ${weather.windspeed}</p>
        <p><strong>Wind Direction:</strong> ${weather.winddirection}</p>
      `;
      contentSection.appendChild(cityContent);

      // Activate the first tab by default
      if (firstTab) {
        tabButton.classList.add("active");
        cityContent.classList.add("active");
        firstTab = false;
      }

      // Tab click event
      tabButton.addEventListener("click", () => {
        document
          .querySelectorAll(".tab")
          .forEach((t) => t.classList.remove("active"));
        document
          .querySelectorAll(".city-content")
          .forEach((c) => c.classList.remove("active"));

        tabButton.classList.add("active");
        cityContent.classList.add("active");
      });
    });
  }

  // 4. BUILD TABLE
  function buildWeatherTable(weatherArray) {
    const tableBody = document.querySelector("#weatherTable tbody");
    tableBody.innerHTML = ""; // Clear old rows

    weatherArray.forEach((weather) => {
      const tr = document.createElement("tr");
      tr.innerHTML = `
        <td>${weather.id}</td>
        <td>${weather.name}</td>
        <td>${weather.temperature}</td>
        <td>${weather.feelslike}</td>
        <td>${weather.humidity}</td>
        <td>${weather.pressure}</td>
        <td>${weather.windspeed}</td>
        <td>${weather.winddirection}</td>
        <td>
          <button class="delete-btn" data-id="${weather.id}">Delete</button>
        </td>
      `;
      tableBody.appendChild(tr);
    });

    // Attach event listeners to each delete button
    const deleteButtons = tableBody.querySelectorAll(".delete-btn");
    deleteButtons.forEach((btn) => {
      btn.addEventListener("click", () => {
        const id = btn.getAttribute("data-id");
        deleteWeather(id);
      });
    });
  }

  // 5. ADD NEW WEATHER (replace API_URL with pythonURI)
  const addWeatherBtn = document.getElementById("addWeatherBtn");
  addWeatherBtn.addEventListener("click", addWeather);

  function addWeather() {
    const name = document.getElementById("w-name").value.trim();
    const temperature = document.getElementById("w-temperature").value.trim();
    const feelslike = document.getElementById("w-feelslike").value.trim();
    const humidity = document.getElementById("w-humidity").value.trim();
    const pressure = document.getElementById("w-pressure").value.trim();
    const windspeed = document.getElementById("w-windspeed").value.trim();
    const winddirection = document
      .getElementById("w-winddirection")
      .value.trim();

    if (
      !name ||
      !temperature ||
      !feelslike ||
      !humidity ||
      !pressure ||
      !windspeed ||
      !winddirection
    ) {
      alert("Please fill out all fields.");
      return;
    }

    const requestBody = {
      name,
      temperature,
      feelslike,
      humidity,
      pressure,
      windspeed,
      winddirection,
    };

    fetch(`${pythonURI}/api/weathers`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(requestBody),
    })
      .then((response) => {
        if (!response.ok) {
          throw new Error("Error adding weather data");
        }
        return response.json();
      })
      .then((newWeather) => {
        alert(`Weather for '${newWeather.name}' added successfully!`);

        // Clear form
        document.getElementById("w-name").value = "";
        document.getElementById("w-temperature").value = "";
        document.getElementById("w-feelslike").value = "";
        document.getElementById("w-humidity").value = "";
        document.getElementById("w-pressure").value = "";
        document.getElementById("w-windspeed").value = "";
        document.getElementById("w-winddirection").value = "";

        // Refresh data
        fetchDataFromBackend();
      })
      .catch((error) => {
        console.error("Error adding weather data:", error);
        alert("Failed to add weather. Check console for details.");
      });
  }

  // 6. DELETE WEATHER (replace API_URL with pythonURI)
  function deleteWeather(id) {
    if (!confirm("Are you sure you want to delete this record?")) {
      return;
    }
    fetch(`${pythonURI}/api/weathers`, {
      method: "DELETE",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ id: Number(id) }),
    })
      .then((response) => {
        if (!response.ok) {
          throw new Error("Error deleting weather data");
        }
        return response.json();
      })
      .then((result) => {
        alert(result.message || result);
        // Re-fetch data
        fetchDataFromBackend();
      })
      .catch((error) => {
        console.error("Error deleting:", error);
        alert("Failed to delete. Check console for details.");
      });
  }

  // 7. UPDATE WEATHER
    function updateWeather(weatherId) {
    const newName = prompt("Enter new city name:");
    const newTemperature = prompt("Enter new temperature:");
    const newFeelsLike = prompt("Enter new feels-like temperature:");
    const newHumidity = prompt("Enter new humidity:");
    const newPressure = prompt("Enter new pressure:");
    const newWindSpeed = prompt("Enter new wind speed:");
    const newWindDirection = prompt("Enter new wind direction:");

    if (newName && newTemperature && newFeelsLike && newHumidity && newPressure && newWindSpeed && newWindDirection) {
        fetch(`http://127.0.0.1:8887/api/weathers/${weatherId}`, {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                name: newName,
                temperature: newTemperature,
                feelslike: newFeelsLike,
                humidity: newHumidity,
                pressure: newPressure,
                windspeed: newWindSpeed,
                winddirection: newWindDirection
            })
        })
        .then(response => response.json())
        .then(data => {
            const resultContainer = document.getElementById('resultContainer');
            if (data) {
                resultContainer.innerHTML = `<p>Weather updated successfully: ${data.name}, ${data.temperature}°C</p>`;
                document.getElementById('getAllWeatherButton').click(); // Refresh the weather list
            }
        })
        .catch(error => {
            const resultContainer = document.getElementById('resultContainer');
            resultContainer.innerHTML = `<p>Error updating weather: ${error.message}</p>`;
        });
    }
  }
  
  // 8. APPEND UNITS
  document
    .getElementById("tempUnitBtn")
    .addEventListener("click", () => appendUnit("w-temperature", "°C"));
  document
    .getElementById("feelsUnitBtn")
    .addEventListener("click", () => appendUnit("w-feelslike", "°C"));
  document
    .getElementById("humidUnitBtn")
    .addEventListener("click", () => appendUnit("w-humidity", "%"));
  document
    .getElementById("pressureUnitBtn")
    .addEventListener("click", () => appendUnit("w-pressure", "hPa"));

  function appendUnit(inputId, unit) {
    const input = document.getElementById(inputId);
    if (!input.value) {
      // If empty, just add the unit
      input.value = unit;
    } else if (!input.value.includes(unit)) {
      // If doesn't already contain the unit
      // add a space + the unit
      input.value += (input.value.endsWith(" ") ? "" : " ") + unit;
    }
  }
</script>

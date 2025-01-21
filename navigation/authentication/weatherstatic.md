---
layout: post
title: Weatherstatic
permalink: /weatherstatic
menu: nav/home.html
search_exclude: true
---

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
    max-width: 400px;
  }
  .city-content {
    display: none;
  }
  .city-content.active {
    display: block;
  }
</style>

<div id="weatherApp">
  <h1>Weather Data</h1>
  <div class="tabs" id="tabs"></div>
  <div class="content-section" id="contentSection"></div>
</div>

<script>
// Change the URL if your backend runs on a different address
const API_URL = "http://127.0.0.1:8887/weather";

fetch(API_URL)
  .then((response) => response.json())
  .then((data) => {
    createTabs(data);
  })
  .catch((error) => {
    console.error("Error fetching weather data:", error);
  });

function createTabs(weatherData) {
  const tabsContainer = document.getElementById("tabs");
  const contentSection = document.getElementById("contentSection");
  let firstTab = true;

  // For each city in the weather data
  Object.keys(weatherData).forEach((cityKey) => {
    const cityInfo = weatherData[cityKey];

    // Create the clickable tab
    const tabButton = document.createElement("div");
    tabButton.className = "tab";
    tabButton.textContent = cityInfo.name;
    tabsContainer.appendChild(tabButton);

    // Create the city content div
    const cityContent = document.createElement("div");
    cityContent.className = "city-content";
    cityContent.innerHTML = `
      <h2>${cityInfo.name}</h2>
      <p><strong>Temperature:</strong> ${cityInfo.temperature}</p>
      <p><strong>Feels Like:</strong> ${cityInfo.feelslike}</p>
      <p><strong>Humidity:</strong> ${cityInfo.humidity}</p>
      <p><strong>Pressure:</strong> ${cityInfo.pressure}</p>
      <p><strong>Wind Speed:</strong> ${cityInfo.windspeed}</p>
      <p><strong>Wind Direction:</strong> ${cityInfo.winddirection}</p>
    `;
    contentSection.appendChild(cityContent);

    // Activate the first tab by default
    if (firstTab) {
      tabButton.classList.add("active");
      cityContent.classList.add("active");
      firstTab = false;
    }

    // When the tab is clicked, show the corresponding city content
    tabButton.addEventListener("click", () => {
      document.querySelectorAll(".tab").forEach((t) => t.classList.remove("active"));
      document.querySelectorAll(".city-content").forEach((c) => c.classList.remove("active"));

      tabButton.classList.add("active");
      cityContent.classList.add("active");
    });
  });
}
</script>
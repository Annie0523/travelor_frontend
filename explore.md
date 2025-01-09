---
layout: post
title: Explore
search_exclude: true
description: A map to explore
hide: true
permalink: /explore
menu: nav/home.html
---

<html lang="en">
<head>
  <meta charset="UTF-8"/>
  <title>Good Cities to Travel to around the world (Leaflet + OSM)</title>
  <link rel="stylesheet" href="https://unpkg.com/leaflet/dist/leaflet.css" />

  <style>
    html, body {
      margin: 0;
      padding: 0;
      height: 100%;
      font-family: Arial, sans-serif;
    }
    #container {
      display: flex;
      height: 100vh;
      width: 100%;
    }
    #map {
      flex: 3;
      height: 100%;
    }
    #sidebar {
      flex: 1;
      padding: 20px;
      box-sizing: border-box;
      overflow-y: auto;
      background-color: #f5f5f5;
      border-left: 1px solid #ccc;
    }
    #filter-section {
      margin-bottom: 20px;
    }
    .wonder-checkbox {
      margin: 5px 0;
      display: block;
    }
    .filter-label {
      display: block;
      font-weight: bold;
      margin: 10px 0 5px;
    }
    select, input[type="text"] {
      width: 100%;
      margin-bottom: 10px;
      padding: 5px;
    }
    #info {
      border: 1px solid #ccc;
      padding: 10px;
      background-color: #fff;
      margin-top: 20px;
    }
    #selected-location {
      margin-top: 10px;
      font-weight: bold;
    }
  </style>
</head>
<body>

<div id="container">
  <!-- The Map -->
  <div id="map"></div>

  <!-- The Sidebar / Filter Options -->
  <div id="sidebar">
    <h2>Filters</h2>

  <!-- ================== FILTERS ================== -->
  <!-- The Cities Filter -->
  <div id="filter-section">
      <div class="filter-label">Cities</div>
      <label class="wonder-checkbox">
        <input type="checkbox" class="wonder-option" value="tokyo" checked/> Tokyo
      </label>
      <label class="wonder-checkbox">
        <input type="checkbox" class="wonder-option" value="mumbai" checked/> Mumbai
      </label>
      <label class="wonder-checkbox">
        <input type="checkbox" class="wonder-option" value="cairo" checked/> Cairo
      </label>
      <label class="wonder-checkbox">
        <input type="checkbox" class="wonder-option" value="lagos" checked/> Lagos
      </label>
      <label class="wonder-checkbox">
        <input type="checkbox" class="wonder-option" value="london" checked/> London
      </label>
      <label class="wonder-checkbox">
        <input type="checkbox" class="wonder-option" value="paris" checked/> Paris
      </label>
      <label class="wonder-checkbox">
        <input type="checkbox" class="wonder-option" value="new_york_city" checked/> New York City
      </label>
      <label class="wonder-checkbox">
        <input type="checkbox" class="wonder-option" value="mexico_city" checked/> Mexico City
      </label>
      <label class="wonder-checkbox">
        <input type="checkbox" class="wonder-option" value="sao_paulo" checked/> Salo Paulo
      </label>
      <label class="wonder-checkbox">
        <input type="checkbox" class="wonder-option" value="buenos_aires" checked/> Buenos Aires
      </label>
    </div>

  <!-- Category Filter -->
  <div id="filter-section">
      <div class="filter-label">Category</div>
      <select id="category-filter">
        <option value="">--Select Category--</option>
        <option value="historical">Historical</option>
        <option value="cultural">Cultural</option>
        <option value="natural">Natural</option>
        <option value="Religious">Religious</option>
        <option value="Scenic">Scenic</option>
        <option value="Modern">Modern</option>
      </select>
    </div>

  <!-- Location Filter -->
  <div id="filter-section">
      <div class="filter-label">Location</div>
      <input type="text" id="location-filter" placeholder="Enter location or city..."/>
    </div>

  <!-- Interest Tag Filter -->
  <div id="filter-section">
      <div class="filter-label">Interest Tags</div>
      <input type="text" id="interest-filter" placeholder="ex: Empire State, Anime"/>
    </div>

  <!-- Selected Marker Info -->
    <div id="selected-location">No location selected yet.</div>
  </div>
</div>

<!-- ================== MAP & SCRIPT ================== -->
<script src="https://unpkg.com/leaflet/dist/leaflet.js"></script>
<script>
  // Global variables
  let map;
  // Store all { wonder, marker } so we can filter them
  let wondersMarkers = [];
  // Store the red pin (user-selected marker)
  let userSelectedMarker = null;
// 1. Initialize the Leaflet map
  function initLeafletMap() {
    map = L.map('map').setView([20, 0], 2);
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
      maxZoom: 19
    }).addTo(map);
// Set up filter listeners
    document.querySelectorAll('.wonder-option').forEach(checkbox => {
      checkbox.addEventListener('change', applyFilters);
    });
    document.getElementById('category-filter').addEventListener('change', applyFilters);
    document.getElementById('location-filter').addEventListener('input', applyFilters);
    document.getElementById('interest-filter').addEventListener('input', applyFilters);
// Single click on map to place a red pin
    map.on("click", (e) => {
      placeSelectedMarker(e.latlng);
    });
// After map init, fetch data from your backend
    fetchDataFromBackend();
  }
// 2. Fetch data from the backend API & create markers
  function fetchDataFromBackend() {
    // Change /cities to the correct endpoint on your Flask app
    fetch('http://127.0.0.1:5000/cities')
      .then(response => {
        if (!response.ok) {
          throw new Error('Network response was not ok: ' + response.status);
        }
        return response.json();
      })
      .then(data => {
        // data should be an array of wonders (city objects) from your backend
        // Clear existing markers from the map (if any)
        wondersMarkers.forEach(({ marker }) => marker.remove());
        wondersMarkers = [];
// Create new markers from the fetched data
        data.forEach((wonder) => {
          const blueIcon = L.icon({
            iconUrl: generateSVGPin('#4169E1'),
            iconSize: [25, 41],
            iconAnchor: [12, 41],
            popupAnchor: [1, -34],
            shadowSize: [41, 41]
          });
const marker = L.marker(wonder.position, {
            title: wonder.name,
            icon: blueIcon
          }).addTo(map);
wondersMarkers.push({ wonder, marker });
        });
// Once we have new markers, apply filters immediately
        applyFilters();
      })
      .catch(error => {
        console.error('Error fetching data from backend:', error);
      });
  }
// 3. Helper function to generate an inline SVG data URI (a colored pin)
  function generateSVGPin(colorHex) {
    // Must be in backticks so it’s a string, not raw HTML
    const svg = `
      <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 384 512">
        <path fill="${colorHex}" d="M168 0C75.3 0 0 75.3 0 168C0 297 168
          512 168 512C168 512 336 297 336 168C336 75.3 260.7 0 168 0zM168
          240c-39.8 0-72-32.2-72-72 0-39.8 32.2-72 72-72 39.8 0 72 32.2
          72 72C240 207.8 207.8 240 168 240z"/>
      </svg>
    `;
    return "data:image/svg+xml;base64," + btoa(svg);
  }
// 4. Place/Move the user-selected marker (red pin)
  function placeSelectedMarker(location) {
    if (userSelectedMarker) {
      userSelectedMarker.setLatLng(location);
    } else {
      const redIcon = L.icon({
        iconUrl: generateSVGPin('#FF0000'),
        iconSize: [25, 41],
        iconAnchor: [12, 41],
        popupAnchor: [1, -34],
        shadowSize: [41, 41]
      });
      userSelectedMarker = L.marker(location, {
        icon: redIcon,
        title: "Selected Location"
      }).addTo(map);
    }
    map.setView(location, map.getZoom());
    document.getElementById("selected-location").innerText =
      `Lat: ${location.lat.toFixed(4)}, Lng: ${location.lng.toFixed(4)}`;
  }
// 5. Apply filters based on user input
  function applyFilters() {
    const activeWonders = Array.from(document.querySelectorAll('.wonder-option:checked'))
      .map(cb => cb.value.toLowerCase());
const categorySelected = document.getElementById('category-filter').value.toLowerCase();
    const locationInput = document.getElementById('location-filter').value.toLowerCase();
    const interestInput = document.getElementById('interest-filter').value.toLowerCase();
wondersMarkers.forEach(({ wonder, marker }) => {
      let isVisible = true;
// City checkbox filter (based on wonder.value)
      if (!activeWonders.includes(wonder.value.toLowerCase())) {
        isVisible = false;
      }
// Category filter
      if (categorySelected && wonder.category.toLowerCase() !== categorySelected) {
        isVisible = false;
      }
// Location filter (search by name)
      if (locationInput && !wonder.name.toLowerCase().includes(locationInput)) {
        isVisible = false;
      }
// Interest filter
      if (interestInput && !wonder.interest.toLowerCase().includes(interestInput)) {
        isVisible = false;
      }
// Show or hide the marker on the map
      if (isVisible) {
        marker.addTo(map);
      } else {
        marker.remove();
      }
    });
  }
// 6. Initialize when the window loads
  window.onload = initLeafletMap;
</script>
</body>
</html>
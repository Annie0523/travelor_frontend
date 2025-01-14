---
layout: post
title: Explore
search_exclude: true
description: A map with some popular cities
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
      margin-bottom: 30px;
    }
    .city-checkbox {
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

<div id="filter-section">
  <button id="satellite-toggle" style="margin-top: 20px; padding: 10px; font-size: 14px;">
    Toggle Satellite View
  </button>
</div>

  <!-- ================== FILTERS ================== -->
  <!-- The Cities Filter -->
  <div id="filter-section">
      <div class="filter-label">Cities</div>
      <label class="city-checkbox">
        <input type="checkbox" class="city-option" value="tokyo" checked/> Tokyo
      </label>
      <label class="city-checkbox">
        <input type="checkbox" class="city-option" value="mumbai" checked/> Mumbai
      </label>
      <label class="city-checkbox">
        <input type="checkbox" class="city-option" value="cairo" checked/> Cairo
      </label>
      <label class="city-checkbox">
        <input type="checkbox" class="city-option" value="lagos" checked/> Lagos
      </label>
      <label class="city-checkbox">
        <input type="checkbox" class="city-option" value="london" checked/> London
      </label>
      <label class="city-checkbox">
        <input type="checkbox" class="city-option" value="paris" checked/> Paris
      </label>
      <label class="city-checkbox">
        <input type="checkbox" class="city-option" value="new_york_city" checked/> New York City
      </label>
      <label class="city-checkbox">
        <input type="checkbox" class="city-option" value="mexico_city" checked/> Mexico City
      </label>
      <label class="city-checkbox">
        <input type="checkbox" class="city-option" value="sao_paulo" checked/> Sao Palo
      </label>
      <label class="city-checkbox">
        <input type="checkbox" class="city-option" value="buenos_aires" checked/> Buenos Aires
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
  let map;
  let citysMarkers = [];
  let userSelectedMarker = null;
  const interestFilter = document.getElementById('interest-filter');
  const interestDisplay = document.createElement('div');
  interestDisplay.style.display = 'none';
  interestDisplay.style.fontSize = '20px';
  interestDisplay.style.color = '#555';
  interestFilter.parentNode.appendChild(interestDisplay);
 let allInterests = [];
  let interestIndex = 0;
  let interestInterval;
// 1. The Leaflet map code 
// Map layers ex(satelite)
const defaultLayer = L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
  maxZoom: 20,
  attribution: '© OpenStreetMap contributors'
});
const satelliteLayer = L.tileLayer('https://{s}.google.com/vt/lyrs=s&x={x}&y={y}&z={z}', {
  subdomains: ['mt0', 'mt1', 'mt2', 'mt3'],
  maxZoom: 20,
  attribution: '© Google Maps'
});
// Track current map layer
let currentLayer = defaultLayer;
function initLeafletMap() {
  map = L.map('map', {
    layers: [defaultLayer] // Start with the default layer
  }).setView([22, 0], 2);
// Add satellite view toggle functionality
  document.getElementById('satellite-toggle').addEventListener('click', () => {
    if (map.hasLayer(defaultLayer)) {
      map.removeLayer(defaultLayer);
      map.addLayer(satelliteLayer);
    } else {
      map.removeLayer(satelliteLayer);
      map.addLayer(defaultLayer);
    }
  });
// Existing event listeners and functionality
  document.querySelectorAll('.city-option').forEach(checkbox => {
    checkbox.addEventListener('change', applyFilters);
  });
  document.getElementById('category-filter').addEventListener('change', applyFilters);
  document.getElementById('location-filter').addEventListener('input', applyFilters);
  document.getElementById('interest-filter').addEventListener('input', applyFilters);
map.on("click", (e) => {
    placeSelectedMarker(e.latlng);
  });
fetchDataFromBackend();
  fetchInterestsForHover();
}
// Fetching data from the backend API using fetch command
  function fetchDataFromBackend() {
    fetch('http://127.0.0.1:8887/cities')
      .then(response => {
        if (!response.ok) {
          throw new Error('Network response was not ok: ' + response.status);
        }
        return response.json();
      })
      .then(data => {
        citysMarkers.forEach(({ marker }) => marker.remove());
        citysMarkers = [];
        data.forEach((city) => {
          const blueIcon = L.icon({
            iconUrl: generateSVGPin('#4169E1'),
            iconSize: [25, 41],
            iconAnchor: [12, 41],
            popupAnchor: [1, -34],
            shadowSize: [41, 41]
          });
          const marker = L.marker(city.position, {
            title: city.name,
            icon: blueIcon
          }).addTo(map);
          citysMarkers.push({ city, marker });
        });
        applyFilters();
      })
      .catch(error => {
        console.error('Error fetching data from backend:', error);
      });
  }
// Fetch interests by hovering over interest
  function fetchInterestsForHover() {
    return fetch('http://127.0.0.1:8887/cities')
      .then(response => {
        if (!response.ok) {
          throw new Error('Backend not reachable');
        }
        return response.json();
      })
      .then(data => {
        allInterests = data.flatMap(city => city.interest.split(', ').map(interest => interest.trim()));
      })
      .catch(error => {
        console.error('Error fetching interests:', error);
      });
  }
// 3. Helper function to generate an inline SVG data URI (a colored pin)
  function generateSVGPin(colorHex) {
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
// 4. Place a red pin on the map
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
// Show cycling interests when hovering
  function startCyclingInterests() {
    if (allInterests.length === 0) return;
interestDisplay.style.display = 'block';
    interestInterval = setInterval(() => {
      interestDisplay.innerText = allInterests[interestIndex];
      interestIndex = (interestIndex + 1) % allInterests.length;
    }, 1000);
  }
// Stop cycling interests
  function stopCyclingInterests() {
    interestDisplay.style.display = 'none';
    clearInterval(interestInterval);
  }
// Attach hover event listeners to interest filter
  interestFilter.addEventListener('mouseenter', startCyclingInterests);
  interestFilter.addEventListener('mouseleave', stopCyclingInterests);
// 6. Apply filters
  function applyFilters() {
    const activecitys = Array.from(document.querySelectorAll('.city-option:checked'))
      .map(cb => cb.value.toLowerCase());
    const categorySelected = document.getElementById('category-filter').value.toLowerCase();
    const locationInput = document.getElementById('location-filter').value.toLowerCase();
    const interestInput = document.getElementById('interest-filter').value.toLowerCase();
citysMarkers.forEach(({ city, marker }) => {
      let isVisible = true;
      if (!activecitys.includes(city.value.toLowerCase())) {
        isVisible = false;
      }
      if (categorySelected && city.category.toLowerCase() !== categorySelected) {
        isVisible = false;
      }
      if (locationInput && !city.name.toLowerCase().includes(locationInput)) {
        isVisible = false;
      }
      if (interestInput && !city.interest.toLowerCase().includes(interestInput)) {
        isVisible = false;
      }
      if (isVisible) {
        marker.addTo(map);
      } else {
        marker.remove();
      }
    });
  }
window.onload = initLeafletMap;
</script>
</body>
</html>
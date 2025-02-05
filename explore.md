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
    /* Original page styling */
    html, body {
      margin: 0;
      padding: 0;
      height: 100%;
      font-family: Arial, sans-serif;
    }
    #container {
      display: flex;
      /* Increased the map and sidebar widths */
      height: 100vh;
      width: 100%;
    }
    /* Make the map bigger: changed flex from 4 to 5 */
    #map {
      flex: 5;
      height: 100%;
    }
    /* Make the sidebar bigger: changed flex from 1.5 to 2 */
    #sidebar {
      flex: 2;
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


    /* ADDED: Make #selected-location text red, white background, light border, some padding */
    #selected-location {
      margin-top: 10px;
      font-weight: bold;
      color: red;               /* text color red */
      background-color: #fff;   /* white background */
      border: 1px solid #ccc;   /* light border */
      padding: 10px;            /* spacing inside */
    }


    /* Button styling for dynamic colors */
    #location-btn {
      margin-top: 10px;
      padding: 8px;
      font-size: 14px;
      cursor: pointer;
      border: none;
      color: #fff;
    }
    /* Default (Add mode, fields empty) => Gray */
    #location-btn.gray {
      background-color: #777;
    }
    /* Add mode, all fields filled => Red */
    #location-btn.red {
      background-color: #d9534f;
    }
    /* Edit mode => Blue */
    #location-btn.blue {
      background-color: #0275d8;
    }


    /* ----------- New CSS for Orange Toggle Satellite Button ---------- */
    #satellite-toggle {
      margin-top: 20px;
      padding: 10px 15px;
      font-size: 14px;
      background-color: orange;
      color: #fff;
      border: none;
      border-radius: 4px;
      cursor: pointer;
      transition: background-color 0.3s ease;
    }
    #satellite-toggle:hover {
      background-color: #ff9500; /* slightly different orange on hover */
    }


    /* ----------- Dropdown for City Checkboxes ----------- */
    .dropdown {
      position: relative;
      display: inline-block;
    }
    .dropbtn {
      background-color: #eee;
      color: #333;
      padding: 8px 12px;
      font-size: 14px;
      border: 1px solid #ccc;
      cursor: pointer;
      border-radius: 4px;
    }
    .dropbtn:hover {
      background-color: #ddd;
    }
    .dropdown-content {
      display: none;
      position: absolute;
      background-color: #fff;
      min-width: 200px;
      border: 1px solid #ccc;
      z-index: 999;
      padding: 10px;
    }
    .dropdown-content label {
      display: block;
      margin: 5px 0;
    }
    .dropdown-content input[type="checkbox"] {
      margin-right: 5px;
    }
    .show {
      display: block; /* utility to toggle display on/off */
    }


    /* ADDED: a big box around name, value, position, category, interest, and add location */
    #big-form {
      border: 2px solid #ccc;     /* border around the form */
      background-color: #fff;     /* white background */
      padding: 15px;              /* some inner spacing */
      border-radius: 6px;         /* optional slight rounding */
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
      <!-- Orange Satellite Toggle Button -->
      <button id="satellite-toggle">
        Toggle Satellite View
      </button>
    </div>


  <!-- ================== FILTERS ================== -->
  <!-- Replaced the old city checkboxes with a dropdown -->
  <div id="filter-section">
      <div class="filter-label">Cities</div>
      <div class="dropdown">
        <button class="dropbtn" id="city-dropdown-btn">Select Cities</button>
        <div class="dropdown-content" id="city-dropdown-content">
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
      </div>
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


  <!-- ================== ADD/UPDATE LOCATION FORM ================== -->
  <!-- EVERYTHING in "big-form" is same lines, just wrapped in this new div -->
  <div id="filter-section">
      <div id="big-form">
        <h3 id="form-title">Add a New Location</h3>


  <label for="explore-name">Name:</label>
        <input type="text" id="explore-name" placeholder="e.g. Chicago" />


  <label for="explore-value">Value:</label>
        <input type="text" id="explore-value" placeholder="e.g. chicago" />


  <label for="explore-position">Position (lat, lng):</label>
        <input type="text" id="explore-position" placeholder="e.g. 41.8781, -87.6298" />


  <label for="explore-category">Category:</label>
        <select id="explore-category">
          <option value="">--Select Category--</option>
          <option value="historical">Historical</option>
          <option value="cultural">Cultural</option>
          <option value="natural">Natural</option>
          <option value="Religious">Religious</option>
          <option value="Scenic">Scenic</option>
          <option value="Modern">Modern</option>
        </select>


  <label for="explore-interest">Interest:</label>
        <input type="text" id="explore-interest" placeholder="e.g. CHICAGO: deep-dish, windy city" />


  <button id="location-btn" class="gray">Add Location</button>
      </div>
    </div>


  </div><!-- End #sidebar -->
</div><!-- End #container -->


<!-- ================== MAP & SCRIPT ================== -->
<script src="https://unpkg.com/leaflet/dist/leaflet.js"></script>
<script>
  let map;
  let citysMarkers = [];
  let userSelectedMarker = null;
  // Variables for controlling add vs. edit mode
  let editingCityId = null; // null means add mode; if we set it to an ID, we're editing that location
const knownCityValues = [
    "tokyo", "mumbai", "cairo", "lagos", "london",
    "paris", "new_york_city", "mexico_city", "sao_paulo", "buenos_aires"
  ];
// For interest hover
  let allInterests = [];
  let interestIndex = 0;
  let interestInterval;
const interestFilter = document.getElementById('interest-filter');
  const interestDisplay = document.createElement('div');
  interestDisplay.style.display = 'none';
  interestDisplay.style.fontSize = '20px';
  interestDisplay.style.color = '#555';
  interestFilter.parentNode.appendChild(interestDisplay);
const nameInput = document.getElementById('explore-name');
  const valueInput = document.getElementById('explore-value');
  const positionInput = document.getElementById('explore-position');
  const categorySelect = document.getElementById('explore-category');
  const interestInput = document.getElementById('explore-interest');
  const locationBtn = document.getElementById('location-btn');
  const formTitle = document.getElementById('form-title');
// ----------------------- SETUP pythonURI -----------------------
  // Instead of calling CORS anywhere or some local proxy, we define a direct URI:
  const pythonURI = (() => {
    // Adjust your domain/port if needed
    if (location.hostname === "localhost") {
      return "http://localhost:8887";
    } else if (location.hostname === "127.0.0.1") {
      return "http://127.0.0.1:8887";
    } else {
      // Change to your actual deployed Flask or Python server
      return "https://flask2025.nighthawkcodingsociety.com";
    }
  })();
function initLeafletMap() {
    map = L.map('map', {
      layers: [defaultLayer]
    }).setView([20, 0], 2);
document.getElementById('satellite-toggle').addEventListener('click', () => {
      if (map.hasLayer(defaultLayer)) {
        map.removeLayer(defaultLayer);
        map.addLayer(satelliteLayer);
      } else {
        map.removeLayer(satelliteLayer);
        map.addLayer(defaultLayer);
      }
    });
// Filter changes (for city checkboxes, category, location, interest)
    document.querySelectorAll('.city-option').forEach(checkbox => {
      checkbox.addEventListener('change', applyFilters);
    });
    document.getElementById('category-filter').addEventListener('change', applyFilters);
    document.getElementById('location-filter').addEventListener('input', applyFilters);
    document.getElementById('interest-filter').addEventListener('input', applyFilters);
// For city dropdown toggle
    const cityDropdownBtn = document.getElementById('city-dropdown-btn');
    const cityDropdownContent = document.getElementById('city-dropdown-content');
    cityDropdownBtn.addEventListener('click', () => {
      cityDropdownContent.classList.toggle('show');
    });
    window.addEventListener('click', function(e) {
      if (!e.target.matches('#city-dropdown-btn')) {
        if (cityDropdownContent.classList.contains('show')) {
          cityDropdownContent.classList.remove('show');
        }
      }
    });
// Place pin on map click
    map.on("click", (e) => {
      placeSelectedMarker(e.latlng);
    });
// Initialize or refresh data
    fetchDataFromBackend();
    fetchExploreInterests();
// Setup form event
    locationBtn.addEventListener('click', submitLocation);
// Listen for changes in the form fields so we can update button color
    [nameInput, valueInput, positionInput, categorySelect, interestInput].forEach(elem => {
      elem.addEventListener('input', updateAddButtonState);
    });
  }
// ----------------------- BACKEND COMMUNICATION -----------------------
  // 1) GET all Explore data
  function fetchDataFromBackend() {
    fetch(`${pythonURI}/api/explores`)
      .then(response => {
        if (!response.ok) {
          throw new Error('Error fetching data from /api/explores');
        }
        return response.json();
      })
      .then(data => {
        // Clear existing markers
        citysMarkers.forEach(({ marker }) => map.removeLayer(marker));
        citysMarkers = [];
// Create new markers
        data.forEach(city => {
          const coords = city.position.split(',').map(str => parseFloat(str.trim()));
          const lat = coords[0];
          const lng = coords[1];
// Decide marker color
          let colorHex = "#0000FF"; // blue for known
          if (!knownCityValues.includes(city.value.toLowerCase())) {
            colorHex = "#00FF00"; // green for newly added
          }
const customIcon = L.icon({
            iconUrl: generateSVGPin(colorHex),
            iconSize: [25, 41],
            iconAnchor: [12, 41],
            popupAnchor: [1, -34],
            shadowSize: [41, 41]
          });
const marker = L.marker([lat, lng], { icon: customIcon });
// Build popup content: Always show a red "Delete" and a blue "Update" button
          let popupHtml = `
            <b>${city.name}</b><br>
            ${city.interest}<br><br>
            <button class="delete-btn" data-id="${city.id}"
              style="background-color:red;color:white;border:none;padding:5px;cursor:pointer;">
              Delete
            </button>
            <button class="edit-btn" data-id="${city.id}"
              style="background-color:blue;color:white;border:none;padding:5px;cursor:pointer;">
              Update
            </button>
          `;
          marker.bindPopup(popupHtml);
          marker.addTo(map);
// On marker click, fill "Position" field
          marker.on('click', () => {
            positionInput.value = city.position;
          });
// Listen for popup open to attach events
          marker.on('popupopen', (e) => {
            const popupNode = e.popup._contentNode;
            const deleteBtn = popupNode.querySelector('.delete-btn');
            if (deleteBtn) {
              deleteBtn.addEventListener('click', () => {
                doDeleteCity(city.id);
              });
            }
            const editBtn = popupNode.querySelector('.edit-btn');
            if (editBtn) {
              editBtn.addEventListener('click', () => {
                startEditCity(city);
              });
            }
          });
citysMarkers.push({ city, marker });
        });
applyFilters();
      })
      .catch(error => console.error('Error fetching data:', error));
  }
// 2) GET interests
  function fetchExploreInterests() {
    fetch(`${pythonURI}/api/explores`)
      .then(response => {
        if (!response.ok) {
          throw new Error('Error fetching interests from /api/explores');
        }
        return response.json();
      })
      .then(data => {
        allInterests = data.flatMap(explore => {
          return explore.interest.split(',').map(tag => tag.trim());
        });
      })
      .catch(error => console.error('Error fetching interests:', error));
  }
// 3) POST or PUT location
  function submitLocation() {
    if (editingCityId) {
      updateLocation();
    } else {
      addLocation();
    }
  }
function addLocation() {
    if (!validateForm()) return;
const requestBody = {
      name: nameInput.value.trim(),
      value: valueInput.value.trim(),
      position: positionInput.value.trim(),
      category: categorySelect.value.trim(),
      interest: interestInput.value.trim()
    };
fetch(`${pythonURI}/api/explores`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(requestBody)
    })
      .then(response => {
        if (!response.ok) {
          throw new Error('Error adding new explore location');
        }
        return response.json();
      })
      .then(data => {
        alert(`New location '${data.name}' added successfully!`);
        fetchDataFromBackend();
        clearForm();
      })
      .catch(error => {
        console.error('Error adding new explore:', error);
        alert('Failed to add the new location. Check console for details.');
      });
  }
function updateLocation() {
    if (!validateForm()) return;
const requestBody = {
      id: editingCityId,
      name: nameInput.value.trim(),
      value: valueInput.value.trim(),
      position: positionInput.value.trim(),
      category: categorySelect.value.trim(),
      interest: interestInput.value.trim()
    };
fetch(`${pythonURI}/api/explores`, {
      method: 'PUT',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(requestBody)
    })
      .then(response => {
        if (!response.ok) {
          throw new Error('Error updating this location');
        }
        return response.json();
      })
      .then(result => {
        alert("Thank you for updating the location!");
        editingCityId = null;
        fetchDataFromBackend();
        clearForm();
      })
      .catch(error => {
        console.error('Error updating location:', error);
        alert('Failed to update the location. Check console for details.');
      });
  }
// 4) DELETE
  function doDeleteCity(cityId) {
    if (!confirm("Are you sure you want to delete this location?")) return;
fetch(`${pythonURI}/api/explores`, {
      method: 'DELETE',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ id: cityId })
    })
      .then(response => {
        if (!response.ok) {
          throw new Error('Error deleting this location');
        }
        return response.json();
      })
      .then(result => {
        alert(result.message || result);
        fetchDataFromBackend();
      })
      .catch(error => {
        console.error('Error deleting:', error);
        alert('Failed to delete the location. Check console for details.');
      });
  }
// ----------------------- EDIT MODE FUNCTIONS -----------------------
  function startEditCity(city) {
    editingCityId = city.id;
    nameInput.value = city.name;
    valueInput.value = city.value;
    positionInput.value = city.position;
    categorySelect.value = city.category;
    interestInput.value = city.interest;
formTitle.textContent = "Edit Location";
    locationBtn.textContent = "Update Location";
    locationBtn.classList.remove("gray", "red");
    locationBtn.classList.add("blue");
  }
function clearForm() {
    editingCityId = null;
    nameInput.value = "";
    valueInput.value = "";
    positionInput.value = "";
    categorySelect.value = "";
    interestInput.value = "";
formTitle.textContent = "Add a New Location";
    locationBtn.textContent = "Add Location";
    updateAddButtonState();
  }
function validateForm() {
    if (
      !nameInput.value.trim() ||
      !valueInput.value.trim() ||
      !positionInput.value.trim() ||
      !categorySelect.value.trim() ||
      !interestInput.value.trim()
    ) {
      alert("Please fill in all fields.");
      return false;
    }
    return true;
  }
// ----------------------- UTILS -----------------------
  const defaultLayer = L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 20,
    attribution: '© OpenStreetMap contributors'
  });
  const satelliteLayer = L.tileLayer('https://{s}.google.com/vt/lyrs=s&x={x}&y={y}&z={z}', {
    subdomains: ['mt0', 'mt1', 'mt2', 'mt3'],
    maxZoom: 20,
    attribution: '© Google Maps'
  });
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
positionInput.value = `${location.lat.toFixed(4)}, ${location.lng.toFixed(4)}`;
    updateAddButtonState();
  }
function startCyclingInterests() {
    if (allInterests.length === 0) return;
    interestDisplay.style.display = 'block';
    interestInterval = setInterval(() => {
      interestDisplay.innerText = allInterests[interestIndex];
      interestIndex = (interestIndex + 1) % allInterests.length;
    }, 1000);
  }
function stopCyclingInterests() {
    interestDisplay.style.display = 'none';
    clearInterval(interestInterval);
  }
  interestFilter.addEventListener('mouseenter', startCyclingInterests);
  interestFilter.addEventListener('mouseleave', stopCyclingInterests);
function applyFilters() {
    const activecitys = Array.from(document.querySelectorAll('.city-option:checked'))
      .map(cb => cb.value.toLowerCase());
    const categorySelected = document.getElementById('category-filter').value.toLowerCase();
    const locationInput = document.getElementById('location-filter').value.toLowerCase();
    const interestInput = document.getElementById('interest-filter').value.toLowerCase();
citysMarkers.forEach(({ city, marker }) => {
      let isVisible = true;
if (knownCityValues.includes(city.value.toLowerCase())) {
        if (!activecitys.includes(city.value.toLowerCase())) {
          isVisible = false;
        }
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
function updateAddButtonState() {
    if (editingCityId) {
      locationBtn.textContent = "Update Location";
      locationBtn.classList.remove("gray", "red");
      locationBtn.classList.add("blue");
      return;
    }
locationBtn.textContent = "Add Location";
const nameFilled = !!nameInput.value.trim();
    const valueFilled = !!valueInput.value.trim();
    const posFilled = !!positionInput.value.trim();
    const catFilled = !!categorySelect.value.trim();
    const interestFilled = !!interestInput.value.trim();
if (nameFilled && valueFilled && posFilled && catFilled && interestFilled) {
      locationBtn.classList.remove("gray", "blue");
      locationBtn.classList.add("red");
    } else {
      locationBtn.classList.remove("red", "blue");
      locationBtn.classList.add("gray");
    }
  }
// add uri function and also change the link to the port
  window.onload = initLeafletMap;
</script>
</body>
</html>

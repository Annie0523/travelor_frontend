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

  <!-- Leaflet core stylesheet -->
  <link rel="stylesheet" href="https://unpkg.com/leaflet/dist/leaflet.css" />

  <!-- Preload Google Fonts -->
  <link rel="preload" href="https://fonts.googleapis.com/css?family=Open+Sans:400,700&display=swap" as="style">
  <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Open+Sans:400,700&display=swap">

  <style>
    html, body {
      margin: 0;
      padding: 0;
      height: 100%;
      font-family: 'Open Sans', Arial, sans-serif;
      background: #B3D9FF;
    }
    #container {
      display: flex;
      height: 100vh;
      width: 100%;
    }
    #map {
      flex: 5;
      height: 100%;
    }
    #sidebar {
      flex: 2;
      padding: 20px;
      box-sizing: border-box;
      overflow-y: auto;
      background-color: #f5f5f5;
      border-left: 1px solid #ccc;
      border-radius: 0 0 10px 10px;
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
      border: 1px solid #ccc;
      border-radius: 4px;
    }
    #info {
      border: 1px solid #ccc;
      padding: 10px;
      background-color: #fff;
      margin-top: 20px;
    }
    #location-btn {
      margin-top: 10px;
      padding: 8px;
      font-size: 14px;
      cursor: pointer;
      border: none;
      color: #fff;
      border-radius: 4px;
    }
    .gray { background-color: #777; }
    .red { background-color: #d9534f; }
    .blue { background-color: #0275d8; }
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
      background-color: #ff9500;
    }
    .dropdown {
      position: relative;
      display: inline-block;
    }
    .dropbtn {
      background-color: #D8BFD8;
      color: #333;
      padding: 8px 12px;
      font-size: 14px;
      border: 1px solid #ccc;
      cursor: pointer;
      border-radius: 4px;
    }
    .dropbtn:hover {
      background-color: #ccc;
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
    .show { display: block; }
    #big-form {
      border: 2px solid #ccc;
      background-color: #fff;
      padding: 15px;
      border-radius: 6px;
    }
    /* Interest Tags control styling */
    #interest-tags-container {
      display: flex;
      align-items: center;
      gap: 5px;
      margin-bottom: 10px;
    }
    #interest-tags-container input {
      flex: 1;
      padding: 5px;
    }
    #add-interest-btn {
      padding: 3px 6px;
      font-size: 12px;
      cursor: pointer;
      transition: box-shadow 0.3s ease;
    }
    #interest-count {
      font-size: 12px;
      color: #888;
    }
    #arrow-container {
      display: flex;
      gap: 2px;
    }
    .interest-arrow {
      cursor: pointer;
      padding: 3px;
      font-size: 12px;
    }
    #current-interest-tag {
      margin-top: 5px;
      padding: 5px;
      border: 1px solid #ccc;
      border-radius: 4px;
      display: none;
      width: 100%;
    }
    #position-container {
      display: flex;
      gap: 4%;
      margin-bottom: 10px;
    }
    #position-container input {
      width: 48%;
    }
    /* Modal styling for error and success messages */
    .modal {
      display: none;
      position: fixed;
      z-index: 10000;
      left: 0;
      top: 0;
      width: 100%;
      height: 100%;
      background-color: rgba(0,0,0,0.5);
      align-items: center;
      justify-content: center;
    }
    .modal-content {
      background-color: #fff;
      padding: 20px 30px;
      border-radius: 8px;
      text-align: center;
      box-shadow: 0 2px 10px rgba(0,0,0,0.3);
      max-width: 400px;
      width: 80%;
    }
    .modal-content p {
      font-size: 18px;
      color: #333;
      margin: 0 0 20px;
    }
    .modal-button {
      background-color: #0275d8;
      color: #fff;
      border: none;
      padding: 10px 20px;
      font-size: 16px;
      border-radius: 4px;
      cursor: pointer;
      transition: background-color 0.3s ease;
    }
    .modal-button:hover {
      background-color: #025aa5;
    }
    /* Success modal button override */
    .modal-success .modal-button {
      background-color: #5cb85c;
    }
    .modal-success .modal-button:hover {
      background-color: #4cae4c;
    }
  </style>
</head>
<body>
  <div id="container">
    <div id="map"></div>
    <div id="sidebar">
      <h2>Filters</h2>
      <div id="filter-section">
        <button id="satellite-toggle">Toggle Satellite View</button>
      </div>
      <div id="filter-section">
        <div class="filter-label">Cities</div>
        <div class="dropdown">
          <button class="dropbtn" id="city-dropdown-btn">Select Cities</button>
          <div class="dropdown-content" id="city-dropdown-content">
            <!-- This will be populated dynamically -->
          </div>
        </div>
      </div>
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
      <div id="filter-section">
        <div class="filter-label">Location</div>
        <input type="text" id="location-filter" placeholder="Enter location or city..." />
      </div>
      <div id="filter-section">
        <div class="filter-label">Interest Tags</div>
        <input type="text" id="interest-filter" placeholder="ex: Empire State, Anime" />
      </div>
      <div id="filter-section">
        <div id="big-form">
          <h3 id="form-title">Add a New Location</h3>
          <label for="explore-name">Name:</label>
          <input type="text" id="explore-name" placeholder="e.g. Chicago" />
          <label for="explore-value">Value:</label>
          <input type="text" id="explore-value" placeholder="e.g. chicago" />
          <label>Position (lat, lng):</label>
          <div id="position-container">
            <input type="text" id="explore-lat" placeholder="Latitude" />
            <input type="text" id="explore-lng" placeholder="Longitude" />
          </div>
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
          <label for="explore-interest">Interest Tags:</label>
          <div id="interest-tags-container">
            <input type="text" id="explore-interest" placeholder="Enter an interest tag" />
            <button type="button" id="add-interest-btn">+</button>
            <span id="interest-count">0</span>
            <div id="arrow-container">
              <button type="button" class="interest-arrow" id="interest-up">▲</button>
              <button type="button" class="interest-arrow" id="interest-down">▼</button>
            </div>
          </div>
          <input type="text" id="current-interest-tag" placeholder="Current tag"/>
          <button id="location-btn" class="gray">Add Location</button>
        </div>
      </div>
    </div>
  </div>

  <!-- Modal for error and success messages -->
  <div id="message-modal" class="modal">
    <div class="modal-content">
      <p id="modal-message"></p>
      <button id="modal-ok-btn" class="modal-button">OK</button>
    </div>
  </div>

  <!-- Leaflet core library -->
  <script src="https://unpkg.com/leaflet/dist/leaflet.js"></script>

  <script type="module">
    import { pythonURI, fetchOptions } from '{{site.baseurl}}/assets/js/api/config.js';
    const safeFetchOptions = { ...fetchOptions, credentials: 'omit' };
    const baseURL = pythonURI.endsWith('/') ? pythonURI.slice(0, -1) : pythonURI;
    const URL = baseURL;
    let map;
    let citysMarkers = [];
    let userSelectedMarker = null;
    let editingCityId = null;
    let interestTags = [];
    let currentInterestIndex = 0;
    
    const interestFilter = document.getElementById('interest-filter');
    const interestDisplay = document.createElement('div');
    interestDisplay.style.display = 'none';
    interestDisplay.style.fontSize = '20px';
    interestDisplay.style.color = '#555';
    interestFilter.parentNode.appendChild(interestDisplay);
    
    const nameInput = document.getElementById('explore-name');
    const valueInput = document.getElementById('explore-value');
    const latInput = document.getElementById('explore-lat');
    const lngInput = document.getElementById('explore-lng');
    const categorySelect = document.getElementById('explore-category');
    const locationBtn = document.getElementById('location-btn');
    const formTitle = document.getElementById('form-title');
    
    // Modal dialog functions
    const messageModal = document.getElementById('message-modal');
    const modalMessage = document.getElementById('modal-message');
    const modalOkBtn = document.getElementById('modal-ok-btn');
    // Remove any modal type classes when OK is clicked.
    modalOkBtn.addEventListener('click', () => {
      messageModal.style.display = 'none';
      messageModal.classList.remove('modal-error', 'modal-success');
    });
    function showModal(message, type) {
      modalMessage.textContent = message;
      // Set the OK button color based on message type.
      if(type === 'success'){
        messageModal.classList.add('modal-success');
      } else {
        messageModal.classList.remove('modal-success');
      }
      messageModal.style.display = 'flex';
    }
    function showErrorModal(message) {
      showModal(message, 'error');
    }
    function showSuccessModal(message) {
      showModal(message, 'success');
    }
    
    function initLeafletMap() {
      const worldBounds = L.latLngBounds([ -85.0219, -172.9874 ], [84.6709, 205.2936 ]);
      map = L.map('map', { 
        layers: [defaultLayer], 
        maxBounds: worldBounds, 
        maxBoundsViscosity: 1.0,
        minZoom: 2, 
        maxZoom: 20 
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
      
      document.getElementById('category-filter').addEventListener('change', applyFilters);
      document.getElementById('location-filter').addEventListener('input', applyFilters);
      document.getElementById('interest-filter').addEventListener('input', applyFilters);
      
      const cityDropdownBtn = document.getElementById('city-dropdown-btn');
      const cityDropdownContent = document.getElementById('city-dropdown-content');
      cityDropdownBtn.addEventListener('click', () => {
        cityDropdownContent.classList.toggle('show');
      });
      window.addEventListener('click', function(e) {
        if (!e.target.matches('#city-dropdown-btn')) {
          cityDropdownContent.classList.remove('show');
        }
      });
      
      map.on("click", (e) => {
        placeSelectedMarker(e.latlng);
      });
      fetchDataFromBackend();
      fetchExploreInterests();
      locationBtn.addEventListener('click', submitLocation);
      [nameInput, valueInput, categorySelect].forEach(elem => {
        elem.addEventListener('input', updateAddButtonState);
      });
      nameInput.addEventListener('input', () => {
        const sanitized = nameInput.value.toLowerCase().replace(/[^a-z]/g, '');
        valueInput.value = sanitized;
      });
      valueInput.addEventListener('input', () => {
        valueInput.value = valueInput.value.toLowerCase().replace(/[^a-z]/g, '');
      });
      
      // Glow plus button red when interest input is not empty.
      document.getElementById('explore-interest').addEventListener('input', function(){
        const plusBtn = document.getElementById('add-interest-btn');
        if(this.value.trim() !== ''){
          plusBtn.style.boxShadow = '0 0 10px 2px red';
        } else {
          plusBtn.style.boxShadow = '';
        }
      });
      
      document.getElementById('add-interest-btn').addEventListener('click', () => {
        const interestInputField = document.getElementById('explore-interest');
        const tag = interestInputField.value.trim();
        if(tag !== ''){
          const plusBtn = document.getElementById('add-interest-btn');
          plusBtn.style.boxShadow = '';
          interestTags.push(tag);
          interestInputField.value = '';
          plusBtn.style.opacity = 0;
          setTimeout(() => {
            plusBtn.style.transition = 'opacity 1s';
            plusBtn.style.opacity = 1;
          }, 100);
          document.getElementById('interest-count').innerText = interestTags.length;
          if(interestTags.length > 0){
            currentInterestIndex = interestTags.length - 1;
            const currentDisplay = document.getElementById('current-interest-tag');
            currentDisplay.style.display = 'block';
            currentDisplay.value = interestTags[currentInterestIndex] || '';
          }
          updateAddButtonState();
        }
      });
      
      document.getElementById('interest-up').addEventListener('click', () => {
        if(interestTags.length > 0){
          interestTags[currentInterestIndex] = document.getElementById('current-interest-tag').value;
          currentInterestIndex = (currentInterestIndex + 1) % interestTags.length;
          document.getElementById('current-interest-tag').value = interestTags[currentInterestIndex];
        }
      });
      document.getElementById('interest-down').addEventListener('click', () => {
        if(interestTags.length > 0){
          interestTags[currentInterestIndex] = document.getElementById('current-interest-tag').value;
          currentInterestIndex = (currentInterestIndex - 1 + interestTags.length) % interestTags.length;
          document.getElementById('current-interest-tag').value = interestTags[currentInterestIndex];
        }
      });
      document.getElementById('current-interest-tag').addEventListener('input', function(){
          interestTags[currentInterestIndex] = this.value;
      });
    }
    
    function fetchDataFromBackend() {
      fetch(`${URL}/api/explores`, safeFetchOptions)
        .then(response => {
          if (!response.ok) {
            throw new Error('Error fetching data from /api/explores');
          }
          return response.json();
        })
        .then(data => {
          citysMarkers.forEach(({ marker }) => map.removeLayer(marker));
          citysMarkers = [];
          data.forEach(city => {
            const coords = city.position.split(',').map(str => parseFloat(str.trim()));
            const lat = coords[0];
            const lng = coords[1];
            let colorHex = "#0000FF";
            if(city.value.toLowerCase().indexOf('_') === -1){
              colorHex = "#00FF00";
            }
            const customIcon = L.icon({
              iconUrl: generateSVGPin(colorHex),
              iconSize: [25, 41],
              iconAnchor: [12, 41],
              popupAnchor: [1, -34],
              shadowSize: [41, 41]
            });
            const marker = L.marker([lat, lng], { icon: customIcon });
            let popupHtml = `
              <b>${city.name}</b><br>
              ${city.interest}<br><br>
              <button class="delete-btn" data-id="${city.id}" style="background-color:red;color:white;border:none;padding:5px;cursor:pointer;">
                Delete
              </button>
              <button class="edit-btn" data-id="${city.id}" style="background-color:blue;color:white;border:none;padding:5px;cursor:pointer;">
                Update
              </button>
            `;
            marker.bindPopup(popupHtml);
            marker.addTo(map);
            marker.on('click', () => {
              const pos = marker.getLatLng();
              latInput.value = pos.lat.toFixed(4);
              lngInput.value = pos.lng.toFixed(4);
            });
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
          updateCityDropdown(data);
          applyFilters();
        })
        .catch(error => {
          console.error('Error fetching data:', error);
          showErrorModal('Error fetching data from /api/explores. Check console for details.');
        });
    }
    
    // Update the cities dropdown to sort entries alphabetically by name.
    function updateCityDropdown(data) {
      const dropdown = document.getElementById('city-dropdown-content');
      dropdown.innerHTML = '';
      const uniqueCities = new Map();
      data.forEach(city => {
        uniqueCities.set(city.value.toLowerCase(), city.name);
      });
      const sortedCities = Array.from(uniqueCities.entries()).sort((a, b) => a[1].localeCompare(b[1]));
      sortedCities.forEach(([value, name]) => {
        const label = document.createElement('label');
        label.className = 'city-checkbox';
        const input = document.createElement('input');
        input.type = 'checkbox';
        input.className = 'city-option';
        input.value = value;
        input.checked = true;
        input.addEventListener('change', applyFilters);
        label.appendChild(input);
        label.appendChild(document.createTextNode(' ' + name));
        dropdown.appendChild(label);
      });
    }
    
    function fetchExploreInterests() {
      fetch(`${URL}/api/explores`, safeFetchOptions)
        .then(response => {
          if (!response.ok) {
            throw new Error('Error fetching interests from /api/explores');
          }
          return response.json();
        })
        .then(data => {
          // Additional interest logic can be added here if needed.
        })
        .catch(error => {
          console.error('Error fetching interests:', error);
          showErrorModal('Error fetching interests from /api/explores. Check console for details.');
        });
    }
    
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
        position: latInput.value.trim() + ', ' + lngInput.value.trim(),
        category: categorySelect.value.trim(),
        interest: interestTags.join(', ')
      };
      fetch(`${URL}/api/explores`, {
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
          showSuccessModal(`New location '${data.name}' added successfully!`);
          fetchDataFromBackend();
          clearForm();
        })
        .catch(error => {
          console.error('Error adding new explore:', error);
          showErrorModal('Failed to add the new location. Check console for details.');
        });
    }
    
    function updateLocation() {
      if (!validateForm()) return;
      const requestBody = {
        id: editingCityId,
        name: nameInput.value.trim(),
        value: valueInput.value.trim(),
        position: latInput.value.trim() + ', ' + lngInput.value.trim(),
        category: categorySelect.value.trim(),
        interest: interestTags.join(', ')
      };
      fetch(`${URL}/api/explores`, {
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
          showSuccessModal("Thank you for updating the location!");
          editingCityId = null;
          fetchDataFromBackend();
          clearForm();
        })
        .catch(error => {
          console.error('Error updating location:', error);
          showErrorModal('Failed to update the location. Check console for details.');
        });
    }
    
    function doDeleteCity(cityId) {
      if (!confirm("Are you sure you want to delete this location?")) return;
      fetch(`${URL}/api/explores`, {
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
          showSuccessModal(result.message || result);
          fetchDataFromBackend();
        })
        .catch(error => {
          console.error('Error deleting:', error);
          showErrorModal('Failed to delete the location. Check console for details.');
        });
    }
    
    function startEditCity(city) {
      editingCityId = city.id;
      nameInput.value = city.name;
      valueInput.value = city.value;
      const coords = city.position.split(',');
      if(coords.length === 2) {
        latInput.value = coords[0].trim();
        lngInput.value = coords[1].trim();
      }
      categorySelect.value = city.category;
      interestTags = city.interest.split(',').map(tag => tag.trim()).filter(tag => tag);
      currentInterestIndex = 0;
      document.getElementById('interest-count').innerText = interestTags.length;
      if(interestTags.length > 0){
        document.getElementById('current-interest-tag').style.display = 'block';
        document.getElementById('current-interest-tag').value = interestTags[currentInterestIndex];
      } else {
        document.getElementById('current-interest-tag').style.display = 'none';
      }
      formTitle.textContent = "Edit Location";
      locationBtn.textContent = "Update Location";
      locationBtn.classList.remove("gray", "red");
      locationBtn.classList.add("blue");
    }
    
    function clearForm() {
      editingCityId = null;
      nameInput.value = "";
      valueInput.value = "";
      latInput.value = "";
      lngInput.value = "";
      categorySelect.value = "";
      document.getElementById('explore-interest').value = "";
      interestTags = [];
      currentInterestIndex = 0;
      document.getElementById('interest-count').innerText = "0";
      document.getElementById('current-interest-tag').value = "";
      document.getElementById('current-interest-tag').style.display = 'none';
      formTitle.textContent = "Add a New Location";
      locationBtn.textContent = "Add Location";
      updateAddButtonState();
    }
    
    // Updated validateForm to use the modal dialog for error messages.
    function validateForm() {
      if (
        !nameInput.value.trim() ||
        !valueInput.value.trim() ||
        !latInput.value.trim() ||
        !lngInput.value.trim() ||
        !categorySelect.value.trim() ||
        interestTags.length === 0
      ) {
        let errorMsg = "Please fill in all fields and add at least one interest tag.";
        if(interestTags.length === 0) {
          errorMsg += " Don't forget to click the plus to add the tag.";
        }
        showErrorModal(errorMsg);
        return false;
      }
      return true;
    }
    
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
          <path fill="${colorHex}" d="M168 0C75.3 0 0 75.3 0 168C0 297 168 512 168 512C168 512 336 297 336 168C336 75.3 260.7 0 168 0zM168 240c-39.8 0-72-32.2-72-72 0-39.8 32.2-72 72-72 39.8 0 72 32.2 72 72C240 207.8 207.8 240 168 240z"/>
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
      latInput.value = location.lat.toFixed(4);
      lngInput.value = location.lng.toFixed(4);
      updateAddButtonState();
    }
    
    function applyFilters() {
      const activecitys = Array.from(document.querySelectorAll('.city-option:checked'))
        .map(cb => cb.value.toLowerCase());
      const categorySelected = document.getElementById('category-filter').value.toLowerCase();
      const locationInputVal = document.getElementById('location-filter').value.toLowerCase();
      const interestInputVal = document.getElementById('interest-filter').value.toLowerCase();
      citysMarkers.forEach(({ city, marker }) => {
        let isVisible = true;
        if (activecitys.length > 0 && !activecitys.includes(city.value.toLowerCase())) {
          isVisible = false;
        }
        if (categorySelected && city.category.toLowerCase() !== categorySelected) {
          isVisible = false;
        }
        if (locationInputVal && !city.name.toLowerCase().includes(locationInputVal)) {
          isVisible = false;
        }
        if (interestInputVal && !city.interest.toLowerCase().includes(interestInputVal)) {
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
      } else {
        locationBtn.textContent = "Add Location";
      }
      const nameFilled = !!nameInput.value.trim();
      const valueFilled = !!valueInput.value.trim();
      const posFilled = !!latInput.value.trim() && !!lngInput.value.trim();
      const catFilled = !!categorySelect.value.trim();
      const interestFilled = interestTags.length > 0;
      if (nameFilled && valueFilled && posFilled && catFilled && interestFilled) {
        locationBtn.classList.remove("gray", "blue");
        locationBtn.classList.add("red");
        document.querySelectorAll('#big-form input, #big-form select').forEach(el => {
          el.style.boxShadow = '0 0 5px 2px lightblue';
        });
      } else {
        locationBtn.classList.remove("red", "blue");
        locationBtn.classList.add("gray");
        document.querySelectorAll('#big-form input, #big-form select').forEach(el => {
          el.style.boxShadow = '';
        });
      }
    }
    
    window.onload = initLeafletMap;
  </script>
</body>
</html>

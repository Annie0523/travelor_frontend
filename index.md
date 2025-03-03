---
layout: post
title: The Travelers
search_exclude: true
description: A website for all travelers
hide: true
menu: nav/home.html
---

<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>The Travelers</title>

  <!-- Instead of preload, do preconnect + normal stylesheet to avoid font warnings -->
  <link rel="preconnect" href="https://fonts.googleapis.com" crossorigin>
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Roboto:400,700&display=swap">

  <!-- Three.js for Interactive Globe -->
  <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>

  <style>
    /* Global & Smooth Scrolling */
    html { scroll-behavior: smooth; }
    body {
      font-family: 'Roboto', sans-serif;
      margin: 0;
      background: #f7f9fb;
      color: #333;
    }
    
    /* Header & Navigation */
    header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding: 20px 50px;
      background: linear-gradient(135deg, #0056b3, #007bff);
      color: white;
      border-bottom-left-radius: 20px;
      border-bottom-right-radius: 20px;
      position: relative;
    }
    header .logo {
      font-size: 2.2rem;
      font-weight: 500;
    }
    nav {
      display: flex;
      gap: 15px;
    }
    nav button {
      background: linear-gradient(45deg, #0056b3, #007bff);
      color: white;
      border: none;
      padding: 8px 16px;
      border-radius: 50px;
      cursor: pointer;
      transition: background 0.3s, transform 0.3s;
      font-size: 0.9rem;
    }
    nav button:hover {
      background: linear-gradient(45deg, #007bff, #009cff);
      transform: scale(1.05);
    }
    .hamburger {
      display: none;
      flex-direction: column;
      gap: 5px;
      cursor: pointer;
    }
    .hamburger span {
      width: 25px;
      height: 3px;
      background: white;
      border-radius: 2px;
    }
    .mobile-nav {
      display: none;
      flex-direction: column;
      position: absolute;
      top: 70px;
      right: 50px;
      background: linear-gradient(135deg, #0056b3, #007bff);
      border-radius: 15px;
      padding: 10px;
      z-index: 10;
    }
    .mobile-nav button {
      margin: 5px 0;
      border-radius: 50px;
      padding: 8px 16px;
      font-size: 0.9rem;
    }
    
    /* Interactive Travel Sphere */
    #travelSphereContainer {
      width: 100%;
      height: 400px;
      background: #e0e7ee;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      margin-bottom: 40px;
    }
    #travelSphere {
      width: 100%;
      height: 100%;
      border-radius: 20px;
    }
    #dragHint {
      font-size: 0.9rem;
      color: #555;
      margin-top: 8px;
    }
    
    /* Destinations Banner */
    .destinations {
      text-align: center;
      padding: 100px 20px;
      background: url('https://assets.thehansindia.com/h-upload/2023/04/15/1346887-road-trips.jpg') center/cover fixed;
      color: white;
      border-bottom-left-radius: 25px;
      border-bottom-right-radius: 25px;
    }
    .destinations h1 {
      font-size: 2.8rem;
      margin-bottom: 20px;
    }
    .destinations p {
      font-size: 1.2rem;
      margin-bottom: 30px;
    }
    .destinations .intro {
      font-size: 1rem;
      margin-top: 20px;
      color: #d0e9ff;
    }
    .buttons-container {
      display: flex;
      justify-content: center;
      gap: 20px;
    }
    .buttons-container button {
      padding: 10px 20px;
      font-size: 0.9rem;
      background: #ff5722;
      color: white;
      border: none;
      border-radius: 50px;
      cursor: pointer;
      transition: background 0.3s, transform 0.3s;
    }
    .buttons-container button:hover {
      background: #e64a19;
      transform: scale(1.03);
    }
    
    /* Hero Slider */
    .slider {
      position: relative;
      max-width: 1000px;
      margin: 50px auto;
      overflow: hidden;
      border-radius: 20px;
      box-shadow: 0 6px 12px rgba(0,0,0,0.15);
    }
    .slides {
      display: flex;
      transition: transform 0.5s ease-in-out;
    }
    .slide {
      min-width: 100%;
      box-sizing: border-box;
    }
    .slide img {
      width: 100%;
      border-radius: 20px;
      max-height: 400px;
      object-fit: cover;
    }
    .slider-nav {
      position: absolute;
      top: 50%;
      width: 100%;
      display: flex;
      justify-content: space-between;
      transform: translateY(-50%);
    }
    .slider-nav button {
      background: rgba(0,0,0,0.5);
      border: none;
      color: white;
      padding: 10px;
      border-radius: 50%;
      cursor: pointer;
      transition: background 0.3s;
    }
    .slider-nav button:hover {
      background: rgba(0,0,0,0.7);
    }
    
    /* Cards & Lightbox */
    .section-title {
      font-size: 1.5rem;
      font-weight: 500;
      text-align: center;
      margin: 50px 0 20px;
    }
    .card-container {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 30px;
      padding: 0 50px;
    }
    .card {
      background: white;
      border-radius: 20px;
      box-shadow: 0 4px 8px rgba(0,0,0,0.1);
      overflow: hidden;
      cursor: pointer;
      transition: transform 0.3s ease, box-shadow 0.3s ease;
    }
    .card:hover {
      transform: scale(1.05);
      box-shadow: 0 6px 12px rgba(0,0,0,0.2);
    }
    .card img {
      width: 100%;
      height: 200px;
      object-fit: cover;
      border-top-left-radius: 20px;
      border-top-right-radius: 20px;
    }
    .card-content {
      padding: 20px;
    }
    .card-title {
      font-size: 1.2rem;
      font-weight: 500;
      margin-bottom: 10px;
    }
    .card-text {
      font-size: 0.9rem;
      color: #555;
    }
    #lightboxModal {
      display: none;
      position: fixed;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      background: rgba(0,0,0,0.8);
      justify-content: center;
      align-items: center;
      z-index: 1000;
    }
    #lightboxModal img {
      max-width: 90%;
      max-height: 90%;
      border-radius: 15px;
    }
    
    /* Explore Vacations Button */
    button.explore-vacations {
      margin: 30px 50px;
      background-color: #26a69a;
      border: none;
      border-radius: 20px;
      color: #fff;
      padding: 12px 24px;
      font-size: 1rem;
      cursor: pointer;
      transition: background 0.3s;
    }
    button.explore-vacations:hover {
      background-color: #21978b;
    }
    
    /* Stats Section */
    .stats {
      display: flex;
      justify-content: center;
      gap: 40px;
      background: #e0f7fa;
      padding: 40px 20px;
    }
    .stat {
      text-align: center;
    }
    .stat-number {
      font-size: 2rem;
      font-weight: bold;
      color: #0077c0;
    }
    .stat-label {
      font-size: 1rem;
      color: #005b96;
    }
    
    /* Travel Tips Section */
    .travel-tips {
      background: linear-gradient(135deg, #e0f7fa, #b3e5fc);
      padding: 50px 20px;
      text-align: center;
      border-top-left-radius: 25px;
      border-top-right-radius: 25px;
      margin-top: 40px;
    }
    .travel-tips h2 {
      font-size: 2rem;
      margin-bottom: 20px;
      color: #0077c0;
    }
    .travel-tips p {
      font-size: 1.1rem;
      color: #005b96;
    }
    
    /* FAQ Accordion */
    .faq {
      max-width: 800px;
      margin: 40px auto;
    }
    .faq-item {
      background: #fff;
      border: 1px solid #ccc;
      border-radius: 15px;
      margin-bottom: 10px;
      overflow: hidden;
    }
    .faq-question {
      padding: 15px;
      cursor: pointer;
      background: #e0e0e0;
      font-weight: bold;
    }
    .faq-answer {
      padding: 15px;
      display: none;
      font-size: 0.95rem;
    }
    
    /* Social Media Share Buttons */
    .share-buttons {
      text-align: center;
      margin-top: 30px;
    }
    .share-buttons a {
      margin: 0 10px;
      text-decoration: none;
      color: #007bff;
      font-size: 1.5rem;
    }
    
    /* Newsletter Signup Modal */
    #newsletterModal {
      display: none;
      position: fixed;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      background: rgba(0,0,0,0.7);
      justify-content: center;
      align-items: center;
      z-index: 1000;
    }
    #newsletterModal .modal-content {
      background: white;
      padding: 30px;
      border-radius: 20px;
      text-align: center;
      max-width: 400px;
      width: 90%;
    }
    #newsletterModal input[type="email"] {
      width: 80%;
      padding: 10px;
      margin: 10px 0;
      border-radius: 25px;
      border: 1px solid #ccc;
    }
    #newsletterModal button {
      background: #007bff;
      color: white;
      border: none;
      padding: 10px 20px;
      border-radius: 50px;
      cursor: pointer;
      transition: background 0.3s;
    }
    #newsletterModal button:hover {
      background: #0056b3;
    }
    
    /* Chatbot Widget (Travelor AI) */
    #chatbot-toggle {
      position: fixed;
      bottom: 20px;
      right: 20px;
      width: 60px;
      height: 60px;
      background-color: #007bff;
      border: none;
      border-radius: 50%;
      color: white;
      font-size: 30px;
      cursor: pointer;
      z-index: 1000;
      box-shadow: 0 4px 8px rgba(0,0,0,0.2);
    }
    #chatbot {
      position: fixed;
      bottom: 90px;
      right: 20px;
      width: 300px;
      max-height: 400px;
      background: #fff;
      border: 2px solid #03a9f4;
      border-radius: 20px;
      overflow: auto;
      resize: both;
      box-shadow: 0 4px 12px rgba(0,0,0,0.15);
      display: none;
      flex-direction: column;
      z-index: 1000;
      cursor: move;
    }
    #chatbot-header {
      background: #007bff;
      color: white;
      padding: 10px;
      text-align: center;
      font-weight: bold;
      cursor: move;
      user-select: none;
    }
    #chatbot-messages {
      flex: 1;
      padding: 10px;
      overflow-y: auto;
      background: #f7f9fb;
    }
    #chatbot-input {
      display: flex;
      border-top: 1px solid #ccc;
    }
    #chatbot-input input {
      flex: 1;
      border: none;
      padding: 10px;
      font-size: 1rem;
      outline: none;
    }
    #chatbot-input button {
      background: #007bff;
      border: none;
      color: white;
      padding: 10px 15px;
      cursor: pointer;
      transition: background 0.3s;
    }
    #chatbot-input button:hover {
      background: #0056b3;
    }
    .loading-bar {
      width: 100%;
      height: 5px;
      background: linear-gradient(90deg, #03a9f4, #4dd0e1);
      animation: loading 1s infinite;
      margin-bottom: 10px;
    }
    @keyframes loading {
      0% { transform: translateX(-100%); }
      100% { transform: translateX(100%); }
    }
  </style>
</head>
<body>
  <!-- Chatbot Toggle Button -->
  <button id="chatbot-toggle">💬</button>
  
  <!-- Header -->
  <header>
    <div class="logo" aria-label="TravelSphere Logo">TravelSphere</div>
    <nav aria-label="Primary Navigation">
      <button>Home</button>
      <a href="https://annie0523.github.io/travelor_frontend/explore"><button>Explore</button></a>
      <button>Profile</button>
    </nav>
    <div class="hamburger" onclick="toggleMobileNav()" aria-label="Toggle Navigation">
      <span></span><span></span><span></span>
    </div>
    <div class="mobile-nav" id="mobileNav">
      <button onclick="toggleMobileNav()">Home</button>
      <a href="https://annie0523.github.io/travelor_frontend/explore"><button onclick="toggleMobileNav()">Explore</button></a>
      <button onclick="toggleMobileNav()">Profile</button>
    </div>
  </header>
  
  <!-- Interactive Travel Sphere -->
  <section id="travelSphereContainer">
    <canvas id="travelSphere"></canvas>
    <div id="dragHint">Click and drag the globe to rotate (avoid moving too fast to prevent accidental clicks)</div>
  </section>
  
  <!-- Destinations Banner -->
  <section class="destinations">
    <h1>Explore the World – Find Your Perfect Destination!</h1>
    <p>Your journey begins here. Discover, connect, and share your travel experiences.</p>
    <p class="intro">Our platform provides curated recommendations, personalized insights, and detailed reviews to ensure every trip is unforgettable.</p>
    <div class="buttons-container">
      <button onclick="location.href='https://annie0523.github.io/travelor_frontend/login'">Log In</button>
    </div>
  </section>
  
  <!-- Hero Slider -->
  <section class="slider" aria-label="Featured Destinations">
    <div class="slides" id="slides">
      <div class="slide">
        <img src="https://www.ancient-origins.net/sites/default/files/field/image/The-Great-Wall-of-China.jpg" alt="Great Wall of China">
      </div>
      <div class="slide">
        <img src="https://media.cntraveler.com/photos/6244a325633ca4951bd9a1d9/16:9/w_2580,c_limit/Great%20Sand%20Dunes%20National%20Park_josh-gordon-ONxt3hLkvs0-unsplash.jpg" alt="Death Valley's Starnight">
      </div>
      <div class="slide">
        <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTc9-DW8OD8RwGAI6RC966ZQc1xIbdzkk19WsO_EQl-rxXf8GfDotNW0Sk5xNY0GqOdeP0" alt="Zhangjiajie National Forest Park">
      </div>
    </div>
    <div class="slider-nav">
      <button onclick="prevSlide()" aria-label="Previous Slide">&#10094;</button>
      <button onclick="nextSlide()" aria-label="Next Slide">&#10095;</button>
    </div>
  </section>
  
  <!-- Featured Destinations Cards -->
  <section>
    <h2 class="section-title">Featured Destinations</h2>
    <div class="card-container">
      <div class="card" onclick="openLightbox(this)">
        <img src="https://www.ancient-origins.net/sites/default/files/field/image/The-Great-Wall-of-China.jpg" alt="Great Wall of China">
        <div class="card-content">
          <div class="card-title">Great Wall of China</div>
          <p class="card-text">A majestic marvel spanning across China.</p>
        </div>
      </div>
      <div class="card" onclick="openLightbox(this)">
        <img src="https://media.cntraveler.com/photos/6244a325633ca4951bd9a1d9/16:9/w_2580,c_limit/Great%20Sand%20Dunes%20National%20Park_josh-gordon-ONxt3hLkvs0-unsplash.jpg" alt="Death Valley's Starnight">
        <div class="card-content">
          <div class="card-title">Death Valley's Starnight</div>
          <p class="card-text">Experience the wonder of starlit deserts.</p>
        </div>
      </div>
      <div class="card" onclick="openLightbox(this)">
        <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTc9-DW8OD8RwGAI6RC966ZQc1xIbdzkk19WsO_EQl-rxXf8GfDotNW0Sk5xNY0GqOdeP0" alt="Zhangjiajie National Forest Park">
        <div class="card-content">
          <div class="card-title">Zhangjiajie National Forest Park</div>
          <p class="card-text">The inspiration behind floating mountains.</p>
        </div>
      </div>
    </div>
  </section>
  
  <!-- Lightbox Modal -->
  <div id="lightboxModal" onclick="closeLightbox()">
    <img id="lightboxImg" src="" alt="Enlarged image">
  </div>
  
  <!-- Explore Vacations Button -->
  <button class="explore-vacations" onclick="window.location.href='https://annie0523.github.io/travelor_frontend/vacations'">
    🌍 Explore Vacations
  </button>
  
  <!-- Stats Section -->
  <section class="stats">
    <div class="stat">
      <div class="stat-number" id="destCount">0</div>
      <div class="stat-label">Destinations</div>
    </div>
    <div class="stat">
      <div class="stat-number" id="travelerCount">0</div>
      <div class="stat-label">Travelers</div>
    </div>
    <div class="stat">
      <div class="stat-number" id="reviewCount">0</div>
      <div class="stat-label">Reviews</div>
    </div>
  </section>
  
  <!-- Travel Tips Section -->
  <section class="travel-tips" aria-label="Travel Tips">
    <h2>Travel Tips</h2>
    <p id="travelTip">Tip: Always check local weather before booking your trip!</p>
  </section>
  
  <!-- FAQ Accordion -->
  <section class="faq" aria-label="Frequently Asked Questions">
    <h2 class="section-title">Frequently Asked Questions</h2>
    <div class="faq-item">
      <div class="faq-question" onclick="toggleFAQ(this)">How do I book a trip?</div>
      <div class="faq-answer">You can book directly through our platform after logging in.</div>
    </div>
    <div class="faq-item">
      <div class="faq-question" onclick="toggleFAQ(this)">What payment methods are accepted?</div>
      <div class="faq-answer">We accept all major credit cards and digital wallets.</div>
    </div>
    <div class="faq-item">
      <div class="faq-question" onclick="toggleFAQ(this)">Can I get personalized recommendations?</div>
      <div class="faq-answer">Absolutely! Our platform tailors suggestions based on your interests.</div>
    </div>
  </section>
  
  <!-- Social Media Share Buttons -->
  <div class="share-buttons">
    <a href="#" aria-label="Share on Facebook">&#xf09a;</a>
    <a href="#" aria-label="Share on Twitter">&#xf099;</a>
    <a href="#" aria-label="Share on Instagram">&#xf16d;</a>
  </div>
  
  <!-- Newsletter Signup Modal -->
  <div id="newsletterModal">
    <div class="modal-content">
      <h2>Subscribe to Our Newsletter</h2>
      <p>Get the latest travel tips and destination updates.</p>
      <input type="email" placeholder="Enter your email" id="newsletterEmail">
      <br>
      <button onclick="subscribeNewsletter()">Subscribe</button>
      <button onclick="closeNewsletterModal()">Close</button>
    </div>
  </div>
  
  <!-- Chatbot Widget (Travelor AI) -->
  <div id="chatbot">
    <div id="chatbot-header">Travelor AI</div>
    <div id="chatbot-messages"></div>
    <div id="chatbot-input">
      <input type="text" id="chatbot-user-input" placeholder="Ask about locations..." aria-label="Chat input">
      <button id="chatbot-send" onclick="sendChatbotMessage()">Send</button>
    </div>
  </div>

  <!-- EXACT "Leave a Comment" Feature -->
  <section class="comment-section" style="text-align:center; margin-top:40px;">
    <button onclick="openCommentModal()">Leave a Comment</button>
    <ul id="comment-list" class="comment-list" style="list-style:none; margin:20px auto 40px; padding:0; max-width:600px;"></ul>
  </section>
  <div id="comment-modal"
       style="display:none; position:fixed; top:0; left:0; width:100%; height:100%; 
              background:rgba(0,0,0,0.5); justify-content:center; align-items:center;">
    <div class="modal-content" style="background:#fff; padding:20px; border-radius:8px; width:300px; text-align:center;">
      <textarea id="comment-input" placeholder="Enter your comment"
                style="width:100%; height:80px; margin-bottom:10px;"></textarea>
      <button onclick="submitComment()">Submit</button>
      <button onclick="closeCommentModal()">Close</button>
    </div>
  </div>

  <script type="module">
    // Inline configuration for API endpoints
    const pythonURI = "http://127.0.0.1:8402";
    const fetchOptions = {};
    const safeFetchOptions = { ...fetchOptions, credentials: 'omit' };
    const baseURL = pythonURI.endsWith('/') ? pythonURI.slice(0, -1) : pythonURI;
    const URL = baseURL;
    
    /* Hamburger Menu Toggle */
    function toggleMobileNav() {
      const mobileNav = document.getElementById('mobileNav');
      mobileNav.style.display = (mobileNav.style.display === 'flex') ? 'none' : 'flex';
    }
    window.toggleMobileNav = toggleMobileNav;
    
    /* --- Interactive Travel Sphere with Embedded Navigation Markers --- */
    let sphereScene, sphereCamera, sphereRenderer, sphereMesh;
    const markers = [];
    
    function createTextSprite(message, parameters = {}) {
      const fontface = parameters.fontface || "Arial";
      const fontsize = parameters.fontsize || 32;
      const borderThickness = parameters.borderThickness || 4;
      const borderColor = parameters.borderColor || { r:0, g:0, b:0, a:1.0 };
      const bgColor = parameters.backgroundColor || { r:255, g:255, b:255, a:1.0 };
      
      const canvas = document.createElement('canvas');
      const context = canvas.getContext('2d');
      context.font = fontsize + "px " + fontface;
      const metrics = context.measureText(message);
      const textWidth = metrics.width;
      canvas.width = textWidth + borderThickness * 4;
      canvas.height = fontsize * 1.8 + borderThickness * 4;
      
      // Draw an oval shape
      context.beginPath();
      context.ellipse(canvas.width/2, canvas.height/2, canvas.width/2, canvas.height/2, 0, 0, 2 * Math.PI);
      context.fillStyle = `rgba(${bgColor.r},${bgColor.g},${bgColor.b},${bgColor.a})`;
      context.fill();
      context.lineWidth = borderThickness;
      context.strokeStyle = `rgba(${borderColor.r},${borderColor.g},${borderColor.b},${borderColor.a})`;
      context.stroke();
      
      // Center text
      context.font = fontsize + "px " + fontface;
      context.fillStyle = "rgba(0,0,0,1)";
      context.textAlign = "center";
      context.textBaseline = "middle";
      context.fillText(message, canvas.width / 2, canvas.height / 2);
      
      const texture = new THREE.Texture(canvas);
      texture.needsUpdate = true;
      const spriteMat = new THREE.SpriteMaterial({ map: texture });
      const sprite = new THREE.Sprite(spriteMat);
      sprite.scale.set(canvas.width / 150, canvas.height / 150, 1);
      return sprite;
    }
    
    function createNavigationMarker(phi, theta, label, link) {
      const sprite = createTextSprite(label, {
        fontsize: 32,
        borderThickness: 4,
        backgroundColor: { r:34, g:139, b:34, a:1.0 },
        borderColor: { r:0, g:100, b:0, a:1.0 }
      });
      sprite.userData = { url: link };
      sprite.position.setFromSphericalCoords(1.1, phi, theta);
      sphereMesh.add(sprite);
      markers.push(sprite);
    }
    
    function initSphere() {
      const canvas = document.getElementById('travelSphere');
      sphereRenderer = new THREE.WebGLRenderer({ canvas, antialias: true });
      sphereRenderer.setSize(canvas.clientWidth, canvas.clientHeight);
      sphereScene = new THREE.Scene();
      sphereCamera = new THREE.PerspectiveCamera(45, canvas.clientWidth / canvas.clientHeight, 0.1, 1000);
      sphereCamera.position.z = 3;
      
      // Globe
      const geo = new THREE.SphereGeometry(1, 32, 32);
      const mat = new THREE.MeshStandardMaterial({ color: 0x007bff });
      sphereMesh = new THREE.Mesh(geo, mat);
      sphereScene.add(sphereMesh);
      
      // Light
      const light = new THREE.DirectionalLight(0xffffff, 1);
      light.position.set(5, 5, 5);
      sphereScene.add(light);
      
      // Markers
      createNavigationMarker(Math.PI / 2, Math.PI / 4, "Home", "https://annie0523.github.io/travelor_frontend/");
      createNavigationMarker(Math.PI / 2, Math.PI / 2, "Explore", "https://annie0523.github.io/travelor_frontend/explore");
      createNavigationMarker(Math.PI / 2, 3 * Math.PI / 4, "Profile", "https://annie0523.github.io/travelor_frontend/profile");
      
      handleDragAndClick();
      animateSphere();
    }
    
    function animateSphere() {
      requestAnimationFrame(animateSphere);
      sphereRenderer.render(sphereScene, sphereCamera);
    }
    
    window.addEventListener('resize', () => {
      const canvas = document.getElementById('travelSphere');
      sphereRenderer.setSize(canvas.clientWidth, canvas.clientHeight);
      sphereCamera.aspect = canvas.clientWidth / canvas.clientHeight;
      sphereCamera.updateProjectionMatrix();
    });
    
    /* Drag to rotate the globe */
    let mouseDown = false;
    let isDragging = false;
    let startX = 0, startY = 0;
    const threshold = 5;
    function handleDragAndClick() {
      const globeCanvas = document.getElementById('travelSphere');
      globeCanvas.addEventListener('mousedown', e => {
        mouseDown = true;
        isDragging = false;
        startX = e.clientX;
        startY = e.clientY;
      });
      globeCanvas.addEventListener('mousemove', e => {
        if (!mouseDown) return;
        const dx = e.clientX - startX;
        const dy = e.clientY - startY;
        if (!isDragging && Math.sqrt(dx*dx + dy*dy) > threshold) {
          isDragging = true;
        }
        if (isDragging) {
          const q = new THREE.Quaternion().setFromEuler(new THREE.Euler(
            toRadians(dy * 0.5),
            toRadians(dx * 0.5),
            0,
            'XYZ'
          ));
          sphereMesh.quaternion.multiplyQuaternions(q, sphereMesh.quaternion);
          startX = e.clientX;
          startY = e.clientY;
        }
      });
      globeCanvas.addEventListener('mouseup', e => {
        mouseDown = false;
        if (!isDragging) {
          // treat as click
          const mouse = new THREE.Vector2(
            (e.clientX / window.innerWidth)*2 - 1,
            -(e.clientY / window.innerHeight)*2 + 1
          );
          const raycaster = new THREE.Raycaster();
          raycaster.setFromCamera(mouse, sphereCamera);
          const hits = raycaster.intersectObjects(markers);
          if (hits.length > 0) {
            const url = hits[0].object.userData.url;
            if (url) window.location.href = url;
          }
        }
      });
      globeCanvas.addEventListener('mouseleave', () => {
        mouseDown = false;
      });
    }
    function toRadians(angle) { return angle * (Math.PI / 180); }
    
    initSphere();
    
    /* Hero Slider */
    const slidesEl = document.getElementById('slides');
    let currentSlide = 0;
    const totalSlides = slidesEl.children.length;
    function showSlide(i) {
      if (i < 0) currentSlide = totalSlides-1;
      else if (i >= totalSlides) currentSlide = 0;
      else currentSlide = i;
      slidesEl.style.transform = `translateX(-${currentSlide*100}%)`;
    }
    window.nextSlide = () => showSlide(currentSlide + 1);
    window.prevSlide = () => showSlide(currentSlide - 1);
    setInterval(() => showSlide(currentSlide + 1), 5000);
    
    /* Lightbox for Cards */
    window.openLightbox = function(card) {
      const imgSrc = card.querySelector('img').src;
      document.getElementById('lightboxImg').src = imgSrc;
      document.getElementById('lightboxModal').style.display = 'flex';
    };
    window.closeLightbox = function() {
      document.getElementById('lightboxModal').style.display = 'none';
    };
    
    /* Stats Counters */
    function animateCounter(id, start, end, duration) {
      let current = start;
      const increment = (end - start)/(duration/50);
      const el = document.getElementById(id);
      const timer = setInterval(() => {
        current += increment;
        if (current >= end) {
          current = end;
          clearInterval(timer);
        }
        el.textContent = Math.floor(current);
      }, 50);
    }
    animateCounter('destCount',0,50,2000);
    animateCounter('travelerCount',0,100,2000);
    animateCounter('reviewCount',0,10,2000);
    
    /* Rotating Travel Tips */
    const travelTips = [
      "Tip: Always check local weather before booking your trip!",
      "Tip: Research local transportation options to save time and money.",
      "Tip: Learn a few key phrases of the local language.",
      "Tip: Always carry a copy of your important documents.",
      "Tip: Check for local events and festivals during your visit.",
      "Tip: Book accommodations in advance during peak season.",
      "Tip: Try the local cuisine to enhance your travel experience.",
      "Tip: Pack light and smart for easier mobility.",
      "Tip: Stay connected with local travel apps for real-time updates.",
      "Tip: Embrace the local culture to enrich your journey."
    ];
    let tipIndex = 0;
    const travelTipEl = document.getElementById('travelTip');
    setInterval(() => {
      tipIndex = (tipIndex+1) % travelTips.length;
      travelTipEl.textContent = travelTips[tipIndex];
    },7000);
    
    /* FAQ Accordion */
    window.toggleFAQ = function(elem) {
      const answer = elem.nextElementSibling;
      answer.style.display = answer.style.display === 'block' ? 'none' : 'block';
    };
    
    /* Newsletter */
    window.subscribeNewsletter = function() {
      alert("Thank you for subscribing!");
      closeNewsletterModal();
    };
    window.closeNewsletterModal = function() {
      document.getElementById('newsletterModal').style.display = 'none';
    };
    
    /* Chatbot (Travelor AI) */
    const chatbotToggle = document.getElementById('chatbot-toggle');
    const chatbotDiv = document.getElementById('chatbot');
    const chatbotMessages = document.getElementById('chatbot-messages');
    const chatbotUserInput = document.getElementById('chatbot-user-input');
    
    chatbotToggle.addEventListener('click', () => {
      chatbotDiv.style.display = (chatbotDiv.style.display === 'flex') ? 'none' : 'flex';
    });
    
    function appendChatMessage(sender, text) {
      const msg = document.createElement('div');
      msg.style.marginBottom = '10px';
      msg.style.textAlign = (sender==="Travelor AI"?"left":"right");
      msg.innerHTML = `<strong>${sender}:</strong> ${text}`;
      chatbotMessages.appendChild(msg);
      chatbotMessages.scrollTop = chatbotMessages.scrollHeight;
    }
    
    window.sendChatbotMessage = function() {
      const userText = chatbotUserInput.value.trim();
      if(!userText) return;
      appendChatMessage("You", userText);
      chatbotUserInput.value = '';
      
      // Loading bar
      const loadingBar = document.createElement('div');
      loadingBar.className = 'loading-bar';
      chatbotMessages.appendChild(loadingBar);
      chatbotMessages.scrollTop = chatbotMessages.scrollHeight;
      
      fetch(`${URL}/api/chatbot`, {
        ...safeFetchOptions,
        method: 'POST',
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message: userText })
      })
      .then(resp=>{
        if(!resp.ok) throw new Error("Chatbot request failed: " + resp.statusText);
        return resp.json();
      })
      .then(data=>{
        if(chatbotMessages.contains(loadingBar)) {
          chatbotMessages.removeChild(loadingBar);
        }
        if(data.error) {
          appendChatMessage("Travelor AI","Error: "+data.error);
        } else {
          appendChatMessage("Travelor AI", data.reply);
        }
      })
      .catch(err=>{
        console.error(err);
        if(chatbotMessages.contains(loadingBar)) {
          chatbotMessages.removeChild(loadingBar);
        }
        appendChatMessage("Travelor AI","Error contacting chatbot. Please try again.");
      });
    };
    
    // Draggable Chatbot
    const chatbotHeader = document.getElementById('chatbot-header');
    let offsetX=0, offsetY=0, initialX=0, initialY=0;
    
    chatbotHeader.addEventListener('mousedown', e=>{
      e.preventDefault();
      initialX=e.clientX; 
      initialY=e.clientY;
      document.addEventListener('mousemove', dragMove);
      document.addEventListener('mouseup', dragEnd);
    });
    function dragMove(e){
      e.preventDefault();
      offsetX=initialX - e.clientX;
      offsetY=initialY - e.clientY;
      initialX=e.clientX;
      initialY=e.clientY;
      chatbotDiv.style.top = (chatbotDiv.offsetTop - offsetY)+"px";
      chatbotDiv.style.left= (chatbotDiv.offsetLeft - offsetX)+"px";
    }
    function dragEnd(){
      document.removeEventListener('mousemove', dragMove);
      document.removeEventListener('mouseup', dragEnd);
    }
    
    /* EXACT "Leave a Comment" Feature */
    const commentModal = document.getElementById('comment-modal');
    const commentInput = document.getElementById('comment-input');
    const commentList = document.getElementById('comment-list');
    const comments = [];
    
    window.openCommentModal = function(){
      commentModal.style.display='flex';
    };
    window.closeCommentModal = function(){
      commentModal.style.display='none';
      commentInput.value='';
    };
    window.submitComment = async function(){
      const cmt= commentInput.value.trim();
      if(!cmt)return;
      try {
        await fetch(`${URL}/api/comment`,{
          ...safeFetchOptions,
          method:'POST',
          headers:{'Content-Type':'application/json'},
          body:JSON.stringify({comment:cmt})
        });
        await fetchComments();
      } catch(err){
        console.error("Error adding comment:",err);
      }
      closeCommentModal();
    };
    window.fetchComments = async function(){
      try {
        const res=await fetch(`${URL}/api/comment`, safeFetchOptions);
        const data=await res.json();
        comments.length=0;
        comments.push(...data);
        renderComments();
      } catch(err){
        console.error("Error fetching comments:", err);
      }
    };
    window.renderComments = function(){
      commentList.innerHTML='';
      comments.forEach(entry=>{
        const li=document.createElement('li');
        li.textContent=entry;
        commentList.appendChild(li);
      });
    };
    document.addEventListener('DOMContentLoaded', fetchComments);
  </script>
</body>
</html>

---
layout: post
title: Meet the Developers
permalink: /developer
menu: nav/home.html
search_exclude: true
---
<style>
    .container {
        display: flex;
        justify-content: center;
        width: 100%;
        max-width: 1200px;
        padding: 20px;
        box-sizing: border-box;
    }
    .form-container {
        display: flex;
        flex-direction: column;
        max-width: 800px;
        width: 100%;
        background-color: #ffffff;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        color: #333;
    }
    .form-container h2 {
        font-size: 1.5em;
        margin-bottom: 15px;
        color: #0056b3;
    }
    .form-container label {
        margin-bottom: 5px;
        font-weight: bold;
        color: #495057;
    }
    .form-container input, 
    .form-container textarea, 
    .form-container select {
        margin-bottom: 10px;
        padding: 10px;
        border-radius: 5px;
        border: 1px solid #ced4da;
        width: 100%;
        font-size: 1em;
        background-color: #f8f9fa;
        color: #495057;
    }
    .form-container input:focus, 
    .form-container textarea:focus, 
    .form-container select:focus {
        outline: none;
        border-color: #0056b3;
        box-shadow: 0 0 5px rgba(0, 86, 179, 0.5);
    }
    .form-container button {
        padding: 10px;
        border-radius: 5px;
        border: none;
        background-color: #0056b3;
        color: #ffffff;
        cursor: pointer;
        font-size: 1em;
        transition: background-color 0.3s ease;
    }
    .form-container button:hover {
        background-color: #004494;
    }
    .data {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        color: #333;
        max-width: 800px;
        width: 100%;
    }
    .data .left-side {
        font-size: 1.2em;
        color: #0056b3;
    }
    .student-item {
        margin-bottom: 20px;
    }
    .student-item h2 {
        margin: 0;
        color: #333;
    }
    .student-item p {
        margin: 5px 0;
    }
</style>

<div class="container">
    <h1>Meet the Developers</h1>
    <div id="student-container"></div>
</div>

<script>
    async function fetchStudentData(endpoint) {
        try {
            const response = await fetch(endpoint);
            if (!response.ok) {
                throw new Error('Failed to fetch student data: ' + response.statusText);
            }
            return await response.json();
        } catch (error) {
            console.error('Error fetching student data:', error);
            return null;
        }
    }

    async function fetchAllStudents() {
        const endpoints = [
            '/api/student/johan',
            '/api/student/luke',
            '/api/student/anyi',
            '/api/student/collin',
            '/api/student/michelle'
        ];

        const studentData = await Promise.all(endpoints.map(fetchStudentData));
        displayStudents(studentData.filter(data => data !== null));
    }

    function displayStudents(studentData) {
        const studentContainer = document.getElementById('student-container');
        studentContainer.innerHTML = ''; // Clear previous content

        if (studentData.length === 0) {
            studentContainer.innerHTML = '<p>No student data available.</p>';
            return;
        }

        studentData.forEach(student => {
            const studentItem = document.createElement('div');
            studentItem.className = 'student-item';
            studentItem.innerHTML = `
                <h2>${student.FirstName || 'Unknown'} ${student.LastName || ''}</h2>
                <p><strong>DOB:</strong> ${student.DOB || 'N/A'}</p>
                <p><strong>Residence:</strong> ${student.Residence || 'N/A'}</p>
                <p><strong>Email:</strong> ${student.Email || 'N/A'}</p>
                <p><strong>Favorite Videogame:</strong> ${student.Favorite_Videogame || 'N/A'}</p>
                <p><strong>Hobbies:</strong> ${(student.Hobbies && student.Hobbies.join(', ')) || 'None'}</p>
            `;
            studentContainer.appendChild(studentItem);
        });
    }

    // Fetch and display students when the page loads
    document.addEventListener('DOMContentLoaded', fetchAllStudents);
</script>

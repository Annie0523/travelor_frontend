---
layout: post
title: Meet the Developers
permalink: /developer
menu: nav/home.html
search_exclude: true
---
<table id="demo" class="table">
    <thead>
        <tr>
            <th>First Name</th>
            <th>Last Name</th>
            <th>DOB</th>
            <th>Residence</th>
            <th>Email</th>
            <th>Favorite_Videogame</th>
            <th>Hobbies</th>
        </tr>
    </thead>
    <tbody id="result">
      <!-- javascript generated data -->
    </tbody>
  </table>

<script>
  // prepare HTML result container for new output
  let resultContainer = document.getElementById("result");
  
  // prepare URL
  url = "http://127.0.0.1:8887/api/students";

  // set options for cross origin header request
  let options = {
    method: 'GET', // *GET, POST, PUT, DELETE, etc.
    mode: 'cors', // no-cors, *cors, same-origin
    cache: 'default', // *default, no-cache, reload, force-cache, only-if-cached
    credentials: 'include', // include, *same-origin, omit
    headers: {
      'Content-Type': 'application/json',
    },
  };

  // fetch the API
  fetch(url, options)
    // response is a RESTful "promise" on any successful fetch
    .then(response => {
      // check for response errors and display
      if (response.status !== 200) {
          console.error(response.status);
          return;
      }
      // valid response will contain json data
      response.json().then(data => {
          console.log(data);
          for (const row of data) {
            // tr and td build out for each row
            const tr = document.createElement("tr");
            const firstname = document.createElement("td");
            const lastname = document.createElement("td");
            const dob = document.createElement("td");
            const residence = document.createElement("td");
            const email = document.createElement("td");
            const favorite_videogame = document.createElement("td");
            const hobbies = document.createElement("td");
            // data is specific to the API
            firstname.innerHTML = row.FirstName; 
            lastname.innerHTML = row.LastName; 
            dob.innerHTML = row.DOB;
            residence.innerHTML = row.Residence; 
            email.innerHTML = row.Email;
            favorite_videogame.innerHTML = row.Favorite_Videogame;
            hobbies.innerHTML = row.Hobbies;
            // this builds each td into tr
            tr.appendChild(firstname);
            tr.appendChild(lastname);
            tr.appendChild(dob);
            tr.appendChild(residence);
            tr.appendChild(email);
            tr.appendChild(favorite_videogame);
            tr.appendChild(hobbies);
            // add HTML to container
            resultContainer.appendChild(tr);
          }
      })
  })
  
</script>
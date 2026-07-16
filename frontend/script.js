const API_URL = "http://127.0.0.1:5000/users";


// Add User
function addUser(){

    let name = document.getElementById("name").value;
    let email = document.getElementById("email").value;


    fetch(API_URL, {

        method:"POST",

        headers:{
            "Content-Type":"application/json"
        },

        body: JSON.stringify({
            name:name,
            email:email
        })

    })

    .then(response => response.json())

    .then(data => {

        alert(data.message);

        getUsers();

    });

}



// Get Users
function getUsers(){

    fetch(API_URL)

    .then(response => response.json())

    .then(users=>{

        let list =
        document.getElementById("userList");


        list.innerHTML="";


        users.forEach(user=>{

            let li =
            document.createElement("li");


            li.innerHTML =
            user.name + " - " + user.email;


            list.appendChild(li);

        });

    });

}


getUsers();

function get_user_password() {

    
}

// Here we can not go for => function, as this has limited area of accesss
document.getElementById("submit_btn").addEventListener("click", function (e) {

    //alert("Hello");
    e.preventDefault();  

   let userName = document.getElementById("exampleInputName").value;
    console.log(userName);

});

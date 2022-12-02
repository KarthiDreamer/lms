var usertap = document.getElementById("user");

usertap.addEventListener("click",()=>{
    document.getElementById("demo").innerHTML="User Tapped!";
});

var admintap = document.getElementById("admin");

admintap.addEventListener("click",function(){
    document.getElementById("demo").innerHTML="Admin Tapped!";
});


function getresponse_api() {
    const url = 'http://localhost:5000/api_google';
    console.log("API was called")
    fetch(url)
        .then(response => response.json())
        .then(json => console.log(json))
}
var nom = document.getElementById("api_google");
nom.addEventListener("click",getresponse_api)


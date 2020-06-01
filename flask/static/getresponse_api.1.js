
function getresponse_api() {
    console.log("API was called")
    var myInit = {
        method: 'GET'
    }
    var input_research = document.getElementById("user_input").value;
    user_raw_text: user_input_value,
    const url = 'http://localhost:5000/api_google&user_input;
    console.log(url)
    fetch(url,myInit)
        .then(response => response.json())
        .then(json => console.log(json))
    console.log(input_research)

}
var nom = document.getElementById("api_google");
nom.addEventListener("click",getresponse_api)



// Called to display the answer of grandpy in the page application
function grandpyAnswer(){
    var user_input = document.getElementById("user_input");
    var user_input_value = user_input.value;
    $("#chat ul").append('<li class="question"><div class="speech-bubble">' + user_input_value + '</div></li>');
    user_input.value = "";
    $("#chat").scrollTop($('#chat').prop("scrollHeight"));
    url = `api_google?user_raw_text=${user_input_value}`
    $.get(url)
    .done(function(response){       
        $("#chat ul").append('<li class="answer"><div class="speech-bubble">Je ne me souviens plus</div></li>');
        $("#chat ul").append('<div class="answer"><div class="speech-bubble"><div id="map" style="width:400px;height:400px"></div></div></div>');
        initMap();

    }).fail(function() {
        $("#chat ul").append('<li class="answer"><div class="speech-bubble">Je ne me souviens plus</div></li>');
        $("#chat ul").append('<div class="answer"><div class="speech-bubble"><div id="map" style="width:400px;height:400px"></div></div></div>');
        initMap();
        var name  = dict_return["latitude"];
        console.log(name)

    });

}
// init function for the google map api
var map;
function initMap() {
  map = new google.maps.Map(document.getElementById("map"), {
    center: {lat: lat, lng: lng},
    zoom: 8
  });
}


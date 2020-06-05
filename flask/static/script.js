// Called to display the answer of grandpy in the page application
var compteur = 0;
function grandpyAnswer(){
    var user_input = document.getElementById("user_input");
    var user_input_value = user_input.value;
    $("#chat ul").append('<li class="question"><div class="speech-bubble">' + user_input_value + '</div></li>');
    user_input.value = "";
    $("#chat").scrollTop($('#chat').prop("scrollHeight"));
    url = `api_google?user_raw_text=${user_input_value}`;

    $.get(url, function (data, status){
      console.log(data)
      compteur++
      var id_map = "map_"+compteur
      $("#chat ul").append('<li class="answer"><div class="speech-bubble">Je ne me souviens plus</div></li>');
      $("#chat ul").append('<div class="answer"><div class="speech-bubble"><div id="' + id_map + '" style="width:400px;height:400px"></div></div></div>');
      console.log("Succès");
      create_map(data["latitude"],data["longitude"],id_map)
    // })
    // .done(function(response){       
    //     $("#chat ul").append('<li class="answer"><div class="speech-bubble">Je ne me souviens plus</div></li>');
    //     $("#chat ul").append('<div class="answer"><div class="speech-bubble"><div id="map" style="width:400px;height:400px"></div></div></div>');
    //     console.log("Succès");
    }).fail(function() {
        $("#chat ul").append('<li class="answer"><div class="speech-bubble">Je ne me souviens plus</div></li>');
        $("#chat ul").append('<div class="answer"><div class="speech-bubble"><div id="map" style="width:400px;height:400px"></div></div></div>');  
        console.log("Echec");
    });

}
// init function for the google map api
var map;
function create_map(lat,lng,id) {
  map = new google.maps.Map(document.getElementById(id), {
    center: {lat: lat, lng: lng},
    zoom: 8
  });
}


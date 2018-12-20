var map;
var geocoder;
function InitializeMap() {

  var latlng = new google.maps.LatLng(-7.258206, 112.754206);
  var myOptions =
  {
    zoom: 18,
    center: latlng,
    mapTypeId: google.maps.MapTypeId.ROADMAP,
    disableDefaultUI: true
  };
  map = new google.maps.Map(document.getElementById("map"), myOptions);
}

function FindLocation() {
  geocoder = new google.maps.Geocoder();
  InitializeMap();

  var address = document.getElementById("addressinput").value;
  geocoder.geocode({ 'address': address }, function (results, status) {
    if (status == google.maps.GeocoderStatus.OK) {
      map.setCenter(results[0].geometry.location);
      var marker = new google.maps.Marker({
          map: map,
          position: results[0].geometry.location
      });
    }
    else {
      alert("Geocode was not successful for the following reason: " + status);
    }
  });
}


function Button1_onclick() {
  FindLocation();
}

window.onload = InitializeMap;

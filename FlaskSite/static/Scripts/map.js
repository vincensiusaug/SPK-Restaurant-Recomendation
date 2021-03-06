var map;
var geocoder;
function InitializeMap() {
  var name = rest;
  var latlng = new google.maps.LatLng(lat, lng);
  var myOptions =
  {
    zoom: 18,
    center: latlng,
    mapTypeId: google.maps.MapTypeId.ROADMAP,
    disableDefaultUI: true
  };
  map = new google.maps.Map(document.getElementById("map"), myOptions);
  var marker = new google.maps.Marker({
    position: latlng,
    map: map,
    title: name
  });

}

window.onload = InitializeMap;

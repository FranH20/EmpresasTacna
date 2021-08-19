const tileProvider = 'https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}'
let mymap = L.map('mapid').setView([-18.01465, -70.25362], 12);
L.tileLayer(tileProvider, {
    attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
    maxZoom: 18,
    id: 'mapbox/streets-v11',
    tileSize: 512,
    zoomOffset: -1,
    accessToken: 'pk.eyJ1IjoiZnJhbmgyMCIsImEiOiJja2Z5c2l4Y3EwNW1sMnFvYm0wMTcyeGhtIn0.eooMrlzfLjBMclV2XbRb4Q'
}).addTo(mymap);
let marker = L.marker(coordenadas).addTo(mymap);
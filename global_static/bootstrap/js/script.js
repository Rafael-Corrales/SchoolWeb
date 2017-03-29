$(function(){
	// var gMap = null;
	// var gMarker = null;
	// var geocoder = null;
	// var gLatLon = null;
	// var mapSetting = null;
	// var LATI = 13.3066233;
	// var LONGI = -87.178852;

	function inicio(){

	//	mostrarMapa(LATI, LONGI);
		alert("funciona");
		var gMap = null;
		var gMarker = null;
		var geocoder = null;
		var gLatLon = null;
		var mapSetting = null;
		var LATI = 13.3066233;
		var LONGI = -87.178852;
		$('#Latitud').val(LATI);
		$('#Longitud').val(LONGI);

		gLatLon = new google.maps.LatLng(LATI, LONGI);
		mapSetting = {
			center: gLatLon,
			zoom: 5,
			mapTypeId: google.maps.MapTypeId.ROADMPAP
		}

		}
		gMap = new google.maps.Map($('#mapa').get(0), mapSetting);


	};

//	function mostrarMapa(lat, lon){
//		$('#Latitud').val(lat);
//		$('#Longitud').val(lon);

//		gLatLon = new google.maps.LatLng(lat, lon);
//
//		gMap = new google.maps.Map($('#mapa').get(0), {
//			center: gLatLon,
//			zoom: 5,
//			mapTypeId: google.maps.MapTypeId.ROADMPAP
//		});


//	};
	inicio();
});
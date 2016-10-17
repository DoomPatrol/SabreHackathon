/* Project specific Javascript goes here. */

/*
Formatting hack to get around crispy-forms unfortunate hardcoding
in helpers.FormHelper:

    if template_pack == 'bootstrap4':
        grid_colum_matcher = re.compile('\w*col-(xs|sm|md|lg|xl)-\d+\w*')
        using_grid_layout = (grid_colum_matcher.match(self.label_class) or
                             grid_colum_matcher.match(self.field_class))
        if using_grid_layout:
            items['using_grid_layout'] = True

Issues with the above approach:

1. Fragile: Assumes Bootstrap 4's API doesn't change (it does)
2. Unforgiving: Doesn't allow for any variation in template design
3. Really Unforgiving: No way to override this behavior
4. Undocumented: No mention in the documentation, or it's too hard for me to find
*/
$('.form-group').removeClass('row');

$(document).ready(function() {
  $('.modal-trigger').leanModal();
});

$('#departDate').on('click', function() {
  $('#departDate').datepicker({dateFormat: "yy-mm-dd"});
});

$('#returnDate').on('click', function() {
  $('#returnDate').datepicker({dateFormat: "yy-mm-dd"});
});


$('.post-form').on('submit', function() {
  $(this).parent('col').empty()
})

$('form').on('submit', function() {
  $('form').serializeArray();
});

$('.travel-search').on('click', function() {
  $('.search-button').attr('value', ($(this).attr('value')));
});


(function($){
    $.fn.serializeObject = function() {
        var data = $(this).serializeArray();
        var obj = {};
        for (i in data) {
        	if (typeof obj[data[i].name] === 'undefined') {
	        	obj[data[i].name] = [];
	        	obj[data[i].name][0] = {};
        		obj[data[i].name][0] = data[i].value;
        	} else {
	        	var l = obj[data[i].name].length;
	        	obj[data[i].name][l] = {};
        		obj[data[i].name][l] = data[i].value;
	        }
        }
        for (i in obj) {
        	if (obj[i].length == 1) {
        		obj[i] = obj[i][0];
        	}

        }
        return obj;
    }
})(jQuery);

$('#searchForm').on('submit', function(e) {
  e.preventDefault();
  console.log(e);
  var origin = $('#origin').val();
  var destination = $('#destination').val();
  var depart_date = $('#departDate').val();
  var return_date = $('#returnDate').val();
  var cust_id = $('.search-button').attr('value');

  console.log(depart_date);

  var main_url = 'http://travelbrain.herokuapp.com/flight/search?origin='+ origin +'&destination='+ destination +'&departuredate='+ depart_date +'&returndate='+ return_date
  console.log(preferences_by_customer);
  if(preferences_by_customer[cust_id] !== undefined){
    if(preferences_by_customer[cust_id][0].alliance === '*O' || preferences_by_customer[cust_id][0].alliance === 'ONEWORLD'){
      main_url = main_url+'&includedcarriers=AA'
    } else if (preferences_by_customer[cust_id][0].alliance === '*S' || preferences_by_customer[cust_id][0].alliance === 'SKYTEAM'){
      main_url = main_url+'&includedcarriers=DL'
    } else if(preferences_by_customer[cust_id][0].alliance === '*A' || preferences_by_customer[cust_id][0].alliance === 'STARALLIANCE'){
      main_url = main_url+'&includedcarriers=UA'
    }
  }
  console.log(main_url);
  $.ajax({
    url: main_url,
    success: function(results) {
      console.log(results);
      $('.modal-body').empty();
      var flight_result = $('#flight-result').clone();
      var flights = [];
      for(i = 0; i < 5; i++){
        flights[i] = {};
        flights[i].passengerName = 'Roman Kalyakin';
        flights[i].pnr = '34MB21';
        flights[i].cust_id = cust_id;
        flights[i].carrier = results.PricedItineraries[i].TPA_Extensions.ValidatingCarrier.Code;
        flights[i].price = {};
        flights[i].price.amount = results.PricedItineraries[i].AirItineraryPricingInfo.ItinTotalFare.TotalFare.Amount;
        flights[i].price.currency = 'USD';
        flights[i].segments = [];
        for(b = 0; c = results.PricedItineraries[i].AirItinerary.OriginDestinationOptions.OriginDestinationOption.length, b < c; b++ ){
          console.log(b);
          flights[i].segments[b] = {};

          flights[i].segments[b].flightNumber = results.PricedItineraries[i].TPA_Extensions.ValidatingCarrier.Code + results.PricedItineraries[i].AirItinerary.OriginDestinationOptions.OriginDestinationOption[b].FlightSegment[0].FlightNumber;
          flights[i].segments[b].aircraftType = results.PricedItineraries[i].AirItinerary.OriginDestinationOptions.OriginDestinationOption[b].FlightSegment[0].Equipment.AirEquipType;
          flights[i].segments[b].departureAirport = results.PricedItineraries[i].AirItinerary.OriginDestinationOptions.OriginDestinationOption[b].FlightSegment[0].DepartureAirport.LocationCode;
          flights[i].segments[b].arrivalAirport = results.PricedItineraries[i].AirItinerary.OriginDestinationOptions.OriginDestinationOption[b].FlightSegment[0].ArrivalAirport.LocationCode;
          flights[i].segments[b].departureTime = results.PricedItineraries[i].AirItinerary.OriginDestinationOptions.OriginDestinationOption[b].FlightSegment[0].DepartureDateTime;
          flights[i].segments[b].arrivalTime = results.PricedItineraries[i].AirItinerary.OriginDestinationOptions.OriginDestinationOption[b].FlightSegment[0].ArrivalDateTime;
        }
        // flights[i].price = results.PricedItineraries[i].AirItineraryPricingInfo.ItinTotalFare.TotalFare.Amount;
        // flights[i].carrier = results.PricedItineraries[i].TPA_Extensions.ValidatingCarrier.Code;
        $(flight_result).css('visibility', 'visible');
        $(flight_result).find('.flight-price').html(results.PricedItineraries[i].AirItineraryPricingInfo.ItinTotalFare.TotalFare.Amount);
        $(flight_result).find('.airline-carrier').html(results.PricedItineraries[i].TPA_Extensions.ValidatingCarrier.Code);
        $(flight_result).find('.booking-button').attr('value', i);
        console.log(results.PricedItineraries[i]);
        $(".modal-body").append(flight_result.clone());
      }

      $('.booking-button').on('click', function(f) {
        f.preventDefault();
        var flight_value = $(this).attr('value');

        trip_object = {
          "customer": "/api/v1/customer/"+cust_id+'/',
          "airfare_cost": parseInt(flights[flight_value].price.amount),
          "carrier": flights[flight_value].carrier,
          "depart_date": flights[flight_value].segments[0].departureTime,
          "return_date": flights[flight_value].segments[1].departureTime,
          "origin": flights[flight_value].segments[0].departureAirport,
          "destination": flights[flight_value].segments[0].arrivalAirport

        }

        $.ajax({
          url: "https://travelbrain.herokuapp.com/conversation/"+flights[flight_value].cust_id,
          type: "POST",
          data: JSON.stringify(flights[flight_value]),
          contentType: "application/json",
          success: function(response){
            console.log(response);
          }
        });

        $.ajax({
          url: 'http://1423edbc.ngrok.io/api/v1/trip/',
          type: "POST",
          contentType: "application/json",
          data: JSON.stringify(trip_object),
          success: function(response){
            console.log(response);
          },
          error: function(er){
            console.log(er);
          }
        });
        console.log(trip_object);


      });
      console.log(flights);
    },
    error: function(err){
      console.log(err);
    }

  });

  console.log(depart_date);
  console.log(origin);
});

jQuery(function ($) {
    'use strict';

    //Responsive Nav
    $('li.dropdown').find('.fa-angle-down').each(function () {
        $(this).on('click', function () {
            if ($(window).width() < 768) {
                $(this).parent().next().slideToggle();
            }
            return false;
        });
    });

    //Fit Vids
    if ($('#video-container').length) {
        $("#video-container").fitVids();
    }

    //Initiat WOW JS
    new WOW().init();

    // portfolio filter
    $(window).load(function () {

        $('.main-slider').addClass('animate-in');
        $('.preloader').remove();
        //End Preloader

        if ($('.masonery_area').length) {
            $('.masonery_area').masonry();//Masonry
        }

        var $portfolio_selectors = $('.portfolio-filter >li>a');

        if ($portfolio_selectors.length) {

            var $portfolio = $('.portfolio-items');
            $portfolio.isotope({
                itemSelector: '.portfolio-item',
                layoutMode: 'fitRows'
            });

            $portfolio_selectors.on('click', function () {
                $portfolio_selectors.removeClass('active');
                $(this).addClass('active');
                var selector = $(this).attr('data-filter');
                $portfolio.isotope({filter: selector});
                return false;
            });
        }

    });


    $('.timer').each(count);
    function count(options) {
        var $this = $(this);
        options = $.extend({}, options || {}, $this.data('countToOptions') || {});
        $this.countTo(options);
    }

    // Search
    $('.fa-search').on('click', function () {
        $('.field-toggle').fadeToggle(200);
    });

    // Contact form
    var form = $('#main-contact-form');
    form.submit(function (event) {
        event.preventDefault();
        var form_status = $('<div class="form_status"></div>');
        $.ajax({
            url: $(this).attr('action'),
            beforeSend: function () {
                form.prepend(form_status.html('<p><i class="fa fa-spinner fa-spin"></i> Email is sending...</p>').fadeIn());
            }
        }).done(function (data) {
            form_status.html('<p class="text-success">Thank you for contact us. As early as possible  we will contact you</p>').delay(3000).fadeOut();
        });
    });

    // Progress Bar
    $.each($('div.progress-bar'), function () {
        $(this).css('width', $(this).attr('data-transition') + '%');
    });

    if ($('#gmap').length) {
        var map;

        map = new GMaps({
            el: '#gmap',
            lat: lat,
            lng: lng,
            scrollwheel: false,
            zoom: 16,
            zoomControl: true,
            searchBox: true,
            panControl: false,
            streetViewControl: false,
            mapTypeControl: false,
            overviewMapControl: false,
            clickable: false
        });

        map.addMarker({
            lat: lat,
            lng: lng,
            animation: google.maps.Animation.DROP,
            verticalAlign: 'bottom',
            horizontalAlign: 'center',
            backgroundColor: '#3e8bff',
        });

        var markers = [];
        var map = map.map;

        // Create the search box and link it to the UI element.
        var input = /** @type {HTMLInputElement} */(
            document.getElementById('pac-input'));
        map.controls[google.maps.ControlPosition.TOP_LEFT].push(input);

        var searchBox = new google.maps.places.SearchBox(
            /** @type {HTMLInputElement} */(input));

        // [START region_getplaces]
        // Listen for the event fired when the user selects an item from the
        // pick list. Retrieve the matching places for that item.
        google.maps.event.addListener(searchBox, 'places_changed', function () {
            var places = searchBox.getPlaces();

            if (places.length == 0) {
                return;
            }
            for (var i = 0, marker; marker = markers[i]; i++) {
                marker.setMap(null);
            }

            // For each place, get the icon, place name, and location.
            markers = [];
            var bounds = new google.maps.LatLngBounds();
            for (var i = 0, place; place = places[i]; i++) {
                console.log(place.geometry.location);
                $('#id_lat').val(place.geometry.location.lat());
                $('#id_lng').val(place.geometry.location.lng());
                var image = {
                    url: place.icon,
                    size: new google.maps.Size(71, 71),
                    origin: new google.maps.Point(0, 0),
                    anchor: new google.maps.Point(17, 34),
                    scaledSize: new google.maps.Size(25, 25)
                };

                // Create a marker for each place.
                var marker = new google.maps.Marker({
                    map: map,
                    icon: image,
                    title: place.name,
                    position: place.geometry.location
                });

                markers.push(marker);

                bounds.extend(place.geometry.location);
            }

            map.fitBounds(bounds);
        });
        // [END region_getplaces]

        // Bias the SearchBox results towards places that are within the bounds of the
        // current map's viewport.
        google.maps.event.addListener(map, 'bounds_changed', function () {
            var bounds = map.getBounds();
            searchBox.setBounds(bounds);
        });
    }

});
jQuery(document).foundation();

// Main Menu
jQuery('.main-ul-nav li .nav-sub-menus').not(jQuery('.nav-sub-wrap .nav-sub-menus')).wrap('<div class="nsw" />');


 window.onscroll = function() {scrollFunction()};

        function scrollFunction() {
            if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
                document.getElementById("BtnTopo").style.display = "block";
            } else {
                document.getElementById("BtnTopo").style.display = "none";
            }
        }

        function topFunction() {
            document.body.scrollTop = 0;
            document.documentElement.scrollTop = 0;
        }



jQuery('.main-ul-nav li .nav-sub-wrap .nsw').each(function(index, element) {
    if (jQuery(element).children().length === 1) {
        if (jQuery(element).children().attr('class') == 'nav-sub-menus') {
            jQuery(element).parents('li').addClass('ord-nav-offset');
            jQuery(element).parent().addClass('ord-nav').removeClass('container');
            jQuery(element).removeClass('row');
        } else {
            jQuery(element).addClass('mm-full');
        }
    }

    if (jQuery(element).children().length === 0) {
        jQuery(element).parent().remove();
    }

    if (jQuery(element).children().length === 2) {
        jQuery(element).find('.nav-sub-posts').addClass('small-9');
        jQuery(element).find('.nav-sub-posts .small-3:last-child').remove();
        jQuery(element).find('.nav-sub-posts .small-3').addClass('small-4').removeClass('small-3');
        jQuery(element).find('.nav-sub-menus').addClass('small-3').insertBefore(jQuery(element).find('.nav-sub-posts'));
        jQuery(element).find('.nav-sub-menus:not(:first-child)').remove();
    }
});

jQuery('.nav-sub-menus > ul > li > .nav-sub-menus').each(function(index, element) {
    jQuery(element).wrap('<div class="nav-sub-wrap ord-nav" />');
    jQuery(element).wrap('<div class="nsw" />');
});


jQuery('.main-ul-nav li').mouseenter(function() {
    jQuery(this).find('> .nav-sub-wrap').show().animate({opacity: 1}, 130);
}).mouseleave(function() {
    jQuery(this).find('> .nav-sub-wrap').animate({opacity: 0}, 130).hide();
});


jQuery(function($) {

    /*
     *  render_map
     *
     *  This function will render a Google Map onto the selected jQuery element
     *
     *  @type	function
     *  @date	8/11/2013
     *  @since	4.3.0
     *
     *  @param	$el (jQuery element)
     *  @return	n/a
     */

    function render_map( $el ) {

        // var
        var $markers = $el.find('.marker');

        // vars
        var args = {
            zoom		: 7,
            center		: new google.maps.LatLng(0, 0),
            scrollwheel : false,
            //disableDefaultUI: false,
            panControl  : true,
            zoomControl : true,
            scaleControl: true,
            streetViewControl: false,
            overviewMapControl: true,
            rotateControl: false,
            mapTypeId	: google.maps.MapTypeId.ROADMAP
        };

        // create map
        var map = new google.maps.Map( $el[0], args);

        // add a markers reference
        map.markers = [];

        // add markers
        $markers.each(function(){

            add_marker( jQuery(this), map );

        });

        // center map
        center_map( map );

    }

    /*
     *  add_marker
     *
     *  This function will add a marker to the selected Google Map
     *
     *  @type	function
     *  @date	8/11/2013
     *  @since	4.3.0
     *
     *  @param	$marker (jQuery element)
     *  @param	map (Google Map object)
     *  @return	n/a
     */

    function add_marker( $marker, map ) {

        // var
        var latlng = new google.maps.LatLng( $marker.attr('data-lat'), $marker.attr('data-lng') );

        // create marker
        var marker = new google.maps.Marker({
            position	: latlng,
            map			: map
        });

        // add to array
        map.markers.push( marker );

        // if marker contains HTML, add it to an infoWindow
        if( $marker.html() )
        {
            // create info window
            var infowindow = new google.maps.InfoWindow({
                content		: $marker.html()
            });

            // show info window when marker is clicked
            google.maps.event.addListener(marker, 'click', function() {

                infowindow.open( map, marker );

            });
        }

    }

    /*
     *  center_map
     *
     *  This function will center the map, showing all markers attached to this map
     *
     *  @type	function
     *  @date	8/11/2013
     *  @since	4.3.0
     *
     *  @param	map (Google Map object)
     *  @return	n/a
     */

    function center_map( map ) {

        // vars
        var bounds = new google.maps.LatLngBounds();

        // loop through all markers and create bounds
        $.each( map.markers, function( i, marker ){

            var latlng = new google.maps.LatLng( marker.position.lat(), marker.position.lng() );

            bounds.extend( latlng );

        });

        // only 1 marker?
        if( map.markers.length == 1 )
        {
            // set center of map
            map.setCenter( bounds.getCenter() );
            map.setZoom( 15 );
        }
        else
        {
            // fit to bounds
            map.fitBounds( bounds );
        }

    }


    jQuery(document).ready(function(){

        jQuery('.acf-map').each(function(){

            render_map( jQuery(this) );

        });

        /* CONFIGURA A BUSCA POR AREA CULTURAL - só aparece se o campo artistas estiver marcado */
        $("#areacultural").hide();
        $( 'select[name="post_type"]').change(function() {
            var campo = $('select[name="post_type"] option:selected').val();
            if(campo=="artista") {
                $("#areacultural").show();
            } else {
                $("#areacultural").hide();
                $('select[name="category_name"]').val('');

            }
        })

    });

});


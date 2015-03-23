var call_status = document.getElementById("call_status");

function make_call(phone_number) {
    $.ajax({
        url: "/api/call", // the endpoint
        type: "POST", // http method
        data: {to_number: phone_number}, // data sent with the post request

        // handle a successful response
        success: function (json) {
            console.log(json); // log the returned json to the console
            console.log("success"); // another sanity check
            check_call_status(json.sid, $("#call_status"));
        }
    })
}


function check_call_status(sid, elm) {
    $.ajax({
        url: "/api/call/" + sid, // the endpoint
        type: "GET", // http method

        // handle a successful response
        success: function (json) {
            console.log(json);
            call_status.innerHTML = json.status;
            if (json.status != "completed") {
                setTimeout(function() {check_call_status(sid, elm);}, 500)
            } else {
                update_greeting();
            }
        }

    })

}

function update_greeting() {
    $.ajax({
        url: "/api/greeting/current",
        type: "GET", // http method

        // handle a successful response
        success: function (json) {
            console.log(json);
            document.getElementById("greeting_div").innerHTML = '<audio controls><source src="'+ json.greeting_url + '" type="audio/ogg" id="greeting_file"></audio>';
        }

    })
}

var csrftoken = $.cookie('csrftoken');

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
function sameOrigin(url) {
    // test that a given url is a same-origin URL
    // url could be relative or scheme relative or absolute
    var host = document.location.host; // host + port
    var protocol = document.location.protocol;
    var sr_origin = '//' + host;
    var origin = protocol + sr_origin;
    // Allow absolute or scheme relative URLs to same origin
    return (url == origin || url.slice(0, origin.length + 1) == origin + '/') ||
        (url == sr_origin || url.slice(0, sr_origin.length + 1) == sr_origin + '/') ||
        // or any other URL that isn't scheme relative or absolute i.e relative.
        !(/^(\/\/|http:|https:).*/.test(url));
}
$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && sameOrigin(settings.url)) {
            // Send the token to same-origin, relative URLs only.
            // Send the token only if the method warrants CSRF protection
            // Using the CSRFToken value acquired earlier
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});

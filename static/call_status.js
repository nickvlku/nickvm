var call_status = document.getElementById("call_status");

swampdragon.onChannelMessage(function (channels, message) {
    console.log("in here");
    call_status.innerHTML = message.data.status;
});


swampdragon.ready(function() {
    swampdragon.subscribe('calls', 'call_status', null);
    console.log("woot");

});
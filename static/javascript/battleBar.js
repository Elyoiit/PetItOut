<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.3/jquery.min.js"/>

var x = null;
function moveBlue(){
if(x==null){
  var blueBar = document.getElementsByClassName("progress-bar");
  
  var parentWidth = $('.progress-bar').offsetParent().width();
  var width = $('.progress-bar').width();
  var i = Math.round(100*width/parentWidth);
      var write =  parseInt($("#vnums-l").text())+1;
      var writeString = write.toString();
   
      document.getElementById("vnums-l").innerHTML=writeString;      
      var oppo = parseInt($("#vnums-r").text());      
      var result = write/(write+oppo)*100;
      alert(result)
      $("#progress-bar").css("width", result+"%");
      
}
else{
alert("can only vote once!");
}
}

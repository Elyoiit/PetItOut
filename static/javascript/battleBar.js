<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.3/jquery.min.js"/>

var x = null;
$('vnums_b').click(function(){
    $.ajax({
        type:"POST",
        url:"{% url 'PetItOut:battle' battle_view.petprofileBlue.userprofile.user.username%}",
        data:{'content_id': $(this).attr('name'),'operation':'like_submit_blue','csrfmiddlewaretoken': '{{ csrf_token }}'},
        dataType:"json",
        success:function(){moveBlue()}
    });

        function moveBlue(){
            {
            if(x==null){
            var blueBar = document.getElementsByClassName("progress-bar");
            
            var parentWidth = $('.progress-bar').offsetParent().width();
            var width = $('.progress-bar').width();
            var i = Math.round(100*width/parentWidth);
                var write =  parseInt($("#vnums-l").text())+1;
                var writeString = write.toString();
                    x=1;
                document.getElementById("vnums-l").innerHTML=writeString;      
                var oppo = parseInt($("#vnums-r").text());      
                var result = write/(write+oppo)*100;
                $("#progress-bar").css("width", result+"%");
                
            }
            else{
            alert("can only vote once!");
            }
        }
    }
});
    
$('vnums_red').click(function(){
$.ajax({
        type:"POST",
        url:"{% url 'PetItOut:battle' battle_view.petprofileRed.userprofile.user.username%}",
        data:{'content_id': $(this).attr('name'),'operation':'like_submit_red','csrfmiddlewaretoken': '{{ csrf_token }}'},
        dataType:"json",
        success:
            function(){ moveRed()}
            });
        
        function moveRed(){
        if(x==null){
            var blueBar = document.getElementsByClassName("progress-bar");
            x=1;
            var parentWidth = $('.progress-bar').offsetParent().width();
            var width = $('.progress-bar').width();
            var i = Math.round(100*width/parentWidth);
                var write =  parseInt($("#vnums-r").text())+1;
                var writeString = write.toString();
            
                document.getElementById("vnums-r").innerHTML=writeString;      
                var oppo = parseInt($("#vnums-l").text());      
                var result = oppo/(write+oppo)*100;
                $("#progress-bar").css("width", result+"%");
            }
            else{
            alert("can only vote once!");
            }
            }
        });
        function moveRed(){
        if(x==null){
            var blueBar = document.getElementsByClassName("progress-bar");
            x=1;
            var parentWidth = $('.progress-bar').offsetParent().width();
            var width = $('.progress-bar').width();
            var i = Math.round(100*width/parentWidth);
                var write =  parseInt($("#vnums-r").text());
                var writeString = write.toString();
            
                document.getElementById("vnums-r").innerHTML=writeString;      
                var oppo = parseInt($("#vnums-l").text());      
                var result = oppo/(write+oppo)*100;
                $("#progress-bar").css("width", result+"%");
            }
            else{
            alert("can only vote once!");
            }
            }
        function moveBlue(){
            {
            if(x==null){
            var blueBar = document.getElementsByClassName("progress-bar");
            
            var parentWidth = $('.progress-bar').offsetParent().width();
            var width = $('.progress-bar').width();
            var i = Math.round(100*width/parentWidth);
                var write =  parseInt($("#vnums-l").text());
                var writeString = write.toString();
                    x=1;
                document.getElementById("vnums-l").innerHTML=writeString;      
                var oppo = parseInt($("#vnums-r").text());      
                var result = write/(write+oppo)*100;
                $("#progress-bar").css("width", result+"%");
                
            }
            else{
            alert("can only vote once!");
            }
        }
    }
    

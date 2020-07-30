var url = '/home/';
console.log("csrf",csrftoken);
$(document).ready(function(){
    var div = $("#scrollel");
    var pos = div.position();
    $(window).scroll(function () {
        // console.log("windowpos,pos",windowpos,pos);
     var windowpos = $(window).scrollTop();
     if (windowpos >= (pos.top-600)) {
       getData(result);
     }
     else {
       
     }
    
   });
  });


// getData(result)
function getData(result_value){
    fetch(url, {
        method: 'POST', 
        headers: {
          'Content-Type': 'application/json',
           'X-CSRFToken':csrftoken,
        },
       
        body: JSON.stringify({'result':result_value}) 
      }).then(response => response.json())
      .then(data => {
        console.log('Success:', data);
        result =result_value + 3;
        json_data = JSON.parse(data);
        for(var i = 0;i<json_data.length;i++){
            addToDOM(json_data[i]);
        }
        
      })
      .catch((error) => {
        console.log('Error:', error);
      });
      
    }


    function addToDOM(json_data){
        console.log('json_data ',json_data);
        
    }

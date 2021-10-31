$(document).ready(function () {
  $(".TitleBar ul li ").click(function (e) { 
    //e.preventDefault();
    
    x = $(this).data('s');
    
    $("#"+x).siblings("div").addClass('none');
    $("#"+x).removeClass("none")
    
     
    
    
  });  
  $(".submit2").click(function (e) { 
    e.preventDefault();
    
    x = $(this).data('s');
    
    $("#"+x).siblings("div").addClass('none');
    $("#"+x).removeClass("none")
    
     
    
    
  });  

$("textarea").dblclick(function (e) { 
  e.preventDefault();
  console.log("Bengo");
  $(this).attr("readonly", false);
  if ($('#EditSubmit').length === 0) {
    $("p[class='Comment']").append('<input class="submit" id="EditSubmit" name="Submit" type="submit" value="Edit">');
};



});


$(".demo").click(function (e) { 
  console.log(e);

  
  
});  
  



});
//end Ready

function Clone(id , to) {
  return function() {
      console.log("HOPE");
      
      x= $("#"+id).clone()

      x.find("tbody tr td ").each(function (i,e ) { 
        e.firstElementChild.value = ""
      });
      x.appendTo("#"+to);
           };
}


$("#clone0").click(Clone("Text" , "TextDiv" ));
$("#clone1").click(Clone("Link" , "LinkDiv" ));

var slideIndex = 1;
showSlides(slideIndex);

function plusSlides(n) {
  showSlides(slideIndex += n);
}

function currentSlide(n) {
  showSlides(slideIndex = n);
}

function showSlides(n) {
  var i;
  var slides = document.getElementsByClassName("mySlides");
  var dots = document.getElementsByClassName("demo");
  var captionText = document.getElementById("caption");
  if (n > slides.length) {slideIndex = 1}
  if (n < 1) {slideIndex = slides.length}
  for (i = 0; i < slides.length; i++) {
      slides[i].style.display = "none";
  }
  for (i = 0; i < dots.length; i++) {
      dots[i].className = dots[i].className.replace(" active", "");
  }
  slides[slideIndex-1].style.display = "block";
  dots[slideIndex-1].className += " active";
  captionText.innerHTML = dots[slideIndex-1].alt;
};


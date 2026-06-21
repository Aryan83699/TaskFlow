const button=document.getElementById('submitButton');

button.addEventListener('mouseenter',function(){
   button.style.border="2px solid pink";

})

button.addEventListener('mouseleave',function(){
    button.style.border=null;
})
//event listener to enable and disable the post button
const caption = document.getElementById('caption')
const postimage = document.getElementById('postimage')
const postbutton = document.getElementById('post')

postimage.addEventListener('change', ()=>{
    postbutton.classList.replace('bg-gray-100', 'bg-blue-600')
    postbutton.classList.replace('text-black', 'text-white')
    postbutton.disabled = false  
})  

caption.addEventListener('keyup', (a)=>{
    const value = a.currentTarget.value;
    if(value==""){
        postbutton.classList.replace('bg-blue-600','bg-gray-100')
        postbutton.classList.replace('text-white', 'text-black')
        postbutton.disabled = true
    }
    else{
        postbutton.classList.replace('bg-gray-100', 'bg-blue-600')
        postbutton.classList.replace('text-black', 'text-white')
        postbutton.disabled = false     
    }
})

//clear all entry in form on click cancel button
const cancelbutton = document.getElementById('cancelbutton')
const formdiv = document.getElementById('post_button')
const postbutton1 = document.getElementById('post')

cancelbutton.addEventListener('click', ()=>{
    formdiv.reset()
    postbutton.disabled = true
    postbutton1.classList.replace('bg-blue-400','bg-gray-100')    
})

//eventlistener to display delete post option or follow option
const postdiv = document.getElementsByClassName('postdiv')
const dottedline = document.getElementsByClassName('postoption')
const delete_post = document.getElementsByClassName('deletepost')

for(var i=0;i<postdiv.length;i++){

    function someFunc(i){
        dottedline[i].addEventListener('click', ()=>{
        delete_post[i].classList.toggle('opacity-0')
        })}
    
    someFunc(i);
}

//event listener for like button
const like_button = document.getElementsByClassName('like_button')
const postdivi = document.getElementsByClassName('postdiv')
const form = document.getElementsByClassName('like')


for(var e=0;e<postdivi.length;e++){
    function somefunction(index){
        like_button[index].addEventListener('click',()=>{
    
        like_button[index].classList.toggle("text-blue-500");
    })
    }
    somefunction(e);
}




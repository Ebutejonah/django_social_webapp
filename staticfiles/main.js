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
    if(value=="" ){
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
    postbutton.disabled = true
    postbutton.classList.replace('text-white', 'text-black')
    postbutton1.classList.replace('bg-blue-600','bg-gray-100')
    formdiv.reset()       
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


//toggle functionality for light/dark modes
const sunIcon = document.getElementById("sun");
const moonIcon = document.getElementById("moon");

const userTheme = localStorage.getItem("theme");
const systemTheme = window.matchMedia("(prefered-color-scheme: dark)").matches;

const iconToggle = ()=>{
    sunIcon.classList.toggle("hidden");
    moonIcon.classList.toggle("hidden");
};

const themeCheck = ()=>{
    if(userTheme === "dark" || (!userTheme && systemTheme)){
        document.documentElement.classList.add("dark");
        moonIcon.classList.add("hidden");
        return;
    }
    sunIcon.classList.add("hidden");
};

const themeSwitch = ()=> {
    if (document.documentElement.classList.contains("dark")){
        document.documentElement.classList.remove("dark");
        localStorage.setItem("theme", "Light");
        iconToggle();
        return;
    }
    document.documentElement.classList.add("dark");
    localStorage.setItem("theme", "dark");
    iconToggle();
};

sunIcon.addEventListener("click", ()=>{
    themeSwitch();
});

moonIcon.addEventListener("click", ()=>{
    themeSwitch();
});

themeCheck();

//displaying selected image before posting
/*function readURL(input){
    if (input.files && input.files[0]){

        var reader = new FileReader();
        reader.onload = function(e){
            $('#blah').attr('src', e.target.result).width(200).height(full).border(999);

        };
        reader.readAsDataURL(input.files[0]);
    }
} in html onchange="readURL(this)";*/
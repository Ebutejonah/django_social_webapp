// let other_profiles = document.getElementsByClassName('other_profiles')
// let option = document.getElementsByClassName('follow')
// let followed = document.getElementsByClassName('followed')
// const follow_btn = document.getElementsByClassName('follow_btn')
// let profiles_usernames = []
// let profiles = "{{suggest}}"
// let new_profiles = profiles.replace(/&#x27;/ig, '"')
// let final_profiles = new_profiles.replace(/UUID/ig, '')
// let last_profiles = final_profiles.replaceAll('(', '')
// let finite_profiles = last_profiles.replaceAll(')', '')
// let end_profiles = finite_profiles.replace(/datetime.datetime/ig, '"datetime.datetime')
// let total_profiles = end_profiles.replace(/utc/ig, 'utc"')
// let totals = total_profiles.replace(/None/ig, '""')
// let js_profiles = JSON.parse(totals)

// for(i=0;i<other_profiles.length;i++){
//     let profile_username = js_profiles[i]["username"]
//     profiles_usernames.push(profile_username)
// }

// for(i=0;i<other_profiles.length;i++){
//     function follow(i){
//         follow_btn[i].addEventListener('click',()=>{
//             let data = {username:profiles_usernames[i]}
//             console.log(totals)
//             console.log(profiles_usernames)
//             fetch("{%url 'follow'%}",{
//                 method: "POST",
//                 headers: {"Content-Type":"application/json",
//                         "X-CSRFToken": csrftoken},
//                 body: JSON.stringify(data),
//             })
//             .then(function(response){
//                 responseClone = response.clone()
//                 return response.json()
//             })
//             .then(function(data){
//             console.log(data)
//             if (data['checker']==1){
//                 follow_btn[i].classList.add('hidden')
//                 followed[i].innerHTML = "Following"
                    
//             }
//             else if (data['checker']==0){
//                 option[i].classList.remove("bg-red-400","hover:bg-red-500")
//                 option[i].classList.add("bg-blue-500","hover:bg-blue-600")
//                 option[i].innerHTML = "Follow"
//             }
//             },function(rejectionReason){
//             console.log("Error parson JSON from response:",rejectionReason, responseClone)
//             responseClone.text()
//             .then(function(bodyText){
//                 console.log("Received the following instead of valid JSON:", bodyText)
//             })
//         })
//         })
//     }
// follow(i)
// }


// function getCookie(name) {
    // let cookieValue = null;
    // if (document.cookie && document.cookie !== '') {
    //     const cookies = document.cookie.split(';');
    //     for (let i = 0; i < cookies.length; i++) {
    //         const cookie = cookies[i].trim();
    //         // Does this cookie string begin with the name we want?
    //         if (cookie.substring(0, name.length + 1) === (name + '=')) {
    //             cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
    //             break;
    //         }
    //     }
    // }
    // return cookieValue;
    // }
    // const csrftoken = getCookie('csrftoken');

    // let user = '{{user_object.username}}'
    // const follow_btn = document.getElementById('follow')
    // const unfollow_btn = document.getElementById('unfollow')
    // const num_of_followers = document.getElementById('num_of_followers')
    // let url = "{%url 'follow'%}"
    // const follow_btn1 = document.getElementById('follow_button')
    // function follow(){
    // follow_btn1.addEventListener('click', ()=>{
           
    //     let data = {username:user}
    //     fetch(url,{
    //         method: "POST",
    //         headers: {"Content-Type":"application/json",
    //                 "X-CSRFToken": csrftoken},
    //         body: JSON.stringify(data),
    //     })
    //     .then(function (response){
    //         responseClone = response.clone()
    //         return response.json()
    //     })
    //     .then(function(data){
    //         console.log(data)
    //         if (data['checker']==1){
    //             follow_btn.classList.remove("bg-blue-500","hover:bg-blue-600")
    //             follow_btn.classList.add("bg-red-400","hover:bg-red-500")
    //             follow_btn.innerHTML = "Unfollow"
    //         }
    //         else if (data['checker']==0){
    //             follow_btn.classList.remove("bg-red-400","hover:bg-red-500")
    //             follow_btn.classList.add("bg-blue-500","hover:bg-blue-600")
    //             follow_btn.innerHTML = "Follow"
    //         }
    //         if (data['num_of_followers']==0){
    //             num_of_followers.innerHTML = data['num_of_followers'] + " followers"
    //         }
    //         if (data['num_of_followers']==1){
    //             num_of_followers.innerHTML = data['num_of_followers'] + " follower"
    //         }
    //         else{
    //             num_of_followers.innerHTML = data['num_of_followers'] + " followers"
    //         }
    //     },function(rejectionReason){
    //         console.log("Error parson JSON from response:",rejectionReason, responseClone)
    //         responseClone.text()
    //         .then(function(bodyText){
    //             console.log("Received the following instead of valid JSON:", bodyText)
    //         })
    //     })
    // })
 
    // }
    // follow()
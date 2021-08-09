const usernameField = document.querySelector('#usernameField');
const feedbackArea = document.querySelector('.invalid-feedback');

usernameField.addEventListener('keyup', (e)=>{
    const usernameVal = e.target.value;

    username.classlist.remove('is-invalid');
    feedbackArea.style.display = 'none';

    if(username.length > 0){
        d = fetch('/authentication/validate-username',
        {body : JSON.stringify({username : usernameVal}),
        method : 'POST'}
        ).then(res => res.json())
        .then(data => {
            if(data.username_error){
                username.classlist.add('is-invalid');
                feedbackArea.style.display = 'block';
                feedbackArea.innerHTML = `<p>${data.username_error}</p>`
            }
        });
    }

})
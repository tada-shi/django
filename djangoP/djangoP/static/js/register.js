const usernameField = document.querySelector('#usernameField');
const usernameFeedbackArea = document.querySelector('.usernameFeedbackArea');
const emailField = document.querySelector('#emailField');
const emailFeedbackArea = document.querySelector('.emailFeedBackArea');
const usernameSuccessOutput = document.querySelector('.usernameSuccessOutput');
const emailSuccessOutput = document.querySelector('.emailSuccessOutput');
const showPasswordToggle = document.querySelector('.showPasswordToggle');
const passwordField = document.querySelector('#passwordField');
const submitBtn = document.querySelector('.submit-btn');

const handlePowerToggle = (e) => {
    if(showPasswordToggle.textContent == 'SHOW'){
        showPasswordToggle.textContent = 'HIDE';
        passwordField.setAttribute('type', 'text')
    }else{
        showPasswordToggle.textContent = 'SHOW';
        passwordField.setAttribute('type' , 'password')
    }
}

usernameField.addEventListener('keyup', (e)=>{
    usernameSuccessOutput.style.display = 'block';
    const usernameVal = e.target.value;
    usernameSuccessOutput.textContent = `${usernameVal}`;

    usernameField.classList.remove('is-invalid');
    usernameFeedbackArea.style.display = 'none';

    if(usernameVal.length > 0){
        d = fetch('/authentication/validate-username',
        {body : JSON.stringify({username : usernameVal}),
        method : 'POST'}
        ).then(res => res.json())
        .then(data => {
            usernameSuccessOutput.style.display = 'none';
            if(data.username_error){
                submitBtn.setAttribute('disable', 'disable')
                usernameField.classList.add('is-invalid');
                usernameFeedbackArea.style.display = 'block';
                usernameFeedbackArea.innerHTML = `<p>${data.username_error}</p>`
            }
        });
    }

})

emailField.addEventListener('keyup', (e)=>{
    emailSuccessOutput.style.display = 'block';
    const emailVal = e.target.value;
    emailSuccessOutput.textContent = `${emailVal}`;

    emailField.classList.remove('is-invalid');
    emailFeedbackArea.style.display = 'none';

    if(emailVal.length > 0){
        d = fetch('/authentication/validate-email',
        {body : JSON.stringify({email : emailVal}),
        method : 'POST'}
        ).then(res => res.json())
        .then(data => {
            emailSuccessOutput.style.display = 'none';
            if(data.email_error){
                submitBtn.setAttribute('disable', 'disable')
                emailField.classList.add('is-invalid');
                emailFeedbackArea.style.display = 'block';
                emailFeedbackArea.innerHTML = `<p>${data.email_error}</p>`
            }
        });
    }

})

showPasswordToggle.addEventListener('click', handlePowerToggle);

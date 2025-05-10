// Password toggle functionality
const togglePassword = document.getElementById('toggle-password');
const passwordDisplay = document.getElementById('password-display');
const passwordDiv = document.querySelector('.pass');
const actualPassword = passwordDiv.textContent;
let passwordVisible = false;

togglePassword.addEventListener('click', function() {
    if (passwordVisible) {
        passwordDisplay.textContent = '*********';
        togglePassword.innerHTML = '<i class="fas fa-eye"></i>';
    } else {
        passwordDisplay.textContent = actualPassword;
        togglePassword.innerHTML = '<i class="fas fa-eye-slash"></i>';
    }
    passwordVisible = !passwordVisible;
});

// Back link animation
const backLink = document.querySelector('.back-link');
backLink.addEventListener('mouseover', function() {
    this.style.color = '#ff8c00';
    this.style.transform = 'translateX(-5px)';
});

backLink.addEventListener('mouseout', function() {
    this.style.color = '#333';
    this.style.transform = 'translateX(0)';
});


const cb1 = document.getElementById('cb1');
const cb2 = document.getElementById('cb2');
const cb3 = document.getElementById('cb3');
const deleteBtn = document.getElementById('deleteBtn');
const warning = document.getElementById('warning');
const userEmail = document.getElementById('user-email').innerText.trim();
const inputEmail = document.getElementById('input-email');
const mismatchMsg = document.getElementById('mismatch-msg');

function checkAll() {
    const emailMatches = inputEmail.value.trim() === userEmail;
    const checkboxesChecked = cb1.checked && cb2.checked && cb3.checked;

    if (!emailMatches) {
        mismatchMsg.style.display = 'block';
    } else {
        mismatchMsg.style.display = 'none';
    }

    if (checkboxesChecked && emailMatches) {
        deleteBtn.disabled = false;
        warning.style.display = 'none';
    } else {
        deleteBtn.disabled = true;
        warning.style.display = checkboxesChecked ? 'none' : 'block';
    }
}

cb1.addEventListener('change', checkAll);
cb2.addEventListener('change', checkAll);
cb3.addEventListener('change', checkAll);
inputEmail.addEventListener('input', checkAll);
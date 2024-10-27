function showSignUp() {
  document.getElementById("signInForm").classList.add("hidden");
  document.getElementById("signUpForm").classList.remove("hidden");
  document.querySelector(".right h2").innerText = "Welcome Back!";
  document.querySelector(".right p").innerText =
    "If you already have an account";
  document.querySelector(".right .btn").innerText = "SIGN IN";
  document.querySelector(".right .btn").setAttribute("onclick", "showSignIn()");
}

function showSignIn() {
  document.getElementById("signUpForm").classList.add("hidden");
  document.getElementById("signInForm").classList.remove("hidden");
  document.querySelector(".right h2").innerText = "Hello, User!";
  document.querySelector(".right p").innerText = "If you don't have an account";
  document.querySelector(".right .btn").innerText = "CREATE AN ACCOUNT";
  document.querySelector(".right .btn").setAttribute("onclick", "showSignUp()");
}

function validateForm() {
  const inputs = document.querySelectorAll("#signUpForm input");
  let valid = true;
  const password = document.getElementById("password").value;
  const confirmPassword = document.getElementById("confirmPassword").value;
  const commonPasswords = [
    "password",
    "123456",
    "123456789",
    "12345678",
    "12345",
    "1234567",
    "password1",
    "qwerty",
    "abc123",
    "111111",
  ];
  let passwordErrors = [];

  inputs.forEach((input) => {
    if (!input.checkValidity()) {
      valid = false;
      input.style.borderColor = "#f44336";
    } else {
      input.style.borderColor = "#ccc";
    }
  });

  if (password !== confirmPassword) {
    valid = false;
    document.getElementById("confirmPassword").style.borderColor = "#f44336";
    passwordErrors.push("Passwords do not match.");
  }

  if (!validatePassword(password)) {
    valid = false;
    document.getElementById("password").style.borderColor = "#f44336";
    passwordErrors.push(
      "Password must be at least 8 characters long, contain uppercase and lowercase letters, a digit, a special character, and no spaces."
    );
  }

  if (commonPasswords.includes(password.toLowerCase())) {
    valid = false;
    document.getElementById("password").style.borderColor = "#f44336";
    passwordErrors.push("Password is too common.");
  }

  if (valid) {
    document.getElementById("alert").style.display = "none";
    showAlert();
  } else {
    document.getElementById("alert").innerText = passwordErrors.join(" ");
    document.getElementById("alert").style.display = "block";
  }
}

function validatePassword(password) {
  const minLength = 8;
  const hasUpperCase = /[A-Z]/.test(password);
  const hasLowerCase = /[a-z]/.test(password);
  const hasDigit = /[0-9]/.test(password);
  const hasSpecialChar = /[!@#$%^&*(),.?":{}|<>]/.test(password);
  const hasNoSpaces = !/\s/.test(password);

  return (
    password.length >= minLength &&
    hasUpperCase &&
    hasLowerCase &&
    hasDigit &&
    hasSpecialChar &&
    hasNoSpaces
  );
}

function showAlert() {
  const alert = document.getElementById("alert");
  alert.innerText = "Account created successfully!";
  alert.style.display = "block";
  setTimeout(function () {
    alert.style.display = "none";
  }, 3000);
}

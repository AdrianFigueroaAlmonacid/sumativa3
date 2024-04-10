const formularioDgames = document.getElementById("form-cinetopia");

const inputName = document.getElementById("inputName");
const inputLastName = document.getElementById("inputLastName");
const inputUser = document.getElementById("inputUser");
const inputEmail = document.getElementById("inputEmail");
const inputPassword = document.getElementById("inputPassword");
const inputPassword2 = document.getElementById("inputPassword2");
const alertSuccess = document.getElementById("alertSuccess");
const alertName = document.getElementById("nombre-error");
const alertLastName = document.getElementById("apellido-error");
const alertPass = document.getElementById("password2-error");

const regUserName = /^[A-Za-zÑñÁáÉéÍíÓóÚúÜü\s]+$/;
const regPass = /^(?=.*[A-Z])(?=.*\d).+$/;

const mensajeExito = () => {
    alertSuccess.classList.remove("d-none");
    alertSuccess.textContent = "Mensaje enviado con éxito";
};

function limpiarInput() {
    let inputs = document.querySelectorAll('.form-control');
    inputs.forEach(function (input) {
        input.value = '';
        input.classList.remove("is-valid");
        input.classList.remove("is-invalid");
        alertSuccess.classList.add("d-none");
    });
}

document.getElementById('botonLimpiar').addEventListener('click', limpiarInput);

formularioDgames.addEventListener("submit", (e) => {
    e.preventDefault();
    alertSuccess.classList.add("d-none");

    // Limpiar mensajes de error
    alertName.textContent = '';
    alertLastName.textContent = '';
    alertPass.textContent = '';

    // Validar nombre
    const valorInputName = inputName.value.trim();
    if (regUserName.test(valorInputName) && valorInputName.length > 0) {
        console.log("El nombre contiene solo letras y no está vacío.");
        inputName.classList.remove("is-invalid");
        inputName.classList.add("is-valid");
    } else {
        alertName.textContent = 'El nombre está vacío o no cumple con el formato de letras';
        console.log("El nombre está vacío o no cumple con el formato de letras.");
        inputName.classList.add("is-invalid");
    }

    // Validar apellido
    const valorInputLastName = inputLastName.value.trim();
    if (regUserName.test(valorInputLastName) && valorInputLastName.length > 0) {
        console.log("El apellido contiene solo letras y no está vacío.");
        inputLastName.classList.remove("is-invalid");
        inputLastName.classList.add("is-valid");
    } else {
        alertLastName.textContent = 'El apellido está vacío o no cumple con el formato de letras';
        console.log("El apellido está vacío o no cumple con el formato de letras.");
        inputLastName.classList.add("is-invalid");
    }

    // Validar correo electrónico y usuario
    const inputs = [inputUser, inputEmail];
    inputs.forEach(function (input) {
        if (input.value.trim().length > 0) {
            input.classList.add("is-valid");
        } else {
            input.classList.add("is-invalid");
        }
    });

    // Validar contraseña
    if (inputPassword.value.trim() === inputPassword2.value.trim() && regPass.test(inputPassword.value.trim())) {
        console.log("contraseña ok");
        inputPassword.classList.add("is-valid");
        inputPassword2.classList.add("is-valid");
    } else {
        inputPassword2.classList.add("is-invalid");
        alertPass.textContent = 'Contraseña incorrecta';
        console.log("contraseña mal");
    }

    // Verificar si hay algún campo inválido
    const camposInvalidos = document.querySelectorAll('.is-invalid');
    if (camposInvalidos.length === 0) {
        console.log("Formulario enviado con éxito");
        mensajeExito();
        // Enviar formulario si no hay campos inválidos
        formularioDgames.submit();
    }
});


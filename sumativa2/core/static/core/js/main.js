const formularioDgames = document.getElementById("form-cinetopia");

const inputName = document.getElementById("inputName");
const inputLastName = document.getElementById("inputLastName");
const inputUser = document.getElementById("inputUser");
const inputEmail = document.getElementById("inputEmail");
const inputPassword = document.getElementById("inputPassword");
const inputPassword2 = document.getElementById("inputPassword2");
const inputDate = document.getElementById("inputDate");
const inputAddress = document.getElementById("inputAddress");



const alertSuccess = document.getElementById("alertSuccess");
const alertName = document.getElementById("alertName");
const alertLastName = document.getElementById("alertLastName");
const alertPass = document.getElementById("alertPass");


// const alertEmail = document.getElementById("alertEmail");

const regUserName = /^[A-Za-zÑñÁáÉéÍíÓóÚúÜü\s]+$/;
// const regUserEmail = /^[a-z0-9]+(\.[_a-z0-9]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,15})$/;
const regPass = /^(?=.*[A-Z])(?=.*\d).+$/;

const mensajeExito = () => {
    alertSuccess.classList.remove("d-none");
    alertSuccess.textContent = "Mensaje enviado con éxito";
};

// const mensajeError = (errores) => {
//     errores.forEach((item) => {
//         item.tipo.classList.remove("d-none");
//         item.tipo.textContent = item.msg;
//     });
// };

formularioDgames.addEventListener("submit", (e) => {
    e.preventDefault();

    alertSuccess.classList.add("d-none");
    // const errores = [];

    document.getElementById('nombre-error').innerHTML = '';
    document.getElementById('apellido-error').innerHTML = '';
    document.getElementById('password2-error').innerHTML = '';


    // VALIDAR NOMBRE
    const valorInput = inputName.value.trim();

    if (regUserName.test(valorInput) && valorInput.length > 0) {

        console.log("El nombre contiene solo letras y no está vacío.");
        inputName.classList.remove("is-invalid");
        inputName.classList.add("is-valid");
        // alertName.classList.add("d-none");

    } else {
        document.getElementById('nombre-error').innerHTML = 'El nombre está vacío o no cumple con el formato de letras';

        console.log("El nombre está vacío o no cumple con el formato de letras.");
        inputName.classList.add("is-invalid");
        errores.push({
            tipo: alertName,
            msg: "Formato no válido campo apellido, solo letras",
        });

    }


    // VALIDAR APELLIDO
    const valorInput2 = inputLastName.value.trim();
    if (regUserName.test(valorInput2) && valorInput2.length > 0) {

        console.log("El nombre contiene solo letras y no está vacío.");
        inputLastName.classList.remove("is-invalid");
        inputLastName.classList.add("is-valid");
        // alertLastName.classList.add("d-none");

    } else {
        document.getElementById('apellido-error').innerHTML = 'El apellido está vacío o no cumple con el formato de letras';

        console.log("El apellido está vacío o no cumple con el formato de letras.");
        inputLastName.classList.add("is-invalid");
        errores.push({
            tipo: alertLastName,
            msg: "Formato no válido campo apellido, solo letras",
        });

    }


    // VALIDAR MAIL y USER

    let inputs = document.querySelectorAll('.form-control');

    inputs.forEach(function (input) {
        if (input.value.trim().length > 0) {
            input.classList.add("is-valid");
        } else {
            input.classList.add("is-invalid");
        }
    });

    // VALIDAR CONTRASEÑA

    // if (inputPassword2.value.trim() === inputPassword.value.trim()) {
    //     console.log("contraseña ok");
    //     inputPassword.classList.add("is-valid");
    //     inputPassword2.classList.add("is-valid");
    // } else {
    //     inputPassword2.classList.add("is-invalid");
    //     document.getElementById('password2-error').innerHTML = 'Contraseña incorrecta';
    //     console.log("contraseña mal");
    // }


    function validateForm() {
        var inputPassword = document.getElementById("password");
        var inputPassword2 = document.getElementById("password2");
        var regPass = /^(?=.*[A-Z])(?=.*\d).+$/;

        if (inputPassword.value.trim() === inputPassword2.value.trim() && regPass.test(inputPassword.value.trim())) {
            console.log("contraseña ok");
            inputPassword.classList.add("is-valid");
            inputPassword2.classList.add("is-valid");
            return true;
        } else {
            inputPassword2.classList.add("is-invalid");
            document.getElementById('password2-error').innerHTML = 'Contraseña incorrecta';
            console.log("contraseña mal");
            return false;
        }
    }

    document.getElementById('inputPassword2').addEventListener('change', validateForm);




    // VALIDAR EDAD 
    function validarEdad() {
        let fechaInput = document.getElementById('inputDate').value;
        let fechaNacimiento = new Date(fechaInput);
        let fechaActual = new Date();
        let edad = fechaActual.getFullYear() - fechaNacimiento.getFullYear();
        let mes = fechaActual.getMonth() - fechaNacimiento.getMonth();

        if (mes < 0 || (mes === 0 && fechaActual.getDate() < fechaNacimiento.getDate())) {
            edad--;
            console.log('entro a comparacion edad');
            console.log(edad);
        }

        if (edad >= 13) {
            console.log("La edad es 13 o más.");
        } else {
            console.log("La edad es menor que 13.");
        }
    }

    document.getElementById('inputDate').addEventListener('change', validarEdad);


    // LIMPIAR INPUTS
    function limpiarInput() {
        let inputs = document.querySelectorAll('.form-control');

        inputs.forEach(function (input) {
            input.value = '';
            input.classList.remove("is-valid");
            alertSuccess.classList.add("d-none");
        });
    }
    document.getElementById('botonLimpiar').addEventListener('click', limpiarInput);


    // if (errores.length !== 0) {
    //     mensajeError(errores);
    //     return;
    // }


    console.log("Formulario enviado con éxito");
    mensajeExito();
});

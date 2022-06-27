"use strict"

var datosPersonas = [];
var gastos = [];
var parteTotal = document.getElementById('total');

window.onload = function() {
    datosPersonas = [];
    gastos = [];
}

function agregarPersonaYGastoAArray() {
    let persona = document.getElementById('nombre').value;
    let gasto = document.getElementById('gasto').value;

    datosPersonas.push({persona, gasto});
    gastos.push(gasto);
}

function mostrarResultados() {
    let listaDeGastos = document.getElementById('lista');
    listaDeGastos.innerHTML = '';

    for (const datoPersona of datosPersonas) {
        let gastoPorPersona = document.createElement('li');
        gastoPorPersona.innerText = datoPersona["persona"] + ": " + datoPersona["gasto"];

        listaDeGastos.appendChild(gastoPorPersona);
    }
    aportePorPersona();
}

function sumaDeGastos(array) {
    let total = 0;
    for(var i = 0; i < array.length; i++) {
        total += parseFloat(array[i]);
    } 
    return total;
}

function aportePorPersona() {
    const total = sumaDeGastos(gastos).toFixed(2);
    parteTotal.innerText = `Total: ${total}
    A cada uno le toca aportar: ${total / gastos.length}`;
}

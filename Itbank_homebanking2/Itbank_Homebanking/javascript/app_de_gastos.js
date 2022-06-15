"use strict"

const persona = document.getElementById('nombre');
const gasto = document.getElementById('gasto');
const personas = [];
const gastos = [];
const listaDeGastos = document.getElementById('lista');
const parteTotal = document.getElementById('total');

function dividir() {
    adherirGastosaListas();
    ultimoAPantalla();
    TransaccionIndividualHTML();
}

function adherirGastosAListas() {
    personas.push(persona.value);
    gastos.push(gasto.value);
}

function ultimoAPantalla() {
    const li = document.createElement('li');
    li.classList.add('lista-item');  
    const text = document.createTextNode(`${personas[personas.length - 1]}: $${gastos[gastos.length - 1]}`);
    li.append(text);
    listaDeGastos.appendChild(li);
}

function TransaccionIndividualHTML() {
    const total = sumarValores(gastos).toFixed(2);
    parteTotal.innerText = `Total: ${total}
    A cada uno le toca aportar: ${total / gastos.length}`;
}

function adicionValores(array) {
    let total = 0;
    for(var i = 0; i < array.length; i++) {
        total += parseFloat(array[i]);
    } 
    return total;
}


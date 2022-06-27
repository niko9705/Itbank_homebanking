const lista = document.getElementById('lista');
const tabla =document.getElementById('table');
console.log(lista);
console.log(tabla);

lista.addEventListener('click', (e) =>{
	console.log(tabla);
	tabla.classList.toggle('activo');
	console.log(e.target);
});
	

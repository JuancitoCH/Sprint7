const currenciesAPI = 'https://www.dolarsi.com/api/api.php?type=valoresprincipales'


const fetchCurrencies = (url, callback) => {
  fetch(url)
    .then((currencies) => currencies.json())
    .then((currencies) => {
      const currenciesFiltradas = callback(currencies);
      
      armar(currenciesFiltradas);
    })
};
const filterMainCurrencies = (currencies) => {
  return currencies.filter(
    (currencie) =>
      currencie.casa.nombre == "Dolar Oficial" ||
      currencie.casa.nombre == "Dolar Blue" ||
      currencie.casa.nombre == "Dolar turista"
  )
};

fetchCurrencies(currenciesAPI, filterMainCurrencies)

function armar(datos) {
  const contenedorToAppend = document.getElementById('cards-container')
  contenedorToAppend.innerHTML = ''
  // const fecha = document.createElement('p')
  // fecha.textContent = Date.now()

  // contenedorToAppend.appendChild(fecha)

  datos.forEach(element => {

    const col = document.createElement("div")
    const contenedor = document.createElement("div")
    const elemento1 = document.createElement("p")
    const elemento2 = document.createElement("p")
    const elemento3 = document.createElement("p")
    const elemento4 = document.createElement("p")

    col.classList='col'
    col.appendChild(contenedor)

    contenedor.classList='card mx-3 '
    contenedor.style.width='18rem'


    elemento1.classList='card-header h-30 d-inline-block  bg-success text-white bg-opacity-75'
    elemento1.textContent = element.casa.nombre
    contenedor.appendChild(elemento1)

    elemento2.classList = 'card-body h-70 d-inline-block  bg-secondary bg-opacity-75 text-light'
    elemento2.textContent = "Compra: " + "$" + element.casa.compra
    contenedor.appendChild(elemento2)

    elemento3.classList = 'card-3 h-5 d-inline-block  bg-light'
    elemento3.textContent = "Venta: " + "$" + element.casa.venta
    contenedor.appendChild(elemento3)

    elemento4.classList = 'card-4 h-5 d-inline-block bg-success text-white bg-opacity-75 rounded-bottom'
    elemento4.textContent = "Variación: " + "$" + element.casa.variacion
    contenedor.appendChild(elemento4)
    contenedorToAppend.appendChild(contenedor)

  });
}
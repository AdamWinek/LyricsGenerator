function sendRequest(){


  data = fetch('/generate')
  .then((response) => {
    return response.json();
  })
  .then((data) => {
    console.log(data);
    
  });
  document.getElementById("buttonResponse").textContent = data;
}
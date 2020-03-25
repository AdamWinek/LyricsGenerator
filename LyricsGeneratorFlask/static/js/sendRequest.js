function sendRequest(){
  console.log("here")

  fetch('/generate')
  .then((response) => {
    return response.json();
  })
  .then((data) => {
    console.log(data);
    
  });
  console.log(data)
}
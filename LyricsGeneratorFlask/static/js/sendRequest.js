function sendRequest(){


  data = fetch('http://127.0.0.1:5000/generate')
  .then((response) => {
    return response.json();
  })
  .then((data) => {
    console.log(data);
    
  });
  console.log(data)
}

window.onload=function(){
  document.getElementById("button").addEventListener("click", sendRequest)
 
}

function sendRequest(e){
  console.log(e);
  e.preventDefault();
  var inputText = document.getElementById("lyricsInput").value;
  var check = document.getElementById("check")
  var loading = document.getElementById("loading")
  check.style.display = "none"
  loading.style.display = "block"
  console.log(inputText);
  const myHeaders = new Headers({'Input': inputText});
  const myRequest = new Request('/generate', {
    method: 'GET',
    headers: myHeaders,
    mode: 'cors',
    cache: 'default',
  });
  data = fetch(myRequest)
  .then((response) => {
    return response.json();
  })
  .then((data) => {
    document.getElementById("returnText").textContent = "";
    lyricsText = data["lyrics"];
    lyricsText = lyricsText.split("newline").join("<br/>")
    console.log(lyricsText)
    document.getElementById("returnText").innerHTML += lyricsText;
    
  });
  check.style.display = "block !important"
  loading.style.display = "none !important"
  
  
}

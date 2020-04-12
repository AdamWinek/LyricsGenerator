
window.onload=function(){
  document.getElementById("button").addEventListener("click", sendRequest)

}

function sendRequest(e){
  console.log(e)
  e.preventDefault()
  data = fetch('/generate')
  .then((response) => {
    return response.json();
  })
  .then((data) => {
    document.getElementById("returnText").textContent = "";
    lyricsText = data["lyrics"];
    console.log(lyricsText)
    document.getElementById("returnText").textContent += lyricsText;
    
  });
  
  
  
}
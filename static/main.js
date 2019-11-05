if ('serviceWorker' in navigator) {
    navigator.serviceWorker.register('service-worker.js')
    .then(function(registration) {
      console.log(`Registration successful, scope is: ${registration.scope}`);
    })
    .catch(function(error) {
      console.log(`Service worker registration failed, error: ${error}`);
    });
  }

  
    async function getActivty(){
      try{
      const response = await fetch('http://www.boredapi.com/api/activity/')
      if(!response.ok) throw response.statusText;
      const json = await response.json();
      console.log(json.activity);
      let h1 = document.getElementById('boredom');
      h1.innerText = json.activity;
      }catch(error){
      console.log(`Fetch failed : ${error}`);
      }
      }
  
  
getActivty();

/*async function addStar(star){
try{
id = star.id
const response = await fetch('star',{method:'POST',body:{'id':id,'csrfmiddlewaretoken':}});
if(!response.ok) throw response.statusText;
  }catch(error){
    console.log(`Fetch failed : ${error}`);
  }
}

*/
// -- Gloabl variables --
// -- adding indicate if user clicked on the camera or site button to add in the site
var addingcamera = new Boolean(false);
var addingsite = new Boolean(false);
// screenH is the vertical screen resolution for the actual monitor
// screenW is the horizontal screen resolution for the actual monitor
var screenW = 0;
var screenH = 0;
var rectW = 0;
var rectH = 0;
var camID = 0;
var siteID = 0;


window.onload = function() {
  // Init global variables
  const element = document.getElementById("main-content");
  const rect = element.getBoundingClientRect();
  rectW = rect.width;
  rectH = rect.height;
  screenW = screen.availWidth;
  screenH = screen.availHeight;
};

function addcamera(x,y) {
  const image = document.createElement("img");
  image.src = imgcamera //Img en variable para enviar lo que desees
  camID = camID + 1;
  camname= "cam" + camID;
  image.alt = camname
  image.id = camname;
  image.classList.add("image");
  image.style.left = `${(x + 70) - image.width / 2}px`;
  image.style.top = `${(y +54) - image.height / 2}px`;
  image.style.position = 'Absolute'
  // Append the image to the container
  const container = document.getElementById("main-content");
  container.appendChild(image);
  // add
  console.log("camera added");
  modalForm(document.getElementById(camname), {
    formURL: newcamURL })
  
}


function addsite(x,y) {
  const image = document.createElement("img");
  image.src = imgsite //Img en variable para enviar lo que desees
  siteID = siteID + 1;
  sitename= "site" + siteID
  image.alt = sitename
  image.classList.add("image");
  image.style.left = `${(x + 70) - image.width / 2}px`;
  image.style.top = `${(y +54) - image.height / 2}px`;
  image.style.position = 'Absolute'
  // Append the image to the container
  const container = document.getElementById("main-content");
  container.appendChild(image);
  // add
  console.log("site added");
  
}


function centralclick(event) {
  // Gat coordinates of click
  const x = event.clientX - 70;
  const y = event.clientY - 50;
  if (addingcamera == true)
    {  
    console.log("adding canera: " + addingcamera) ;
    // just control
    addcamera(x,y)
    } 
  else if (addingsite == true)
    {
    console.log("adding site: " + addingsite) ;
    addsite(x,y)
    }
}

// --- New elements ---
function newcamera() {
    if (addingcamera == true){
      addingcamera = false;
    } else {
      addingcamera = true;
      addingsite = false
    }
  }

  function newsite() {
    // var popup = window.open("https://process.honeywell.com/us/en/products/control-and-supervisory-systems/modular-controllers/?utm_source=honeywell_city&utm_medium=lamina&utm_campaign=manufacturing_industry", "popup", "fullscreen");
    // if (popup.outerWidth < screen.availWidth || popup.outerHeight < screen.availHeight)
    // {
    //   popup.moveTo(0,0);
    //   popup.resizeTo(screen.availWidth, screen.availHeight);
    // }
    if (addingsite == true){
      addingsite = false;
    } else {
      addingsite = true;
      addingcamera = false
    }
  }
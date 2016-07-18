console.log("Hello, Chris!");

function doAnimation() {
  console.log("Ready set go!");
  $('p').animate( {fontsize: 24}, 1500);
}

$(document).ready(doAnimation);

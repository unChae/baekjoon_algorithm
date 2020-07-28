var fs = require('fs');
var input = fs.readFileSync('/dev/stdin').toString().split(' ');

  let H = parseInt(input[0]);
  let M = parseInt(input[1]);
  
  if(M<45) {
      if(H==0) {
          console.log("23",M-45+60);
      }else {
          console.log(H-1,M-45+60);
      }
  }else {
      console.log(H,M-45);
  }

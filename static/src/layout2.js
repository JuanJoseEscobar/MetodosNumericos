function  activacionText(namepad){
    const mmenu = document.querySelector('#homeitem');
    const mmenu2 = document.querySelector(namepad);
    mmenu.classList.remove("active")
    mmenu2.classList.add("active")
}

window.onload = () => {
    let url = String(document.URL)
    
    const div = url.split("/")

    for(i = 0; i < div.length; i++){
        if(div[i] == "Bisec"){
            activacionText('#metoditem');
            break
        }else if(div[i] == "RFalsa"){
            activacionText('#metoditem');
            break
        }else if(div[i] == "Secante"){
            activacionText('#metoditem');
            break
        }else if(div[i] == "Newton"){
            activacionText('#metoditem');
            break
        }else if(div[i] == "Derivadas"){
            activacionText('#deritem');
            break
        }else if(div[i] == "Polynomio"){
            activacionText('#polyitem');
            break
        }else if(div[i] == "Graficar"){
            activacionText('#grafitem');
            break
        }
        
    }
  };


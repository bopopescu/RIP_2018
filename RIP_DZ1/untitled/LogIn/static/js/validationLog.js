function validate() {
    myelem1 = document.getElementById('name');
    if (document.querySelector('input[type="text"]').value.length < 4) {
        myelem1.className = "formField err";
        document.getElementsByClassName('button')[0].disabled = true;
    } else if (document.querySelector('input[type="text"]').value.length >= 4) {
        myelem1.className = "formField";
    }
    myelem1 = document.getElementById('pass');
    if (document.querySelector('input[type="password"]').value.length < 4) {
        myelem1.className = "formField err";
        document.getElementsByClassName('button')[0].disabled = true;
    } else if (document.querySelector('input[type="password"]').value.length >= 4) {
        myelem1.className = "formField";
    }

    if(document.querySelector('input[type="text"]').value.length >= 4 &&
        document.querySelector('input[type="password"]').value.length >= 4)
    {
        document.getElementsByClassName('button')[0].disabled = false;
    }
}

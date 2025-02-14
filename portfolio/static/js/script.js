// contact flash message

// function closeFlashMessage(){
//     const flashMessage = document.getElementById('flashMessage');
//     flashMessage.style.display = 'none';

// }

function closeThankMessage(){
    const flashMessage = document.getElementById('thankMessage');
    flashMessage.style.display = 'none';

}

// show the flash message if exists (check the presence of dom)
window.onload = () => {
    const flashMessage = document.getElementById('thankMessage');
    if (flashMessage){
        flashMessage.style.display = 'flex';
        setTimeout(() => {
            flashMessage.style.display = 'none';
        }, 5000);
    }
}
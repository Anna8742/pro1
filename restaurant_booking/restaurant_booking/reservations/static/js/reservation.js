document.getElementById('reservation-form').addEventListener('submit', function(event) {
    event.preventDefault();

    let formData = new FormData(this);

    fetch('/create/', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('success-message').innerText = data.message;
    })
    .catch(error => console.error('Error:', error));
});

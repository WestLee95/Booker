function handleFileUpload(event) {
    const fileInput = document.getElementById('fileInput');
    const file = fileInput.files[0];
    if (file) {
        // Display the selected file name
        const convertButton = document.querySelector('.convert-button');
        convertButton.textContent = `Convert ${file.name} to Audio`;
    }
}

function uploadFile() {
    const fileInput = document.getElementById('fileInput');
    const file = fileInput.files[0];

    if (!file) {
        alert('Please select a file to upload.');
        return;
    }

    const formData = new FormData();
    formData.append('file', file);

    fetch('/convert', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            window.location.href = `/download/${data.filename}`;
        } else {
            alert('Failed to convert PDF to audio.');
        }
    })
    .catch(error => {
        console.error('Error:', error);
        alert('An error occurred while uploading the file.');
    });
}

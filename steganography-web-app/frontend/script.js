document.getElementById('encode-button').addEventListener('click', async () => {
    const imageInput = document.getElementById('image-upload');
    const messageInput = document.getElementById('secret-message');
    const downloadLink = document.getElementById('download-link');

    if (!imageInput.files[0] || !messageInput.value) {
        alert('Selecione uma imagem e digite uma mensagem.');
        return;
    }

    const formData = new FormData();
    formData.append('image', imageInput.files[0]);
    formData.append('message', messageInput.value);

    const response = await fetch('/encode', {
        method: 'POST',
        body: formData
    });

    if (response.ok) {
        const blob = await response.blob();
        const url = URL.createObjectURL(blob);
        downloadLink.href = url;
        downloadLink.download = 'imagem_codificada.png';
        downloadLink.style.display = 'inline';
        downloadLink.textContent = 'Baixar imagem com mensagem';
    } else {
        alert('Erro codificando imagem');
    }
});

document.getElementById('decode-button').addEventListener('click', async () => {
    const imageInput = document.getElementById('image-upload-decode');
    const extractedMessage = document.getElementById('extracted-message');

    if (!imageInput.files[0]) {
        alert('Selecione uma imagem para decodificar.');
        return;
    }

    const formData = new FormData();
    formData.append('image', imageInput.files[0]);

    const response = await fetch('/decode', {
        method: 'POST',
        body: formData
    });

    const data = await response.json();
    extractedMessage.textContent = data.message || 'Nenhuma mensagem secreta encontrada.';
});
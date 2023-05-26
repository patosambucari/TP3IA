// Obtener referencias a los elementos HTML
const canvas = document.getElementById('canvas');
const recognizeButton = document.getElementById('recognizeButton');

// Obtener el contexto 2D del lienzo
const ctx = canvas.getContext('2d');

// Tamaño del lienzo
const canvasSize = 300;
canvas.width = canvasSize;
canvas.height = canvasSize;

// Tamaño de cada píxel
const pixelSize = canvasSize / 10;

// Inicializar el lienzo con píxeles en blanco
const clearCanvas = () => {
  ctx.fillStyle = 'white';
  ctx.fillRect(0, 0, canvasSize, canvasSize);
};

// Dibujar un píxel en el lienzo
const drawPixel = (x, y, color) => {
  ctx.fillStyle = color;
  ctx.fillRect(x * pixelSize, y * pixelSize, pixelSize, pixelSize);
};

// Alternar el estado de un píxel (blanco/negro)
const togglePixel = (x, y) => {
  const pixelData = ctx.getImageData(x * pixelSize, y * pixelSize, pixelSize, pixelSize).data;
  const isWhite = pixelData[0] === 255 && pixelData[1] === 255 && pixelData[2] === 255;
  const color = isWhite ? 'black' : 'white';
  drawPixel(x, y, color);
};

// Obtener los datos de la imagen del lienzo
const getImageData = () => {
  const imageData = [];
  for (let y = 0; y < 10; y++) {
    for (let x = 0; x < 10; x++) {
      const pixelData = ctx.getImageData(x * pixelSize, y * pixelSize, pixelSize, pixelSize).data;
      const isWhite = pixelData[0] === 255 && pixelData[1] === 255 && pixelData[2] === 255;
      imageData.push(isWhite ? 1 : -1);
    }
  }
  return imageData;
};

// Enviar los datos de la imagen al backend para reconocer el patrón
const recognizePattern = () => {
  const imageData = getImageData();

  // Enviar los datos al backend utilizando fetch
  fetch('/recognize', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      image_data: imageData,
    }),
  })
    .then((response) => response.json())
    .then((data) => {
      // Mostrar el resultado en el lienzo
      for (let y = 0; y < 10; y++) {
        for (let x = 0; x < 10; x++) {
          const index = y * 10 + x;
          const color = data.retrieved_pattern[index] === 1 ? 'black' : 'white';
          drawPixel(x, y, color);
        }
      }
    })
    .catch((error) => {
      console.error('Error:', error);
    });
};

// Limpiar el lienzo al cargar la página
window.onload = clearCanvas;

// Manejar el evento de clic en el lienzo
canvas.addEventListener('click', (event) => {
  const x = Math.floor(event.offsetX / pixelSize);
  const y = Math.floor(event.offsetY / pixelSize);
  togglePixel(x, y);
});

// Manejar el clic en el botón "Recognize"
recognizeButton.addEventListener('click', recognizePattern);

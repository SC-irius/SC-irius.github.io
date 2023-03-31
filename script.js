// Récupérer la jauge
const gauge = document.querySelector(".gauge");

// Récupérer l'aiguille
const needle = document.querySelector(".needle");

// Récupérer l'input pour le pourcentage
const percentInput = document.querySelector("#percent");

// Définir les couleurs de la jauge
const colors = [
  { percent: 0, color: "red" },
  { percent: 40.5, color: "red" },
  { percent: 40.6, color: "orange" },
  { percent: 60.5, color: "orange" },
  { percent: 60.6, color: "yellow" },
  { percent: 80.5, color: "yellow" },
  { percent: 80.6, color: "green" },
  { percent: 100, color: "green" },
];

// Fonction pour placer l'aiguille en fonction du pourcentage
function setNeedle(percent) {
  // Déterminer l'angle en degrés en fonction du pourcentage
  const angle = percent / 100 * 135 - 135;

  // Faire tourner l'aiguille
  needle.style.transform = `rotate(${angle}deg)`;
}

// Écouter les changements de l'input pour le pourcentage
percentInput.addEventListener("input", (e) => {
  const percent = e.target.value;
  setNeedle(percent);

  // Trouver la couleur correspondante en fonction du pourcentage
  let color = "green";
  for (let i = 0; i < colors.length; i++) {
    if (percent <= colors[i].percent) {
      color = colors[i].color;
      break;
    }
  }

  // Appliquer la couleur à la jauge
  gauge.style.borderRightColor = color;
});

<?php
  // On récupère les variables depuis le formulaire HTML 
  $rue = $_GET["rue"];
  $prix = $_GET["prix"];
  $expected_income = $_GET["expected_income"];
  $surface = $_GET["surface"];
  $zone_prix_m2 = $_GET["zone_prix_m2"];
  $age = $_GET["age"];
  $presence_ecoles = $_GET["presence_ecoles"];
  $presence_transports = $_GET["presence_transports"];
  $presence_commerces = $_GET["presence_commerces"];
  $zone_inondable = $_GET["zone_inondable"];
  $s8 = $_GET["s8"];
  $s42 = $_GET["s42"];
  $type_bien = $_GET["type_bien"];
  $etat = $_GET["etat"];
  $tendance_marche_immobilier = $_GET["tendance_marche_immobilier"];
  $q_eau_ville = $_GET["q_eau_ville"];
  $nb_immigrations = $_GET["nb_immigrations"];
  $t_vacances_locatives = $_GET["t_vacances_locatives"];
?> 
<html> 
<head> 
<title>Résultat du script Python</title> 
</head> 
<body> 
<!-- CORPS --> 
  
<div id=“resultat”> 
<p>Voici le résultat du script python :</p> 
<?php 
  // On exécute le script python en lui passant les variables comme arguments 
  // et on récupère sa sortie dans un tableau 
  exec("python realt_metrics_usa.py $rue $prix $expected_income $surface $zone_prix_m2 $age $presence_ecoles $presence_transports $presence_commerces $zone_inondable $s8 $s42 $type_bien $etat $tendance_marche_immobilier $q_eau_ville $nb_immigrations $t_vacances_locatives ", $output); 
  // On affiche le contenu du tableau 
  foreach ($output as $line) { echo $line . “<br>”; } 
?> 
</div> 
</body> 
</html>

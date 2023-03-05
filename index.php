<?php
	function getDescription($image){
		$sub = substr($image,2,24); 
		//echo($sub .".txt");
		if (file_exists($sub .".txt") ) {
			$txt = fopen($sub .".txt","r");
			$out = fread($txt,filesize($sub.".txt"));
			fclose($txt);
			return "<h3>".$out."</h3><br>";
		}else{
			return ("<h2>No Description Found</h2><br>");
		}
		
	}
	$folder = './';
	$images = glob($folder .'*.{png}',GLOB_BRACE);
	foreach ($images as $image){
		$sub = substr($image,7,19); 
		echo("<img src='$image' style='image-rendering: pixelated;' width='255'><br><h1>$sub</h1>");
		echo(getDescription($image));
	}
	
?>
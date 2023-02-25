<?php
    $array = array("firstname" => "", "name"=> "", "email"=> "", "message"=> "", "firstnameError"=> "", "nameError"=>"", "emailError"=> "", "phoneError"=> "", "messageError"=>"", "success"=>false);
    $emailInfo = "eloi.bastide92@gmail.com";

    if($_SERVER["REQUEST_METHOD"] == "POST"){
        $array["firstname"] = verifyInput($_POST["firstname"]);
        $array["name"] = verifyInput($_POST["name"]);
        $array["email"] = verifyInput($_POST["email"]);
        $array["phone"] = verifyInput($_POST["phone"]);
        $array["message"] = verifyInput($_POST["message"]);
        $array["success"] = true;
        $emailText="";

        if(empty($firstname)){
            $array["firstnameError"] = "je veux connaitre ton prenom";
            $array["success"]= false;
        }
        else{
            $emailText .= "Firstname: {$array["firstname"]}\n";
        }
        if(empty($name)){
            $array["nameError"] = "je veux connaitre ton nom";
            $array["success"]= false;
        }
        else{
            $emailText .= "Name:{$array["name"]}\n";
        }        
        if(!isEmail($email)){
            $array["emailError"] = "tu essaie de me rouler, ce n'est pas un email";
            $array["success"]= false;
        }
        else{
            $emailText .= "Email: {$array["email"]}\n";
        }
        if(!isPhone($phone)){
            $array["phoneError"] = "veuillez entrez un numero de telephone";
            $array["success"]= false;;
        }
        else{
            $emailText .= "Phone: {$array["phone"]}\n";
        }
        if(empty($message)){
            $array["messageError"]= "je veux connaitre un message";
            $array["success"]= false;
        }
        else{
            $emailText .= "Message: {$array["message"]}\n";
        }
        if($array["success"]){
            $headers = "From: {$array["firstname"]} {$array["name"]} <{$array["email"]}>\r\nReply-to: {$array["email"]}";
            mail($emailInfo, "un message de votrr site", $emailText, $headers);
        }

        echo json_encode($sarray);
    }
    function isPhone($var){
        return preg_match("/^[0-9]*$/", $var);
    }

    function isEmail(){
        return filter_var($var, FILTER_VALIDATE_EMAIL);
    }
    function verifyInput($var){
        $var= trim($var);
        $var = stripslashes($var);
        $var =htmlspecialchars($var);

        return $var;
    }
?>
<!DOCTYPE html>
<html>
<head>
    <title></title>
</head>
<body>
    <form action="" method="post">
        <textarea rows="10" cols="90" name="code"></textarea><br/>
        <input type="submit" name="request" value="request解密">
        <input type="submit" name="response" value="response解密">
    </form>
</body>
</html>

<?php
session_start();
@set_time_limit(0);
@error_reporting(0);
function E($D,$K){
    for($i=0;$i<strlen($D);$i++) {
        $D[$i] = $D[$i]^$K[$i+1&15];
    }
    return $D;
}
function Q($D){
    return base64_encode($D);
}
function O($D){
    return base64_decode($D);
}
$P='pass';
$V='payload';
$T='3c6e0b8a9c15224a';
$code = $_POST['code'];

if(isset($_POST['response'])){
        $head = substr($code,16);
        $tail = '/'.substr($head,-16).'/';
        $out1 = preg_replace($tail,'',$head);
}

if(isset($_POST['request'])){
    $out1 = urldecode($code);
}
$out = O(E(O($out1),$T));
echo '<textarea rows="15" cols="90">'.$out.'</textarea><br/>'
?>



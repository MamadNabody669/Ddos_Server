<?php
//GetFrom-Information
$TokenBot = $_POST['TokenF'];
$ChatIDBot = $_POST['ChatIdF'];
$TextBot = $_POST['TextF'];


//SendMessage-TelegramBot

define ('url',$TokenBot.'/');

$message = urlencode($TextBot);
file_get_contents(url."sendmessage?text=".$message."&chat_id="."$ChatIDBot"."&parse_mode=HTML");



?>
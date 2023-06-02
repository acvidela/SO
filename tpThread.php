<?php


class miThread extends Thread {
  private $id;
 
  public function __construct($i){
  $this->id=$i;
 }

 public function run(){
  while(true){
   echo ($this->id);
   sleep(1);
  }
 }
}

$t1 = new miThread(1);   //creo el primer Thead con id 1
$t2 = new miThread(2);    //creo el segundo Thead con id 2
$t1->run();              // Lanza a correr el thread1
sleep(5);                 //Espero 5 segundos para que se vea que trabaja 1 solo un rato
$t2->run();             // Lanza a correr el thread2 y se debberian ver inercalados en pantalla.


?>


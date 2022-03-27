# Tetris - 16 Jun 2021
Това е моят проект по въведение в скриптовите езици. Той представлява играта Tetris, в която играеш докато не стигнеш 10-то ниво или пък не загубиш - това става, когато достигнеш най-горното положение на полето за игра с последния блок. Когато run-ете кода, ще се появи менюто, което включва в себе си бутон, който води към играта, бутон, който спира програмата, статистика на вашите игри - най-високо достигнато ниво, най-много спечелени точки (печелят се 20 точки за всеки ред, запълнен с блокове), броят на победите Ви до този момент и аналогично - броят на вашите загуби. Когато започнете игра, ще Ви се появи кафяво поле, в което ще се spawn-ват блокчета, които трябва да наредите. Докато играете, винаги ще можете да излезете от играта - това става като се натисне средният бутон на мишката. Ако загубите по време на игра, ще се появи надпис "YOU LOST!" и след 5 секунди играта ще се затвори, а ако победите - ще се появи надпис "YOU WIN!" и отново след 5 секунди играта ще бъде затворена.   

# Buttons
 - За да натиснете бутона "PLAY", ще тряба да използвате левия бутон на мишката, за бутона "QUIT" в менюто - десния, а за същия бутон, но вече в самата игра - средния.
 - Докато играете ще слушате музика, която може да се пуска само ако сте с Windows. Тя се пуска автоматично в менюто, но може да бъде спряна с бутона "p", и пусната отново - с бутона "o". По време на игра ще можете да спрете всички звуци с бутона "l".
 - За да контролирате вашият блок по време на играта, може да използвате лява и дясна стрелка за съответните посоки и "a" и "d" - за същото. Със "space" можете да завъртате съответния блок.

# Modules
 - За тази игра са използвани стандартните библиотеки за Python версия 3.9 - turtle, random и time, както и winsound, която е достъпна за Windows и заради която този код няма да функционира правилно за Linux.

# Something about the code
 - функцията FileCheck() приема името на подадения файл и проверява дали съществува в същата директория, в която се намира кода;
 - функцията play() пуска песента, която ѝ е подадена веднъж;
 - функцията playRep() пуска подадената песен безкрайно;
 - функцията playRepWithBut() е като горната, но се използва, за да спира и пуска песента;
 - функцията save_stats() запазва точките, нивото, победите и загубите от последната игра в посочения файл;
 - класът Block() създава блокчето, което местите;
 - класът Score() създава резултата, който се вижда по време на игра;
 - класът Level() създава нивото, което се вижда по време на игра;
 - класът Button() създава бутоните, които можете да натискате;
 - field е list, в който се изобразяват блокчетата с цифри. Той е рисуван от функцията draw_field(), която рисува на определени кординати върху прозореца на играта със цвят, който е на индекс(отговарящ на съответното число) в масива Colors;
 - функцията new_level() обновява съответното нивото, което се променя спрямо резултата, който ѝ е подаден;
 - функцията check_field() проверява дали в подаденото поле има ред, който е запълнен с блокчета. Ако има такъв, той се изтрива и всичко над него се премества с един ред надолу;
 


# Termux-Games
# Coded by: Khansaad1275 (You dont become a coder by just changing the credits)
# Github: https://github.com/khansaad1275/Termux-Games



echo -e "\e[032m" "Please Don't copy the Code And Give creadits If you are using this project"


clear


echo "play Games in Termux by - ITAIA CYBER ARMY"

echo -e "\e[1;92m"
apt install ruby -y && gem install lolcat
pkg install figlet

figlet bastet | lolcat && echo Installing..................... | lolcat
echo -e "\e[1;92m"
pkg install bastet

figlet Pacman | lolcat && echo Installing..................... | lolcat
echo -e "\e[1;92m"
pkg install pacman4console

figlet M-buggy | lolcat && echo Installing..................... | lolcat
echo -e "\e1;92m"
pkg install moon-buggy

figlet invaders | lolcat && echo Installing..................... | lolcat
echo -e "\e[1;92m"
pkg install ninvaders

figlet snake | lolcat && echo Installing..................... | lolcat
echo -e "\e[1;92m"
pkg install nsnake

figlet Greed | lolcat && echo Installing..................... | lolcat
echo -e "\e[1;92m"
pkg install greed

figlet Nethack | lolcat && echo Installing..................... | lolcat
echo -e "\e[1;92m"
pkg install nethack

figlet Sudoku | lolcat && echo Installing..................... | lolcat
echo -e "\e[1;92m"
pkg install nudoku && apt install nudoku

figlet Hangman | lolcat && echo Installing..................... | lolcat
echo -e "\e[1;92m"
pkg install git -y

figlet Python | lolcat && echo Installing..................... | lolcat
echo -e "\e[1;92m"
pkg install python -y

figlet "2048" | lolcat && echo Installing..................... | lolcat
echo -e "\e[1;92m"
pkg install git -y && pkg install wget -y && pkg install clang -y && wget https://raw.githubusercontent.com/mevdschee/2048.c/master/2048.c && sleep 2 && gcc -o 2048 2048.c

echo "Visit @termux_hacking for more scripts" | lolcat -a
echo ""
echo -e 'Type bash game.sh to start the Games' | lolcat -a

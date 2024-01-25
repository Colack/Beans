:: Assuming that the user is in the root directory and has gcc installed

IF NOT EXIST bin (
    mkdir bin
)

gcc -o bin\main.exe main.c core\beans.c core\interpreter.c

echo "Compilation complete."
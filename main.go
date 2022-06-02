package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

const Author = "Colack"
const Email = "UniformKitten281@gmail.com"
const Version = "0.0.1"
const ErrorLog = "====== Error Logging ======"

func main() {
	args := os.Args[1:]

	if len(args) != 0 {
		if args[0] == "run" {
			run(args[1])
		} else if args[0] == "version" {
			fmt.Println("Version:", Version)
			fmt.Println("Author:", Author)
			fmt.Println("Email:", Email)
		} else if args[0] == "compile" {

		} else if args[0] == "help" {
			fmt.Println("Usage:")
			fmt.Println("\tgo run main.go run [file] - Display a .beans file, and all commands in it.")
			fmt.Println("\tgo run main.go compile [file] - Compile a .beans file to a .md file.")
			fmt.Println("\tgo run main.go help - Display this help message.")
			fmt.Println("\tgo run main.go version - Display the version of this program.")
		} else {
			fmt.Printf("The command \"%s\" does not exist.", args[0])
			fmt.Printf("\nUse \"go run main.go help\" for more information.")
		}
	} else {
		fmt.Printf("Beans Version %s\n", Version)
	}
}

func run(filePath string) {
	readFile, err := os.Open(filePath)
	if err != nil {
		fmt.Println(err)
	}

	fileScanner := bufio.NewScanner(readFile)
	fileScanner.Split(bufio.ScanLines)
	var fileLines []string

	for fileScanner.Scan() {
		fileLines = append(fileLines, fileScanner.Text())
	}

	readFile.Close()

	for _, line := range fileLines {

		if strings.HasPrefix(line, "//") {
			continue
		} else if strings.HasPrefix(line, "display") {
			fmt.Println(line)
		}
	}
}

func compile(filePath string) {

}

func errorLog(errorMessage string) {
	// Create a new file, and write to it.
	f, err := os.Create("error.txt")
	if err != nil {
		fmt.Println(err)
	}

	defer f.Close()

	f.WriteString(ErrorLog + "\n" + errorMessage + "\n" + ErrorLog)
}

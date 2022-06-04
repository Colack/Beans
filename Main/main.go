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

var i = 0
var errTrue = false

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

	if fileLines[0] == "beans init" {
		if fileLines[1] == "beans create" {
			if _, err := os.Stat("main.beans"); err == nil {
				fmt.Println("main.beans already exists.")
			} else {
				f, err := os.Create("main.beans")
				if err != nil {
					fmt.Println(err)
				}
				defer f.Close()
				for i := 0; i < len(fileLines); i++ {
					f.WriteString(fileLines[i] + "\n")
				}
				for i := 1; i < len(fileLines); i++ {
					if fileLines[i] == "beans init" {
						fmt.Println("You have already initialized this file.")
						errTrue = true
					}
				}
				if errTrue == false {
					for _, line := range fileLines {

						if strings.HasPrefix(line, "//") {
							continue
						} else if strings.HasPrefix(line, "console") {
							fmt.Println("Console: " + line)
						} else if strings.HasPrefix(line, "header") {
							fmt.Println("====== " + line + " ======")
						} else if strings.HasPrefix(line, "print") {
							fmt.Println(line)
						}
					}
				} else {
					fmt.Println("ERR: You have already initialized this file.")
					fmt.Println("Use \"go run main.go help\" for more information.")
				}
			}

		} else {
			for i := 1; i < len(fileLines); i++ {
				if fileLines[i] == "beans init" {
					fmt.Println("You have already initialized this file.")
					errTrue = true
				}
			}
			if errTrue == false {
				for _, line := range fileLines {

					if strings.HasPrefix(line, "//") {
						continue
					} else if strings.HasPrefix(line, "console") {
						fmt.Println("Console: " + line)
					} else if strings.HasPrefix(line, "header") {
						fmt.Println("====== " + line + " ======")
					} else if strings.HasPrefix(line, "print") {
						fmt.Println(line)
					}
				}
			} else {
				fmt.Println("ERR: You have already initialized this file.")
				fmt.Println("Use \"go run main.go help\" for more information.")
			}
		}
	} else {
		fmt.Println("ERR: This is not a beans file.")
		fmt.Println("Use \"go run main.go help\" for more information.")
	}
}

func compile(filePath string) {

}

func error(errorMessage string) {
	typer := os.Args[1:]
	stringo := os.Args[2:]
	name := os.Args[3:]
	if len(typer) != 0 {
		if typer[0] == "0" {
			fmt.Println("Creating a file called " + name[0] + "...")
			f, err := os.Create(name[0])
			if err != nil {
				fmt.Println(err)
			}
			fmt.Println("File created.")
			defer f.Close()
			fmt.Println("Writing to file...")
			f.WriteString(stringo[0])
			fmt.Println("File written.")

		} else if typer[0] == "1" {
			fmt.Println("Creating a file called " + name[0] + "...")
			f, err := os.Create(name[0])
			if err != nil {
				fmt.Println(err)
			}
			fmt.Println("File created.")
			defer f.Close()
			fmt.Println("Writing to file...")
			f.WriteString(ErrorLog + "\n" + errorMessage + "\n" + ErrorLog)
			fmt.Println("File written.")
		} else {
			fmt.Println("Incorrect usage.")
			fmt.Println("Correct inputs: \n0 for writing self \n1 for writing default error log")
		}
	}
}

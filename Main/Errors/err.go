package main

import (
	"fmt"
	"os"
)

func errLog(errorMessage string) {
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

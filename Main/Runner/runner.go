package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func runner(filePath string) {
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

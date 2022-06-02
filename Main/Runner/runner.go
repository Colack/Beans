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

	for _, line := range fileLines {

		if strings.HasPrefix(line, "//") {
			continue
		} else if strings.HasPrefix(line, "display") {
			fmt.Println(line)
		}
	}
}

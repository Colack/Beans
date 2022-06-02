package main

import (
	"fmt"
	"os"
)

func errLog(errorMessage string) {
	// Create a new file, and write to it.
	f, err := os.Create("error.txt")
	if err != nil {
		fmt.Println(err)
	}

	defer f.Close()

	f.WriteString(ErrorLog + "\n" + errorMessage + "\n" + ErrorLog)
}

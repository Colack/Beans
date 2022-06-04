package main

import (
	"fmt"
	"os"
)

func beanserr(errorMessage string) {
	fmt.Println("Creating new error log...")
	f, err := os.Create("beanserr.log")
	if err != nil {
		fmt.Println(err)
	}
	fmt.Println("File created.")
	defer f.Close()
	fmt.Println("Writing to file...")
	f.WriteString(ErrorLog + "\n" + errorMessage + "\n" + ErrorLog)
	fmt.Println("File written.")
}

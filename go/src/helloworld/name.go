package main

func main() {
	firstName := "John"
	updateName(&firstName)
	println(firstName)
}

func updateName(name *string) {
	*name = "David"
}

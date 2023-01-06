#!/bin/python3

import requests

def main() -> None:
	res = requests.get("http://localhost:3000/todos")
	if res.status_code == 200:
		res = res.json()
		print(res)
	else:
		print(res.status_code)
	pass

if __name__ == "__main__":
	main()


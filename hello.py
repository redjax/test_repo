def say_hello(name: str = None):
  if not name:
    name: str = "World"
  assert isinstance(name, str), TypeError(f"name arg must be a string. Got type: ({type(name)})")

  print(f"Hello, {name}!")


def get_name() -> str:
  _name: str = input("What is your name? ")

  return _name

if __name__ == "__main__":
  name: str = "Test"

  say_hello(name=test)
  

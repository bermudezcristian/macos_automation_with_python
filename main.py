import os

def execution_initial_setup():
  import initial_setup
  #initial_setup.main()

def application_settings():
  import application_settings
  application_settings.main()

def personal_settings():
  import personal_settings
  personal_settings.main()

def get_user_choice():
  print("[1]: Run Initial Setup")
  print("[0]: Exit")
  return input("Selected option: ")

def main():
  choice = ""
  while str(choice) != "0":
    print("MacOS Automation with Python")
    choice = str(get_user_choice())
    if choice == "1":
      execution_initial_setup()
      application_settings()
      personal_settings()
      choice = "0"
    elif choice == "0":
      print("Bye!")
    else:
      print("You didn't choice anything")

if __name__ == "__main__":
  main()

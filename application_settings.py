import os

def ssh_keys():
  print("Configuring SSH Keys")
  # TODO Check if directory exists
  # TDOO Check if directory has the correct permissions
  commands = [
    "mkdir ~/.ssh",
    "chmod 0700 ~/.ssh"
  ]
  for command in commands:
    print(command)
    # os.system(command)
  # TODO Bring config file
  # TODO Bring ssh key file
  # TODO Bring ssh
  command = "chmod 0600 ~/.ssh/*"
  os.system(command)

def brew_formulas():
  print("Configuring Brew Formulas")
  # antigen
  # awscli
    # aws configure import --csv file://credentials.csv  
  # gh
  command = "gh auth login"
  #os.system(command)
    # TODO Check if gh is configured
  # gpg
  # jq
  # nvm
  # pinentry-mac
  # pyenv
  # vim
  command = "cp ~/macos_automation_with_python/dotfiles/.vimrc ~/.vimrc"
  os.system(command)
  # warrensbox/tap/tfswitch
  os.system("tfswitch -u")
  # watch

def main():
  print("Configuring Applications")
  ssh_keys()
  brew_formulas()

if __name__ == "__main__":
  main()

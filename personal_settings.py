import os

def folders():
  folders = [
    "~/Work/Trafilea/GitHub"
  ]
  for folder in folders:
    command = "mkdir -p " + folder
    os.system(command)

def vim():
  os.system("cp ~/macos_automation_with_python/dotfiles/.vimrc ~/.vimrc")
  os.system("cp ~/macos_automation_with_python/dotfiles/.alacritty.yml ~/.alacritty.yml")

def main():
  folders()
  vim()

if __name__ == "__main__" : 
  main()

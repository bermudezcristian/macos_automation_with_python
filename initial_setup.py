import os

def cmd_exists(cmd):
  return any(
    os.access(os.path.join(path, cmd), os.X_OK)
      for path in os.environ["PATH"].split(os.pathsep)
  )

def homebrew():
  brew_tap = [
    "boltops-tools/software"
  ]

  brew_formulas = [
    "antigen",
    "awscli",
    "gh",
    "gpg",
    "jq",
    "nvm",
    "pinentry-mac",
    "pyenv",
    "terraspace",
    "tmux",
    "vim",
    "warrensbox/tap/tfswitch",
    "watch"
  ]

  brew_casks = [
    "alacritty",
    "asana",
    "discord",
    "docker",
    "firefox",
    "google-chrome",
    "obs",
    "slack",
    "spotify",
    "telegram",
    "whatsapp",
    "zoom"
  ]

  for tap in brew_tap:
    command = "brew tap " + tap
    os.system(command)

  for formula in brew_formulas:
    command = "brew install " + formula
    os.system(command)

  for cask in brew_casks:
    command = "brew install --cask " + cask
    os.system(command)

def main():
  if cmd_exists("brew") is False:
    os.system("/bin/bash -c \"$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)\"")
  homebrew()

if __name__ == "__main__":
  main()

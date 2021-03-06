## Shellpocket

<img style="filter: invert(1)" src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/terminal.svg" width="30" height="12"> Quickly generate reverse shells from predefined templates for use in pentesting.

## Setting up

1. Clone the repository from https://github.com/tperich/shellpocket
2. Run `pip install -r requirements` to install dependencies
3. Run `./shellpocket.py -h`

NOTE: You can add your own shells in [/shells.py](/shells.yml)

## To do
 - [x] Load shells from a file
 - [x] Send from choice menu to stdin
 - [x] Replace url,port via args
 - [ ] Separate by category for nicer printing
 - [ ] Support for other entities (ex. useful commands)
 - [ ] Local DB support
 - [ ] Support adding/deleting/updating shells using the menu

## Thanks
 - To MrPineMan for [Awesome-Reverse-Shell](https://github.com/MrPineMan/Awesome-Reverse-Shell) collection
const TicTacToe = require("discord-tictactoe");

new TicTacToe({
  token:
    "MTA5MjkyNjI0OTM0NjgxNDA3Mg.Glbsml.0gOwLkcDmsFHSOFfGVpLdCiz74sHl0TzOKIJK4",
  language: "en",
  command: "tictactoe",
  commandOptionName: "opponent",
  textCommand: "!tictactoe",
})
  .login()
  .then(() => console.log("Bot is online"));

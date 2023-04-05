require("dotenv").config();
const TicTacToe = require("discord-tictactoe");
const TOKEN = process.env.BOT_TOKEN;

new TicTacToe({
  token: TOKEN,
  language: "en",
  command: "tictactoe",
  commandOptionName: "opponent",
  textCommand: "!tictactoe",
})
  .login()
  .then(() => console.log("Bot is online"));

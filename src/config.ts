import dotenv from "dotenv";
dotenv.config();

const { CLIENT_ID, GUILD_ID, BOT_TOKEN } = process.env;

if (!CLIENT_ID || !GUILD_ID || !BOT_TOKEN) {
  throw new Error("Missing Environment Variables");
}

const config: Record<string, string> = {
    CLIENT_ID,
    GUILD_ID,
    BOT_TOKEN
};

export { config };
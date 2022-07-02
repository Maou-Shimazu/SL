import { Client } from "discord.js";
import { config } from "./config";
import { log } from "./logger";
import * as commandModules from "./commands";

const commands = Object(commandModules);

export const client = new Client({
    intents: ["GUILDS", "GUILD_MEMBERS", "GUILD_MESSAGES", "DIRECT_MESSAGES"],
});

client.once("ready", () => {
    log.info("Bot is ready!");
});

client.on("interactionCreate", async interaction => { // on interaction:  depreciated
    if (!interaction.isCommand())
        return;
    const { commandName } = interaction;
    commands[commandName].execute(interaction, client);
});

client.login(config.BOT_TOKEN);
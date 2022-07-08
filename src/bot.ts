import { Client, TextChannel } from "discord.js";
import { config } from "./config";
import { log } from "./logger";
import { status } from "./misc/webhook";
import * as uptime from "./misc/uptime";
import * as commandModules from "./commands";
import * as componentModules from "./components";
import * as prefix from "./prefix-commands";

const components = Object(componentModules);
const commands = Object(commandModules);
const prefixCommands = Object(prefix);

export const client = new Client({
    intents: ["GUILDS", "GUILD_MEMBERS", "GUILD_MESSAGES", "DIRECT_MESSAGES"],
});

client.once("ready", () => {
    log.info("Bot is ready!");
    client.user?.setPresence({
        activities: [
            {
                name: "prefix: !s",
                type: "LISTENING",
                url: "https://discord.com/api/oauth2/authorize?client_id=896585118787985478&permissions=8&scope=bot",
            },
        ],
        status: "online",
    });
    status(true);
    uptime.startUptimeCounter();
});

client.on("guildMemberAdd", async (interaction) => {
    const channel = await client.channels
        .fetch("878110758867705976")
        .then((channel) => channel as TextChannel);
    if (!channel) return;
    else
        await (
            await channel.send({
                embeds: [components["embeds"].welcomeEmbed(interaction)],
            })
        ).react("👋");
});

client.on("interactionCreate", async (interaction) => {
    if (!interaction.isCommand()) return;
    const { commandName } = interaction;
    commands[commandName].execute(interaction, client);
});

client.on("messageCreate", async (message) => {
    if (message.author.bot) return;

    // eslint-disable-next-line @typescript-eslint/no-non-null-assertion
    if (message.mentions.has(client.user!)) {
        await message.reply(
            "Hello esteemed, gentle-individual. The prefix for Shimazu's Guardian is `!s`."
        );
    }
    if (message.content.toLocaleLowerCase().includes("nigga")) {
        message.delete();
    }

    let args: string[];
    if (message.guild) {
        let prefix;

        if (message.content.startsWith(config.PREFIX)) {
            prefix = config.PREFIX;
        }

        if (!prefix) return;
        args = message.content.slice(prefix.length).trim().split(/\s+/);
    } else {
        // handle DMs
        const slice = message.content.startsWith(config.PREFIX)
            ? config.PREFIX.length
            : 0;
        args = message.content.slice(slice).split(/\s+/);
    }

    // const command = shift()?.toLowerCase();
    const command: string = args[0].toLowerCase();
    if (!prefixCommands[command]) {
        message.channel.send(`Command "${command}" not found.`);
    } else {
        prefixCommands[command].execute(message, client, args);
    }
    log.info(command);
});

process.on("SIGINT", function () {
    log.info("Caught interrupt signal");
    log.info("Bot is offline!");
    status(false);
    client.destroy();
});

client.login(config.BOT_TOKEN);

import { Client, TextChannel } from "discord.js";
import { config } from "./config";
import { log } from "./logger";
import * as commandModules from "./commands";
import * as componentModules from "./components";
import { status } from "./misc/webhook";

const components = Object(componentModules);
const commands = Object(commandModules);

export const client = new Client({
    intents: ["GUILDS", "GUILD_MEMBERS", "GUILD_MESSAGES", "DIRECT_MESSAGES"],
});

client.once("ready", () => {
    log.info("Bot is ready!");
    client.user?.setPresence({
        activities: [
            {
                name: "prefix: !sl",
                type: "LISTENING",
                url: "https://discord.com/api/oauth2/authorize?client_id=896585118787985478&permissions=8&scope=bot",
            },
        ],
        status: "online",
    });
    status(true);
});

client.on("guildMemberAdd", async (interaction) => {
    const channel = await client.channels
        .fetch("878110758867705976")
        .then((channel) => channel as TextChannel);
    if (!channel) return;
    else
        await (
            await channel.send({
                embeds: [components["embeds"].welcomeEmbed(interaction)], // check if valid
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
        await message.reply("Rival, Please, stfu, thank you.");
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
    const command = args[0].toLowerCase();

    // commands
    if (command == "ping") {
        const api_results: number[] = [];
        const sent = await message.reply({
            content: "Pinging...",
        });
        for (const i in [...Array(5).keys()]) {
            await new Promise((resolve) => setTimeout(resolve, 1000)).then(() => {
                sent.edit(`Pinging... ${i}`);
                api_results.push((sent.createdTimestamp - client.ws.ping) - message.createdTimestamp ); // still dosent send proper api results
            });
        }
        log.info(api_results);
        sent.edit(
            `**Ping: **: ${client.ws.ping}ms\n**Lowest:** ${Math.min(
                ...api_results
            )}ms\n**Highest:** ${Math.max(
                ...api_results
            )}ms\n**Roundtrip latency**: ${
                sent.createdTimestamp - message.createdTimestamp
            }ms`
        );
    }
});

process.on("SIGINT", function() {
    log.info("Caught interrupt signal");
    log.info("Bot is offline!");
    status(false);
    client.destroy();
});

client.login(config.BOT_TOKEN);

import { Message } from "discord.js";
import { SlashCommandBuilder } from "@discordjs/builders";
import { about } from "../components/about-embed";
import { getCurrentUptime } from "../misc/uptime";
import humanizeDuration from "humanize-duration";

export const data = new SlashCommandBuilder().setName("about").setDescription("About Shimazu Legends!");

export async function execute(message: Message) {
    const uptime = getCurrentUptime();
    return message.reply({
        embeds: [
            about(
                humanizeDuration(uptime, { largest: 2, round: true }),
                message
            ),
        ],
    });
}

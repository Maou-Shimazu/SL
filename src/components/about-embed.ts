import { Message, MessageEmbed } from "discord.js";

export function about(uptime: string, msg: Message): MessageEmbed {
    const basicInfoRows = [
        ["Uptime", uptime.trim()],
        ["API latency", `${msg.client.ws.ping}ms`],
        ["Server timezone", Intl.DateTimeFormat().resolvedOptions().timeZone],
    ];
    return new MessageEmbed()
        .setColor("#0099ff")
        .setTitle("About Shimazu Legends")
        .setThumbnail(msg.client.user?.displayAvatarURL() as string)
        .addField("Status", basicInfoRows.map(([label, value]) => `${label}: **${value}**`).join("\n"))
        .setTimestamp();
}

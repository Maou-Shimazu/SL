import { Client, Message, MessageEmbed } from "discord.js";
import humanizeDuration from "humanize-duration";

export function info(
    message: Message,
    client: Client,
    id: string
): MessageEmbed {
    const user = client.users.cache.find((user) => user.id == id);
    const userInfo = [
        ["Name", `**${user?.username}#${user?.discriminator}**`],
        ["ID", `\`${user?.id}\``],
        ["Created", `${user?.createdAt.toDateString()}`],
        ["Mention", `<@${user?.id}>`],
    ];
    return new MessageEmbed()
        .setColor("#0099ff")
        .setTitle("\n")
        .setAuthor({
            name: ((("User: " + user?.username) as string) +
                "#" +
                user?.discriminator) as string,
            iconURL: user?.avatarURL() as string,
        })
        .addField(
            "User information",
            userInfo.map(([label, value]) => `${label}: ${value}`).join("\n")
        )
        .setTimestamp();
}

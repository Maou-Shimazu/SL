import { Message, Client } from "discord.js";
import { info } from "../components/info-embed";

export async function execute(
    message: Message,
    client: Client,
    args: Array<string>
) {
    const id = args.length == 1 ? message.author.id : args[1];
    return message.channel.send({ embeds: [info(message, client, id)] });
}

import { Client, Message } from "discord.js";

export async function execute(message: Message, client: Client){
    message.channel.send("And So it begins.");
}
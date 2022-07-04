import { Client, Message, BaseGuildTextChannel } from "discord.js";

export async function execute(message: Message, client: Client) {
    const times: number[] = [];
    const messages: Message[] = [];
    let msgToMsgDelay: number | undefined;

    for (let i = 0; i < 4; i++) {
        const start = performance.now();
        const msg = await message.channel.send(`Calculating ping... ${i + 1}`);
        times.push(performance.now() - start);
        messages.push(msg);

        if (msgToMsgDelay === undefined) {
            msgToMsgDelay = msg.createdTimestamp - message.createdTimestamp;
        }
    }

    const highest = Math.round(Math.max(...times));
    const lowest = Math.round(Math.min(...times));
    const mean = Math.round(
        times.reduce((total, ms) => total + ms, 0) / times.length
    );

    const channel = message.channel as BaseGuildTextChannel;
    channel.bulkDelete(messages);

    message.channel.send(
        `**Ping:\n**Lowest: **${lowest}ms\n**Highest: **${highest}ms\n**Mean: **${mean}ms\n**Time between ping command and first reply: **${msgToMsgDelay}ms\n**Client Latency: **${client.ws.ping}ms**
      `
    );
}

import { GuildMember, MessageEmbed } from "discord.js";
import { rand } from "../misc/greetings";

export function welcomeEmbed(interaction: GuildMember): MessageEmbed {
    return new MessageEmbed()
        .setColor("#00ff00")
        .setTitle(`Welcome!`)
        .setDescription(rand.replace(`<USER>`, `**${interaction.user.username}**`))
        .setThumbnail(interaction.user.displayAvatarURL());
}

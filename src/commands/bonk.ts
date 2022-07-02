import { SlashCommandBuilder } from "@discordjs/builders";
import { CommandInteraction, User } from "discord.js";

export const data = new SlashCommandBuilder()
    .setName("bonk")
    .setDescription("Bonk Someone or yourself!")
    .addUserOption((user) =>
        user.setName("user").setRequired(false).setDescription("The user to bonk")
    );

export async function execute(interaction: CommandInteraction) {
    const user: User | null = interaction.options.getUser("user");
    if (user)
        interaction.reply(`https://pfpet.herokuapp.com/d/bonk/${user.id}.gif`);
    else {
        const { user } = interaction;
        interaction.reply(`https://pfpet.herokuapp.com/d/bonk/${user.id}.gif`);
    }
}

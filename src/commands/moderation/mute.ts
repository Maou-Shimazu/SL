import { SlashCommandBuilder } from "@discordjs/builders";
import { CommandInteraction, GuildMemberRoleManager, Role } from "discord.js";
import { PermissionFlagsBits } from "discord-api-types/v10";

export const data = new SlashCommandBuilder()
    .setName("mute")
    .setDescription("Mute Someone.")
    .addUserOption((user) =>
        user
            .setName("user")
            .setRequired(true)
            .setDescription("The user to mute")
    )
    .addIntegerOption((num) =>
        num.setName("time").setRequired(true).setDescription("The time to mute")
    ).addRoleOption((role) => {
        return role
            .setName("role")
            .setRequired(true)
            .setDescription("The mute role.");
    })
    .addStringOption((str) =>
        str
            .setName("reason")
            .setRequired(false)
            .setDescription("The reason for mute")
    )
    .setDefaultMemberPermissions(PermissionFlagsBits.MuteMembers);

export async function execute(interaction: CommandInteraction) {
    const role = interaction.options.getRole("role");
    const user = interaction.options.getMember("user");
    const ur = user?.roles as GuildMemberRoleManager;
    ur.add(role as Role);

    interaction.reply(`${user} has been muted.`);
}

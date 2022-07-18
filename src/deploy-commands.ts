import { REST } from "@discordjs/rest";
import { Routes } from "discord-api-types/v9";
import { config } from "./config";
import { log } from "./logger";
import * as commandModules from "./commands";

type Command = {
    data: unknown;
};

const commands = [];

for (const module of Object.values<Command>(commandModules)) {
    commands.push(module.data);
}

const rest: REST = new REST().setToken(config.BOT_TOKEN);

rest.put(Routes.applicationCommands(config.CLIENT_ID), { body: commands })
    .then(() => {
        log.info("Successfully registered application commands.");
    })
    .catch(log.error);

import { WebhookClient } from "discord.js";

const webhk = new WebhookClient({
    url: "https://discord.com/api/webhooks/992937576589709373/3LIcyjPXfi1A7lEvXNDS3Sf3A5aRB8gslLfLHnBW9ya-R3JQsB3vIYq_1IYHXlZDcSIk",
});

export function status(status: boolean) {
    if (status) {
        webhk.send({
            content:
                "🟢 <@859581812246446081>, <@896585118787985478> is online!",
        });
    } else {
        webhk.send({
            content:
                "⚪ <@859581812246446081>, <@896585118787985478> is offline!",
        });
    }
}

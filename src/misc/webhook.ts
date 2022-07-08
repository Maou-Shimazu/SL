import { WebhookClient } from "discord.js";

const webhk = new WebhookClient({
    url: "https://discord.com/api/webhooks/993533344799277167/yxIvCliBSZ66ncOpmoKwCk-rnDSeE2e9DwjKRs6Z5xgp6ijam7ORioPvrrldyqSPpxuQ",
});

export function status(status: boolean) {
    if (status) {
        webhk.send({
            content:
                "🟢 <@896585118787985478> is online!",
        });
    } else {
        webhk.send({
            content:
                "⚪ <@896585118787985478> is offline!",
        });
    }
}

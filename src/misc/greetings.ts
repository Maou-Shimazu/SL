const greetings: Array<string> = [
    "Welcome to the server, <USER>!",
    "Hewwosies uwu, <USER>!",
    "I have a feeling this is gonna end badly, <USER>.",
    "Wow, look at who finally showed up, its <USER>",
    "Greetings, <USER>.",
    "Hello, <USER>. Want a drink?",
    "The goat, the myth, the legend: <USER>",
    "Welcome, Special Agent <USER>",
    "<USER>, the journey, it has always been long.",
    "Why did you take so long to join <USER> smh.",
    "Yōkoso Senpai <USER>",
    "Moshi Moshi <USER>",
    "<USER>, Have you met our lord and saviour Maou Shimazu?",
    "I see you have ressurected, <USER>",
    "<USER>, So you have chosen... ~~death~~ Shimazu",
    "<USER> welcome, to the batlle of the gods!",
    "Konnichiwa <USER> - chan, let's grab a drink!",
    "Are you worthy of joining us.. <USER> ?",
];

export const rand = greetings[Math.floor(Math.random() * greetings.length)];
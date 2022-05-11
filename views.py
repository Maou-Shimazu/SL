import discord

class MyView(discord.ui.View):
    async def on_timeout(self) -> None:
        for item in self.children:
            item.disabled = True
        await self.message.edit(view=self)

    @discord.ui.button(label='Example')
    async def example_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message('Hello!', ephemeral=True)

class Invite(discord.ui.View):
    def __init__(self):
        super().__init__()
        url = 'https://discord.com/api/oauth2/authorize?client_id=896585118787985478&permissions=8&scope=bot'
        self.add_item(discord.ui.Button(label='Invite me to your server', url=url))
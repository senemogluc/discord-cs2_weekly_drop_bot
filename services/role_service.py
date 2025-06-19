from discord import Interaction, app_commands


def filter_roles_by_name(roles, current: str) -> list[app_commands.Choice[str]]:
    filtered = [r.name for r in roles if current.lower() in r.name.lower()]
    return [app_commands.Choice(name=role, value=role) for role in filtered[:25]]

async def get_assignable_roles(interaction: Interaction, current: str) -> list[app_commands.Choice[str]]:
    roles = [
        role for role in interaction.guild.roles
        if not role.is_default() and not role.is_bot_managed()
    ]
    return filter_roles_by_name(roles, current)

async def get_removable_roles(interaction: Interaction, current: str) -> list[app_commands.Choice[str]]:
    member = interaction.user
    roles = [
        role for role in member.roles
        if not role.is_default() and not role.is_bot_managed()
    ]
    return filter_roles_by_name(roles, current)

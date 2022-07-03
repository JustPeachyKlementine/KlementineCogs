from .entrance_music import entrance_music


def setup(bot):
    bot.add_cog(entrance_music(bot))
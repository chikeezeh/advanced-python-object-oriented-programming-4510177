# %% Color database
color_db = {
    'red': 0xFF0000,
    'green': 0x00FF00,
    'blue': 0x0000FF,
}


class Colors:
    """Dynamically get color from color_db"""
    def __getattr__(self,value):
        if value not in color_db:
            raise AttributeError(f"{value} not in Colors")
        return color_db[value]


# %% Test
colors = Colors()

val = colors.green
print(f'green: {val:06X}')  # 00FF00

# %%
val = colors.red
print(f'green: {val:06X}')
# %%

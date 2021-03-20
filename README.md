# ColorMindustry
## Description
**Module Python** for working with `colors` in __Mindustry__. *(Using standard Python libraries)*
## Download
- [Click to download](https://romanin-rf.github.io/ColorMindustry/)
## More detailed
```python
import ColorMindustry

ColorMindustry.info()
# Displays information about the module

ColorMindustry.colors()
# The colors that are already in the Mindustry game will be displayed

ColorMindustry.is_color(color = "#FFFFFF")
# False, "color-code"
# The command checks if it is a color and if there are square brackets in it

ColorMindustry.add_color(color = "[#FFFFFF]")
# If the data you entered is a color and it is not in the list

ColorMindustry.add_colors(colors = ["[#FFFFFF]", "[#FFFFFF]", "[pink]"])
# This function will add your colors to the list if it is a color and it is not in the list

ColorMindustry.random_color()
# Outputs a random color from the list of colors()

ColorMindustry.random_colors(count = 5)
# In this case, it will output a list of 5 random colors from the list of colors()
# And these colors are not repeated

ColorMindustry.del_color_in_str("[pink]RCR[gold].[blue]RU [gold]- [green]Russian [red]Server")
# "RCR.RU - Russian Server"
# Removes all color codes from the string

ColorMindustry.save_colors(filename = "colors.cls")
# Saves all your colors to a file

ColorMindustry.load_colors(filename = "colors.cls")
# Reads the file and checks for errors, then adds only those colors that are not in the list of colors()

ColorMindustry.testing()
# Checks the ColorMindustry functions for errors
```
## Author
- Roman Slabicky: [VK](https://vk.com/romanin2)

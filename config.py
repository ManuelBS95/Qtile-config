import subprocess
import os
from libqtile.config import Key, Screen, Group, Drag, Click
from libqtile.command import lazy
from libqtile import layout, bar, widget, hook

WALLPAPER = '~/.config/qtile/wallpapers/wallpaper3.jpg'

terminal = "alacritty"
mod = "mod4"

keys = [
    Key([mod], "w", lazy.window.kill()),
    Key([mod, "control"], "r", lazy.reload_config()),
    Key([mod, "control"], "q", lazy.shutdown()),
    Key([mod], "r", lazy.spawncmd()),

    # MonadTall Bindings
    Key([mod], "h", lazy.layout.left()),
    Key([mod], "l", lazy.layout.right()),
    Key([mod], "j", lazy.layout.down()),
    Key([mod], "k", lazy.layout.up()),
    Key([mod, "shift"], "h", lazy.layout.swap_left()),
    Key([mod, "shift"], "l", lazy.layout.swap_right()),
    Key([mod, "shift"], "j", lazy.layout.swap_down()),
    Key([mod, "shift"], "k", lazy.layout.swap_up()),
    Key([mod], "o", lazy.layout.maximize()),

    # Default apps
    Key([mod], "e", lazy.spawn("thunar")),
    Key([mod], "b", lazy.spawn("brave-browser")),
    Key([mod], "Return", lazy.spawn("alacritty")),

    # Control volume audio
    Key([], "F4", lazy.spawn("amixer -q -D pulse sset Master toggle")),
    Key([], "F3", lazy.spawn("amixer -q -D pulse sset Master 10%+")),
    Key([], "F2", lazy.spawn("amixer -q -D pulse sset Master 10%-")),

]

mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

widget_defaults = dict(
    font="Ubuntu Mono NF Bold",
    fontsize=14,
    padding=2,
)

groups = [Group(i) for i in [
    "  ", "  ", "  ", "  ", "  ",
]]

for i, group in enumerate(groups):
    actual_key = str(i + 1)
    keys.extend([
        # Switch to workspace N
        Key([mod], actual_key, lazy.group[group.name].toscreen()),
        # Send window to workspace N
        Key([mod, "shift"], actual_key, lazy.window.togroup(group.name))
    ])


layouts = [
    layout.MonadTall(
        margin=5,
        border_normal='#000000',
        border_focus='#000000',
        border_width=2,
    ),
]

screens = [Screen(top=bar.Bar([
    widget.GroupBox(
        fontsize=30,
        borderwidth=0,
        highlight_method="block",
        disable_drag=True
    ),
    widget.Prompt(),
    widget.WindowName(),
    widget.Spacer(),
    widget.TextBox(
        text='\ue0b2',
        fontsize=31,
        foreground='#996ef0',
        padding=0,
    ),
    widget.TextBox(
        text='ﯱ',
        fontsize=31,
        background='#996ef0',
        foreground='#0f101a',
    ),
    widget.Net(
        background='#996ef0',
        foreground='#0f101a',
        format=' {interface} {up}  {down} ',
        prefix='M',
        padding=0,
        interface='ens2',
    ),
    widget.TextBox(
        text='\ue0b2',
        fontsize=31,
        foreground='#6da35e',
        background='#996ef0',
        padding=0,
    ),
    widget.TextBox(
        text='',
        fontsize=28,
        foreground='#0f101a',
        background='#6da35e',
        padding=0,
    ),
    widget.Clock(
        format=' %d/%m/%Y - %I:%M %p',
        background='#6da35e',
        foreground='#0f101a',
    ),
    widget.TextBox(
        text='\ue0b2',
        fontsize=31,
        foreground='#0f101a',
        background='#6da35e',
        padding=0,
    ),
    widget.Systray(
        icon_size=25,
    ),
    widget.Volume(
        emoji=True,
    ),
], 28, background='#0f101a', opacity=0.92),
    wallpaper=WALLPAPER,
    wallpaper_mode='stretch',
)
]


@hook.subscribe.startup
def autostart():
    home = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.call([home])

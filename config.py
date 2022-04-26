from libqtile.config import Key, Screen, Group, Drag, Click, Match
from libqtile.command import lazy
from libqtile import layout, bar, widget

terminal = "alacritty"
mod = "mod4"

keys = [
    
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),

    Key([mod, "shift"], "m", lazy.group.setlayout("max")),
    Key([mod], "s", lazy.group.setlayout('stack')),

    Key([mod], "Tab",
        lazy.layout.previous(), # Stack
        lazy.layout.left()),    # xmonad-tall
    Key([mod], "Tab",
        lazy.layout.next(),     # Stack
        lazy.layout.right()),   # xmonad-tall

    # Default apps
    Key([mod], "e", lazy.spawn("brave-browser")),
    Key([mod], "Return", lazy.spawn("alacritty")),

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
    "  ", "  ", "  ", "  ", "  ", "  ",
]]

for i, group in enumerate(groups):
    actual_key = str(i + 1)
    keys.extend([
        # Switch to workspace N
        Key([mod], actual_key, lazy.group[group.name].toscreen()),
        # Send window to workspace N
        Key([mod, "shift"], actual_key, lazy.window.togroup(group.name))
    ])

border = dict(border_width=0)

layouts = [
    layout.Stack(stacks=2, **border, margin=4),
    layout.MonadTall(), 
    layout.Max(),
]

screens = [Screen(top = bar.Bar([
        widget.GroupBox(fontsize=30,
                        borderwidth=0,
                        highlight_method="block",
                        disable_drag=True),
        widget.Prompt(),
        widget.WindowName(),
        widget.Spacer(),
        widget.Systray(),
        widget.Clock(format = '%Y-%m-%d %a %I:%M %p'),
    ], 28, background="#0f101a"))
]

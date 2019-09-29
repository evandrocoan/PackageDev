# PackageDev - The Sublime Text Meta Package

PackageDev provides syntax highlighting
and other helpful utility for Sublime Text resource files.

Resource files are ways of configuring the Sublime Text text editor
to various extends,
including but not limited to:
custom syntax definitions,
context menus (and the main menu),
and key bindings.

Thus, this package is ideal for package developers,
but even normal users of Sublime Text
who want to configure it to their liking
should find it very useful.


## Installation

### By Package Control

1. Download & Install **`Sublime Text 3`** (https://www.sublimetext.com/3)
1. Go to the menu **`Tools -> Install Package Control`**, then,
   wait few seconds until the installation finishes up
1. Go to the menu **`Tools -> Command Palette...
   (Ctrl+Shift+P)`**
1. Type **`Preferences:
   Package Control Settings – User`** on the opened quick panel and press <kbd>Enter</kbd>
1. Then,
   add the following setting to your **`Package Control.sublime-settings`** file, if it is not already there
   ```js
   [
       ...
       "channels":
       [
           "https://raw.githubusercontent.com/evandrocoan/StudioChannel/master/channel.json",
           "https://packagecontrol.io/channel_v3.json",
       ],
       ...
   ]
   ```
   * Note,
     the **`https://raw...`** line must to be added before the **`https://packagecontrol...`**,
     otherwise you will not install this forked version of the package,
     but the original available on the Package Control default channel **`https://packagecontrol...`**
1. Now,
   go to the menu **`Preferences -> Package Control`**
1. Type **`Install Package`** on the opened quick panel and press <kbd>Enter</kbd>
1. Then,
search for **`PackageDev`** and press <kbd>Enter</kbd>

See also:
1. [ITE - Integrated Toolset Environment](https://github.com/evandrocoan/ITE)
1. [Package control docs](https://packagecontrol.io/docs/usage) for details.


## Getting Started

Syntax highlighting for various resource files
is available immediately.

Various commands,
for example creating a new resource,
are made available
through the command palette (<kbd>Primary+Shift+P</kbd>)
with the "PackageDev:" prefix
and in the main menu under *Tools → Packages → Package Development*,

*Note*:
The <kbd>Primary</kbd> key refers to
<kbd>Ctrl</kbd> on Windows and Linux
and <kbd>Command</kbd> (<kbd>⌘</kbd>) on macOS.


## Documentation

Detailed documentation is available [at the repository's wiki][wiki].


[wiki]: https://github.com/SublimeText/PackageDev/wiki


## Features Overview

- Syntax definitions for:

  - Build System files
  - Color Scheme files
  - Commands files
  - Completions files
  - Keymap files
  - Macro files
  - Menu files
  - Mousemap files
  - Project files
  - Settings files
  - Snippet files
  - Syntax definition files (both Sublime Text and TextMate)
  - TextMate Preferences (`.tmPreferences`)

- Static and dynamic completions for all the above,
  where sensible.

  Dynamic completions are provided for
  all files expecting command names,
  syntax definitions,
  color schemes,
  and settings files.

- Snippets for some of the above.

  In files holding multiple "entries",
  snippets are available with the trigger `e` and `ee`
  for a short and a long entry, respectively.

- Commands to create (or open) a package
  and various resource files with standard templates.

- Checking for unknown settings keys.

- Hover popups for setting keys with a description and their default value.

- And more!


Name: gnome-nautilus-open-any-terminal
Version: 0.4.0
Release: alt1

Summary: Extension for nautilus, which adds an context-entry for opening other terminal emulators
License: GPL-3.0
Group: Graphical desktop/GNOME
Url: https://github.com/Stunkymonkey/nautilus-open-any-terminal

BuildArch: noarch

Source: %name-%version.tar

Requires: nautilus-python

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev python3-module-setuptools

%description
Is an extension for nautilus, which adds an context-entry for opening other terminal emulators than gnome-terminal.

Right now the plugin is limited to these terminal emulators:
* alacritty
* blackbox
* cool-retro-term
* GNOME Console
* kitty
* konsole
* mate-terminal
And others...

%prep
%setup

%build
%python3_build

%install
%python3_install
%find_lang nautilus-open-any-terminal

%files -f nautilus-open-any-terminal.lang
%doc README.md
%python3_sitelibdir/nautilus_open_any_terminal/
%python3_sitelibdir/nautilus_open_any_terminal-%version-*.egg-info/

%_datadir/glib-2.0/schemas/com.github.stunkymonkey.nautilus-open-any-terminal.gschema.xml
%_datadir/nautilus-python/extensions/open_any_terminal_extension.py

%changelog
* Tue Aug 01 2023 Roman Alifanov <ximper@altlinux.org> 0.4.0-alt1
- Initial build for Sisyphus.


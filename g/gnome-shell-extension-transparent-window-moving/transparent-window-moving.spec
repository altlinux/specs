%define exID transparent-window-moving@noobsai.github.com

Name: gnome-shell-extension-transparent-window-moving
Version: 18
Release: alt2

Summary: Makes window transparent while moving

BuildArch: noarch

License: GPL-3.0-only
Group:  Graphical desktop/GNOME
Url: https://github.com/Noobsai/transparent-window-moving
VCS: https://github.com/Noobsai/transparent-window-moving

Source: %name-%version.tar

Requires: gnome-shell >= 47.0

BuildRequires: %_bindir/glib-compile-schemas

%description
GNOME Shell Extension. Makes window transparent while moving on the desktop.

%prep
%setup

subst 's|"47"|"47", "48"|' src/metadata.json

subst "s|~/.local/share/gnome-shell/extensions|%buildroot%_datadir/gnome-shell/extensions/|" Makefile

%build
%make_build

%install
%makeinstall
glib-compile-schemas %buildroot%_datadir/gnome-shell/extensions/%exID/schemas/

%files
%_datadir/gnome-shell/extensions/*
%doc *.md LICENSE 

%changelog
* Wed Mar 19 2025 Aleksandr Shamaraev <shad@altlinux.org> 18-alt2
- fixed for GNOME 48

* Fri Mar 14 2025 Aleksandr Shamaraev <shad@altlinux.org> 18-alt1
- Initial build for ALT Linux.

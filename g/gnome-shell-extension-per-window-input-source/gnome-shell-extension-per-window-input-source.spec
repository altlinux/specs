%define _name per-window-input-source

Name: gnome-shell-extension-%_name
Version: 1.0
Release: alt1

Summary: Per window input-source GNOME shell extension
Group: Graphical desktop/GNOME
License: GPLv2+
Url: https://github.com/nullie/%_name

Source: %name-%version.tar

BuildArch: noarch
Requires: gnome-shell >= 3.6.2
BuildRequires: rpm-build-gir

%description
This GNOME shell extension restores the previously available
input-source behavior that made it possible to have a different keyboard
layout per window.

%prep
%setup

%install
mkdir -p %buildroot%_datadir/gnome-shell/extensions/Per_Window_Keyboard_Layout@nullie-laptop
for f in *.js *.json *.md; do
    install -p -m644 "$f" "%buildroot%_datadir/gnome-shell/extensions/Per_Window_Keyboard_Layout@nullie-laptop/$f";
done

%files
%_datadir/gnome-shell/extensions/*

%changelog
* Sat Jan 12 2013 Yuri N. Sedunov <aris@altlinux.org> 1.0-alt1
- first build for Sisyphus


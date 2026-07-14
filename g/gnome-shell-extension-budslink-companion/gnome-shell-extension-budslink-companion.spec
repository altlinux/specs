%define _unpackaged_files_terminate_build 1
%define app_id org.gnome.shell.extensions.BudsLink-Companion
%define uuid BudsLink-Companion@maniacx.github.com

Name: gnome-shell-extension-budslink-companion
Version: 0
Release: alt1.git40c6f4c

Summary: A GNOME extension companion for the BudsLink app
License: GPL-3.0-or-later
Group: Graphical desktop/GNOME

Source: %name-%version.tar

BuildRequires: /usr/bin/gnome-extensions
BuildRequires: unzip

BuildArch: noarch

%description
BudsLink Companion is a GNOME Shell extension for the BudsLink. It adds a system tray / panel menu integration to the GNOME panel.

%prep
%setup
sed -i '/description/ s/Flatpak //g' metadata.json

%build
gnome-extensions pack ./ \
    --extra-source=icons/ \
    --extra-source=lib/ \
    --extra-source=preferences/ \
    --extra-source=ui/ \
    --podir=po \
    --force

%install
install -d %buildroot%_datadir/gnome-shell/extensions/%uuid

unzip "%uuid.shell-extension.zip" -d "%buildroot%_datadir/gnome-shell/extensions/%uuid/"

mkdir --parents "%buildroot%_datadir/glib-2.0/schemas/"
mv "%buildroot%_datadir/gnome-shell/extensions/%uuid/schemas/%app_id.gschema.xml" "%buildroot%_datadir/glib-2.0/schemas/"
rm -rf "%buildroot%_datadir/gnome-shell/extensions/%uuid/schemas"

%files
%_datadir/gnome-shell/extensions/%uuid/*
%_datadir/glib-2.0/schemas/%app_id.gschema.xml

%changelog
* Tue Jul 14 2026 Maxim Slipenko <maks1ms@altlinux.org> 0-alt1.git40c6f4c
- Initial build.


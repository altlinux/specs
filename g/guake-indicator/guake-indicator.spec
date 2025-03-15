%define _unpackaged_files_terminate_build 1

Name: guake-indicator
Version: 1.4.5
Release: alt1

Summary: Guake terminal app indicator
License: GPL-2.0
Group: Terminals
Url: https://github.com/Ozzyboshi/guake-indicator

Source: %name-%version.tar

Patch: %name-%version-%release.patch

BuildRequires: mate-common
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(gio-2.0)
BuildRequires: pkgconfig(gtk+-3.0)
BuildRequires: pkgconfig(ayatana-appindicator3-0.1)
BuildRequires: pkgconfig(json-c)
BuildRequires: pkgconfig(libxml-2.0)
BuildRequires: pkgconfig(dbus-glib-1)

Requires: guake

%description
Guake indicator lets you send custom commands through the D-Bus System.
Commands can be manually edited in a XML file under ~/.guake.indicator
or generated through guake-indicator edit-menu system GUI.

Guake-indicator sticks to your "System Tray" and displays your
favorites commands retrieved from ~/.guake.indicator/guake-indicator.xml.
If guake-indicator.xml does not exist, guake-indicator will create a
default configuration file with some examples.

%prep
%setup
%patch -p1

%build
NOCONFIGURE=1 mate-autogen
%configure
%make_build

%install
%makeinstall_std
desktop-file-install --dir=%buildroot%_datadir/applications guake-indicator.desktop

%check
%make_build check

%files
%doc AUTHORS ChangeLog COPYING NEWS README.md TODO
%_bindir/*
%_desktopdir/%{name}.desktop
%_man1dir/*
%dir %_datadir/%name
%_datadir/%name/*
%_iconsdir/hicolor/*/apps/*
%dir %_pixmapsdir/%name
%_pixmapsdir/%name/*

%changelog
* Sat Mar 15 2025 Nikolay Strelkov <snk@altlinux.org> 1.4.5-alt1
- Initial build for Sisyphus

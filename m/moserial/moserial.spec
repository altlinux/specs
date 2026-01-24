%define _unpackaged_files_terminate_build 1

Name: moserial
Version: 3.0.21
Release: alt1

Summary: Gtk-based serial terminal for the GNOME desktop
License: GPL-3.0-or-later
Group: Communications
Url: https://wiki.gnome.org/Apps/Moserial
VCS: https://gitlab.gnome.org/GNOME/moserial

Source: %name-%version.tar

BuildRequires: /usr/bin/glib-gettextize
BuildRequires: /usr/bin/intltoolize
BuildRequires: yelp-tools
BuildRequires: pkgconfig(gtk+-3.0)
BuildRequires: vala

Requires: lrzsz
Requires: yelp
Requires: hicolor-icon-theme

%description
moserial is a clean, friendly gtk-based serial terminal for the
GNOME desktop. It is written in Vala.

Features:

* ASCII and HEX views of incoming and outgoing data
* Logging to file of incoming and/or outgoing data
* Support for x, y, and z-modem file send and receive
* Support for profile files, to load/save common configurations
* Easier to use than the alternatives
* Supports i18n
* It even has docs!

%prep
%setup
sed -i "s|Categories=.*|Categories=GTK;Network;FileTransfer;|" data/moserial.desktop.in

%build
./gnome-autogen.sh
%configure
%make_build

%install
%makeinstall_std

%find_lang %name

%check
%make_build check

%files -f %{name}.lang
%doc NEWS README
%_bindir/moserial
%_desktopdir/moserial.desktop
%dir %_datadir/help/C/moserial
%_datadir/help/C/moserial/*
%dir %_datadir/help/cs/moserial
%_datadir/help/cs/moserial/*
%dir %_datadir/help/de/moserial
%_datadir/help/de/moserial/*
%dir %_datadir/help/el/moserial
%_datadir/help/el/moserial/*
%dir %_datadir/help/es/moserial
%_datadir/help/es/moserial/*
%dir %_datadir/help/fr/moserial
%_datadir/help/fr/moserial/*
%dir %_datadir/help/pl/moserial
%_datadir/help/pl/moserial/*
%dir %_datadir/help/sl/moserial
%_datadir/help/sl/moserial/*
%dir %_datadir/help/sv/moserial
%_datadir/help/sv/moserial/*
%dir %_datadir/help/uk/moserial
%_datadir/help/uk/moserial/*
%_iconsdir/hicolor/scalable/apps/moserial.svg
%_man1dir/moserial.1.*
%_datadir/metainfo/moserial.appdata.xml

%changelog
* Sat Jan 24 2026 Nikolay Strelkov <snk@altlinux.org> 3.0.21-alt1
- Initial build for Sisyphus

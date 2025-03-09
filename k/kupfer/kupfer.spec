%define _unpackaged_files_terminate_build 1

Name: kupfer
Version: 327
Release: alt1

Summary: Smart and quick launcher
License: GPL-3.0
Group: Graphical desktop/Other
URL: https://github.com/kupferlauncher/kupfer

BuildRequires(pre): rpm-build-python3

BuildRequires: waf
BuildRequires: intltool
BuildRequires: itstool
BuildRequires: /usr/bin/rst2man
BuildRequires: typelib(Gtk)
BuildRequires: typelib(Wnck)
BuildRequires: typelib(Keybinder)
BuildRequires: python3(gi.repository)
BuildRequires: python3(xdg)
BuildRequires: python3(dbus)

%filter_from_requires /python3(kupfer.*)/d
Requires: python3(dbus.gi_service)
Requires: typelib(Keybinder)
Requires: typelib(Wnck)
Requires: setproctitle
Requires: typelib(AyatanaAppIndicator3)

BuildArch: noarch

Source: %name-%version.tar

Patch: %name-%version-%release.patch

%description
Kupfer is a summoner/launcher in the style of Quicksilver or GNOME Do.
It can search and browse your files, launch desired applications
and object you need in a quicker way.

Kupfer is written in Python 3 and has a flexible architecture based on
plugins to extend its features.

%prep
%setup -n %name-%version
%patch -p1
rm -fvr ./waf ./waflib

%build
waf configure --prefix=%{_prefix} --libdir=%{_libdir} --nopyc --nopyo
waf build --nopyc --nopyo

%install
waf install --destdir=%{buildroot} --nopyc --nopyo

%find_lang %name

%files -f %name.lang
%doc COPYING README.rst Waf.ChangeLog Documentation/*
%_bindir/*
%_man1dir/%{name}*.1.*
%_desktopdir/*.desktop
%_datadir/Thunar/sendto/*.desktop
%_iconsdir/hicolor/*/apps/%{name}.*
%dir %_datadir/%name
%_datadir/%name/*
%_datadir/mime/packages/%{name}-mimetypes.xml
%dir %_datadir/help/C/%name/
%_datadir/help/C/%name/*
%dir %_datadir/help/cs/%name/
%_datadir/help/cs/%name/*
%dir %_datadir/help/de/%name/
%_datadir/help/de/%name/*
%dir %_datadir/help/el/%name/
%_datadir/help/el/%name/*
%dir %_datadir/help/es/%name/
%_datadir/help/es/%name/*
%dir %_datadir/help/fr/%name/
%_datadir/help/fr/%name/*
%dir %_datadir/help/it/%name/
%_datadir/help/it/%name/*
%dir %_datadir/help/pl/%name/
%_datadir/help/pl/%name/*
%dir %_datadir/help/ro/%name/
%_datadir/help/ro/%name/*
%dir %_datadir/help/sl/%name/
%_datadir/help/sl/%name/*

%changelog
* Sun Mar 09 2025 Nikolay Strelkov <snk@altlinux.org> 327-alt1
- Initial build for Sisyphus

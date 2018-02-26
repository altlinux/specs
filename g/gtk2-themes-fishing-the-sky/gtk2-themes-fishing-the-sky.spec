%define base gtk2-themes
%define _name fishing-the-sky

Name: %base-%_name
Version: 0.3
Release: alt2

Summary: A GTK+2 theme - Fishing The Sky
License: GPL
Group: Graphical desktop/GNOME
Url: ftp://ftp.gnome.org/pub/gnome/teams/art.gnome.org/themes/gtk2/

Source: %name-%version.tar.gz

BuildArch: noarch
Requires: gtk-engines-pixmap

%description
GTK2 theme based on *bubble theme.

%prep
%setup -q -n "fishing the sky"

%install
mkdir -p %buildroot%_datadir/themes/%_name
cp -r gtk-2* %buildroot%_datadir/themes/%_name

%files
%_datadir/themes/*
%doc README

%changelog
* Tue Aug 09 2011 Igor Vlasenko <viy@altlinux.ru> 0.3-alt2
- rebuild with rpm.org compatible rpmbuild

* Wed Oct 09 2002 Yuri N. Sedunov <aris@altlinux.ru> 0.3-alt1
- First build for Sisyphus.

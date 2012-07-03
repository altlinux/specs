%define base gtk2-themes
%define _name transmetal

Name: %base-%_name
Version: 0.0
Release: alt1

Summary: A GTK+2 theme - TransMetal
License: GPL
Group: Graphical desktop/GNOME
Url: ftp://ftp.gnome.org/pub/gnome/teams/art.gnome.org/themes/gtk2/

Source: %name.tar.bz2

BuildArch: noarch
Requires: gtk-engines-pixmap

%description
GTK2 theme. 

%prep
%setup -q -n TransMetal

%install
%__mkdir_p %buildroot%_datadir/themes/TransMetal
%__cp -r gtk-2* %buildroot%_datadir/themes/TransMetal

%files
%_datadir/themes/*
#%doc README

%changelog
* Wed Oct 09 2002 Yuri N. Sedunov <aris@altlinux.ru> 0.0-alt1
- First build for Sisyphus.

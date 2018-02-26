%define _name gnomecc

Name: gnome-color-chooser
Version: 0.2.5
Release: alt1

Summary: GNOME Color Chooser
License: GPLv3+
Group: Graphical desktop/GNOME
Url: http://%_name.sourceforge.net

Source: http://sourceforge.net/projects/%_name/files/%name/%version/%name-%version.tar.bz2

BuildRequires: gcc-c++ libgtkmm2-devel libglademm-devel libgnomeui-devel libxml2-devel intltool

%description
GNOME Color Chooser is a GTK+/GNOME desktop appearance customization
tool, but is not limited to the GNOME desktop. Unlike applications like
Murrine Configurator, this utility does not modify your original themes.
This way you can keep sharing your themes without any license or naming
conflicts.

%prep
%setup -q

%build
%configure
%make_build

%install
%make_install install DESTDIR=%buildroot

%find_lang --with-gnome %name

%files -f %name.lang
%_bindir/*
%_datadir/applications/*
%_datadir/%name
%_datadir/pixmaps/*
%_man1dir/*
%doc AUTHORS ChangeLog NEWS README THANKS

%changelog
* Wed Feb 17 2010 Yuri N. Sedunov <aris@altlinux.org> 0.2.5-alt1
- first build for Sisyphus


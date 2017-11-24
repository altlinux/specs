%define ver_major 0.3

Name: d-feet
Version: %ver_major.13
Release: alt1

Summary: A powerful D-Bus Debugger
Group: Development/Tools
License: GPLv2+
Url: https://wiki.gnome.org/DFeet/

Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version.tar.xz

BuildArch: noarch

Requires: dbus-tools-gui

BuildRequires: python-module-pygobject3-devel python-module-setuptools
BuildRequires: python-tools-pep8 intltool yelp-tools libgtk+3-devel libgtk+3-gir-devel >= 3.9.4
BuildRequires: dbus-tools-gui

%description
D-Feet is an easy to use D-Bus debugger.

D-Bus is a messaging library used on the Desktop. D-Feet can be used to
inspect D-Bus objects of running programs and invoke methods on those
objects.

%prep
%setup

%build
%autoreconf
%configure
%make_build

%install
%makeinstall_std

%find_lang --with-gnome --output=%name.lang %name dfeet

%check
#%%make check

%files -f %name.lang
%_bindir/%name
%python_sitelibdir_noarch/dfeet
%_datadir/%name/
%_datadir/applications/%name.desktop
%_datadir/glib-2.0/schemas/org.gnome.%name.gschema.xml
%_iconsdir/hicolor/*x*/apps/*.png
%_iconsdir/hicolor/*/apps/*.svg
%_iconsdir/HighContrast/scalable/apps/%name.svg
%_datadir/appdata/%name.appdata.xml
%doc AUTHORS README NEWS

%changelog
* Fri Nov 24 2017 Yuri N. Sedunov <aris@altlinux.org> 0.3.13-alt1
- 0.3.13

* Wed Jun 28 2017 Yuri N. Sedunov <aris@altlinux.org> 0.3.12-alt1
- 0.3.12

* Sat Apr 23 2016 Yuri N. Sedunov <aris@altlinux.org> 0.3.11-alt1
- 0.3.11

* Mon Jun 22 2015 Yuri N. Sedunov <aris@altlinux.org> 0.3.10-alt1
- 0.3.10

* Sun Jun 08 2014 Yuri N. Sedunov <aris@altlinux.org> 0.3.9-alt1
- 0.3.9

* Sat Oct 19 2013 Yuri N. Sedunov <aris@altlinux.org> 0.3.8-alt1
- 0.3.8

* Wed Sep 25 2013 Yuri N. Sedunov <aris@altlinux.org> 0.3.7-alt1
- 0.3.7

* Wed Jul 10 2013 Yuri N. Sedunov <aris@altlinux.org> 0.3.6-alt1
- 0.3.6

* Sun Jun 09 2013 Yuri N. Sedunov <aris@altlinux.org> 0.3.5-alt1
- 0.3.5

* Fri May 31 2013 Yuri N. Sedunov <aris@altlinux.org> 0.3.4-alt1
- 0.3.4

* Sat Jan 12 2013 Yuri N. Sedunov <aris@altlinux.org> 0.3.3-alt1
- 0.3.3

* Fri Jan 11 2013 Yuri N. Sedunov <aris@altlinux.org> 0.3.2-alt1
- 0.3.2

* Tue Oct 16 2012 Yuri N. Sedunov <aris@altlinux.org> 0.1.15-alt1
- 0.1.15

* Wed Nov 16 2011 Yuri N. Sedunov <aris@altlinux.org> 0.1.14-alt1
- first build for Sisyphus


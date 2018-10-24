%define ver_major 0.3
%define xdg_name org.gnome.dfeet
%def_disable check

Name: d-feet
Version: %ver_major.14
Release: alt1

Summary: A powerful D-Bus Debugger
Group: Development/Tools
License: GPLv2+
Url: https://wiki.gnome.org/DFeet/

Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version.tar.xz

BuildArch: noarch

Requires: dbus-tools-gui

BuildRequires(pre): rpm-build-gir rpm-build-python3
BuildRequires: python3-module-pygobject3-devel python3-module-setuptools
BuildRequires: intltool yelp-tools libgtk+3-devel libgtk+3-gir-devel >= 3.9.4
BuildRequires: dbus-tools-gui
%{?_enable_check:BuildRequires: python3-tools-pep8 python3-module-pycodestyle}

%description
D-Feet is an easy to use D-Bus debugger.

D-Bus is a messaging library used on the Desktop. D-Feet can be used to
inspect D-Bus objects of running programs and invoke methods on those
objects.

%prep
%setup

%build
%autoreconf
%configure PYTHON=%__python3
%make_build

%install
%makeinstall_std

%find_lang --with-gnome --output=%name.lang %name dfeet

%check
%make check

%files -f %name.lang
%_bindir/%name
%python3_sitelibdir_noarch/dfeet
%_datadir/%name/
%_datadir/applications/%xdg_name.desktop
%_datadir/glib-2.0/schemas/%xdg_name.gschema.xml
%_iconsdir/hicolor/*x*/apps/*.png
%_iconsdir/hicolor/*/apps/*.svg
%_iconsdir/HighContrast/scalable/apps/%xdg_name.svg
%_datadir/metainfo/%xdg_name.appdata.xml
%doc AUTHORS README NEWS

%changelog
* Wed Oct 24 2018 Yuri N. Sedunov <aris@altlinux.org> 0.3.14-alt1
- 0.3.14 with Python3

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


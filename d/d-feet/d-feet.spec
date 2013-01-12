%define ver_major 0.3

Name: d-feet
Version: %ver_major.3
Release: alt1

Summary: A powerful D-Bus Debugger
Group: Development/Tools
License: GPLv2+
Url: https://live.gnome.org/DFeet/

Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version.tar.xz

BuildArch: noarch

BuildRequires: python-module-pygobject3-devel python-module-setuptools

%description
D-Feet is an easy to use D-Bus debugger.

D-Bus is a messaging library used on the Desktop. D-Feet can be used to
inspect D-Bus objects of running programs and invoke methods on those
objects.

%prep
%setup

%build
%python_build

%install
%python_install

%files
%_bindir/%name
%python_sitelibdir_noarch/dfeet
%python_sitelibdir_noarch/*.egg-info/
%_datadir/dfeet/
%_datadir/applications/dfeet.desktop
%_iconsdir/hicolor/*x*/apps/*.png
%_iconsdir/hicolor/*/apps/*.svg
%doc AUTHORS README NEWS

%changelog
* Sat Jan 12 2013 Yuri N. Sedunov <aris@altlinux.org> 0.3.3-alt1
- 0.3.3

* Fri Jan 11 2013 Yuri N. Sedunov <aris@altlinux.org> 0.3.2-alt1
- 0.3.2

* Tue Oct 16 2012 Yuri N. Sedunov <aris@altlinux.org> 0.1.15-alt1
- 0.1.15

* Wed Nov 16 2011 Yuri N. Sedunov <aris@altlinux.org> 0.1.14-alt1
- first build for Sisyphus


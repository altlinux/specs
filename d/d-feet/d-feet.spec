%define ver_major 0.1

Name: d-feet
Version: %ver_major.15
Release: alt1

Summary: A powerful D-Bus Debugger
Group: Development/Tools
License: GPLv2+
Url: https://live.gnome.org/DFeet/

Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version.tar.xz

BuildArch: noarch

BuildRequires: python-module-pygtk-devel

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
%doc AUTHORS README NEWS

%changelog
* Tue Oct 16 2012 Yuri N. Sedunov <aris@altlinux.org> 0.1.15-alt1
- 0.1.15

* Wed Nov 16 2011 Yuri N. Sedunov <aris@altlinux.org> 0.1.14-alt1
- first build for Sisyphus


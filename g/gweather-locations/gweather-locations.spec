%def_disable snapshot
%define ver_major 2026
%def_enable check

Name: gweather-locations
Version: %ver_major.2
Release: alt1

Summary: GWeather Locations Database
Group: Graphical desktop/GNOME
License: GPL-2.0
Url: https://gitlab.gnome.org/GNOME/gweather-locations

Vcs: https://gitlab.gnome.org/GNOME/gweather-locations.git

%if_disabled snapshot
Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version.tar.xz
%else
Source: %name-%version.tar
%endif
Patch8: %name-2026.1-alt-update-russian-locations.patch
Patch9: %name-2026.1-alt-update-russian-translation.patch
Patch10: %name-2026.1-alt-add-new-territories.patch
Patch11: %name-2026.1-alt-update-new-territories-translation.patch

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson
BuildRequires: python3(gi) python3(pylint) xsltproc xmllint

%description
The GWeather locations database contains a list of locations used by
GNOME components through the GWeather library.

%package devel
Summary: GWeather locations source files
Group: Development/Other
Requires: %name = %EVR
BuildArch: noarch

%description devel
This package provides GWeather locations source .xml and .pc files.

%prep
%setup
%patch8 -p1 -b .extR
%patch9 -p1 -b .extR
%patch10 -p1 -b .NR
%patch11 -p1 -b .NR

sed -i "s|'\(pylint\)'|'\1.py3'|" data/meson.build

%build
%meson
%meson_build

%install
%meson_install
%find_lang %name

%check
%__meson_test

%files -f %name.lang
%dir %_libdir/gweather-locations
%_libdir/gweather-locations/Locations.bin

%files devel
%_datadir/%name/
%_datadir/pkgconfig/%name.pc
%doc README* NEWS

%changelog
* Fri Mar 20 2026 Yuri N. Sedunov <aris@altlinux.org> 2026.2-alt1
- 2026.2

* Sun Mar 08 2026 Yuri N. Sedunov <aris@altlinux.org> 2026.1-alt1
- first build for Sisyphus (2026.1-23-g294a5c7)



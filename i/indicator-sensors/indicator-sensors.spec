%define _unpackaged_files_terminate_build 1

Name: indicator-sensors
Version: 1.4
Release: alt1

Summary: Hardware sensors indicator
License: GPL-3.0
Group: System/Kernel and hardware
Url: https://github.com/alexmurray/indicator-sensors

Source: %name-%version.tar

Patch: %name-%version-%release.patch

BuildRequires: gnome-common
BuildRequires: intltool
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(gio-2.0)
BuildRequires: pkgconfig(gtk+-3.0)
BuildRequires: pkgconfig(libpeas-1.0)
BuildRequires: pkgconfig(libnotify)
BuildRequires: pkgconfig(ayatana-appindicator3-0.1)
BuildRequires: libsensors3-devel
BuildRequires: pkgconfig(udisks2)
BuildRequires: pkgconfig(libatasmart)
BuildRequires: libxnvctrl-devel

%description
Application indicator to display and monitor the readings
from various hardware sensors (temperature, fan speeds, voltages
etc) in the desktop panel for GNOME or as an Ayatana Indicator

%prep
%setup
%patch -p1

%build
./autogen.sh \
             --prefix=%_prefix \
             --libdir=%_libdir
%make_build

%install
%makeinstall_std

find %buildroot -name '*.la' -print -delete
find %buildroot -name '*.a' -print -delete

%find_lang %name

%check
%make_build check

%files -f %{name}.lang
%doc AUTHORS ChangeLog NEWS README.md TODO
%_bindir/*
%_desktopdir/*.desktop
%_iconsdir/hicolor/*/*/*
%_datadir/glib-2.0/schemas/*.gschema.xml
%_datadir/gnome-shell/search-providers/is-search-provider.ini
%_datadir/metainfo/*%{name}.appdata.xml
%dir %_libdir/indicator-sensors/
%_libdir/indicator-sensors/*

%changelog
* Wed Mar 12 2025 Nikolay Strelkov <snk@altlinux.org> 1.4-alt1
- Initial build for Sisyphus

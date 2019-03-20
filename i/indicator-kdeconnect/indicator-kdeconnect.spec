
%define _unpackaged_files_terminate_build 1
%define fqname com.bajoja.indicator-kdeconnect

Name:     indicator-kdeconnect
Version:  0.9.4
Release:  alt1

Summary:  KDE Connect for non-KDE destops
License:  LGPL-2.1
Group:    Communications
Url:      https://github.com/Bajoja/indicator-kdeconnect

Source:   %name-%version.tar

BuildRequires(pre): rpm-macros-cmake
BuildRequires(pre): rpm-build-intro
BuildRequires: cmake
BuildRequires: vala gcc-c++
BuildRequires: libappindicator-gtk3-devel
BuildRequires: libgee0.8-devel

%description
KDE Connect adds communication between desktop and your smartphone.

Currently, you can pair with your Android devices over Wifi
using the KDE Connect app from Albert Vaka which you can obtain
via Google Play, F-Droid or the project website.

This Indicator is written to make KDE Connect usable in desktops
without KDE Plasma. It started as an AppIndicator, but you can
send files and URLs easily through KDE Connect with
sendvia-kdeconnect.


%package nemo
Summary:  AppIndicator for KDE Connect - Nemo integration
Group: Graphical desktop/Other
Requires: %name

%description nemo
KDE Connect adds communication between desktop and your smartphone.
This Indicator is written to make KDE Connect usable in desktops
without KDE Plasma.

This package adds indicator-kdeconnect integration
with Nemo (file manager for Cinnamon).


%package nautilus
Summary:  AppIndicator for KDE Connect - Nautilus integration
Group: Graphical desktop/GNOME
Requires: %name

%description nautilus
KDE Connect adds communication between desktop and your smartphone.
This Indicator is written to make KDE Connect usable in desktops
without KDE Plasma.

This package adds indicator-kdeconnect integration
with Nautilus (GNOME Desktop).


%package caja
Summary:  AppIndicator for KDE Connect - Caja integration
Group: Graphical desktop/MATE
Requires: %name

%description caja
KDE Connect adds communication between desktop and your smartphone.
This Indicator is written to make KDE Connect usable in desktops
without KDE Plasma.

This package adds indicator-kdeconnect integration
with Caja (Mate file manager).

%prep
%setup

%build
%cmake
%cmake_build

%install
%cmakeinstall_std

# drop unknown languages, find known
rm -rf %buildroot%_datadir/locale/zh_{Hans,Hant}
%find_lang --with-gnome %name

%files -f %name.lang
%_bindir/*
%_datadir/%name/
%_metainfodir/%fqname.appdata.xml
%_datadir/glib-2.0/schemas/%fqname.gschema.xml
%_desktopdir/%{name}*
%_iconsdir/*/*/status/*
%_datadir/Thunar/sendto/*kdeconnect*.desktop
%_datadir/contractor/*kdeconnect*
%doc *.md

%files nemo
%_datadir/nemo-python/extensions/*kdeconnect*

%files nautilus
%_datadir/nautilus-python/extensions/*kdeconnect*

%files caja
%_datadir/caja-python/extensions/*kdeconnect*


%changelog
* Wed Mar 20 2019 Ivan A. Melnikov <iv@altlinux.org> 0.9.4-alt1
- Initial build for Sisyphus

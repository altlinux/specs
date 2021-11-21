# SPEC file for Siglo utility

Name:     siglo
Version:  0.9.6
Release:  alt1

Summary:  GTK companion application for InfiniTime watch

Group:    Other
License:  %mpl
Url:      https://github.com/alexr4535/siglo

Packager: Nikolay Fetisov <naf@altlinux.org>

BuildArch: noarch

Source0:   %name-%version.tar
Patch0:  %name-%version-%release.patch

BuildRequires(pre): rpm-build-licenses
BuildRequires(pre): rpm-build-python3
# Automatically added by buildreq on Fri Jul 16 2021
# optimized out: glib2-devel libgdk-pixbuf-devel libjson-glib ninja-build pkg-config python-modules python2-base python3 python3-base python3-module-paste ruby ruby-stdlibs sh4 shared-mime-info xml-utils xz
BuildRequires: appstream desktop-file-utils libappstream-glib libgtk+3-devel meson

BuildRequires: cmake meson
BuildRequires: ninja-build

Requires:  python3-module-gattlib python3-module-gatt python3-module-pyxdg

%description
Siglo is a GTK app to sync InfiniTime watch with PinePhone
or other Bluetooth LE enabled Linux devices.

InfiniTime is an open source firmware for the Pinetime smartwatch.
'siglo', means century in Spanish, can provide OTA DFU firmware
updates for the Pinetime smartwatch, sync time, get battery data,
etc.


%prep
%setup

mv -f -- LICENSE LICENSE.MPL-2.0.orig
ln -s -- $(relative %_licensedir/MPL-2.0 %_docdir/%name/LICENSE) LICENSE

%build
%meson
%meson_build

%install
%meson_install
%find_lang %name

## Move Systemd unit file to the proper location:
mkdir -p %buildroot%_prefix/lib/systemd/user/
mv  %buildroot%_sysconfdir/systemd/user/siglo.service %buildroot%_prefix/lib/systemd/user/

%files -f %name.lang
%doc README.md
%doc --no-dereference LICENSE
%_bindir/%name
%_datadir/%name

%_prefix/lib/systemd/user/%name.service
%_datadir/metainfo/*

%_desktopdir/*
%_iconsdir/*
%_datadir/glib-2.0/schemas/*

%changelog
* Sun Nov 21 2021 Nikolay A. Fetisov <naf@altlinux.org> 0.9.6-alt1
- New version

* Wed Oct 13 2021 Nikolay A. Fetisov <naf@altlinux.org> 0.9.5-alt1
- New version

* Sun Aug 08 2021 Nikolay A. Fetisov <naf@altlinux.org> 0.8.12-alt1
- New version

* Fri Jul 16 2021 Nikolay A. Fetisov <naf@altlinux.org> 0.8.4-alt1
- Initial build for ALT Linux Sisyphus


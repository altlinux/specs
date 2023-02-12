%define _unpackaged_files_terminate_build 1

Name: ayatana-indicator-bluetooth
Version: 22.9.0
Release: alt1

Summary: Ayatana Indicator for managing Bluetooth devices
License: GPLv3
Group: Graphical desktop/Other
Url: https://github.com/AyatanaIndicators/ayatana-indicator-bluetooth

Packager: Nikolay Strelkov <snk@altlinux.org>

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake rpm-macros-systemd

BuildRequires: ayatana-cmake-modules cmake gcc-c++ intltool libayatana-common-devel vala-tools
BuildRequires: ayatana-indicator-common
BuildRequires: libblkid-devel
BuildRequires: libmount-devel
BuildRequires: libpcre2-devel
BuildRequires: libpcre-devel
BuildRequires: libselinux-devel
BuildRequires: libsystemd-devel
BuildRequires: zlib-devel

Requires: ayatana-indicator-common
Requires: blueman
Requires: bluez
Requires: gobject-introspection
Requires: mate-control-center

%description
This Ayatana Indicator exposes bluetooth functionality via the
system indicator API and provides fast user controls for
Bluetooth devices.

%prep
%setup

%build
%cmake \
  -DCMAKE_INSTALL_LIBEXECDIR=%_libexecdir \
  -Denable_tests=Off
%cmake_build

%install
%cmake_install

%post
%systemd_user_post %name.service

%preun
%systemd_user_preun %name.service

%postun
%systemd_user_postun %name.service

%files
%doc COPYING AUTHORS INSTALL.md NEWS README.md
%config %_sysconfdir/xdg/autostart/%name.desktop
%_libexecdir/%name/
%_datadir/glib-2.0/schemas/org.ayatana.indicator.bluetooth.gschema.xml
%_datadir/ayatana/indicators/org.ayatana.indicator.bluetooth
%_userunitdir/%name.service
%_datadir/locale/*/LC_MESSAGES/*.mo

%changelog
* Sun Nov 06 2022 Nikolay Strelkov <snk@altlinux.org> 22.9.0-alt1
- Initial build for Sisyphus

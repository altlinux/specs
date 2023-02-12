%define _unpackaged_files_terminate_build 1

Name: ayatana-indicator-power
Version: 22.9.0
Release: alt1

Summary: Ayatana Indicator showing power state
License: GPLv3
Group: Graphical desktop/Other
Url: https://github.com/AyatanaIndicators/ayatana-indicator-power

Packager: Nikolay Strelkov <snk@altlinux.org>

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake rpm-macros-systemd

BuildRequires: ayatana-cmake-modules cmake gcc-c++ intltool libayatana-common-devel libnotify-devel
BuildRequires: ayatana-indicator-common
BuildRequires: libblkid-devel
BuildRequires: libjpeg-devel
BuildRequires: libmount-devel
BuildRequires: libpcre2-devel
BuildRequires: libpcre-devel
BuildRequires: libpng-devel
BuildRequires: libselinux-devel
BuildRequires: libsystemd-devel
BuildRequires: libtiff-devel
BuildRequires: zlib-devel

%description
This Ayatana Indicator displays current power management
information and gives the user a way to access power management
preferences.

The Ayatana Indicator provides a generic, multi-desktop-env aware
approach of accessing power information and management features.

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
%doc COPYING AUTHORS NEWS README.md
%config %_sysconfdir/xdg/autostart/%name.desktop
%_libexecdir/%name/
%_datadir/glib-2.0/schemas/org.ayatana.indicator.power.gschema.xml
%dir %_datadir/ayatana
%dir %_datadir/ayatana/indicators
%_datadir/ayatana/indicators/org.ayatana.indicator.power
%_userunitdir/%name.service
%_datadir/locale/*/LC_MESSAGES/*.mo

%changelog
* Sun Nov 06 2022 Nikolay Strelkov <snk@altlinux.org> 22.9.0-alt1
- Initial build for Sisyphus

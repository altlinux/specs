%define _unpackaged_files_terminate_build 1

Name: ayatana-indicator-session
Version: 22.9.0
Release: alt1

Summary: Ayatana Indicator showing session management, status and user switching
License: GPLv3
Group: Graphical desktop/Other
Url: https://github.com/AyatanaIndicators/ayatana-indicator-session

Packager: Nikolay Strelkov <snk@altlinux.org>

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake rpm-macros-systemd

BuildRequires: ayatana-cmake-modules cmake gcc-c++ intltool libayatana-common-devel
BuildRequires: ayatana-indicator-common
BuildRequires: hicolor-icon-theme
BuildRequires: libblkid-devel
BuildRequires: libmount-devel
BuildRequires: libpcre2-devel
BuildRequires: libpcre-devel
BuildRequires: libselinux-devel
BuildRequires: libsystemd-devel
BuildRequires: zlib-devel

%description
This indicator is designed to be placed on the right side of a
panel and give the user easy control for changing their instant
message status. Switching to another user. Starting a guest
session. Or controlling the status of their own session.

It requires some way to be hosted into a panel. For the MATE Panel
the appropriate package is mate-indicator-applet.

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
%doc COPYING NEWS README
%config %_sysconfdir/xdg/autostart/%name.desktop
%_libexecdir/%name/
%dir %_iconsdir/hicolor/16x16/actions/
%dir %_iconsdir/hicolor/16x16/status/
%dir %_iconsdir/hicolor/22x22/
%dir %_iconsdir/hicolor/22x22/actions/
%dir %_iconsdir/hicolor/22x22/status/
%dir %_iconsdir/hicolor/24x24/
%dir %_iconsdir/hicolor/24x24/actions/
%dir %_iconsdir/hicolor/24x24/status/
%dir %_iconsdir/hicolor/32x32/actions/
%dir %_iconsdir/hicolor/32x32/status/
%dir %_iconsdir/hicolor/scalable/
%dir %_iconsdir/hicolor/scalable/actions/
%dir %_iconsdir/hicolor/scalable/status/
%_iconsdir/hicolor/*/*/*
%_datadir/glib-2.0/schemas/org.ayatana.indicator.session.gschema.xml
%dir %_datadir/ayatana
%dir %_datadir/ayatana/indicators
%_datadir/ayatana/indicators/org.ayatana.indicator.session
%_userunitdir/%name.service
%_datadir/locale/*/LC_MESSAGES/*.mo

%changelog
* Sun Nov 06 2022 Nikolay Strelkov <snk@altlinux.org> 22.9.0-alt1
- Initial build for Sisyphus

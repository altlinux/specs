%define _unpackaged_files_terminate_build 1

Name: ayatana-indicator-notifications
Version: 22.9.0
Release: alt1

Summary: Ayatana Indicator for viewing recent notifications
License: GPLv3
Group: Graphical desktop/Other
Url: https://github.com/AyatanaIndicators/ayatana-indicator-notifications

Packager: Nikolay Strelkov <snk@altlinux.org>

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake rpm-macros-systemd

BuildRequires: ayatana-cmake-modules cmake gcc-c++ intltool
BuildRequires: ayatana-indicator-common
BuildRequires: hicolor-icon-theme
BuildRequires: libblkid-devel
BuildRequires: libffi-devel
BuildRequires: libmount-devel
BuildRequires: libnotify-devel
BuildRequires: libpcre2-devel
BuildRequires: libpcre-devel
BuildRequires: libselinux-devel
BuildRequires: libsystemd-devel
BuildRequires: zlib-devel

%description
An Ayatana Indicator applet to display recent notifications sent
to a notification daemon such as notify-osd.

Using dconf-editor, you can blacklist certain notifications, so
that they are not shown anymore by the notifications indicator.

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
%dir %_iconsdir/hicolor/scalable
%dir %_iconsdir/hicolor/scalable/status
%_iconsdir/hicolor/scalable/status/*
%_datadir/glib-2.0/schemas/org.ayatana.indicator.notifications.gschema.xml
%dir %_datadir/ayatana
%dir %_datadir/ayatana/indicators
%_datadir/ayatana/indicators/org.ayatana.indicator.notifications
%_userunitdir/%name.service
%_datadir/locale/*/LC_MESSAGES/*.mo

%changelog
* Sun Nov 06 2022 Nikolay Strelkov <snk@altlinux.org> 22.9.0-alt1
- Initial build for Sisyphus

%define _unpackaged_files_terminate_build 1

Name: ayatana-indicator-display
Version: 22.9.3
Release: alt1

Summary: Ayatana Indicator for Display configuration
License: GPLv3
Group: Graphical desktop/Other
Url: https://github.com/AyatanaIndicators/ayatana-indicator-display

Packager: Nikolay Strelkov <snk@altlinux.org>

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake rpm-macros-systemd

BuildRequires: ayatana-cmake-modules cmake gcc-c++ intltool libayatana-common-devel properties-cpp-devel
BuildRequires: ayatana-indicator-common
BuildRequires: libblkid-devel
BuildRequires: libgudev-devel
BuildRequires: libmount-devel
BuildRequires: libpcre-devel
BuildRequires: libpcre2-devel
BuildRequires: libselinux-devel
BuildRequires: libsystemd-devel
BuildRequires: pkg-config
BuildRequires: zlib-devel

Requires: xsct

%description
This Ayatana Indicator is designed to be placed on the right side
of a panel and give the user easy control for changing their
display settings.

Ayatana Indicators are only available on desktop environments that 
provide a renderer for system indicators (such as MATE, Xfce, Lomiri, 
etc.).

%prep
%setup

%build
%cmake \
  -DCMAKE_INSTALL_LIBEXECDIR=%_libexecdir \
  -Denable_lomiri_features=OFF \
  -Denable_tests=OFF
%cmake_build

%install
%cmake_install

find %buildroot -type 'f' -name '*.la' -delete -print

%post
%systemd_user_post %name.service

%preun
%systemd_user_preun %name.service

%postun
%systemd_user_postun %name.service

%files
%doc COPYING AUTHORS INSTALL.md NEWS README README.md
%config %_sysconfdir/xdg/autostart/%name.desktop
%_libexecdir/%name/
%_datadir/glib-2.0/schemas/org.ayatana.indicator.display.gschema.xml
# This should probably be just org.ayatana.indicator.display,
# but is called rotation_lock for, likely, legacy reasons. Keep
# an eye on it.
%dir %_datadir/ayatana
%dir %_datadir/ayatana/indicators
%_datadir/ayatana/indicators/org.ayatana.indicator.rotation_lock
%dir %_iconsdir/hicolor/scalable
%dir %_iconsdir/hicolor/scalable/status
%_iconsdir/hicolor/scalable/status/*.svg
%_userunitdir/%name.service
%_datadir/locale/*/LC_MESSAGES/*.mo

%changelog
* Sun Jan 29 2023 Nikolay Strelkov <snk@altlinux.org> 22.9.3-alt1
- Initial build for Sisyphus

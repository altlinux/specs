%define _unpackaged_files_terminate_build 1

# psuffix is related to the GTK version. It's usually empty for GTK2.
%define psuffix 3
%define sover   7
Name: ayatana-indicator-application
Version: 22.2.0
Release: alt1

Summary: Ayatana Indicator that takes StatusNotifiers and puts them in the panel
License: GPLv3
Group: Graphical desktop/Other
Url: https://github.com/AyatanaIndicators/ayatana-indicator-application

Packager: Nikolay Strelkov <snk@altlinux.org>

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake rpm-macros-systemd

BuildRequires: cmake libayatana-appindicator3-devel libdbus-glib-devel libdbusmenu-gtk3-devel
BuildRequires: at-spi2-atk-devel
BuildRequires: ayatana-cmake-modules
BuildRequires: ayatana-indicator-common
BuildRequires: bzlib-devel
BuildRequires: intltool
BuildRequires: libat-spi2-core-devel
BuildRequires: libblkid-devel
BuildRequires: libbrotli-devel
BuildRequires: libdatrie-devel
BuildRequires: libepoxy-devel
BuildRequires: libexpat-devel
BuildRequires: libffi-devel
BuildRequires: libfribidi-devel
BuildRequires: libjpeg-devel
BuildRequires: libjson-glib-devel
BuildRequires: libmount-devel
BuildRequires: libpcre2-devel
BuildRequires: libpcre-devel
BuildRequires: libpixman-devel
BuildRequires: libselinux-devel
BuildRequires: libsystemd-devel
BuildRequires: libthai-devel
BuildRequires: libtiff-devel
BuildRequires: libuuid-devel
BuildRequires: libXcomposite-devel
BuildRequires: libXcursor-devel
BuildRequires: libXdamage-devel
BuildRequires: libXdmcp-devel
BuildRequires: libXi-devel
BuildRequires: libXinerama-devel
BuildRequires: libxkbcommon-devel
BuildRequires: libXrandr-devel
BuildRequires: libXtst-devel
BuildRequires: libwayland-cursor-devel
BuildRequires: libwayland-egl-devel

%description
This package provides a library and an ayatana indicator to take the 
application StatusNotifiers and display them on the panel bar.

%prep
%setup

%build
%cmake \
  -DCMAKE_INSTALL_LIBEXECDIR=%_libexecdir \
  -Denable_tests=Off
%cmake_build

%install
%cmake_install
find %buildroot -type f -name "*.la" -delete -print

%post
%systemd_user_post %name.service

%preun
%systemd_user_preun %name.service

%postun
%systemd_user_postun %name.service

%files
%doc COPYING AUTHORS INSTALL.md NEWS README.md
%config %_sysconfdir/xdg/autostart/%name.desktop
%_datadir/%name/
%_libexecdir/%name/
%dir %_libdir/ayatana-indicators%{?psuffix}
%dir %_libdir/ayatana-indicators%{?psuffix}/%sover
%_libdir/ayatana-indicators%{?psuffix}/%sover/libayatana-application.so
%_userunitdir/%name.service

%changelog
* Sun Nov 06 2022 Nikolay Strelkov <snk@altlinux.org> 22.2.0-alt1
- Initial build for Sisyphus

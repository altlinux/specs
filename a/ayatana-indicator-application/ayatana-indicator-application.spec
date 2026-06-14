%define _unpackaged_files_terminate_build 1
%define _libexecdir %_prefix/libexec

%def_with check

# psuffix is related to the GTK version. It's usually empty for GTK2.
%define psuffix 3
%define sover   7
Name: ayatana-indicator-application
Version: 26.6.0
Release: alt1

Summary: Ayatana Indicator that takes StatusNotifiers and puts them in the panel
License: GPLv3
Group: Graphical desktop/Other
Url: https://github.com/AyatanaIndicators/ayatana-indicator-application

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake
BuildRequires(pre): rpm-macros-systemd

BuildRequires: at-spi2-atk-devel
BuildRequires: ayatana-cmake-modules
BuildRequires: ayatana-indicator-common
BuildRequires: bzlib-devel
BuildRequires: cmake
BuildRequires: intltool
BuildRequires: libat-spi2-core-devel
BuildRequires: libayatana-appindicator3-devel
BuildRequires: libblkid-devel
BuildRequires: libbrotli-devel
BuildRequires: libdatrie-devel
BuildRequires: libdbus-glib-devel
BuildRequires: libdbusmenu-gtk3-devel
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
BuildRequires: libwayland-cursor-devel
BuildRequires: libwayland-egl-devel
BuildRequires: libXcomposite-devel
BuildRequires: libXcursor-devel
BuildRequires: libXdamage-devel
BuildRequires: libXdmcp-devel
BuildRequires: libXi-devel
BuildRequires: libXinerama-devel
BuildRequires: libxkbcommon-devel
BuildRequires: libXrandr-devel
BuildRequires: libXtst-devel
BuildRequires: libayatana-appindicator-glib-devel

%if_with check
BuildRequires: ctest
%endif

%description
This package provides a library and an ayatana indicator to take the
application StatusNotifiers and display them on the panel bar.

%prep
%setup

%build
%cmake \
%if_with check
       -DENABLE_TESTS=ON \
%else
       -DENABLE_TESTS=OFF \
%endif
       -DENABLE_COVERAGE=OFF
%cmake_build

%install
%cmake_install
find %buildroot -type f -name "*.la" -delete -print

%check
%ctest -j1 -VV

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
%dir %_libexecdir/%name/
%_libexecdir/%name/%{name}-service
%dir %_libdir/ayatana-indicators%{?psuffix}
%dir %_libdir/ayatana-indicators%{?psuffix}/%sover
%_libdir/ayatana-indicators%{?psuffix}/%sover/libayatana-application.so
%_userunitdir/%name.service

%changelog
* Sun Jun 14 2026 Nikolay Strelkov <snk@altlinux.org> 26.6.0-alt1
- New version 26.6.0.

* Sun Jan 28 2024 Nikolay Strelkov <snk@altlinux.org> 22.2.0-alt3
- Handle review issues:
  + removed obsolete Packager tag
  + break BuildRequires to multiple lines
  + break BuildRequires(pre) to multiple lines
  + do not own systemd dirs (thanks to @antohami)

* Wed Aug 09 2023 Nikolay Strelkov <snk@altlinux.org> 22.2.0-alt2
- Move service to /usr/libexec for compatibility with MATE Tweak and Debian

* Sun Nov 06 2022 Nikolay Strelkov <snk@altlinux.org> 22.2.0-alt1
- Initial build for Sisyphus

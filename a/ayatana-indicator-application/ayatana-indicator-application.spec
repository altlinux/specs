%define _unpackaged_files_terminate_build 1
%define _libexecdir %_prefix/libexec

%def_with check

# psuffix is related to the GTK version. It's usually empty for GTK2.
%define psuffix 3
%define sover   7
Name: ayatana-indicator-application
Version: 26.6.0
Release: alt2

Summary: Ayatana Indicator that takes StatusNotifiers and puts them in the panel
License: GPLv3
Group: Graphical desktop/Other
Url: https://github.com/AyatanaIndicators/ayatana-indicator-application

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake
BuildRequires(pre): rpm-macros-systemd

BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(ayatana-indicator3-0.4)
BuildRequires: pkgconfig(dbus-glib-1)
BuildRequires: pkgconfig(dbusmenu-gtk3-0.4)
BuildRequires: libayatana-appindicator-glib-devel
BuildRequires: pkgconfig(systemd)

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
* Sun Oct 18 2026 Nikolay Strelkov <snk@altlinux.org> 26.6.0-alt2
- Fixed FTBFS by updating build-requires.

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

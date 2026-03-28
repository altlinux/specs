%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

%def_with check

%define _libexecdir %_prefix/libexec

Name: lomiri-location-service
Version: 3.4.1
Release: alt1

Summary: Lomiri Location Service
License: GPL-3.0-only and LGPL-3.0-only
Group: Graphical desktop/Other
Url: https://gitlab.com/ubports/development/core/lomiri-location-service

Source: %name-%version.tar

# sync with version 3.3.0-2 from Debian unstable + local fixes
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-macros-cmake
BuildRequires(pre): rpm-macros-qt5
BuildRequires(pre): rpm-macros-systemd

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: pkgconfig(dbus-1)
BuildRequires: pkgconfig(dbus-cpp)
BuildRequires: pkgconfig(json-c)
BuildRequires: pkgconfig(libapparmor)
BuildRequires: pkgconfig(net-cpp)
BuildRequires: pkgconfig(process-cpp)
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5Location)
BuildRequires: ayatana-cmake-modules
BuildRequires: pkgconfig(libglog)
BuildRequires: pkgconfig(gflags)
BuildRequires: pkgconfig(gtest)
BuildRequires: pkgconfig(libgps)
BuildRequires: pkgconfig(systemd)
BuildRequires: boost-filesystem-devel
BuildRequires: boost-program_options-devel
BuildRequires: doxygen
BuildRequires: pkgconfig(libunwind)

Requires: lib%{name} = %{version}-%{release}

%if_with check
BuildRequires: ctest
BuildRequires: dbus
BuildRequires: /proc
BuildRequires: NetworkManager-daemon
BuildRequires: curl
%endif

%description
Aggregates position/velocity/heading updates and exports them over DBus.

This package contains the service executable and man pages.

%package doc
Summary: Lomiri Location Service documentation
Group: Documentation
BuildArch: noarch

%description doc
Aggregates position/velocity/heading updates and exports them over DBus.

This package contains documentation for the service and client.

%package -n lib%{name}
Summary: Lomiri Location Service client library
Group: System/Libraries

%description -n lib%{name}
Aggregates position/velocity/heading updates and exports them over DBus.

This package contains the shared library needed by client applications.

%package -n lib%{name}-devel
Summary: Lomiri Location Service (development files and tests)
Group: Development/C++
Requires: lib%{name} = %{version}-%{release}

%description -n lib%{name}-devel
Aggregates position/velocity/heading updates and exports them over DBus.

This package contains header files required to develop clients talking to
the Lomiri Location Service and test executables.

%prep
%setup
%patch -p1

%build
%cmake \
       -Wno-dev \
       -DENABLE_TRUST_STORE=OFF \
       -DLOCATION_SERVICE_ENABLE_GPS_PROVIDER=OFF \
       -DLOCATION_SERVICE_ENABLE_GEOCLUE_PROVIDER=ON
%cmake_build

%install
%cmake_install

%find_lang %name

%post
%systemd_post %name.service

%preun
%systemd_preun %name.service

%postun
%systemd_postun %name.service

%check
%ctest -j1 -VV -E '^(remote_providerd_test|delayed_service_test|daemon_and_cli_tests|ichnaea_reporter_test|acceptance_tests)'

%files -f %{name}.lang
%doc AUTHORS ChangeLog COPYING.GPL COPYING.LGPL
%_bindir/lomiri-location-service-providerd
%_bindir/lomiri-location-serviced
%_bindir/lomiri-location-serviced-cli
%_unitdir/lomiri-location-service.service
%exclude %_userunitdir/lomiri-location-service-trust-stored.service
%_datadir/dbus-1/system.d/com.lomiri.location.Service.conf

%exclude %_datadir/locale/it_CARES/LC_MESSAGES/lomiri-location-service.mo
%exclude %_datadir/locale/zh_LATN@pinyin/LC_MESSAGES/lomiri-location-service.mo

%files -n lib%{name}
%_libdir/liblomiri-location-service-connectivity.so.3
%_libdir/liblomiri-location-service-connectivity.so.3.0.0
%_libdir/liblomiri-location-service.so.3
%_libdir/liblomiri-location-service.so.3.0.0
%dir %_qt5_plugindir/position
%_qt5_plugindir/position/libqtposition_lomiri.so

%files -n lib%{name}-devel
%dir %_includedir/lomiri-location-service-3
%_includedir/lomiri-location-service-3/*
%_libdir/liblomiri-location-service-connectivity.so
%_libdir/liblomiri-location-service.so
%_pkgconfigdir/lomiri-location-service-connectivity.pc
%_pkgconfigdir/lomiri-location-service.pc
%dir %_libexecdir/lls-tests
%_libexecdir/lls-tests/*
%dir %_datadir/lomiri-location-service
%_datadir/lomiri-location-service/*
%exclude %_libexecdir/examples/client
%exclude %_libexecdir/examples/service

%files doc
%dir %_datadir/doc/lomiri-location-service
%_datadir/doc/lomiri-location-service/*

%changelog
* Sat Mar 28 2026 Nikolay Strelkov <snk@altlinux.org> 3.4.1-alt1
- New version 3.4.1.

* Thu Feb 05 2026 Nikolay Strelkov <snk@altlinux.org> 3.4.0-alt1
- New version 3.4.0.

* Sat Nov 15 2025 Nikolay Strelkov <snk@altlinux.org> 3.3.0-alt2
- Applied repocop fix for arch-dep-package-consists-of-usr-share

* Sun Jul 27 2025 Nikolay Strelkov <snk@altlinux.org> 3.3.0-alt1
- Initial build for Sisyphus

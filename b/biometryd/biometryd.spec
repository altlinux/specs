%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

# TODO do something related to C++17 support in gtest and this code
%def_without check

Name: biometryd
Version: 0.3.2
Release: alt1

Summary: Mediates and multiplexes access to biometric devices
License: GPL-3.0-only
Group: Graphical desktop/Other
Url: https://gitlab.com/ubports/development/core/biometryd

Packager: Nikolay Strelkov <snk@altlinux.org>

Source: %name-%version.tar

# sync with version 0.3.1-6 from Debian unstable + build issues fix
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-build-cmake
BuildRequires(pre): rpm-macros-qt5
BuildRequires(pre): rpm-build-qml

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: boost-devel
BuildRequires: boost-filesystem-devel
BuildRequires: boost-program_options-devel
BuildRequires: pkgconfig(dbus-cpp)
BuildRequires: pkgconfig(libapparmor)
BuildRequires: pkgconfig(process-cpp)
BuildRequires: pkgconfig(sqlite3)
BuildRequires: pkgconfig(systemd)
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5Qml)
BuildRequires: pkgconfig(libelf)
BuildRequires: pkgconfig(gmock)
BuildRequires: pkgconfig(nlohmann_json)

%if_with check
BuildRequires: ctest
%endif

%description
biometryd mediates and multiplexes access to biometric devices present
on the system, enabling applications and system components to leverage
them for identification and verification of users.

Daemon and helper binaries to be used by services. This package also
contains the qtdeclarative bindings for biometryd.

%package -n lib%{name}
Group: System/Libraries
Summary: biometryd mediates/multiplexes to biometric devices - runtime library

%description -n lib%{name}
biometryd mediates and multiplexes access to biometric devices present
on the system, enabling applications and system components to leverage
them for identification and verification of users.

This package includes the biometryd runtime libraries.

%package -n lib%{name}-devel
Group: Development/Other
Summary: biometryd mediates/multiplexes to biometric devices - development headers
Requires: lib%{name} = %{version}-%{release}

%description -n lib%{name}-devel
biometryd mediates and multiplexes access to biometric devices present
on the system, enabling applications and system components to leverage
them for identification and verification of users.

This package includes all the development headers and libraries for
biometryd.

%prep
%setup
%patch -p1

%build
%cmake \
       -Wno-dev \
       -DENABLE_WERROR=OFF \
       -DWITH_HYBRIS=OFF \
       -DCMAKE_INSTALL_SYSCONFDIR=%_sysconfdir \
       -Dqmlplugindump_exe=%_qt5_bindir/qmlplugindump \
       -DBUILD_TESTING=OFF
%cmake_build

%install
%cmake_install

%check
%ctest -j1 -VV

%files
%doc AUTHORS ChangeLog COPYING
%_bindir/biometryd
%_unitdir/biometryd.service
%dir %_qt5_qmldir/Biometryd
%_qt5_qmldir/Biometryd/libbiometryd-qml.so
%_qt5_qmldir/Biometryd/plugins.qmltypes
%_qt5_qmldir/Biometryd/qmldir
%_sysconfdir/dbus-1/system.d/com.ubports.biometryd.Service.conf
%_sysconfdir/init/biometryd.conf

%files -n lib%{name}
%_libdir/libbiometry.so.1*

%files -n lib%{name}-devel
%dir %_includedir/biometry
%_includedir/biometry/*
%_libdir/libbiometry.so
%_pkgconfigdir/biometryd.pc

%changelog
* Fri Sep 12 2025 Nikolay Strelkov <snk@altlinux.org> 0.3.2-alt1
- New version 0.3.2.

* Thu Jul 17 2025 Nikolay Strelkov <snk@altlinux.org> 0.3.1-alt1
- Initial build for Sisyphus

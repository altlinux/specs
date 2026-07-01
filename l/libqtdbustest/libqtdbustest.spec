%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

%def_with check

%define _libexecdir %_prefix/libexec

Name: libqtdbustest
Version: 0.4.1
Release: alt1

Summary: Library for testing DBus interactions using Qt
License: LGPL-3.0-only
Group: Development/C++
Url: https://gitlab.com/ubports/development/core/libqtdbustest

Source: %name-%version.tar

# sync with version 0.3.3-1 from Debian unstable
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-build-cmake

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(gtest)
BuildRequires: ayatana-cmake-modules

%if_with check
BuildRequires: ctest
BuildRequires: /proc
BuildRequires: python3(dbusmock)
%endif

%description
A simple library for testing Qt based DBus services and clients. This
library is relevant for running unit tests against DBus for Qt
applications.

This package contains the shared library.

%package devel
Group: Development/C++
Summary: Library for testing DBus interactions using Qt (development files)
Requires: %{name} = %{version}-%{release}

%description devel
A simple library for testing Qt based DBus services and clients. This
library is relevant for running unit tests against DBus for Qt
applications.

This package contains header files needed for development.

%package -n qtdbustest-runner
Group: Development/Tools
Summary: Library for testing DBus interactions using Qt (test runner executable)

%description -n qtdbustest-runner
The libqtdbustest library is a simple library for testing Qt based DBus
services and clients.

This package contains a simple executable for running a test script
under a private DBus environment.

%prep
%setup
%patch -p1

%if_without check
sed -i -e '/add_subdirectory(tests)/d' CMakeLists.txt
%endif

%build
%cmake \
       -DCMAKE_INSTALL_LIBEXECDIR=%_libexecdir
%cmake_build

%install
%cmake_install

%check
%ctest -j1 -VV

%files
%_libdir/libqtdbustest.so.1*
%dir %_datadir/libqtdbustest
%_datadir/libqtdbustest/session.conf
%_datadir/libqtdbustest/system.conf
%dir %_libexecdir/libqtdbustest
%_libexecdir/libqtdbustest/watchdog

%files devel
%dir %_includedir/libqtdbustest-1
%dir %_includedir/libqtdbustest-1/libqtdbustest
%_includedir/libqtdbustest-1/libqtdbustest/DBusService.h
%_includedir/libqtdbustest-1/libqtdbustest/DBusTestRunner.h
%_includedir/libqtdbustest-1/libqtdbustest/QProcessDBusService.h
%_includedir/libqtdbustest-1/libqtdbustest/SuicidalProcess.h
%_includedir/libqtdbustest-1/libqtdbustest/config.h
%_libdir/libqtdbustest.so
%_pkgconfigdir/libqtdbustest-1.pc

%files -n qtdbustest-runner
%doc AUTHORS ChangeLog COPYING COPYING.LGPL README.md
%_bindir/qdbus-simple-test-runner

%changelog
* Wed Jul 01 2026 Nikolay Strelkov <snk@altlinux.org> 0.4.1-alt1
- New version 0.4.1.

* Sat Sep 13 2025 Nikolay Strelkov <snk@altlinux.org> 0.4.0-alt1
- New version 0.4.0.

* Fri Jul 18 2025 Nikolay Strelkov <snk@altlinux.org> 0.3.3-alt1
- Initial build for Sisyphus

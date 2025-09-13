%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

%def_with check

%define _libexecdir %_prefix/libexec

Name: dbus-cpp
Version: 5.0.5
Release: alt1

Summary: A header-only dbus-binding leveraging C++-11
License: GPL-3.0-only
Group: Development/C++
Url: https://gitlab.com/ubports/development/core/lib-cpp/dbus-cpp

Source: %name-%version.tar

# sync with version 5.0.4-2 from Debian unstable + local fixes
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-build-cmake

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: boost-devel
BuildRequires: boost-filesystem-devel
BuildRequires: boost-program_options-devel
BuildRequires: pkgconfig(libxml-2.0)
BuildRequires: pkgconfig(dbus-1)
BuildRequires: pkgconfig(process-cpp)
BuildRequires: ayatana-cmake-modules
BuildRequires: libgtest-devel
BuildRequires: boost-asio-devel

%if_with check
BuildRequires: ctest
BuildRequires: dbus
BuildRequires: /proc
%endif

%description
Protocol compiler and generator to automatically generate protocol headers
from introspection XML.

D-Bus is a message bus used for sending messages between applications.

This package contains runtime binaries.

%package -n lib%{name}
Group: System/Libraries
Summary: header-only dbus-binding leveraging C++-11 (runtime libraries)

%description -n lib%{name}
A header-only dbus-binding leveraging C++-11, relying on compile-time
polymorphism to integrate with arbitrary type systems. Runtime portions to
bind to different event loops.

%package -n lib%{name}-devel
Group: System/Libraries
Summary: header-only dbus-binding leveraging C++-11 (development files)
Requires: lib%{name} = %{version}-%{release}

%description -n lib%{name}-devel
A header-only dbus-binding leveraging C++-11, relying on compile-time
polymorphism to integrate with arbitrary type systems.

D-Bus is a message bus used for sending messages between applications.

%prep
%setup
%patch -p1

%build
%cmake \
       -Wno-dev \
       -DBUILD_SHARED_LIBS=ON \
       -DCMAKE_INSTALL_LIBEXECDIR=/usr/libexec/dbus-cpp

%cmake_build

%install
%cmake_install

%check
%ctest -j1 -VV

%files
%doc AUTHORS ChangeLog COPYING.GPL COPYING.LGPL
%_bindir/dbus-cppc

%files -n lib%{name}

%_libdir/libdbus-cpp.so.5*
%_libdir/libdbus-cpp.so.5.0.4
%dir %_datadir/dbus-cpp

%files -n lib%{name}-devel
%dir %_includedir/core
%dir %_includedir/core/dbus
%_includedir/core/dbus/*
%_pkgconfigdir/dbus-cpp.pc
%_libdir/libdbus-cpp.so
%_datadir/dbus-cpp/session.conf
%_datadir/dbus-cpp/system.conf

%dir %_libexecdir/dbus-cpp
%dir %_libexecdir/dbus-cpp/examples
%dir %_libexecdir/dbus-cpp/examples/benchmark
%_libexecdir/dbus-cpp/examples/benchmark/benchmark
%dir %_libexecdir/dbus-cpp/examples/geoclue
%_libexecdir/dbus-cpp/examples/geoclue/geoclue
%dir %_libexecdir/dbus-cpp/examples/ofono
%_libexecdir/dbus-cpp/examples/ofono/ofono
%dir %_libexecdir/dbus-cpp/examples/upower
%_libexecdir/dbus-cpp/examples/upower/upower

%changelog
* Sat Sep 13 2025 Nikolay Strelkov <snk@altlinux.org> 5.0.5-alt1
- New version 5.0.5.

* Thu Jul 17 2025 Nikolay Strelkov <snk@altlinux.org> 5.0.4-alt1
- Initial build for Sisyphus

%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

%def_with check

Name: gmenuharness
Version: 0.1.6
Release: alt1

Summary: GMenu harness library
License: LGPL-3.0-only
Group: Graphical desktop/Other
Url: https://gitlab.com/ubports/development/core/gmenuharness

Source: %name-%version.tar

# sync with version 0.1.6 from Debian unstable
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-build-cmake

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(gio-2.0)
BuildRequires: pkgconfig(liblomiri-api)
BuildRequires: pkgconfig(gtest)
BuildRequires: ayatana-cmake-modules

%if_with check
BuildRequires: ctest
BuildRequires: dbus
BuildRequires: /usr/bin/dbus-test-runner
BuildRequires: /usr/bin/xvfb-run
BuildRequires: pkgconfig(libqtdbustest-1)
%endif

%description
Library containing GMenu harness. This library is useful for testing
GMenuModel structures.

%package -n lib%{name}
Summary: GMenu harness library (development files)
Group: System/Libraries

%description -n lib%{name}
Library containing GMenu harness. This library is useful for testing
GMenuModel structures.

This package contains the gmenuharness shared library.

%package -n lib%{name}-devel
Summary: GMenu harness library (development files)
Group: Development/C++
Requires: lib%{name} = %{version}-%{release}

%description -n lib%{name}-devel
Library containing GMenu harness. This library is useful for testing
GMenuModel structures.

This package contains the gmenuharness header files for development.

%prep
%setup
%patch -p1

%build
%cmake \
%if_with check
       -Denable_tests=ON
%else
       -Denable_tests=OFF
%endif
%cmake_build

%install
%cmake_install

%check
%ctest -j1 -VV

%files -n lib%{name}
%doc COPYING README TODO
%_libdir/libgmenuharness.so.0.1
%_libdir/libgmenuharness.so.0.1.4

%files -n lib%{name}-devel
%dir %_includedir/gmenuharness-0.1
%dir %_includedir/gmenuharness-0.1/lomiri
%dir %_includedir/gmenuharness-0.1/lomiri/gmenuharness
%_includedir/gmenuharness-0.1/lomiri/gmenuharness/MatchResult.h
%_includedir/gmenuharness-0.1/lomiri/gmenuharness/MatchUtils.h
%_includedir/gmenuharness-0.1/lomiri/gmenuharness/MenuItemMatcher.h
%_includedir/gmenuharness-0.1/lomiri/gmenuharness/MenuMatcher.h
%_libdir/libgmenuharness.so
%_pkgconfigdir/libgmenuharness.pc

%changelog
* Sat Jun 27 2026 Nikolay Strelkov <snk@altlinux.org> 0.1.6-alt1
- New version 0.1.6.

* Wed Apr 22 2026 Nikolay Strelkov <snk@altlinux.org> 0.1.5-alt1
- New version 0.1.5.

* Fri Jul 18 2025 Nikolay Strelkov <snk@altlinux.org> 0.1.4-alt1
- Initial build for Sisyphus

%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

%def_with check

%define _libexecdir %_prefix/libexec

Name: wlcs
Version: 1.8.1
Release: alt1

Summary: Wayland Conformance Test Suite
License: GPL-2.0-or-later OR GPL-3.0-or-later
Group: Development/Other
Url: https://github.com/canonical/wlcs

Source: %name-%version.tar

# sync with version 1.7.0-1 in Debian unstable
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-build-cmake

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: pkgconfig(gtest)
BuildRequires: pkgconfig(wayland-client)
BuildRequires: pkgconfig(wayland-server)
BuildRequires: boost-devel

%if_with check
BuildRequires: ctest
%endif

%description
wlcs aspires to be a protocol-conformance-verifying test suite usable by
Wayland compositor implementors.

It is growing out of porting the existing Weston test suite to be run in
Mir's test suite, but it is designed to be usable by any compositor.

wlcs relies on compositors providing an integration module, providing
wlcs with API hooks to start a compositor, connect a client, move a
window, and so on.

This makes both writing and debugging tests easier - the tests are
(generally) in the same address space as the compositor, so there is a
consistent global clock available, it's easier to poke around in
compositor internals, and standard debugging tools can follow control
flow from the test client to the compositor and back again.

%package devel
Summary: Development files for %name
Group: Development/Other
Requires: %name = %{version}-%{release}

%description devel
wlcs aspires to be a protocol-conformance-verifying test suite usable by
Wayland compositor implementors.

The wlcs-devel package contains libraries and header files for
developing Wayland compositor tests that use wlcs.

%prep
%setup
%patch -p1
sed -i '/-Werror/d' CMakeLists.txt

%build
%cmake \
%ifarch i586
       -DWLCS_BUILD_TSAN=OFF
%else
       -DWLCS_BUILD_TSAN=ON
%endif
%cmake_build

%install
%cmake_install

%check
%ctest -V

%files
%doc COPYING.GPL2 COPYING.GPL3 README.rst
%dir %_libexecdir/wlcs/
%_libexecdir/wlcs/wlcs
%_libexecdir/wlcs/wlcs.asan
%ifnarch i586
%_libexecdir/wlcs/wlcs.tsan
%endif
%_libexecdir/wlcs/wlcs.ubsan

%files devel
%doc README.rst
%doc example/
%dir %_includedir/wlcs/
%_includedir/wlcs/display_server.h
%_includedir/wlcs/pointer.h
%_includedir/wlcs/touch.h
%_libdir/pkgconfig/wlcs.pc

%changelog
* Mon Aug 18 2025 Nikolay Strelkov <snk@altlinux.org> 1.8.1-alt1
- New version 1.8.1.

* Mon Jul 14 2025 Nikolay Strelkov <snk@altlinux.org> 1.7.0-alt1
- Initial build for Sisyphus

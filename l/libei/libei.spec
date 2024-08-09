%def_disable snapshot

%define _libexecdir %_prefix/libexec
%define ver_major 1.3
%define api_ver 1.0

%def_disable documentation
%def_enable tests
%define munit_ver 0.2.0

%ifarch armh
# 7/7 libei:sigalrm / eierpecken              TIMEOUT        180.12s 
%def_disable check
%else
%def_enable check
%endif

Name: libei
Version: %ver_major.0
Release: alt1

Summary: A library for Emulated Input
Group: System/Libraries
License: MIT
Url: http://www.freedesktop.org/wiki/Software/libinput/

Vcs: https://gitlab.freedesktop.org/libinput/libei.git

%if_disabled snapshot
Source: https://gitlab.freedesktop.org/libinput/%name/-/archive/%version/%name-%version.tar.bz2
%else
Source: %name-%version.tar
%endif
# https://github.com/nemequ/munit.git
# v0.2.0-38-gfbbdf14
Source1: munit-%munit_ver.tar

%add_python3_path %_libexecdir/%name

%define evdev_ver 1.10

BuildRequires(pre): rpm-macros-meson rpm-build-python3
# for %%valgrind_arches
BuildRequires(pre): rpm-macros-valgrind
BuildRequires: meson gcc-c++ xmllint
BuildRequires: pkgconfig(libevdev) >= %evdev_ver
BuildRequires: pkgconfig(xkbcommon)
BuildRequires: pkgconfig(systemd)
BuildRequires: python3(attr) python3(jinja2)
#BuildRequires: pkgconfig(epoll-shim)
%{?_enable_documentation:BuildRequires: doxygen graphviz hugo}
%{?!_without_check:%{?!_disable_check:
BuildRequires: /proc python3(pytest) python3(xdist)
BuildRequires: python3(dbusmock) python3(structlog) python3(black)
BuildRequires: python3(yaml)
BuildRequires: ruff
%ifarch %valgrind_arches
BuildRequires: valgrind
%endif
}}

%description
libei is a library for Emulated Input, primarily aimed at the Wayland
stack. It provides three parts:

EI (Emulated Input) for the client side (libei).
EIS (Emulated Input Server) for the server side (libeis).
oeffis is an optional helper library for DBus communication with the XDG
RemoteDesktop portal (liboeffis)

The communication between EI and EIS happens over a UNIX socket via a
custom binary protocol. See the EI protocol documentation for details.

For the purpose of this document, libei refers to the project,
libei/libeis to the libraries provided.

%package devel
Summary: libei development package
Group: Development/C
Requires: %name = %EVR

%description devel
This package contains development libraries and header files
that are needed to write applications that use %name.

%package tools
Summary: tools for %name
Group: Development/Tools
Requires: %name = %EVR

%description tools
This package contains commandline tools from %name package.

%prep
%setup -a1
mv munit-%munit_ver subprojects/munit

sed -i 's|pytest-3|py.test-3|' test/meson.build

%build
%meson %{?_disable_documentation:-Ddocumentation=""} \
       %{?_disable_tests:-Dtests=false}
%nil
%meson_build

%install
%meson_install
rm -f %buildroot%_libdir/libmunit.so

%check
# python / protocol-test-valgrind failed in hasher
%__meson_test --no-suite=python -t 4

%files
%_libdir/%name.so.*
%_libdir/libeis.so.*
%_libdir/liboeffis.so.*
%doc COPYING README*

%files devel
%_includedir/%name-%api_ver
%_libdir/%name.so
%_libdir/libeis.so
%_libdir/liboeffis.so
%_pkgconfigdir/%name-%api_ver.pc
%_pkgconfigdir/libeis-%api_ver.pc
%_pkgconfigdir/liboeffis-%api_ver.pc

%files tools
%_bindir/ei-debug-events

%changelog
* Thu Aug 08 2024 Yuri N. Sedunov <aris@altlinux.org> 1.3.0-alt1
- 1.3.0

* Mon Feb 05 2024 Yuri N. Sedunov <aris@altlinux.org> 1.2.1-alt1
- 1.2.1

* Wed Dec 06 2023 Yuri N. Sedunov <aris@altlinux.org> 1.2.0-alt1
- 1.2.0

* Tue Sep 12 2023 Yuri N. Sedunov <aris@altlinux.org> 1.1.0-alt1
- 1.1.0

* Tue Aug 08 2023 Yuri N. Sedunov <aris@altlinux.org> 1.0.0-alt1
- first build for Sisyphus




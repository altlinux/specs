%define _name umockdev
%define api_ver 1.0
%def_disable check

Name: lib%_name
Version: 0.10
Release: alt1

Summary: Hardware devices mocking library for creating unit tests and bug reporting
Group: System/Libraries
License: LGPLv2.1
Url: https://launchpad.net/%_name

# VCS: https://github.com/martinpitt/umockdev.git
Source: %url/trunk/%version.0/+download/%_name-%version.tar.xz

%define glib_ver 2.32

BuildRequires: gtk-doc
BuildRequires: libgio-devel >= %glib_ver
BuildRequires: libudev-devel libgudev-devel
BuildRequires: gobject-introspection-devel
BuildRequires: vala-tools

%description
umockdev mocks Linux devices for creating integration tests for hardware
related libraries and programs. It also provides tools to record the properties
and behaviour of particular devices, and to run a program or test suite under
a test bed with the previously recorded devices loaded. This allows
developers of software like gphoto or libmtp to receive these records in bug
reports and recreate the problem on their system without having access to the
affected hardware.

%package devel
Summary: Development files for %name
Group: Development/C
Requires: /proc
Requires: %name = %version-%release

%description devel
This package contains libraries, header files and documentation for
developing applications that use %name.

%package devel-doc
Summary: Development documentation for %_name
Group: Development/Documentation
Conflicts: %name < %version-%release
BuildArch: noarch

%description devel-doc
This package contains development documentation for %_name.

%package gir
Summary: GObject introspection data for the %name
Group: System/Libraries
Requires: %name = %version-%release

%description gir
GObject introspection data for the %_name library.

%package gir-devel
Summary: GObject introspection devel data for the %name
Group: Development/Other
BuildArch: noarch
Requires: %name-gir = %version-%release
Requires: %name-devel = %version-%release

%description gir-devel
GObject introspection devel data for the %_name library.

%define pkg_docdir %_defaultdocdir/%name-%version

%prep
%setup -n %_name-%version

%build
%autoreconf
%configure \
    --disable-static \
    --enable-gtk-doc \
    --enable-introspection \
    --docdir=%pkg_docdir
%make_build

%install
%makeinstall_std
install -pD -m644 NEWS %buildroot%pkg_docdir

%check
%make check

%files
%_bindir/%_name-record
%_bindir/%_name-run
%_bindir/%_name-wrapper
%_libdir/%name.so.*
%_libdir/%name-preload.so.*
%doc %pkg_docdir

%files devel
%_includedir/%_name-%api_ver/
%_libdir/%name.so
%_pkgconfigdir/%_name-%api_ver.pc
%_vapidir/%_name-%api_ver.vapi

%files devel-doc
%_datadir/gtk-doc/html/%_name/

%files gir
%_typelibdir/UMockdev-%api_ver.typelib

%files gir-devel
%_girdir/UMockdev-%api_ver.gir

%changelog
* Fri Jan 19 2018 Yuri N. Sedunov <aris@altlinux.org> 0.10-alt1
- 0.10

* Sun Sep 24 2017 Yuri N. Sedunov <aris@altlinux.org> 0.9.3-alt1
- 0.9.3

* Mon Feb 13 2017 Yuri N. Sedunov <aris@altlinux.org> 0.8.13-alt1
- first build for Sisyphus




%def_disable snapshot
%define _name umockdev
%define api_ver 1.0

%def_enable gtk_doc
# /sys/devices/ required
%def_disable check

Name: lib%_name
Version: 0.17.15
Release: alt1

Summary: Hardware devices mocking library for creating unit tests and bug reporting
Group: System/Libraries
License: LGPL-2.1-or-later
Url: https://launchpad.net/%_name

%if_disabled snapshot
Source: https://github.com/martinpitt/%_name/releases/download/%version/%_name-%version.tar.xz
%else
Vcs: https://github.com/martinpitt/umockdev.git
Source: %_name-%version.tar
%endif

%define glib_ver 2.32

BuildRequires(pre): rpm-macros-meson rpm-build-gir rpm-build-vala
BuildRequires: meson vala-tools
BuildRequires: libgio-devel >= %glib_ver
BuildRequires: libudev-devel libgudev-devel
BuildRequires: libpcap-devel
BuildRequires: gobject-introspection-devel

%{?_enable_gtk_doc:BuildRequires: gtk-doc}
%{?_enable_check:
BuildRequires: /proc /dev/pts udev valgrind
BuildRequires: python3-module-pygobject3 libgudev-gir-devel
BuildRequires: xorg-server xorg-drv-dummy gphoto2 evtest xinput}

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
%meson \
%{?_enable_gtk_doc:-Dgtk_doc=true}
%nil
%meson_build

%install
%meson_install
install -pD -m644 NEWS %buildroot%pkg_docdir

%check
export PATH=/sbin:$PATH
%__meson_test

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
%_libdir/%name-preload.so
%_pkgconfigdir/%_name-%api_ver.pc
%_vapidir/%_name-%api_ver.vapi

%if_enabled gtk_doc
%files devel-doc
%_datadir/gtk-doc/html/%_name/
%endif

%files gir
%_typelibdir/UMockdev-%api_ver.typelib

%files gir-devel
%_girdir/UMockdev-%api_ver.gir

%changelog
* Thu Nov 24 2022 Yuri N. Sedunov <aris@altlinux.org> 0.17.15-alt1
- 0.17.15

* Mon May 30 2022 Yuri N. Sedunov <aris@altlinux.org> 0.17.13-alt1
- 0.17.13

* Thu May 19 2022 Yuri N. Sedunov <aris@altlinux.org> 0.17.12-alt1
- 0.17.12

* Wed May 11 2022 Yuri N. Sedunov <aris@altlinux.org> 0.17.10-alt1
- 0.17.10

* Thu Mar 24 2022 Yuri N. Sedunov <aris@altlinux.org> 0.17.8-alt1
- 0.17.8

* Thu Mar 03 2022 Yuri N. Sedunov <aris@altlinux.org> 0.17.7-alt1
- 0.17.7

* Fri Jan 21 2022 Yuri N. Sedunov <aris@altlinux.org> 0.17.6-alt1
- 0.17.6

* Tue Jan 18 2022 Yuri N. Sedunov <aris@altlinux.org> 0.17.5-alt1
- 0.17.5

* Wed Jan 12 2022 Yuri N. Sedunov <aris@altlinux.org> 0.17.3-alt1
- 0.17.3

* Mon Jan 10 2022 Yuri N. Sedunov <aris@altlinux.org> 0.17.2-alt1
- 0.17.2

* Sat Dec 25 2021 Yuri N. Sedunov <aris@altlinux.org> 0.17.1-alt1
- 0.17.1

* Thu Sep 16 2021 Yuri N. Sedunov <aris@altlinux.org> 0.16.3-alt1
- 0.16.3

* Wed Aug 25 2021 Yuri N. Sedunov <aris@altlinux.org> 0.16.2-alt1
- 0.16.2

* Sun Jul 04 2021 Yuri N. Sedunov <aris@altlinux.org> 0.16.1-alt1
- 0.16.1

* Thu Jul 01 2021 Yuri N. Sedunov <aris@altlinux.org> 0.16.0-alt1
- 0.16.0

* Mon May 03 2021 Yuri N. Sedunov <aris@altlinux.org> 0.15.5-alt1
- 0.15.5

* Sat Apr 24 2021 Yuri N. Sedunov <aris@altlinux.org> 0.15.4-alt2
- updated to 0.15.4-14-gbc2bf0b

* Mon Jan 04 2021 Yuri N. Sedunov <aris@altlinux.org> 0.15.4-alt1
- 0.15.4

* Fri Jan 01 2021 Yuri N. Sedunov <aris@altlinux.org> 0.15.3-alt1
- 0.15.3

* Thu Nov 26 2020 Yuri N. Sedunov <aris@altlinux.org> 0.15.2-alt1
- 0.15.2

* Tue Nov 17 2020 Yuri N. Sedunov <aris@altlinux.org> 0.15.1-alt1
- 0.15.1 (ported to Meson build system)

* Wed Oct 28 2020 Yuri N. Sedunov <aris@altlinux.org> 0.14.4-alt1
- 0.14.4

* Mon Aug 24 2020 Yuri N. Sedunov <aris@altlinux.org> 0.14.3-alt1
- 0.14.3

* Thu Jul 30 2020 Yuri N. Sedunov <aris@altlinux.org> 0.14.2-alt1
- 0.14.2

* Wed Feb 12 2020 Yuri N. Sedunov <aris@altlinux.org> 0.14.1-alt1
- 0.14.1

* Tue Feb 11 2020 Yuri N. Sedunov <aris@altlinux.org> 0.14-alt1
- 0.14
- fixed License tag

* Wed Aug 28 2019 Yuri N. Sedunov <aris@altlinux.org> 0.13.2-alt1
- 0.13.2

* Mon Jul 22 2019 Yuri N. Sedunov <aris@altlinux.org> 0.13.1-alt1
- 0.13.1

* Thu Nov 22 2018 Yuri N. Sedunov <aris@altlinux.org> 0.12.1-alt1
- 0.12.1

* Tue Aug 28 2018 Yuri N. Sedunov <aris@altlinux.org> 0.12-alt1
- 0.12

* Fri May 11 2018 Yuri N. Sedunov <aris@altlinux.org> 0.11.3-alt1
- 0.11.3

* Wed Apr 04 2018 Yuri N. Sedunov <aris@altlinux.org> 0.11.2-alt1
- 0.11.2

* Thu Mar 01 2018 Yuri N. Sedunov <aris@altlinux.org> 0.11.1-alt1
- 0.11.1

* Tue Feb 27 2018 Yuri N. Sedunov <aris@altlinux.org> 0.11-alt1
- 0.11

* Fri Jan 19 2018 Yuri N. Sedunov <aris@altlinux.org> 0.10-alt1
- 0.10

* Sun Sep 24 2017 Yuri N. Sedunov <aris@altlinux.org> 0.9.3-alt1
- 0.9.3

* Mon Feb 13 2017 Yuri N. Sedunov <aris@altlinux.org> 0.8.13-alt1
- first build for Sisyphus




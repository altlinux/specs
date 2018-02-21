%define libname mesonbuild
%def_without tests

Name: meson
Version: 0.44.1
Release: alt1

Summary: High productivity build system
Group: Development/Python3
License: ASL 2.0
Url: http://mesonbuild.com/

Source: https://github.com/mesonbuild/meson/archive/%version/%name-%version.tar.gz
Source1: %name.macros
Source2: %name.env

BuildArch: noarch

Requires: ninja-build

BuildRequires: rpm-build-python3 python3-devel python3-module-setuptools
BuildRequires: ninja-build
%if_with tests
BuildRequires: gcc gcc-c++ gcc-fortran gcc-objc gcc-objc++
BuildRequires: java-devel /proc
BuildRequires: mono4-core mono4-devel
BuildRequires: boost-devel
BuildRequires: libgtest-devel
BuildRequires: libgmock-devel
BuildRequires: qt5-base-devel
BuildRequires: vala
BuildRequires: libwxGTK3.0-devel
BuildRequires: flex bison
BuildRequires: gnustep-base-devel
BuildRequires: git
BuildRequires: pkgconfig(protobuf) protobuf-c-compiler
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(gobject-introspection-1.0) python3-module-pygobject3 gtk-doc
BuildRequires: pkgconfig(zlib)
BuildRequires: python3-module-Cython
%endif

%description
Meson is a build system designed to optimize programmer productivity.
It aims to do this by providing simple, out-of-the-box support for modern
software development tools and practices, such as unit tests, coverage
reports, Valgrind, CCache and the like.

%prep
%setup

%build
%python3_build

%install
%python3_install
install -Dpm 0644 %SOURCE1 %buildroot%_rpmmacrosdir/%name
install -Dpm 0755 %SOURCE2 %buildroot%_rpmmacrosdir/%name.env

%check
%{?_with_tests:MESON_PRINT_TEST_OUTPUT=1 ./run_tests.py}

%files
%_bindir/%name
%_bindir/%{name}conf
%_bindir/%{name}introspect
%_bindir/%{name}test
%_bindir/wraptool
%python3_sitelibdir/%libname/
%python3_sitelibdir/%name-%version-*.egg-info/
%_man1dir/%name.1.*
%_man1dir/%{name}conf.1.*
%_man1dir/%{name}introspect.1.*
%_man1dir/%{name}test.1.*
%_man1dir/wraptool.1.*
%_rpmmacrosdir/%name
%_rpmmacrosdir/%name.env
%doc COPYING README.*


%changelog
* Wed Feb 21 2018 Yuri N. Sedunov <aris@altlinux.org> 0.44.1-alt1
- 0.44.1
- set locale to en_US.utf8 in meson.env

* Wed Dec 20 2017 Yuri N. Sedunov <aris@altlinux.org> 0.44.0-alt1
- 0.44.0

* Mon Oct 09 2017 Yuri N. Sedunov <aris@altlinux.org> 0.43.0-alt1
- 0.43.0

* Sat Oct 07 2017 Yuri N. Sedunov <aris@altlinux.org> 0.42.1-alt2
- meson.macros: localstatedir=%%_var

* Tue Sep 12 2017 Yuri N. Sedunov <aris@altlinux.org> 0.42.1-alt1
- 0.42.1

* Tue Aug 15 2017 Yuri N. Sedunov <aris@altlinux.org> 0.42.0-alt1
- 0.42.0

* Wed Jul 19 2017 Yuri N. Sedunov <aris@altlinux.org> 0.41.2-alt1
- 0.41.2
- meson.macros: set locale to en_US.utf8 to avoid warnings

* Tue Jun 20 2017 Yuri N. Sedunov <aris@altlinux.org> 0.41.1-alt1
- 0.41.1

* Wed Jun 14 2017 Yuri N. Sedunov <aris@altlinux.org> 0.41.0-alt1
- 0.41.0

* Tue May 02 2017 Yuri N. Sedunov <aris@altlinux.org> 0.40.1-alt1
- 0.40.1

* Mon Apr 24 2017 Yuri N. Sedunov <aris@altlinux.org> 0.40.0-alt1
- 0.40.0

* Sun Mar 19 2017 Yuri N. Sedunov <aris@altlinux.org> 0.39.1-alt1
- 0.39.1

* Wed Mar 08 2017 Yuri N. Sedunov <aris@altlinux.org> 0.39.0-alt1
- 0.39.0

* Wed Feb 08 2017 Yuri N. Sedunov <aris@altlinux.org> 0.38.1-alt1
- 0.38.1

* Wed Feb 01 2017 Yuri N. Sedunov <aris@altlinux.org> 0.38.0-alt1
- 0.38.0

* Wed Dec 21 2016 Yuri N. Sedunov <aris@altlinux.org> 0.37.1-alt1
- 0.37.1

* Wed Nov 16 2016 Yuri N. Sedunov <aris@altlinux.org> 0.36.0-alt1
- 0.36.0

* Tue Oct 18 2016 Yuri N. Sedunov <aris@altlinux.org> 0.35.1-alt1
- 0.35.1

* Sun Sep 11 2016 Yuri N. Sedunov <aris@altlinux.org> 0.34.0-alt1
- 0.34.0

* Mon Aug 08 2016 Yuri N. Sedunov <aris@altlinux.org> 0.33.0-alt1
- 0.33.0

* Thu Jun 30 2016 Yuri N. Sedunov <aris@altlinux.org> 0.32.0-alt1
- first build for Sisyphus
  (based on fc 0.31.0-1 package http://pkgs.fedoraproject.org/cgit/rpms/meson.git/)


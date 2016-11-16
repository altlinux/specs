%define libname mesonbuild
%def_without tests

Name: meson
Version: 0.36.0
Release: alt1

Summary: High productivity build system
Group: Development/Python3
License: ASL 2.0
Url: http://mesonbuild.com/

Source: https://github.com/mesonbuild/meson/archive/%version/%name-%version.tar.gz
Source1: %name.macros

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

%check
%{?_with_tests:MESON_PRINT_TEST_OUTPUT=1 ./run_tests.py}

%files
%_bindir/%name
%_bindir/%{name}conf
%_bindir/%{name}introspect
%_bindir/wraptool
%python3_sitelibdir/%libname/
%python3_sitelibdir/%name-%version-*.egg-info/
%_man1dir/%name.1.*
%_man1dir/%{name}conf.1.*
%_man1dir/%{name}introspect.1.*
%_man1dir/wraptool.1.*
%_rpmmacrosdir/%name
%doc COPYING README.*


%changelog
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


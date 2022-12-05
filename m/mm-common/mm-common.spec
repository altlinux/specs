%define ver_major 1.0

Name: mm-common
Version: %ver_major.5
Release: alt1

Summary: Common build files of the C++ bindings
Group: Development/Tools
License: GPL-2.0
Url: http://gtkmm.org

Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version.tar.xz

BuildArch: noarch

BuildRequires(pre): rpm-macros-meson >= 0.55 rpm-build-python3
BuildRequires: meson
%add_python3_path %_datadir/%name/build

%description
The mm-common module provides the build infrastructure and utilities
shared among the GNOME C++ binding libraries. It is only a required
dependency for building the C++ bindings from the gnome.org version
control repository. An installation of mm-common is not required for
building tarball releases, unless configured to use maintainer-mode.

%package docs
Summary: Documentation for %name, includes example mm module skeleton
Group: Development/C++
Requires: %name = %version-%release

%description docs
Package contains short documentation for %name and example skeleton module,
which could be used as a base for new mm module.

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install

%check
%__meson_test

%files
%_bindir/*
%_datadir/%name/
%_datadir/aclocal/*.m4
%_datadir/pkgconfig/%name-libstdc++.pc
%_datadir/pkgconfig/%name-util.pc
%_man1dir/*
%doc ChangeLog NEWS AUTHORS

%files docs
%dir %_docdir/%name
%_docdir/%name/*

%changelog
* Fri Dec 02 2022 Yuri N. Sedunov <aris@altlinux.org> 1.0.5-alt1
- 1.0.5

* Thu Mar 03 2022 Yuri N. Sedunov <aris@altlinux.org> 1.0.4-alt1
- 1.0.4

* Thu May 20 2021 Yuri N. Sedunov <aris@altlinux.org> 1.0.3-alt1
- 1.0.3

* Fri Sep 25 2020 Yuri N. Sedunov <aris@altlinux.org> 1.0.2-alt1
- 1.0.2

* Thu Jun 04 2020 Yuri N. Sedunov <aris@altlinux.org> 1.0.1-alt1
- 1.0.1

* Tue Oct 29 2019 Yuri N. Sedunov <aris@altlinux.org> 1.0.0-alt1
- 1.0.0

* Sat Apr 07 2018 Yuri N. Sedunov <aris@altlinux.org> 0.9.12-alt1
- 0.9.12

* Fri Aug 25 2017 Yuri N. Sedunov <aris@altlinux.org> 0.9.11-alt1
- 0.9.11

* Sun Feb 07 2016 Yuri N. Sedunov <aris@altlinux.org> 0.9.10-alt1
- 0.9.10

* Fri Nov 27 2015 Yuri N. Sedunov <aris@altlinux.org> 0.9.9-alt1
- 0.9.9

* Wed Jul 15 2015 Yuri N. Sedunov <aris@altlinux.org> 0.9.8-alt1
- 0.9.8

* Mon Sep 15 2014 Yuri N. Sedunov <aris@altlinux.org> 0.9.7-alt1
- 0.9.7

* Sun Oct 07 2012 Yuri N. Sedunov <aris@altlinux.org> 0.9.6-alt1
- 0.9.6

* Wed Mar 30 2011 Yuri N. Sedunov <aris@altlinux.org> 0.9.5-alt1
- 0.9.5

* Tue Mar 15 2011 Yuri N. Sedunov <aris@altlinux.org> 0.9.3-alt1
- 0.9.3

* Fri Feb 05 2010 Yuri N. Sedunov <aris@altlinux.org> 0.9.2-alt1
- 0.9.2

* Sun Jan 03 2010 Yuri N. Sedunov <aris@altlinux.org> 0.9.1-alt1
- new version

* Sun Dec 27 2009 Yuri N. Sedunov <aris@altlinux.org> 0.9-alt1
- first build for Sisyphus



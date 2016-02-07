%define ver_major 0.9

Name: mm-common
Version: %ver_major.10
Release: alt1

Summary: Common build files of the C++ bindings
Group: Development/Tools
BuildArch: noarch
License: GPLv2+ and GFDL
Url: http://gtkmm.org
Source: http://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version.tar.xz

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
%configure
%make_build

%install
%makeinstall_std

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



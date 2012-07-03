%define ver_major 0.9

Name: mm-common
Version: %ver_major.5
Release: alt1

Summary: Common build files of the C++ bindings
Group: Development/Tools
BuildArch: noarch
License: GPLv2+ and GFDL
Url: http://gtkmm.org
Source: http://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version.tar.bz2

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
%setup -q

%build
%configure
%make_build

%install
%make DESTDIR=%buildroot install

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



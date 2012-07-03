%define _name gtksourceviewmm
%define ver_major 2.10
%define api_ver 2.0

Name: lib%_name
Version: %ver_major.3
Release: alt1

Summary: gtksourceviewmm is a C++ wrapper for the gtksourceview widget library
License: LGPL
Group: System/Libraries
Url: http://projects.gnome.org/gtksourceviewmm/
Packager: GNOME Maintainers Team <gnome@packages.altlinux.org>

Source: ftp://ftp.gnome.org/pub/gnome/sources/%_name/%ver_major/%_name-%version.tar.xz

# From configure.in
BuildPreReq: mm-common intltool
BuildPreReq: libgtkmm2-devel
BuildPreReq: libgtk+2-devel
BuildPreReq: libgtksourceview-devel >= 2.9.7
BuildPreReq: doxygen
BuildPreReq: gcc-c++

%description
gtksourceviewmm is a C++ wrapper for the gtksourceview widget library.
It offers all the power of gtksourceview with an interface familiar
to C++ developers, including users of the gtkmm library.

%package devel
Summary: Files to compile applications that use GtkSourceViewmm
Group: Development/GNOME and GTK+
Requires: %name = %version-%release

%description devel
This package contains the files required to develop applications against
the GtkSourceViewmm library.

%package devel-doc
Summary: Development documentation for %_name
Group: Development/GNOME and GTK+
BuildArch: noarch
Conflicts: %name-devel < %version

%description devel-doc
Documentation for %_name.

%define pkgdocdir %_docdir/%_name-%api_ver/

%prep
%setup -q -n %_name-%version

%build
mm-common-prepare
%autoreconf
%configure

%make_build

%check
%make check

%install
%makeinstall

%find_lang %_name-%api_ver

%files -f %_name-%api_ver.lang
%dir %_libdir/%_name-%api_ver/
%_libdir/*.so.*
%doc AUTHORS NEWS README

%files devel
%_includedir/*
%_libdir/*.so
%_libdir/%_name-%api_ver/include/
%_pkgconfigdir/*

%files devel-doc
%_datadir/devhelp/books/%_name-%api_ver/
%pkgdocdir

%changelog
* Wed May 16 2012 Yuri N. Sedunov <aris@altlinux.org> 2.10.3-alt1
- 2.10.3

* Thu Apr 21 2011 Yuri N. Sedunov <aris@altlinux.org> 2.10.1-alt1
- 2.10.1
- build using new mm-common

* Thu Jun 17 2010 Yuri N. Sedunov <aris@altlinux.org> 2.10.0-alt1
- 2.10.0

* Mon May 25 2009 Lebedev Sergey <barabashka@altlinux.org> 2.3.1-alt1
- new version from upstream

* Sat Dec 06 2008 Lebedev Sergey <barabashka@altlinux.org> 2.0-alt1
- initial build

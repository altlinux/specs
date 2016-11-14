%define _name gtksourceviewmm
%define ver_major 3.21
%define api_ver 3.0

Name: lib%{_name}3
Version: %ver_major.3
Release: alt1

Summary: gtksourceviewmm is a C++ wrapper for the gtksourceview widget library
License: LGPL
Group: System/Libraries
Url: http://projects.gnome.org/gtksourceviewmm/

Source: ftp://ftp.gnome.org/pub/gnome/sources/%_name/%ver_major/%_name-%version.tar.xz

# From configure.ac
BuildPreReq: mm-common intltool
BuildPreReq: libgtksourceview3-devel >= 3.18.0 libgtkmm3-devel >= 3.18.0
BuildPreReq: gcc-c++ libstdc++-devel
BuildPreReq: doxygen graphviz xsltproc

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
%setup -n %_name-%version

%build
#NOCONFIGURE=1 ./autogen.sh
#mm-common-prepare --copy --force
#%autoreconf
%configure --disable-static
#--enable-maintainer-mode

%make

%check
%make check

%install
%makeinstall_std

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
* Mon Nov 14 2016 Yuri N. Sedunov <aris@altlinux.org> 3.21.3-alt1
- 3.21.3

* Mon Sep 26 2016 Yuri N. Sedunov <aris@altlinux.org> 3.21.2-alt1
- 3.21.2

* Tue Sep 22 2015 Yuri N. Sedunov <aris@altlinux.org> 3.18.0-alt1
- 3.18.0

* Fri Jun 12 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 3.12.0-alt1.1
- Rebuilt for gcc5 C++11 ABI.

* Wed Apr 29 2015 Yuri N. Sedunov <aris@altlinux.org> 3.12.0-alt1
- 3.12.0

* Mon Mar 25 2013 Yuri N. Sedunov <aris@altlinux.org> 3.2.0-alt3
- rebuilt against libgtksourceview-3.0.so.1

* Thu Apr 19 2012 Yuri N. Sedunov <aris@altlinux.org> 3.2.0-alt2
- updated from upstream git (aa0dcab289)

* Mon Nov 21 2011 Yuri N. Sedunov <aris@altlinux.org> 3.2.0-alt1
- 3.2.0

* Mon Apr 11 2011 Yuri N. Sedunov <aris@altlinux.org> 3.0.0-alt1
- 3.0.0

* Thu Feb 10 2011 Yuri N. Sedunov <aris@altlinux.org> 2.91.5-alt1
- 2.91.5

* Wed Dec 22 2010 Yuri N. Sedunov <aris@altlinux.org> 2.91.2-alt1
- first build for Sisyphus


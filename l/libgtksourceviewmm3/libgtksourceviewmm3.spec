%define _name gtksourceviewmm
%define ver_major 3.2
%define api_ver 3.0

Name: lib%{_name}3
Version: %ver_major.0
Release: alt2

Summary: gtksourceviewmm is a C++ wrapper for the gtksourceview widget library
License: LGPL
Group: System/Libraries
Url: http://projects.gnome.org/gtksourceviewmm/
Packager: GNOME Maintainers Team <gnome@packages.altlinux.org>

Source: ftp://ftp.gnome.org/pub/gnome/sources/%_name/%ver_major/%_name-%version.tar

# From configure.in
BuildPreReq: mm-common intltool
BuildPreReq: libgtksourceview3-devel >= 3.2.0 libgtkmm3-devel >= 3.2.0
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
%setup -q -n %_name-%version

%build
#NOCONFIGURE=1 ./autogen.sh
mm-common-prepare --copy --force
%autoreconf
%configure --enable-maintainer-mode

%make

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


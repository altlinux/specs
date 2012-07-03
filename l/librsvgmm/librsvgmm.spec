%define major 2.26
%define api_version 2.0

Name: librsvgmm
Version: %major.1
Release: alt1

Summary: C++ bindings for SVG viewing library
License: LGPL
Group: System/Libraries
Url: http://library.gnome.org/devel/librsvgmm/stable/

Packager: Pavel Vainerman <pv@altlinux.ru>

#Source: ftp://ftp.gnome.org/pub/gnome/sources/librsvgmm/%major/%name-%version.tar.bz2
Source: ftp://ftp.gnome.org/pub/gnome/sources/librsvgmm/%major/%name-%version.tar

# Automatically added by buildreq on Sat Feb 05 2011
BuildRequires: doxygen fonts-ttf-freefont gcc-c++ glibc-devel-static graphviz libcairomm-devel libglibmm-devel libglibmm-doc librsvg-devel mm-common perl-XML-Parser xsltproc

%description
The librsvgmm C++ binding provides a C++ interface on top of the librsvg C library.

%package devel
Summary: Development files for librsvgmm C++ bindings
Group: Development/GNOME and GTK+
Requires: %name = %version-%release

%description devel
This package contains all necessary files, including libraries and headers,
that C++ programmers will need to develop applications which use
%name.

%package doc
Summary: Documentation for librsvgmm library
Group: Development/C++
BuildArch: noarch
Conflicts: %name < %version

%description doc
This package provides API documentation for librsvgmm library.

%prep
%setup -q
NOCONFIGURE=1 ./autogen.sh

%build
%configure 	--disable-maintainer-mode \
		--disable-static \
		--enable-shared

cd codegen && %make
cd -
cd librsvg/src/ && %make
cd -

%make_build
cd docs/reference && %make

%install
%makeinstall_std

%files
%doc AUTHORS NEWS
%_libdir/lib*.so.*

%files devel
%_includedir/*
%_libdir/lib*.so
%_pkgconfigdir/*.pc
%_libdir/%name-%api_version
%doc ChangeLog

%files doc
#%doc %name-%api_version/reference/html
%_docdir/%name-%api_version/reference/html
%_docdir/%name-%api_version/reference/*.tag
%_datadir/devhelp/books/%name-%api_version

%changelog
* Sat Feb 05 2011 Pavel Vainerman <pv@altlinux.ru> 2.26.1-alt1
- first build


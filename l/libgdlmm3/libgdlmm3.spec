%define _name gdlmm
%define ver_major 3.3
%define api_ver 3.0

Name: lib%{_name}3
Version: %ver_major.2
Release: alt1

Summary: C++ bindings for the gdl library
Group: System/Libraries
License: LGPLv2+
Url: http://www.gtkmm.org/

Source: ftp://ftp.gnome.org/pub/gnome/sources/%_name/%ver_major/%_name-%version.tar.xz
Patch: gdlmm-3.3.2-up-gdl.patch

BuildRequires: gcc-c++ mm-common libglibmm-devel libgtkmm3-devel libgdl3-devel >= 3.4.0
BuildRequires: perl-XML-Parser xsltproc doxygen graphviz

%description
This package contains C++ bindings for the GNOME Development/Docking
(gdl) library.

%package devel
Summary: Development files for %name
Group: Development/C++
Requires: %name = %version-%release

%description devel
The %name-devel package contains libraries and header files for
developing applications that use %_name.

%package devel-doc
Summary: API documentation for %_name
Group: Development/C++
BuildArch: noarch
Conflicts: %name-devel < %version

%description devel-doc
This package contains the API documentation for %_name.

%prep
%setup -n %_name-%version
%patch -p1

%build
%autoreconf
%configure --enable-maintainer-mode
%make_build

%install
make DESTDIR=%buildroot install

%check
make check

%files
%_libdir/*.so.*
%doc AUTHORS NEWS README

%files devel
%_includedir/%_name-%api_ver/
%_libdir/*.so
%_libdir/%_name-%api_ver/
%_libdir/pkgconfig/*.pc

%files devel-doc
%_docdir/%_name-%api_ver/
%_datadir/devhelp/*

%changelog
* Mon May 14 2012 Yuri N. Sedunov <aris@altlinux.org> 3.3.2-alt1
- 3.3.2

* Mon Nov 21 2011 Yuri N. Sedunov <aris@altlinux.org> 3.2.1-alt1
- first build for Sisyphus


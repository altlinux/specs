%define _name gdlmm
%define ver_major 3.7
%define api_ver 3.0
%def_enable snapshot
%def_enable doc

%if_enabled snapshot
%def_disable doc
%endif

Name: lib%{_name}3
Version: %ver_major.3
Release: alt3

Summary: C++ bindings for the gdl library
Group: System/Libraries
License: LGPLv2+
Url: http://www.gtkmm.org/

%if_disabled snapshot
Source: ftp://ftp.gnome.org/pub/gnome/sources/%_name/%ver_major/%_name-%version.tar.xz
%else
Source: %_name-%version.tar
%endif
Patch: gdlmm-3.7.3-cxx11.patch

BuildRequires: gcc-c++ mm-common >= 0.9.8
BuildRequires: libglibmm-devel libgtkmm3-devel libgdl3-devel >= 3.7.0
BuildRequires: perl-XML-Parser
%{?_enable_snapshot:BuildRequires: xsltproc doxygen graphviz}

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
%patch

%build
mm-common-prepare
%autoreconf
%configure \
%{?_enable_snapshot:--enable-maintainer-mode} \
%{?_disable_doc:--disable-documentation}
%make_build

%install
%makeinstall_std

%check
%make check

%files
%_libdir/*.so.*
%doc AUTHORS NEWS README

%files devel
%_includedir/%_name-%api_ver/
%_libdir/*.so
%_libdir/%_name-%api_ver/
%_libdir/pkgconfig/*.pc

%if_enabled doc
%files devel-doc
%_docdir/%_name-%api_ver/
%_datadir/devhelp/*
%endif

%changelog
* Sat Jan 27 2018 Yuri N. Sedunov <aris@altlinux.org> 3.7.3-alt3
- updated to gdlmm-3.7.3-1-gbc271a7

* Wed Sep 30 2015 Yuri N. Sedunov <aris@altlinux.org> 3.7.3-alt2
- rebuilt with newer *mm libraries

* Wed Jun 17 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 3.7.3-alt1.1
- Rebuilt for gcc5 C++11 ABI.

* Fri Mar 01 2013 Yuri N. Sedunov <aris@altlinux.org> 3.7.3-alt1
- 3.7.3

* Sat Dec 01 2012 Yuri N. Sedunov <aris@altlinux.org> 3.3.2-alt3
- updated to 64fc4535

* Tue Oct 02 2012 Yuri N. Sedunov <aris@altlinux.org> 3.3.2-alt2
- rebuilt against libgdl-3.so.5

* Mon May 14 2012 Yuri N. Sedunov <aris@altlinux.org> 3.3.2-alt1
- 3.3.2

* Mon Nov 21 2011 Yuri N. Sedunov <aris@altlinux.org> 3.2.1-alt1
- first build for Sisyphus


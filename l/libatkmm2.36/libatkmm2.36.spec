%def_disable snapshot
%define rname atkmm
%define ver_major 2.36
%define api_ver %ver_major

%def_enable docs
%def_enable check

Name: lib%rname%api_ver
Version: %ver_major.0
Release: alt1

Summary: A C++ interface for ATK library
License: LGPLv2.1+
Group: System/Libraries
Url: http://atkmm.sourceforge.net/

%if_enabled snapshot
Source: %rname-%version.tar
%else
Source: ftp://ftp.gnome.org/pub/gnome/sources/%rname/%ver_major/%rname-%version.tar.xz
%endif

Provides: %rname-%api_ver = %version

%define glibmm_api_ver 2.68
%define glibmm_ver 2.68.0
%define atk_ver 1.18

BuildRequires(pre): meson
BuildRequires: gcc-c++ mm-common 
BuildRequires: libatk-devel >= %atk_ver libglibmm%glibmm_api_ver-devel  >= %glibmm_ver
%{?_enable_docs:BuildRequires: docbook-style-xsl doxygen graphviz xsltproc}

%description
ATK, the Accessibility Tookit, is used to obtain accessibily information
from GTK+ and GNOME widgets.

ATKmm provides a C++ interface to the ATK library.

%package devel
Summary: Headers for developing programs that will use %name
Group: Development/C++
Requires: %name = %EVR
Provides: %rname-%api_ver-devel = %version

%description devel
This package contains the static libraries and header files needed for
developing atkmm applications.

%package devel-doc
Summary: Documentation for developing with %name
Group: Development/C++
BuildArch: noarch
Conflicts: %name-devel < %version

%description devel-doc
This package contains the documentation for
developing atkmm applications.

%prep
%setup -n %rname-%version

%build
%{?_enable_snapshot:mm-common-prepare -f}
%meson \
    %{?_enable_docs:-Dbuild-documentation=true} \
    %{?_enable_snapshot:-Dmaintainer-mode=true
    -Dbuild-documentation=true}
%nil
%meson_build

%install
%meson_install

%check
export LD_LIBRARY_PATH=%buildroot%_libdir
%meson_test

%files
%doc AUTHORS NEWS
%_libdir/*.so.*

%files devel
%_includedir/%rname-%api_ver
%_libdir/*.so
%_libdir/%rname-%api_ver
%_pkgconfigdir/*.pc

%if_enabled docs
%files devel-doc
%_datadir/devhelp/books/%rname-%api_ver
%_docdir/%rname-%api_ver
%endif

%changelog
* Sat Dec 19 2020 Yuri N. Sedunov <aris@altlinux.org> 2.36.0-alt1
- 2.36.0 (new atkmm-2.36 library)
- -- end of atkmm-1.6 --

* Sun Dec 13 2020 Yuri N. Sedunov <aris@altlinux.org> 2.28.1-alt1
- 2.28.1 (ported to Meson build system)

* Thu Mar 21 2019 Yuri N. Sedunov <aris@altlinux.org> 2.28.0-alt1
- 2.28.0

* Sun Nov 04 2018 Yuri N. Sedunov <aris@altlinux.org> 2.24.3-alt1
- 2.24.3

* Sun Nov 29 2015 Yuri N. Sedunov <aris@altlinux.org> 2.24.2-alt1
- 2.24.2

* Mon Sep 21 2015 Yuri N. Sedunov <aris@altlinux.org> 2.24.1-alt1
- 2.24.1

* Thu May 21 2015 Yuri N. Sedunov <aris@altlinux.org> 2.22.7-alt2
- rebuilt with gcc5

* Wed Apr 24 2013 Yuri N. Sedunov <aris@altlinux.org> 2.22.7-alt1
- 2.22.7

* Thu Mar 31 2011 Yuri N. Sedunov <aris@altlinux.org> 2.22.5-alt1
- 2.22.5

* Wed Mar 23 2011 Yuri N. Sedunov <aris@altlinux.org> 2.22.3-alt1
- 2.22.3

* Wed Mar 16 2011 Yuri N. Sedunov <aris@altlinux.org> 2.22.2-alt2
- rebuild for debuginfo

* Sat Jan 15 2011 Yuri N. Sedunov <aris@altlinux.org> 2.22.2-alt1
- 2.22.2

* Sun Nov 21 2010 Yuri N. Sedunov <aris@altlinux.org> 2.22.1-alt1
- 2.22.1

* Mon Oct 18 2010 Yuri N. Sedunov <aris@altlinux.org> 2.22.0-alt1
- 2.22.0

* Thu Jun 24 2010 Yuri N. Sedunov <aris@altlinux.org> 2.21.1-alt1
- first build for Sisyphus


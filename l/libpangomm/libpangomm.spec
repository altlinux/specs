%def_disable snapshot

%define rname pangomm
%define major 2.46
%define api_ver 1.4

%def_enable docs
%def_enable check

Name: lib%rname
Version: %major.2
Release: alt1

Summary: This library provides a C++ interface to pango
License: LGPL-2.1 and GPL-2.0
Group: System/Libraries
Url: http://gtkmm.sourceforge.net/

Conflicts: libgtkmm2 < 2.14.1

%if_enabled snapshot
Source: %rname-%version.tar
%else
Source: ftp://ftp.gnome.org/pub/gnome/sources/%rname/%major/%rname-%version.tar.xz
%endif

%define glib_ver 2.48.0
%define cairo_ver 1.2.2
%define pango_ver 1.46

BuildRequires(pre): meson
BuildRequires: mm-common gcc-c++
BuildRequires: libcairomm-devel >= %cairo_ver
BuildRequires: libglibmm-devel >= %glib_ver
BuildRequires: libpango-devel >= %pango_ver
%{?_enable_docs:BuildRequires: docbook-style-xsl doxygen graphviz xsltproc}

%description
This library provides a C++ interface to pango.

%package devel
Summary: Headers and development files of %name library
Group: Development/GNOME and GTK+
Requires: %name = %version-%release
Conflicts: libgtkmm2-devel < 2.14.1

%description devel
This package contains the headers and various development files needed
for compiling or development of applications that wants C++ interface
of %name library.

%package doc
Summary: %name documentation (html)
Group: Publishing
Requires: %name = %version-%release
BuildArch: noarch

%description doc
%name development documentation (html)

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
%files doc
%_datadir/devhelp/books/%rname-%api_ver
%_docdir/%rname-%api_ver
%endif

%changelog
* Sun Dec 05 2021 Yuri N. Sedunov <aris@altlinux.org> 2.46.2-alt1
- 2.46.2

* Fri May 21 2021 Yuri N. Sedunov <aris@altlinux.org> 2.46.1-alt1
- 2.46.1

* Wed Jan 27 2021 Yuri N. Sedunov <aris@altlinux.org> 2.46.0-alt1
- 2.46.0

* Sun Dec 13 2020 Yuri N. Sedunov <aris@altlinux.org> 2.42.2-alt1
- 2.42.2 (ported to Meson build system)

* Sat Mar 21 2020 Yuri N. Sedunov <aris@altlinux.org> 2.42.1-alt1
- 2.42.1
- fixed License tag

* Mon Nov 05 2018 Yuri N. Sedunov <aris@altlinux.org> 2.42.0-alt1
- 2.42.0

* Mon Nov 05 2018 Yuri N. Sedunov <aris@altlinux.org> 2.40.2-alt1
- 2.40.2

* Sun Sep 04 2016 Yuri N. Sedunov <aris@altlinux.org> 2.40.1-alt1
- 2.40.1

* Mon Mar 28 2016 Yuri N. Sedunov <aris@altlinux.org> 2.40.0-alt1
- 2.40.0

* Wed Mar 09 2016 Yuri N. Sedunov <aris@altlinux.org> 2.39.1-alt1
- 2.39.1

* Wed Mar 09 2016 Yuri N. Sedunov <aris@altlinux.org> 2.38.2-alt1
- 2.38.2

* Mon Sep 21 2015 Yuri N. Sedunov <aris@altlinux.org> 2.38.1-alt1
- 2.38.1

* Thu May 21 2015 Yuri N. Sedunov <aris@altlinux.org> 2.36.0-alt2
- rebuilt with gcc5

* Mon Mar 30 2015 Yuri N. Sedunov <aris@altlinux.org> 2.36.0-alt1
- 2.36.0

* Wed Apr 24 2013 Yuri N. Sedunov <aris@altlinux.org> 2.34.0-alt1
- 2.34.0

* Tue Sep 27 2011 Yuri N. Sedunov <aris@altlinux.org> 2.28.3-alt1
- 2.28.3

* Thu Mar 31 2011 Yuri N. Sedunov <aris@altlinux.org> 2.28.2-alt1
- 2.28.2

* Wed Mar 23 2011 Yuri N. Sedunov <aris@altlinux.org> 2.28.0-alt1
- 2.28.0

* Sat Jan 15 2011 Yuri N. Sedunov <aris@altlinux.org> 2.27.1-alt1
- 2.27.1

* Fri Dec 10 2010 Yuri N. Sedunov <aris@altlinux.org> 2.26.3-alt1
- 2.26.3

* Fri Nov 26 2010 Igor Vlasenko <viy@altlinux.ru> 2.26.2-alt1.qa1
- rebuild using girar-nmu to require/provide setversion
  by request of mithraen@

* Tue May 04 2010 Yuri N. Sedunov <aris@altlinux.org> 2.26.2-alt1
- 2.26.2

* Fri Apr 16 2010 Yuri N. Sedunov <aris@altlinux.org> 2.26.1-alt1
- 2.26.1

* Mon Sep 21 2009 Valery Inozemtsev <shrek@altlinux.ru> 2.26.0-alt1
- 2.26.0

* Tue Nov 04 2008 Vitaly Lipatov <lav@altlinux.ru> 2.14.0-alt1
- initial build for ALT Linux Sisyphus


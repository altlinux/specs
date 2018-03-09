%def_disable snapshot

%define _name cairomm

%def_disable docs
%def_enable check

Name: lib%_name
Version: 1.12.2
Release: alt1

Summary: This library provides a C++ interface to cairo
License: LGPL
Group: System/Libraries
Url: https://cairographics.org/cairomm
Packager: GNOME Maintainers Team <gnome@packages.altlinux.org>

%if_disabled snapshot
Source: https://www.cairographics.org/releases/%_name-%version.tar.gz
%else
#VCS: git://git.cairographics.org/git/cairomm
Source: %_name-%version.tar
%endif

%define cairo_ver 1.10.0
%define sigc_ver 2.6.0

BuildRequires: gcc-c++ mm-common
BuildRequires: libcairo-devel >= %cairo_ver libsigc++2.0-devel >= %sigc_ver
%{?_enable_docs:BuildRequires: doxygen graphviz xsltproc}

%description
This library provides a C++ interface to cairo.

%package devel
Summary: Headers and development files of %name library
Group: Development/GNOME and GTK+
Requires: %name = %version-%release

%description devel
This package contains the headers and various development files needed
for compiling or development of applications that wants C++ interface
of %name library.

%package devel-doc
Summary: Development documentation for %name
Group: Development/Documentation
BuildArch: noarch
Conflicts: %name < %version

%description devel-doc
This package contains documentation needed for developing %_name applications.

%prep
%setup -n %_name-%version

%build
%{?_enable_snapshot:mm-common-prepare --force --copy}
%autoreconf
%configure \
	--disable-static \
	%{?_disable_docs:--disable-documentation} \
	%{?_enable_snapshot:--enable-maintainer-mode}
%make_build

%install
%makeinstall_std

%check
%make check

%files
%doc AUTHORS NEWS
%_libdir/*.so.*

%files devel
%_includedir/cairomm-1.0
%_libdir/cairomm-1.0
%_libdir/*.so
%_pkgconfigdir/*.pc

%if_enabled docs
%files devel-doc
%_datadir/devhelp/books/%_name-%api_ver/
%_datadir/doc/%_name-%api_ver/
%endif

%changelog
* Wed Mar 07 2018 Yuri N. Sedunov <aris@altlinux.org> 1.12.2-alt1
- 1.12.2

* Tue Sep 22 2015 Yuri N. Sedunov <aris@altlinux.org> 1.12.0-alt1
- 1.12.0

* Fri Jun 12 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 1.11.2-alt1.1
- Rebuilt for gcc5 C++11 ABI.

* Mon Oct 20 2014 Valery Inozemtsev <shrek@altlinux.ru> 1.11.2-alt1
- 1.11.2

* Tue Feb 15 2011 Valery Inozemtsev <shrek@altlinux.ru> 1.9.8-alt1
- 1.9.8

* Sat Dec 18 2010 Valery Inozemtsev <shrek@altlinux.ru> 1.9.6-alt1
- 1.9.6

* Thu Nov 25 2010 Igor Vlasenko <viy@altlinux.ru> 1.8.2-alt3.qa1
- rebuild using girar-nmu to require/provide setversion
  by request of mithraen@

* Wed Nov 03 2010 Valery Inozemtsev <shrek@altlinux.ru> 1.8.6-alt1
- 1.8.6

* Sun Aug 08 2010 Valery Inozemtsev <shrek@altlinux.ru> 1.8.2-alt3
- rebuild

* Sun Aug 08 2010 Valery Inozemtsev <shrek@altlinux.ru> 1.8.2-alt2
- rebuild

* Mon Sep 21 2009 Valery Inozemtsev <shrek@altlinux.ru> 1.8.2-alt1
- 1.8.2

* Sun Apr 13 2008 Vitaly Lipatov <lav@altlinux.ru> 1.6.0-alt1
- new version 1.6.0 (with rpmrb script)

* Tue Jan 08 2008 Vitaly Lipatov <lav@altlinux.ru> 1.4.6-alt1
- new version 1.4.6 (with rpmrb script)
- cleanup spec, update buildreq
- move doc to right place (for devhelp)

* Sat Nov 03 2007 Vitaly Lipatov <lav@altlinux.ru> 1.4.4-alt1
- new version 1.4.4 (with rpmrb script)

* Sat Apr 07 2007 Vitaly Lipatov <lav@altlinux.ru> 1.2.4-alt1
- new version 1.2.4 (with rpmrb script)

* Fri Sep 01 2006 Vitaly Lipatov <lav@altlinux.ru> 1.2.2-alt0.1
- new version 1.2.2 (with rpmrb script)

* Mon May 01 2006 Vitaly Lipatov <lav@altlinux.ru> 0.6.0-alt0.1
- new version 0.6.0
- add doxygen for doc generating

* Sun Mar 05 2006 Vitaly Lipatov <lav@altlinux.ru> 0.5.0-alt0.1
- new version (0.5.0)
- split doc to doc package (thanks to pv@)
- fix build bug (thanks to pv@)

* Thu Feb 09 2006 Vitaly Lipatov <lav@altlinux.ru> 0.4.0-alt0.1
- initial build for ALT Linux Sisyphus


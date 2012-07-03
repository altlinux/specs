%define rname pangomm
%define major 2.28

Name: lib%rname
Version: %major.3
Release: alt1

Summary: This library provides a C++ interface to pango
License: LGPL
Group: System/Libraries
Url: http://gtkmm.sourceforge.net/
Packager: GNOME Maintainers Team <gnome@packages.altlinux.org>

Conflicts: libgtkmm2 < 2.14.1

Source: ftp://ftp.gnome.org/pub/gnome/sources/%rname/%major/%rname-%version.tar.xz

BuildRequires: mm-common gcc-c++ libcairomm-devel libglibmm-devel libpango-devel

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
%setup -q -n %rname-%version

%build
%configure \
	--disable-static
%make_build

%install
%make DESTDIR=%buildroot install

%files
%doc AUTHORS NEWS
%_libdir/*.so.*

%files devel
%_includedir/%rname-1.4
%_libdir/*.so
%_libdir/%rname-1.4
%_pkgconfigdir/*.pc

%files doc
%_datadir/devhelp/books/%rname-1.4
%_docdir/%rname-1.4

%changelog
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


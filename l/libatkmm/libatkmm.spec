%define api_version 1.6
%define rname atkmm
%define major 2.22

Name: libatkmm
Version: %major.5
Release: alt1

Summary: A C++ interface for ATK library
License: LGPLv2.1+
Group: System/Libraries
Url: http://atkmm.sourceforge.net/
Packager: GNOME Maintainers Team <gnome@packages.altlinux.org>

Source: ftp://ftp.gnome.org/pub/gnome/sources/%rname/%major/%rname-%version.tar.bz2

Provides: %rname = %version

BuildRequires: gcc-c++ mm-common libatk-devel >= 1.12 libglibmm-devel >= 2.24

%description
ATK, the Accessibility Tookit, is used to obtain accessibily information
from GTK+ and GNOME widgets.

ATKmm provides a C++ interface to the ATK library.

%package devel
Summary: Headers for developing programs that will use %name
Group: Development/C++
Requires: %name = %version-%release
Provides: %rname-devel = %version

%description devel
This package contains the static libraries and header files needed for
developing atkmm applications.

%package doc
Summary: Documentation for developing with %name
Group: Development/C++
BuildArch: noarch
Conflicts: %name-devel < %version

%description doc
This package contains the documentation for
developing atkmm applications.


%prep
%setup -q -n %rname-%version

%build
mm-common-prepare -f
%autoreconf
%configure \
	--disable-static

%make_build

%install
%make DESTDIR=%buildroot atkmm_docdir=%_docdir/%rname-%api_version install

%files
%doc AUTHORS NEWS
%_libdir/*.so.*

%files devel
%_includedir/%rname-%api_version
%_libdir/*.so
%_libdir/%rname-%api_version
%_pkgconfigdir/*.pc

%files doc
%_datadir/devhelp/books/%rname-%api_version
%_docdir/%rname-%api_version

%changelog
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


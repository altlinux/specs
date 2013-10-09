%define _name harfbuzz
%def_without graphite2
%def_disable introspection

Name: lib%_name
Version: 0.9.22
Release: alt1

Summary: HarfBuzz is an OpenType text shaping engine
Group: System/Libraries
License: MIT
Url: http://freedesktop.org/wiki/Software/HarfBuzz

Source: http://www.freedesktop.org/software/%_name/release/%_name-%version.tar.bz2
#Source: %_name-%version.tar

BuildRequires: gtk-doc gcc-c++ glib2-devel libfreetype-devel libcairo-devel libicu-devel
%{?_enable_introspection:BuildRequires: gobject-introspection-devel}
%{?_with_graphite2:BuildRequires: libgraphite2-devel}

%description
HarfBuzz is an implementation of the OpenType Layout engine.
This package provides shared HarfBuzz library.

%package icu
Summary: Shared HarfBuzz library with ICU support.
Group: System/Libraries
Requires: %name = %version-%release

%description icu
HarfBuzz is an implementation of the OpenType Layout engine.
This package provides shared HarfBuzz library with ICU support.

%package devel
Summary: Development files for %name
Group: Development/C++
Requires: %name = %version-%release
Requires: %name-icu = %version-%release

%description devel
The %name-devel package contains files for developing applications that
use HarfBuzz library.

%package devel-doc
Summary: Development documentation for Pango
Group: Development/Documentation
Conflicts: %name < %version-%release
BuildArch: noarch

%description devel-doc
HarfBuzz is an implementation of the OpenType Layout engine.
This package contains development documentation for HarfBuzz.

%package utils
Summary: Utilities from HarfBuzz project
Group: Development/Tools
Requires: %name = %version-%release

%description utils
The %name-utils package provides utilities from %name package.

%package gir
Summary: GObject introspection data for the HarfBuzz library
Group: System/Libraries
Requires: %name = %version-%release

%description gir
GObject introspection data for the HarfBuzz library

%package gir-devel
Summary: GObject introspection devel data for the HarfBuzz library
Group: Development/Other
BuildArch: noarch
Requires: %name-gir = %version-%release

%description gir-devel
GObject introspection devel data for the HarfBuzz library

%prep
%setup -n %_name-%version

%build
%autoreconf
%configure --disable-static \
	--with-glib \
	--with-freetype \
	--with-cairo \
	--with-icu \
	%{?_enable_introspection:--enable-introspection=yes} \
	%{subst_with graphite2}


%make_build

%install
%makeinstall_std

%check
%make check

%files
%_libdir/%name.so.*

%files devel
%_includedir/%_name/
%_libdir/%name.so
%_libdir/%name-icu.so
%_pkgconfigdir/%_name.pc
%_pkgconfigdir/%_name-icu.pc
%doc NEWS AUTHORS COPYING README

%files devel-doc
%_datadir/gtk-doc/html/*

%files icu
%_libdir/%name-icu.so.*

%files utils
%_bindir/hb-view
%_bindir/hb-ot-shape-closure
%_bindir/hb-shape

%if_enabled introspection
%files gir
%_typelibdir/*.typelib

%files gir-devel
%_girdir/*.gir
%endif


%changelog
* Wed Oct 09 2013 Yuri N. Sedunov <aris@altlinux.org> 0.9.22-alt1
- 0.9.22

* Sat Sep 21 2013 Yuri N. Sedunov <aris@altlinux.org> 0.9.21-alt1
- 0.9.21
- new -devel-doc subpackage
- prepared -gir, gir-devel subpackages

* Thu Jun 13 2013 Yuri N. Sedunov <aris@altlinux.org> 0.9.18-alt1
- 0.9.18
- new lib%%name-icu{,-devel} subpackages

* Mon May 13 2013 Yuri N. Sedunov <aris@altlinux.org> 0.9.16-alt1
- 0.9.16

* Sun Apr 14 2013 Yuri N. Sedunov <aris@altlinux.org> 0.9.14-alt1
- 0.9.14

* Tue Mar 19 2013 Yuri N. Sedunov <aris@altlinux.org> 0.9.13-alt1
- 0.9.13

* Tue Feb 19 2013 Yuri N. Sedunov <aris@altlinux.org> 0.9.12-alt1
- 0.9.12

* Thu Jan 10 2013 Yuri N. Sedunov <aris@altlinux.org> 0.9.11-alt1
- 0.9.11

* Fri Dec 07 2012 Yuri N. Sedunov <aris@altlinux.org> 0.9.9-alt1
- 0.9.9

* Wed Nov 14 2012 Yuri N. Sedunov <aris@altlinux.org> 0.9.6-alt1
- 0.9.6

* Tue Sep 18 2012 Yuri N. Sedunov <aris@altlinux.org> 0.9.4-alt1
- first build for Sisyphus


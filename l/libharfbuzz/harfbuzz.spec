%define _name harfbuzz

Name: lib%_name
Version: 0.9.9
Release: alt1

Summary: HarfBuzz is an OpenType text shaping engine
Group: System/Libraries
License: MIT
Url: http://freedesktop.org/wiki/Software/HarfBuzz

Source: http://www.freedesktop.org/software/%_name/release/%_name-%version.tar.bz2
#Source: %_name-%version.tar

BuildRequires: gcc-c++ glib2-devel libfreetype-devel libcairo-devel libicu-devel

%description
HarfBuzz is an implementation of the OpenType Layout engine.
This package provides shared HarfBuzz library.

%package devel
Summary: Development files for %name
Group: Development/C++
Requires: %name = %version-%release

%description devel
The %name-devel package contains files for developing applications that
use HarfBuzz library.

%package utils
Summary: Utilities from HarfBuzz project
Group: Development/Tools
Requires: %name = %version-%release

%description utils
The %name-utils package provides utilities from %name package.

%prep
%setup -n %_name-%version

%build
%autoreconf
%configure --disable-static


%make_build

%install
%makeinstall_std

%check
#%make check

%files
%_libdir/*.so.*

%files devel
%_includedir/%_name/
%_libdir/*.so
%_pkgconfigdir/%_name.pc
%doc NEWS AUTHORS COPYING README

%files utils
%_bindir/hb-view
%_bindir/hb-ot-shape-closure
%_bindir/hb-shape


%changelog
* Fri Dec 07 2012 Yuri N. Sedunov <aris@altlinux.org> 0.9.9-alt1
- 0.9.9

* Wed Nov 14 2012 Yuri N. Sedunov <aris@altlinux.org> 0.9.6-alt1
- 0.9.6

* Tue Sep 18 2012 Yuri N. Sedunov <aris@altlinux.org> 0.9.4-alt1
- first build for Sisyphus


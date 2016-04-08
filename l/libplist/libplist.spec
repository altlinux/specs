Name: libplist
Version: 1.12
Release: alt2

Summary: Library for manipulating Apple Binary and XML Property Lists
Group: System/Libraries
License: LGPLv2+
Url: http://www.libimobiledevice.org/

Source: %url/downloads/%name-%version.tar.bz2

BuildRequires: gcc-c++ cmake libxml2-devel xml-utils
BuildRequires: python-devel python-module-Cython >= 0.18
#BuildRequires: python3-devel rpm-build-python3 python3-module-Cython >= 0.18

%description
libplist is a library for manipulating Apple Binary and XML Property Lists

%package -n %{name}mm
Summary: Cmm wrapper for %name library
Group: System/Libraries
Requires: %name = %version-%release

%description -n %{name}mm
This package provides Cmm interface for %name library

%package -n %{name}mm-devel
Summary: Headers and development files for %{name}mm library
Group: System/Libraries
Requires: %{name}mm = %version-%release
Requires: %name-devel = %version-%release

%description -n %{name}mm-devel
This package contains the headers and development files that are needed
to develop or compile applications which need %{name}mm library

%package devel
Summary: Development package for libplist
Group: Development/C
Requires: %name = %version-%release

%description devel
This package provides development headers and libraries for %name

%package -n python-module-%name
Summary: Python package for libplist
Group: Development/Python
Requires: %name = %version-%release
Requires: %{name}mm = %version-%release

%description -n python-module-%name
Python libraries and bindings for %name

%prep
%setup

%build
%autoreconf
%configure --disable-static
%make_build

%install
%makeinstall_std

%files
%_bindir/plistutil
%_libdir/libplist.so.*
%doc AUTHORS README

%files devel
%_includedir/plist/
%_libdir/libplist.so
%_libdir/pkgconfig/libplist.pc
%exclude %_includedir/plist/plist++.h

%files -n %{name}mm
%_libdir/libplist++.so.*

%files -n %{name}mm-devel
%_includedir/plist/plist++.h
%_libdir/libplist++.so
%_libdir/pkgconfig/libplist++.pc

%files -n python-module-%name
%python_sitelibdir/plist.so
%exclude %python_sitelibdir/plist.la

%changelog
* Fri Apr 08 2016 Yuri N. Sedunov <aris@altlinux.org> 1.12-alt2
- rebuilt for new gcc, python, cython etc.

* Wed Oct 15 2014 Yuri N. Sedunov <aris@altlinux.org> 1.12-alt1
- 1.12

* Tue Mar 25 2014 Yuri N. Sedunov <aris@altlinux.org> 1.11-alt1
- 1.11

* Mon Nov 11 2013 Yuri N. Sedunov <aris@altlinux.org> 1.10-alt2
- fixed %%build for cmake-2.8.12.1-alt1

* Thu Apr 11 2013 Yuri N. Sedunov <aris@altlinux.org> 1.10-alt1
- 1.10

* Tue Mar 19 2013 Yuri N. Sedunov <aris@altlinux.org> 1.9-alt1
- 1.9

* Sun Apr 08 2012 Yuri N. Sedunov <aris@altlinux.org> 1.8-alt1
- 1.8

* Tue Oct 25 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.4-alt1.1
- Rebuild with Python-2.7

* Sun Mar 20 2011 Yuri N. Sedunov <aris@altlinux.org> 1.4-alt1
- 1.4

* Fri Mar 11 2011 Yuri N. Sedunov <aris@altlinux.org> 1.3-alt3
- rebuilt for debuginfo

* Tue Nov 02 2010 Yuri N. Sedunov <aris@altlinux.org> 1.3-alt2
- rebuild

* Thu May 27 2010 Yuri N. Sedunov <aris@altlinux.org> 1.3-alt1
- 1.3

* Mon Jan 25 2010 Yuri N. Sedunov <aris@altlinux.org> 1.2-alt1
- 1.2

* Thu Dec 03 2009 Yuri N. Sedunov <aris@altlinux.org> 0.16-alt1
- first build for Sisyphus


Name: libplist
Version: 1.8
Release: alt1

Summary: Library for manipulating Apple Binary and XML Property Lists
Group: System/Libraries
License: LGPLv2+
Url: http://www.libimobiledevice.org/

Source: http://github.com/downloads/JonathanBeck/%name/%name-%version.tar.bz2

BuildRequires: gcc-c++ cmake libxml2-devel xml-utils python-devel swig python-module-Cython

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
%setup -q

%build
%cmake -DCMAKE_INSTALL_LIBDIR=%_lib
pushd BUILD
%make

%install
pushd BUILD
make DESTDIR=%buildroot install

%files
%_bindir/plutil
%_bindir/plutil-%version
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
%python_sitelibdir/plist/
%python_sitelibdir/plist.so

%changelog
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


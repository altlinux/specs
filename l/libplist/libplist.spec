%def_enable snapshot
%def_disable python
%def_disable python2
%def_enable check

Name: libplist
Version: 2.1.0
Release: alt1

Summary: Library for manipulating Apple Binary and XML Property Lists
Group: System/Libraries
License: LGPLv2+
Url: http://www.libimobiledevice.org/

%if_disabled snapshot
Source: %url/downloads/%name-%version.tar.bz2
%else
# VCS: http://git.sukimashita.com/libplist.git
Source: %name-%version.tar
%endif
Patch: libplist-2.0.0-alt-e2k-lcc123.patch

BuildRequires: gcc-c++ xml-utils
%{?_enable_python:BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-Cython}
%{?_enable_python2:BuildRequires(pre): rpm-build-python
BuildRequires: python-devel python-module-Cython}

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

%package -n python3-module-%name
Summary: Python3 package for libplist
Group: Development/Python3
Requires: %name = %version-%release
Requires: %{name}mm = %version-%release

%description -n python3-module-%name
Python3 libraries and bindings for %name


%prep
%setup -a0
%patch -p1 -b .e2k
%{?_enable_python2:mv %name-%version py2build
subst 's/\(PYTHON-config --ldflags\)/\1 -lpython%__python_version/' py2build/m4/ac_python_devel.m4
}

%build
%add_optflags -D_FILE_OFFSET_BITS=64 %optflags_shared
%autoreconf
%configure --disable-static CC=gcc \
%{?_enable_python:PYTHON=%__python3} \
%{?_disable_python:--without-cython}

%make_build

%if_enabled python2
pushd py2build
%autoreconf
%configure --disable-static PYTHON=%__python
%make_build
popd
%endif

%install
%makeinstall_std

%if_enabled python2
pushd py2build
%makeinstall_std
popd
%endif

%check
%make check

%files
%_bindir/plistutil
%_libdir/libplist.so.*
%doc AUTHORS README* NEWS

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
%_pkgconfigdir/libplist++.pc

%if_enabled python2
%files -n python-module-%name
%python_sitelibdir/plist.so
%exclude %python_sitelibdir/plist.la
%endif

%if_enabled python
%files -n python3-module-%name
%python3_sitelibdir/plist.so
%exclude %python3_sitelibdir/plist.la
%endif

%changelog
* Thu Dec 12 2019 Yuri N. Sedunov <aris@altlinux.org> 2.1.0-alt1
- updated to 2.1.0-11-g878d0d8
- disabled useless python support
- new %%check section

* Tue Jan 08 2019 Yuri N. Sedunov <aris@altlinux.org> 2.0.0-alt2
- updated to 2.0.0-27-g3f96731
- mike@: applied e2k patch to work around lcc-1.23's lack of gcc5 builtins

* Sun Apr 30 2017 Yuri N. Sedunov <aris@altlinux.org> 2.0.0-alt1
- 2.0.0 (fixed CVE-2017-6440, CVE-2017-6439, CVE-2017-6438, CVE-2017-6437,
  CVE-2017-6436, CVE-2017-6435, CVE-2017-5836, CVE-2017-5835, CVE-2017-5834,
  CVE-2017-5545, CVE-2017-5209)

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


%def_enable shared
%def_enable static

%define Name Exempi
%define bname exempi

Name: lib%bname
Version: 2.1.1
Release: alt2

Summary: Library for easy parsing of XMP metadata
Group: System/Libraries
License: %bsd

URL: http://libopenraw.freedesktop.org/wiki/%Name

Source: http://libopenraw.freedesktop.org/download/%bname-%version.tar.gz

BuildRequires(pre): rpm-build-licenses
BuildRequires: boost-test-devel gcc-c++ libexpat-devel zlib-devel

%description
%Name provides a library for easy parsing of XMP metadata. It is a
port of Adobe XMP SDK to work on UNIX.


%package devel
Summary: Headers for developing programs that will use %name
Group: Development/C
Requires: %name%{?_disable_shared:-devel-static} = %version-%release

%description devel
This package contains the libraries and header files needed for
developing with %name.


%if_enabled static
%package devel-static
Summary: Static library for developing programs that will use %name
Group: Development/C
Requires: %name-devel = %version-%release

%description devel-static
This package contains the static library needed for developing with
%name.
%endif


%prep
%setup -n %bname-%version

%build
%define _optlevel 3
%autoreconf
%configure \
    %{subst_enable shared} \
    %{subst_enable static}

%make_build

%install
%make_install DESTDIR=%buildroot install

%if_enabled shared
%files
%doc AUTHORS ChangeLog NEWS README
%_libdir/*.so.*
%endif

%files devel
%{?_disable_shared:%doc AUTHORS ChangeLog NEWS README}
%_includedir/%bname-2.0/
%{?_enable_shared:%_libdir/*.so}
%_pkgconfigdir/*


%if_enabled static
%files devel-static
%_libdir/*.a
%endif


%changelog
* Tue Nov 02 2010 Yuri N. Sedunov <aris@altlinux.org> 2.1.1-alt2
- rebuild

* Tue Aug 25 2009 Yuri N. Sedunov <aris@altlinux.org> 2.1.1-alt1
- 2.1.1

* Sun Dec 28 2008 Led <led@altlinux.ru> 2.1.0-alt1
- 2.1.0
- cleaned up spec

* Mon Aug 25 2008 Led <led@altlinux.ru> 2.0.2-alt1
- 2.0.2

* Tue May 06 2008 Led <led@altlinux.ru> 2.0.1-alt1
- 2.0.1

* Thu Apr 03 2008 Led <led@altlinux.ru> 2.0.0-alt1
- 2.0.0

* Sat Feb 02 2008 Led <led@altlinux.ru> 1.99.9-alt1
- 1.99.9
- cleaned up spec
- initial build for Sisyphus

* Wed Sep 05 2007 Deji Akingunola <dakingun@gmail.com> - 1.99.4-2
- Rebuild for expat 2.0

* Wed Aug 22 2007 Deji Akingunola <dakingun@gmail.com> - 1.99.4-1
- Update tp 1.99.4

* Tue Jul 10 2007 Deji Akingunola <dakingun@gmail.com> - 1.99.3-1
- Initial packaging for Fedora

%def_disable static

Name: eio
Version: 1.0.1
%ifdef beta
Release: alt1.%beta
%else
Release: alt1
%endif

Summary: Enlightenment Input Output Library
License: LGPLv2.1+
Group: System/Libraries
Url: http://www.enlightenment.org/

# http://svn.enlightenment.org/svn/e/trunk/%name
Source: http://download.enlightenment.org/releases/%name-%version.tar.bz2

BuildRequires: libeina-devel >= 1.2.0
BuildRequires: libecore-devel >= 1.2.0
BuildRequires: libeet-devel >= 1.6.0
%{?_enable_static:BuildPreReq: glibc-devel-static}

%description
EIO is a library that intended to provide non blocking IO by using
thread for all operation that may block. It depends only on eina and
ecore right now. It should integrate all the features/functions of
Ecore_File that could block.

%package -n lib%name
Summary: Enlightenment Input Output Library
Group: System/Libraries

%description -n lib%name
Eio is a library that intended to provide non blocking IO by using
thread for all operation that may block. It depends only on eina and
ecore right now. It should integrate all the features/functions of
Ecore_File that could block.

This package contains shared Eio library.

%package -n lib%name-devel
Summary: Enlightenment Input Output Library development files
Group: Development/C
Requires: lib%name = %version-%release

%description -n lib%name-devel
Eio is a library that intended to provide non blocking IO by using
thread for all operation that may block. It depends only on eina and
ecore right now. It should integrate all the features/functions of
Ecore_File that could block.

This package contains headers, development libraries, test programs and
documentation for Eio.

%prep
%setup -q -n %name-%version

%build
%configure \
	%{subst_enable static}

%make_build

%check
%make check

%install
%make DESTDIR=%buildroot install

%files -n lib%name
%_libdir/*.so.*
%doc AUTHORS README

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so
%_libdir/pkgconfig/*

%changelog
* Mon Jun 11 2012 Yuri N. Sedunov <aris@altlinux.org> 1.0.1-alt1
- 1.0.1

* Fri May 11 2012 Yuri N. Sedunov <aris@altlinux.org> 1.0.0-alt1
- 1.0.0

* Tue Dec 06 2011 Yuri N. Sedunov <aris@altlinux.org> 0.1.0.65643-alt1
- first build for Sisyphus


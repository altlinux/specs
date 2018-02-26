%define version 0.18
%define release alt1.3

Summary: Gearman provides a generic application framework to farm out work to other machines.
Name: gearmand
Version: %version
Release: %release
Source0: %name.tar
License: BSD
Group: Development/C
Packager: Sergey Alembekov <rt@altlinux.ru>
URL: http://gearman.org

BuildRequires: perl gcc-c++ boost-devel boost-program_options-devel libevent-devel libuuid-devel

%description
%summary

%package devel
Summary:        Gearmand development files
Group:          Development/C++
Requires:       %name = %version

%description devel
This package contains necessary header files for Gearman development.

%prep
%setup -q -n %name

%build
%configure
%make_build

%install
mkdir %buildroot
make install DESTDIR=%buildroot

%files
%doc ChangeLog README COPYING
%doc %_mandir/man?/*
%_bindir/gearman
%_bindir/gearadmin
%_libdir/libgearman.so.4
%_libdir/libgearman.so.4.0.0
%_sbindir/gearmand
 
%files devel
%_includedir/libgearman/*
%_libdir/libgearman.so
%_pkgconfigdir/gearmand.pc


%changelog
* Thu Apr 05 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.18-alt1.3
- Rebuilt with Boost 1.49.0

* Sun Dec 04 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.18-alt1.2
- Rebuilt with Boost 1.48.0

* Sat Jul 30 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.18-alt1.1
- Rebuilt with Boost 1.47.0

* Tue May 31 2011 Sergey Alembekov <rt@altlinux.ru> 0.18-alt1
- initial release for ALTLinux 


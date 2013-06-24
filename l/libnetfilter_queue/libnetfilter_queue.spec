Name: libnetfilter_queue
Version: 1.0.2
Release: alt1

Summary: API to packets that have been queued by the kernel packet filter
Url: http://netfilter.org/projects/libnetfilter_queue/
License: GPL
Group: System/Libraries
Source: %name-%version.tar

# Automatically added by buildreq on Wed Aug 08 2007
BuildRequires: gcc-c++ libnfnetlink-devel libmnl-devel

%description
libnetfilter_queue is a userspace library providing an API to packets that have 
been queued by the kernel packet filter. It is is part of a system that deprecates 
the old ip_queue / libipq mechanism.

%package devel
Summary: Development part of libnetfilter_queue.
Group: Development/C
Requires: %name = %version-%release

%description devel 
Development part of libnetfilter_queue.

%prep
%setup

%build
autoreconf -fisv
%configure --disable-static
%make_build

%install
mkdir -p %buildroot%_libdir/%name
mkdir -p %buildroot%_includedir/%name
make install DESTDIR=%buildroot

%files
%_libdir/*.so.*
%doc COPYING

%files devel
%_includedir/%name/*
%_libdir/*.so
%_libdir/pkgconfig/*

%changelog
* Tue Jun 25 2013 Anton Farygin <rider@altlinux.ru> 1.0.2-alt1
- New version
- cleanup spec

* Thu Dec 06 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.15-alt1.4
- Fixed build

* Fri Jun 08 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.15-alt1.3
- Fixed build

* Sat Feb 04 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.15-alt1.2
- Removed bad RPATH

* Sun Nov 14 2010 Denis Smirnov <mithraen@altlinux.ru> 0.0.15-alt1.1
- rebuild (with the help of girar-nmu utility)

* Wed Aug  8 2007 Avramenko Andrew <liks@altlinux.ru> 0.0.15-alt1
- Initial build for Sisyphus

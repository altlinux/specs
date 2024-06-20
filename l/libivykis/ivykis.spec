%define rname ivykis
%define soname 0
%def_disable static

Summary: Library for asynchronous I/O readiness notification
Name: libivykis
Version: 0.43.1
Release: alt1

License: LGPLv2+
Url: http://libivykis.sourceforge.net/
Group: System/Libraries
Source0: http://downloads.sourceforge.net/project/libivykis/%version/%rname-%version.tar.gz

%description
ivykis is a library for asynchronous I/O readiness notification.
It is a thin, portable wrapper around OS-provided mechanisms such
as epoll_create(2), kqueue(2), poll(2), poll(7d) (/dev/poll),
port_create(3C) and select(2).

ivykis was mainly designed for building high-performance network
applications, but can be used in any event-driven application that
uses poll(2)able file descriptors as its event sources.

%package -n %{name}%{soname}
Summary: Library for asynchronous I/O readiness notification
Group: System/Libraries
Provides: %name = %EVR
Obsoletes: %name < 0.42.4

%description -n %{name}%{soname}
ivykis is a library for asynchronous I/O readiness notification.
It is a thin, portable wrapper around OS-provided mechanisms such
as epoll_create(2), kqueue(2), poll(2), poll(7d) (/dev/poll),
port_create(3C) and select(2).

ivykis was mainly designed for building high-performance network
applications, but can be used in any event-driven application that
uses poll(2)able file descriptors as its event sources.

%package devel
Summary: Development files for the ivykis package
Group: Development/C
Requires: %name = %EVR
Requires: pkgconfig

%description devel
ivykis is a library for asynchronous I/O readiness notification.
This package contains files needed to develop applications using
ivykis.

%package devel-static
Group: Development/C
License: distributable
Summary: Static %name library
Requires: %name-devel = %EVR

%description devel-static
This package contains static library required to build
statically linked %name-based software.

%prep
%setup -n %rname-%version

%build
%autoreconf
%configure --libdir=%_libdir %{subst_enable static}
%make_build

%install
make DESTDIR=%buildroot install

%files -n %{name}%{soname}
%doc AUTHORS COPYING
%_libdir/libivykis.so.*

%files devel
%_libdir/libivykis.so
%_libdir/pkgconfig/*
%_includedir/iv*
%_man3dir/*.3*

%if_enabled static
%files static
%_libdir/*.a
%endif

%changelog
* Thu Jun 20 2024 L.A. Kostis <lakostis@altlinux.ru> 0.43.1-alt1
- 0.43.1.
- Added missing obsoletes to fix conflict with previous
  version (closes #46174).

* Sun Mar 27 2022 L.A. Kostis <lakostis@altlinux.ru> 0.42.4-alt1
- 0.42.4.
- .spec: fix libname according shared libs policy.

* Mon Sep 04 2017 L.A. Kostis <lakostis@altlinux.ru> 0.42.1-alt1
- Updated to 0.42.1:
  + Fix segfault when calling IV_TASK_INIT() before iv_init().

* Tue May 28 2013 L.A. Kostis <lakostis@altlinux.ru> 0.39-alt0.git20130528
- Updated to 0.39.
- ivykis->libivykis.

* Mon Dec 10 2012 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0.30.5-1
- Update to 0.30.5.

* Sun Oct  7 2012 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0.30.4-2
- Handle review issues (863719#c1)

* Sat Oct  6 2012 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0.30.4-1
- Initial specfile for Fedora and EPEL.

# vim:set ai ts=4 sw=4 sts=4 et:

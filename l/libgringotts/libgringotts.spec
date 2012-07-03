# $Id: libgringotts.spec 169 2004-03-26 15:49:04Z dag $

# Authority: dag

# Upstream: Germano Rizzo <mano@pluto.linux.it>

Summary: libGringotts, a strongbox library
Name: libgringotts
Version: 1.2.1
Release: alt1.1
License: GPL
Group: System/Libraries
URL: http://devel.pluto.linux.it/projects/Gringotts/
Packager: Mykola Grechukh <gns@altlinux.ru>

Source: http://devel.pluto.linux.it/projects/libGringotts/current/%{name}-%{version}.tar.bz2

BuildRequires: libmcrypt-devel, libmhash-devel, zlib-devel, bzip2-devel

%description
libGringotts is a thread-safe C library that allows the programmer
to save data in a particular file format. The data are compressed
and encrypted with a strong encryption algorithm, and saved to the
disk in a secure way. The library gives control over every algorithm
involved in the process, and provides additional security-related
utility functions.
It is very easy to use, and designed to be very light for the system.

%package devel
Summary: Headers and static libraries for gringotts
Group: System/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
These are the files needed to develop applications with libGringotts

%prep
%setup

%build
%configure
%make_build

%install
make DESTDIR=%buildroot install

%files
%doc AUTHORS ChangeLog NEWS README TODO
%{_libdir}/*.so.*

%files devel
%doc docs/manual.htm
%{_libdir}/*.a
%{_libdir}/*.so
%{_libdir}/pkgconfig/*
%{_includedir}/*.h
#exclude %{_libdir}/*.la

%changelog
* Thu Nov 25 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.1-alt1.1
- Rebuilt for soname set-versions

* Tue Jun 22 2010 Mykola Grechukh <gns@altlinux.ru> 1.2.1-alt1
- first build for ALT Linux

* Fri Apr 25 2003 Dag Wieers <dag@wieers.com> - 1.2.1-0
- Updated to release 1.2.1.

* Thu Apr 17 2003 Dag Wieers <dag@wieers.com> - 1.2.0-0
- Updated to release 1.2.0.

* Wed Apr 02 2003 Dag Wieers <dag@wieers.com> - 1.1.1-1
- Fixed libgringotts.pc.

* Tue Jan 07 2003 Dag Wieers <dag@wieers.com> - 1.1.1-0
- Initial package. (using DAR)

%define rname mtdev

Name: lib%rname
Version: 1.1.2
Release: alt1
Summary: Multitouch Protocol Translation Library
Group: System/Libraries
License: MIT
URL: http://bitmath.org/code/mtdev/

Source0: %rname-%version.tar.bz2

BuildRequires: xorg-util-macros

%description
%name is a stand-alone library which transforms all variants of kernel MT
events to the slotted type B protocol. The events put into mtdev may be from
any MT device, specifically type A without contact tracking, type A with
contact tracking, or type B with contact tracking.

%package devel
Summary: Multitouch Protocol Translation Library Development Package
Group: Development/C
Requires: %name = %version-%release

%description devel
Multitouch protocol translation library development package

%prep
%setup -q -n %rname-%version

%build
%autoreconf
%configure \
	--disable-static
%make_build

%install
make DESTDIR=%buildroot install

%files
%_libdir/libmtdev.so.*

%files devel
%_includedir/*.h
%_libdir/libmtdev.so
%_pkgconfigdir/mtdev.pc

%changelog
* Wed Mar 07 2012 Valery Inozemtsev <shrek@altlinux.ru> 1.1.2-alt1
- 1.1.2

* Thu Aug 11 2011 Valery Inozemtsev <shrek@altlinux.ru> 1.1.0-alt1
- initial release


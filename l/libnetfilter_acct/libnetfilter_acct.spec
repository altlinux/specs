Name: libnetfilter_acct
Version: 1.0.3
Release: alt1
Summary: A library providing interface to extended accounting infrastructure

Group: System/Libraries
License: LGPLv2+
Url: http://www.netfilter.org/projects/libnetfilter_acct/index.html
Source0: %name-%version.tar

BuildRequires: libmnl-devel

%description
libnetfilter_acct is the userspace library providing interface to extended
accounting infrastructure.

libnetfilter_acct is used by nfacct.

%package devel
Summary: Development files for %name
Group: System/Libraries
Requires: %name = %version-%release

%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%prep
%setup

%build
autoreconf -fisv
%configure --disable-static
%make_build

%install
%makeinstall_std
find %buildroot -name '*.la' -delete
find examples '(' -name Makefile.in -o -name Makefile ')' -delete

%files
%doc COPYING README
%_libdir/*.so.*

%files devel
%doc COPYING
%doc examples
%_includedir/*
%_libdir/*.so
%_libdir/pkgconfig/%name.pc

%changelog
* Fri Dec 02 2016 Novikov Sergey <sotor@altlinux.org> 1.0.3-alt1
- initial packaging


Name: libpcl
Version: 1.12
Release: alt1
Summary: Portable Coroutine Library (PCL)
Group: System/Libraries
License: GPLv2+
Url: http://xmailserver.org/libpcl.html
Source: http://xmailserver.org/pcl-1.12.tar.gz

%description
The Portable Co-routine Library (PCL) implements the low level
functionality for co-routines in C. Co-routines are a very simple
cooperative multitasking environment where the switch from one task
to another is done explicitly by a function call. Co-routines are a
lot faster and require much less OS resources than processes or
threads.

%package devel
Summary: Development headers and libraries for pcllib
Group: Development/C
Requires: %name = %EVR

%description devel
Development headers and libraries for Portable Co-routine Library (PCL).

%prep
%setup -n pcl-%version

# Note that --disable static is not given because make check requires the static libs
%build
%configure
%make_build

%install
%makeinstall_std
rm -f %buildroot/%_libdir/*.la
rm -f %buildroot/%_libdir/*.a

%check
%make_build check

%files
%_libdir/libpcl.so.*
%doc AUTHORS

%files devel
%_includedir/*
%_libdir/libpcl.so
%_man3dir/*

%changelog
* Tue Sep 24 2019 Alexey Shabalin <shaba@altlinux.org> 1.12-alt1
- initial build

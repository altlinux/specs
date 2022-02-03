Name: libpcl
Version: 1.12
Release: alt2

Summary: Portable Coroutine Library (PCL)
License: GPLv2+
Group: System/Libraries

Url: http://xmailserver.org/libpcl.html
Source: http://xmailserver.org/pcl-1.12.tar.gz
Patch2000: pcl-1.12-alt-e2k.patch

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
%ifarch %e2k
# sed -i "s|struct sigaltstack|stack_t|" pcl/pcl.c
%patch2000 -p1
%endif

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
* Thu Feb 03 2022 Michael Shigorin <mike@altlinux.org> 1.12-alt2
- E2K: fix build (ilyakurdyukov@)

* Tue Sep 24 2019 Alexey Shabalin <shaba@altlinux.org> 1.12-alt1
- initial build

Name: jitterentropy
Version: 2.1.2
Release: alt1

Summary: Library implementing the jitter entropy source
License: BSD or GPLv2
Group: System/Kernel and hardware

Url: https://github.com/smuellerDD/jitterentropy-library
Source0: %name-%version.tar

# Disable Upstream Makefiles debuginfo strip on install
Patch1: jitterentropy-nostrip.patch

%description
Library implementing the CPU jitter entropy source

%package devel
Summary: Development headers for jitterentropy library
Group: Development/C
Requires: %name = %version-%release

%description devel
Development headers and libraries for jitterentropy

%prep
%setup

%patch1 -p1

%build
%make_build

%install
mkdir -p %buildroot/usr/include/
%makeinstall_std PREFIX=/usr LIBDIR=%_lib

%files
%doc README.md COPYING COPYING.bsd COPYING.gplv2
%_libdir/libjitterentropy.so.2*

%files devel
%_includedir/*
%_libdir/libjitterentropy.so
%_mandir/man3/*

%changelog
* Wed Apr 03 2019 Nikolai Kostrigin <nickel@altlinux.org> 2.1.2-alt1
- Initial build for OS ALT
  + based on fedora spec

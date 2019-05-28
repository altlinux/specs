Name: jitterentropy
Version: 2.2.0
Release: alt1

Summary: Library implementing the jitter entropy source
License: BSD or GPLv2
Group: System/Kernel and hardware

Url: https://github.com/smuellerDD/jitterentropy-library
Source: %name-%version.tar

# Disable Upstream Makefiles debuginfo strip on install
Patch: jitterentropy-nostrip.patch

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
%patch -p1
%ifarch %e2k
# strip UTF-8 BOM for lcc < 1.24
find -type f -name '*.cpp' -o -name '*.hpp' -o -name '*.h' |
	xargs -r sed -ri 's,^\xEF\xBB\xBF,,'
%endif

%build
%make_build

%install
mkdir -p %buildroot%_includedir
%makeinstall_std PREFIX=%_usr LIBDIR=%_lib

%files
%doc README* COPYING*
%_libdir/libjitterentropy.so.2*

%files devel
%_includedir/*
%_libdir/libjitterentropy.so
%_man3dir/*

%changelog
* Thu Oct 03 2019 Nikolai Kostrigin <nickel@altlinux.org> 2.2.0-alt1
- New version

* Wed Sep 04 2019 Michael Shigorin <mike@altlinux.org> 2.1.2-alt2
- E2K: strip UTF-8 BOM for lcc < 1.24
- minor spec cleanup

* Wed Apr 03 2019 Nikolai Kostrigin <nickel@altlinux.org> 2.1.2-alt1
- Initial build for OS ALT
  + based on fedora spec

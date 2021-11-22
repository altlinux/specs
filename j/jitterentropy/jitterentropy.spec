%define _unpackaged_files_terminate_build 1
%define soname 3

Name: jitterentropy
Version: 3.3.1
Release: alt1

Summary: Library implementing the jitter entropy source
License: BSD or GPLv2
Group: System/Kernel and hardware

Url: https://github.com/smuellerDD/jitterentropy-library
Source: %name-%version.tar

# build with debug info and do not strip early
Patch: jitterentropy-3.2.0-alt-nostrip.patch

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
%doc README* LICENSE* CHANGES*
%_libdir/libjitterentropy.so.%{soname}*

%files devel
%_includedir/*
%_libdir/libjitterentropy.so
%_man3dir/*

%changelog
* Mon Nov 22 2021 Nikolai Kostrigin <nickel@altlinux.org> 3.3.1-alt1
- New version

* Mon Sep 20 2021 Nikolai Kostrigin <nickel@altlinux.org> 3.3.0-alt1
- New version

* Mon Sep 20 2021 Nikolai Kostrigin <nickel@altlinux.org> 3.2.0-alt1
- New version
  + update nostrip patch
- Spec: rearrange %%doc section

* Thu Oct 03 2019 Nikolai Kostrigin <nickel@altlinux.org> 2.2.0-alt1
- New version

* Wed Sep 04 2019 Michael Shigorin <mike@altlinux.org> 2.1.2-alt2
- E2K: strip UTF-8 BOM for lcc < 1.24
- minor spec cleanup

* Wed Apr 03 2019 Nikolai Kostrigin <nickel@altlinux.org> 2.1.2-alt1
- Initial build for OS ALT
  + based on fedora spec

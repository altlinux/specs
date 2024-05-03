%define _unpackaged_files_terminate_build 1

Name: efivar
Version: 39
Release: alt1

Summary: Tools to manage UEFI variables
License: LGPLv2.1
Group: System/Kernel and hardware

Url: https://github.com/rhinstaller/efivar
Source0: %name-%version.tar
Patch0: %name-%version-%release.patch

Requires: %name-libs = %version-%release

BuildRequires: libpopt-devel libabigail

%description
efivar provides a simple command line interface to the UEFI variable facility.

%package -n lib%name
Summary: Library to manage UEFI variables
Provides: %name-libs = %EVR
Group: System/Libraries

%description -n lib%name
Library to allow for the simple manipulation of UEFI variables.

%package -n lib%name-devel
Summary: Development headers for libefivar
Requires: lib%name = %EVR
Provides: %name-devel = %EVR
Group: Development/C

%description -n lib%name-devel
development headers required to use libefivar.

%prep
%setup
%patch0 -p1

%build
make libdir=%_libdir bindir=%_bindir CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="$RPM_LD_FLAGS" MANDOC="/bin/true"

%install
%makeinstall

%files
%doc README.md COPYING
%_bindir/efivar
%_bindir/efisecdb
%_mandir/man1/*

%files -n lib%name-devel
%_mandir/man3/*
%_includedir/*
%_libdir/*.so
%_libdir/pkgconfig/*.pc

%files -n lib%name
%_libdir/*.so.*

%changelog
* Tue Feb 06 2024 Egor Ignatov <egori@altlinux.org> 39-alt1
- 38 -> 39

* Sat Jul 08 2023 Anton Farygin <rider@altlinux.ru> 38-alt1
- 37 -> 38

* Sat Feb 27 2021 Anton Farygin <rider@altlinux.org> 37-alt5
- added -flto-partition=none to CFLAGS to fix build with gcc-10
  upstream bug https://github.com/rhboot/efivar/issues/156

* Wed Aug 12 2020 Nikolai Kostrigin <nickel@altlinux.org> 37-alt4
- fix bug rendering "efibootmgr -v" to fail to parse boot entries
  by applying upstream patches

* Tue May 12 2020 Nikolai Kostrigin <nickel@altlinux.org> 37-alt3
- remove ExclusiveArch tag to enable build on ppc64le
  + this enables pesign-111+ build

* Thu Oct 24 2019 Anton Farygin <rider@altlinux.ru> 37-alt2
- fixed build with gcc-9 by applying patches from upstream

* Mon Dec 10 2018 Anton Farygin <rider@altlinux.ru> 37-alt1
- new version

* Mon Oct 22 2018 Anton Farygin <rider@altlinux.ru> 36-alt2
- build from upstream git

* Tue Jul 31 2018 Anton Farygin <rider@altlinux.ru> 36-alt1
- new version

* Fri Apr 27 2018 Anton Farygin <rider@altlinux.ru> 35-alt1
- new version

* Mon Feb 26 2018 Anton Farygin <rider@altlinux.ru> 34-alt1
- new version

* Mon Sep 18 2017 Anton Farygin <rider@altlinux.ru> 32-alt1
- new version

* Tue Jun 20 2017 Anton Farygin <rider@altlinux.ru> 31-alt1
- first build for ALT


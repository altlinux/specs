Name: efivar
Version: 34
Release: alt1%ubt
Summary: Tools to manage UEFI variables
License: LGPLv2.1
Group: System/Kernel and hardware
Url: https://github.com/rhinstaller/efivar
Requires: %name-libs = %version-%release
ExclusiveArch: %ix86 x86_64 aarch64
BuildRequires(pre): rpm-build-ubt

BuildRequires: libpopt-devel libabigail
Source0: %name-%version.tar

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

%build
make libdir=%_libdir bindir=%_bindir CFLAGS="$RPM_OPT_FLAGS -flto" LDFLAGS="$RPM_LD_FLAGS -flto"

%install
%makeinstall

%files
%doc README.md COPYING
%_bindir/efivar
%_mandir/man1/*

%files -n lib%name-devel
%_mandir/man3/*
%_includedir/*
%_libdir/*.so
%_libdir/pkgconfig/*.pc

%files -n lib%name
%_libdir/*.so.*

%changelog
* Mon Feb 26 2018 Anton Farygin <rider@altlinux.ru> 34-alt1%ubt
- new version

* Mon Sep 18 2017 Anton Farygin <rider@altlinux.ru> 32-alt1%ubt
- new version

* Tue Jun 20 2017 Anton Farygin <rider@altlinux.ru> 31-alt1%ubt
- first build for ALT


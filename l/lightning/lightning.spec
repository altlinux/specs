%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%define soversion 2
%set_verify_elf_method strict
%add_optflags -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64

%def_with check

Name: lightning
Version: 2.2.3
Release: alt1

Summary: GNU Lightning is a library for dynamic code generation
License: LGPL-3.0+
Group: Development/Other
Url: https://www.gnu.org/software/lightning/
Vcs: http://git.savannah.gnu.org/cgit/lightning.git

Source0: %name-%version.tar
Patch0: %name-%version-alt.patch

BuildRequires: gnulib
BuildRequires: makeinfo

%description
GNU lightning is a library that generates assembly language code at run-time;
it is very fast, making it ideal for Just-In-Time compilers, and it abstracts
over the target CPU, as it exposes to the clients a standardized RISC
instruction set inspired by the MIPS and SPARC chips.

%package -n lib%name-devel
Summary: Development files for %name
Group: Development/Other
Requires: lib%name%soversion = %EVR

%description -n lib%name-devel
The %name-devel package contains development files for %name.

%package -n lib%name%soversion
Summary: A high performance JSON library written in ANSI C
Group: System/Libraries

%description -n lib%name%soversion
GNU lightning is a library that generates assembly language code at run-time;
it is very fast, making it ideal for Just-In-Time compilers, and it abstracts
over the target CPU, as it exposes to the clients a standardized RISC
instruction set inspired by the MIPS and SPARC chips.

%prep
%setup
%autopatch0 -p1

%build
%autoreconf
%configure --disable-static
%make_build

%install
%makeinstall_std

%check
%make check

%files -n lib%name%soversion
%_libdir/lib%name.so.*
%doc AUTHORS THANKS NEWS doc/*.c

%files -n lib%name-devel
%_libdir/lib%name.so
%_includedir/%name.h
%_includedir/%name/
%_pkgconfigdir/%name.pc
%_infodir/%name.info.*

%changelog
* Fri Jun 14 2024 Artem Krasovskiy <aibure@altlinux.org> 2.2.3-alt1
- Updated to 2.2.3.

* Sun Mar 07 2010 Dmitry V. Levin <ldv@altlinux.org> 1.2-alt1
- Updated to 1.2.
- Cleaned up specfile.

* Sun Sep 18 2005 Vitaly Lipatov <lav@altlinux.ru> 1.1.2-alt2
- NMU: fix spec name, update Url, fix Source path, change to tar.bz2
- add Packager

* Tue Dec 16 2003 Ott Alex <ott@altlinux.ru> 1.1.2-alt1
- New release

* Sun Nov 09 2003 Ott Alex <ott@altlinux.ru> 1.1.1-alt1
- New release

* Sun Jul 13 2003 Ott Alex <ott@altlinux.ru> 1.1-alt1
- Initial release

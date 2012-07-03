Name: libffi
Version: 3.0.10
Release: alt1
Epoch: 1

Summary: Foreign Function Interface library
License: BSD-style
Group: System/Libraries
URL: http://sourceware.org/libffi

# http://sourceware.org/libffi/%name-%version.tar.gz
Source: %name-%version.tar
# git://git.altlinux.org/gears/l/libffi.git
Patch: %name-%version-%release.patch

%{?!_without_check:%{?!_disable_check:BuildRequires: dejagnu, gcc-c++, /proc, /dev/pts}}

%description
The libffi library provides a portable, high level programming
interface to various calling conventions.  This allows a programmer
to call any function specified by a call interface description
at run time.

This package contains Foreign Function Interface shared library
which is needed to run Foreign Function Interface dynamically
linked programs

%package devel
Summary: Header files and library for Foreign Function Interface development
Group: Development/Other
Requires: libffi = %epoch:%version-%release

%description devel
The libffi library provides a portable, high level programming
interface to various calling conventions.  This allows a programmer
to call any function specified by a call interface description
at run time.

This package includes the header files and library needed for
Foreign Function Interface development.

%package -n libffi-devel-static
Summary: Static library for Foreign Function Interface development
Group: Development/Other
Requires: libffi-devel = %epoch:%version-%release

%description -n libffi-devel-static
The libffi library provides a portable, high level programming
interface to various calling conventions.  This allows a programmer
to call any function specified by a call interface description
at run time.

This package includes the static library needed for
Foreign Function Interface development.

%prep
%setup
%patch -p1

%build
%autoreconf
%configure
%make_build

%check
[ -w /dev/ptmx -a -f /proc/self/maps ] || exit
make -k check

%install
%makeinstall_std

%files
%_libdir/*.so.*
%doc README

%files devel
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/*
%_man3dir/*
%_infodir/*

%files devel-static
%_libdir/*.a

%changelog
* Mon Sep 19 2011 Alexey Tourbin <at@altlinux.ru> 1:3.0.10-alt1
- Updated to 3.0.10.

* Wed Mar 09 2011 Dmitry V. Levin <ldv@altlinux.org> 1:3.0.9-alt5
- Rebuilt for debuginfo.

* Thu Oct 28 2010 Kirill A. Shutemov <kas@altlinux.org> 1:3.0.9-alt4
- Rebuilt for soname set-versions.

* Fri Aug 20 2010 Dmitry V. Levin <ldv@altlinux.org> 1:3.0.9-alt3
- Fixed exported header files for -m32.

* Fri Aug 20 2010 Dmitry V. Levin <ldv@altlinux.org> 1:3.0.9-alt2
- Relocated header files to standard location.
- Dropped libffiX.Y provides/obsoletes.

* Sat Jul 31 2010 Kirill A. Shutemov <kas@altlinux.org> 1:3.0.9-alt1
- Initial build of standalone libffi for ALT Linux (closes: #20672)

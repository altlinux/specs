Name: liblockfile
Version: 1.16
Release: alt1

Summary: An NFS-safe locking library
License: LGPLv2+
Group: System/Libraries
URL: https://github.com/miquels/liblockfile/

# git://git.altlinux.org/gears/l/liblockfile.git
Source: %name-%version-%release.tar

%description
This package contains liblockfile - a shared library with NFS-safe
locking functions.

%package devel
Summary: The library and header files for building liblockfile-aware applications
License: LGPLv2+
Group: Development/C

%description devel
This is a development package for liblockfile.
It includes the development library, header files, and documentation.

%package -n dotlockfile
Summary: An utility to manage lockfiles
License: GPLv2+
Group: File tools

%description -n dotlockfile
This package contains dotlockfile - a liblockfile-based utility
to manage lockfiles.

%prep
%setup -n %name-%version-%release

%build
%configure --enable-shared
%make_build

%install
mkdir -p %buildroot{%_bindir,%_libdir,%_includedir,%_man1dir,%_man3dir}
install -pm644 liblockfile.so %buildroot%_libdir/liblockfile.so.1
ln -s liblockfile.so.1 %buildroot%_libdir/liblockfile.so
install -pm644 lockfile.h maillock.h %buildroot%_includedir/
install -pm755 dotlockfile %buildroot%_bindir/
install -pm644 *.1 %buildroot%_man1dir/
install -pm644 *.3 %buildroot%_man3dir/

%define _unpackaged_files_terminate_build 1

%files
%doc COPYRIGHT README
%_libdir/liblockfile.so.*

%files devel
%_libdir/liblockfile.so
%_includedir/lockfile.h
%_includedir/maillock.h
%_man3dir/lockfile_create.3*
%_man3dir/maillock.3*

%files -n dotlockfile
%_bindir/dotlockfile
%_man1dir/dotlockfile.1*

%changelog
* Fri Aug 09 2019 Dmitry V. Levin <ldv@altlinux.org> 1.16-alt1
- 1.09 -> 1.16.
- Rewritten spec file.
- Moved dotlockfile to a separate subpackage.

* Thu Sep 11 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.09-alt1
- Version 1.09

* Sun Apr 14 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 1.08-alt3.qa1
- NMU: rebuilt for debuginfo.

* Thu Oct 21 2010 Vladimir V. Kamarzin <vvk@altlinux.org> 1.08-alt3
- Rebuild for soname-set versions

* Wed Dec 03 2008 Vladimir V. Kamarzin <vvk@altlinux.org> 1.08-alt2
- Remove obsolete %%post_ldconfig/%%postun_ldconfig calls

* Wed Oct 29 2008 Vladimir V. Kamarzin <vvk@altlinux.org> 1.08-alt1
- Initial build for ALT Linux (spec from PLD)

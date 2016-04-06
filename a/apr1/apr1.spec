# hey Emacs, its -*- mode: rpm-spec; coding: cyrillic-cp1251; -*-

# %%branch_switch set %%branch_release use
#%%define branch_switch Mxx

%define aprver 1
%define aprdir %_builddir/%name-%version
%add_findreq_skiplist %_datadir/apr-1/build/config.guess

Name: apr%aprver
Version: 1.5.2
Release: %branch_release alt1

Summary: Apache Portable Runtime
Group: System/Libraries
License: %asl
Url: http://apr.apache.org/
Packager: Boris Savelev <boris@altlinux.org>

#Source: http://archive.apache.org/dist/apr/apr-%version.tar.gz
Source: %name-%version.tar

BuildRequires(pre): rpm-macros-branch
BuildPreReq: rpm-build-licenses

%def_disable static
%{?_enable_static:BuildPreReq: glibc-devel-static}

# Automatically added by buildreq on Wed Sep 03 2008
BuildRequires: gcc-c++ glibc-devel-static libuuid-devel python-modules

%package -n lib%name
Summary: Apache Portable Runtime shared library
Group: System/Libraries

%package -n lib%name-devel
Summary: Apache Portable Runtime development files
Group: Development/C
Requires: lib%name = %version-%release
Conflicts: libapr-devel

%if_enabled static
%package -n lib%name-devel-static
Summary: Apache Portable Runtime static library
Group: Development/C
Requires: lib%name-devel = %version-%release
%endif

%description
The mission of the Apache Portable Runtime (APR) is to provide a free
library of C data structures and routines, forming a system portability
layer to as many operating systems as possible, including Unices,
MS Win32, BeOS and OS/2.

%description -n lib%name
The mission of the Apache Portable Runtime (APR) is to provide a free
library of C data structures and routines, forming a system portability
layer to as many operating systems as possible, including Unices,
MS Win32, BeOS and OS/2.
This package contains APR shared library.

%description -n lib%name-devel
The mission of the Apache Portable Runtime (APR) is to provide a free
library of C data structures and routines, forming a system portability
layer to as many operating systems as possible, including Unices,
MS Win32, BeOS and OS/2.
This package contains APR development files.

%if_enabled static
%description -n lib%name-devel-static
The mission of the Apache Portable Runtime (APR) is to provide a free
library of C data structures and routines, forming a system portability
layer to as many operating systems as possible, including Unices,
MS Win32, BeOS and OS/2.
This package contains APR static library.
%endif

%prep
%setup

%build
LIBTOOL_M4=%_datadir/libtool/aclocal/libtool.m4 ./buildconf
%configure \
	--prefix=%prefix \
	--includedir=%_includedir/apr-%aprver \
	--with-installbuilddir=%_datadir/apr-%aprver/build \
	--enable-threads \
	--disable-epoll_create1 \
	--disable-dup3 \
	--disable-accept4 \
	--disable-sock_cloexec \
	--with-devrandom \
	%{subst_enable static}
%make_build

%install
%makeinstall_std
install -m755 build/PrintPath %buildroot%_datadir/apr-%aprver/build/
find %buildroot%_bindir -type f -print0 |
	xargs -r0 grep -FZl "%aprdir" -- |
	xargs -r0 sed -i "s,%aprdir,%_datadir/apr-%aprver," --
find %buildroot%_datadir -type f -print0 |
	xargs -r0 grep -FZl "%aprdir" -- |
	xargs -r0 sed -i "s,%aprdir\(/build\)\?,%_datadir/apr-%aprver/build," --

%check
%make_build check

%files -n lib%name
%doc CHANGES LICENSE NOTICE
%_libdir/lib*.so.*

%files -n lib%name-devel
%doc docs/APRDesign.html docs/canonical_filenames.html
%doc docs/incomplete_types docs/non_apr_programs
%_bindir/*-config
%_libdir/lib*.so
%_libdir/*.exp
%_pkgconfigdir/apr-%aprver.pc
%_datadir/apr-%aprver
%_includedir/*

%if_enabled static
%files -n lib%name-devel-static
%_libdir/lib*.a
%endif

%changelog
* Wed Mar 09 2016 Sergey Alembekov <rt@altlinux.ru> 1.5.2-alt1
- New version 1.5.2

* Fri Nov 16 2012 Aleksey Avdeev <solo@altlinux.ru> 1.4.6-alt1
- New version (1.4.6)
- Security fixes (CVE-2011-1928, oCERT-2011-003)

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.4.4-alt1.1
- Rebuild with Python-2.7

* Fri May 13 2011 Aleksey Avdeev <solo@altlinux.ru> 1.4.4-alt1
- New version (1.4.4)
- Security fixes (CVE-2011-0419)

* Sun Apr 24 2011 Dmitry V. Levin <ldv@altlinux.org> 1.4.2-alt3
- Rebuilt for debuginfo.

* Mon Nov 01 2010 Aleksey Avdeev <solo@altlinux.ru> 1.4.2-alt2
- Rebuilt for soname set-versions.

* Thu Oct 14 2010 Aleksey Avdeev <solo@altlinux.ru> 1.4.2-alt1
- New version (1.4.2)

* Fri Nov 13 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.8-alt1.1

* Fri Aug 14 2009 Aleksey Avdeev <solo@altlinux.ru> 1.3.8-alt1
- New version (1.3.8)
- Security fixes (CVE-2009-2412)
- Add use %%make check (thanks to Graham Leggett)

* Thu Jul 30 2009 Aleksey Avdeev <solo@altlinux.ru> 1.3.7-alt2.1
- NMU
- Fix apr/include/apr_pools.h (Closes: #20916)

* Mon Jul 27 2009 Boris Savelev <boris@altlinux.org> 1.3.7-alt2
- add 2 patches from Debian
- omit new syscalls (closes: #20874)

* Mon Jul 27 2009 Boris Savelev <boris@altlinux.org> 1.3.7-alt1
- new version (1.3.7)

* Wed Jul 22 2009 Boris Savelev <boris@altlinux.org> 1.3.6-alt1
- new version (1.3.6)
- add 2 patch from Sergey Bolshakov

* Fri Jun 26 2009 Boris Savelev <boris@altlinux.org> 1.3.5-alt1
- new version (1.3.5)

* Fri May 22 2009 Boris Savelev <boris@altlinux.org> 1.3.3-alt2
- fix build with new toolchain
- remove post
- add patches from Debian

* Wed Sep 03 2008 Boris Savelev <boris@altlinux.org> 1.3.3-alt1
- new version

* Wed Apr 02 2008 Grigory Batalov <bga@altlinux.ru> 1.2.12-alt2
- Avoid config.guess dependency checking.

* Thu Mar 06 2008 Grigory Batalov <bga@altlinux.ru> 1.2.12-alt1
- New upstream release.
- No need for autoconf_2.5 any more.
- New maintainer.

* Thu Dec 27 2007 Sviatoslav Sviridov <svd@altlinux.ru> 1.2.8-alt2
- Using autoconf version 2.5 (temporary workaround to get it working)

* Thu Jun 14 2007 Aleksey Avdeev <solo@altlinux.ru> 1.2.8-alt1.2
- NMU:
  + adding apr-1.2.8-asf-apr_table_clone.patch: add table copy (clone)
    function for apr, for CVE-2007-1862 fix (see
    <http://issues.apache.org/bugzilla/show_bug.cgi?id=41551> and
    <http://issues.apache.org/bugzilla/attachment.cgi?id=20150>

* Fri Feb 09 2007 Aleksey Avdeev <solo@altlinux.ru> 1.2.8-alt1.1
- NMU:
  + included PrintPath file in libapr1-devel package

* Tue Dec 05 2006 Sviatoslav Sviridov <svd@altlinux.ru> 1.2.8-alt1
- Updated to 1.2.8
- Updated alt-linkage patch (rediffed, installing build/get-version.sh)

* Thu Feb 02 2006 ALT QA Team Robot <qa-robot@altlinux.org> 1.2.2-alt1.1
- Rebuilt for new pkg-config dependencies.

* Sun Jan 22 2006 Sviatoslav Sviridov <svd@altlinux.ru> 1.2.2-alt1
- Switched to apr1 branch
- Updated alt-linkage patch
- Included apr-1.pc file in libapr1-devel package
- Added patch for apr-1.pc
- Updated BuildRequires (added python-base python-modules-encodings due
  to usage of buildconf.py script)

* Mon Oct 17 2005 Sviatoslav Sviridov <svd@altlinux.ru> 1:0.9.7-alt1
- Updated to 0.9.7

* Mon May 30 2005 Sviatoslav Sviridov <svd@altlinux.ru> 1:0.9.6-alt1
- Updated to 0.9.6

* Mon Aug 16 2004 Dmitry V. Levin <ldv@altlinux.org> 1:0.9.5-alt0.4
- Updated to version from apache 2.0.50 tarball.
- Fixed library linkage.
- Renamed source package.
- Package libaprutil separately.
- Do not build static library by default.

* Thu Feb 12 2004 Sviatoslav Sviridov <svd@altlinux.ru> 1:0.9.5-alt0.3
- used workaround for build with libexpat without .la files
- updated BuildRequires
- rebuild with libdb4.2

* Sun Nov 30 2003 Sviatoslav Sviridov <svd@altlinux.ru> 1:0.9.5-alt0.2
- removed *.la files

* Wed Nov 19 2003 Sviatoslav Sviridov <svd@altlinux.ru> 1:0.9.5-alt0.1
- new version: 0.9.5 (from apache 2.0.48 tarball)

* Fri Aug 22 2003 Sviatoslav Sviridov <svd@altlinux.ru> 1:0.9.4-alt1
- new version: 0.9.4 (from apache 2.0.47 tarball)

* Tue Apr 15 2003 Sviatoslav Sviridov <svd@altlinux.ru> 1:0.9.3-alt1
- new version: 0.9.3

* Tue Mar 25 2003 Sviatoslav Sviridov <svd@altlinux.ru> 1:0.9.2-alt0.1
- first build for ALT Linux

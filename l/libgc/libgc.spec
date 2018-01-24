Name: libgc
Version: 7.6.0
Release: alt2

Summary: The Boehm-Demers-Weiser conservative garbage collector

License: MIT and GPLv2+
Group: System/Libraries
Url: http://www.hboehm.info/gc/

# Source-url: http://www.hboehm.info/gc/gc_source/gc-%version.tar.gz
Source: gc-%version.tar
Patch: gc-aarch64.patch
# https://github.com/ivmai/bdwgc/issues/87
Patch1: libgc-7.6.0-upstream-c++.patch

BuildRequires: gcc-c++
BuildRequires: libatomic_ops-devel-static

%{?!_without_check:%{?!_disable_check:BuildRequires: /proc}}

%def_disable static

%description
The Boehm-Demers-Weiser conservative garbage collector can be used as a
garbage collecting replacement for C malloc or C++ new.  Alternatively,
it may be used as a leak detector for C or C++ programs, though that is
not its primary goal.

%package devel
Summary: Development files for libgc
Group: Development/C
Requires: %name = %version-%release

%description devel
The Boehm-Demers-Weiser conservative garbage collector can be used as a
garbage collecting replacement for C malloc or C++ new.  Alternatively,
it may be used as a leak detector for C or C++ programs, though that is
not its primary goal.

This package contains development files for libgc.

%package devel-static
Summary: Static libgc library
Group: Development/C
Requires: %name-devel = %version-%release

%description devel-static
This package contains static libgc library.

%prep
%setup -n gc-%version
#patch -p1
%patch1 -p1

%build
# see bugzilla.redhat.com/689877
export CPPFLAGS='-DUSE_GET_STACKBASE_FOR_MAIN=1 -DUSE_LIBC_PRIVATES=1'
%configure \
	--enable-cplusplus \
	--enable-large-config \
	--enable-threads=posix \
	--with-libatomic-ops=yes \
	--enable-shared=yes \
	%{subst_enable static} \
%ifarch %{ix86}
	--enable-parallel-mark \
%endif
	#
sed -ri 's/^(hardcode_libdir_flag_spec|runpath_var)=.*/\1=/' libtool
%make_build

%install
%makeinstall_std

mkdir -p %buildroot%_man3dir/
install -pm644 doc/gc.man %buildroot%_man3dir/gc.3

%check
export LD_LIBRARY_PATH=%buildroot%_libdir:$PWD/.libs
%make_build -k check

%files
%_libdir/*.so.*
%doc ChangeLog README.QUICK README.md doc/README.cords
%doc doc/README.environment

%files devel
%_libdir/*.so
%_includedir/gc/
%_includedir/gc.h
%_includedir/gc_cpp.h
%_pkgconfigdir/bdw-gc.pc
%_man3dir/*
# exclude docs from the wrong place
%exclude %_datadir/gc/
%doc doc/README.linux doc/README.arm.cross doc/README.autoconf doc/README.cmake
%doc doc/*.html

%if_enabled static
%files devel-static
%_libdir/*.a
%endif

%changelog
* Wed Jan 24 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 7.6.0-alt2
- Fixed build with new toolchain.

* Wed Aug 24 2016 Vitaly Lipatov <lav@altlinux.ru> 7.6.0-alt1
- new version 7.6.0 (with rpmrb script)

* Tue Jul 26 2016 Vitaly Lipatov <lav@altlinux.ru> 7.4.4-alt1
- new version 7.4.4 (with rpmrb script)

* Wed Feb 24 2016 Vitaly Lipatov <lav@altlinux.ru> 7.4.2-alt1
- new version (7.4.2) with rpmgs script
- build with external libatomic-ops

* Fri Sep 18 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 7.2d-alt3
- Added aarch64 architecture support.

* Mon Sep 03 2012 Dmitry V. Levin <ldv@altlinux.org> 7.2d-alt2
- Built with USE_LIBC_PRIVATES again to make GC_linux_main_stack_base()
  work without /proc mounted.

* Sat Sep 01 2012 Dmitry V. Levin <ldv@altlinux.org> 7.2d-alt1
- Updated to 7.2d.

* Sat Feb 04 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 7.1-alt3.1
- Removed bad RPATH

* Fri Mar 25 2011 Alexey Tourbin <at@altlinux.ru> 7.1-alt3
- rebuilt for debuginfo

* Thu Nov 25 2010 Igor Vlasenko <viy@altlinux.ru> 7.1-alt2.qa1
- rebuild using girar-nmu to require/provide setversion
  by request of mithraen@

* Tue Jul 14 2009 Vitaly Lipatov <lav@altlinux.ru> 7.1-alt2
- fix build

* Sat Jan 10 2009 Vitaly Lipatov <lav@altlinux.ru> 7.1-alt1
- new version 7.1 (with rpmrb script)

* Sat Jan 12 2008 Vitaly Lipatov <lav@altlinux.ru> 7.0-alt3
- add ChangeLog, move development docs to -devel package
- NOTE: 7.0 is not binary compatible with 6.0, soname is not changed :(
- move to System/Libraries rpm group

* Mon Jan 07 2008 Vitaly Lipatov <lav@altlinux.ru> 7.0-alt2
- fix includedir place (thanks to kas@)
- cleanup spec

* Sun Jan 06 2008 Vitaly Lipatov <lav@altlinux.ru> 7.0-alt1
- new version 7.0
- add Debian patch for fix ARM build
- remove glibc-devel-static from buildreqs

* Mon Jun 05 2006 Vitaly Lipatov <lav@altlinux.ru> 6.7-alt0.1
- new version 6.7 (with rpmrb script)
- apply missed patch against unresolved symbols :)

* Thu Feb 09 2006 Anton Farygin <rider@altlinux.ru> 6.6-alt2
- NMU: fixed unresolved symbols on x86_64

* Sun Nov 13 2005 Vitaly Lipatov <lav@altlinux.ru> 6.6-alt1
- new version

* Sat Mar 19 2005 Vitaly Lipatov <lav@altlinux.ru> 6.4-alt2
- add USE_LIBC_PRIVATES=1 (fix bug #6282)

* Sun Jan 30 2005 Vitaly Lipatov <lav@altlinux.ru> 6.4-alt1
- new version

* Tue Oct 19 2004 Vitaly Lipatov <lav@altlinux.ru> 6.3-alt1
- new version
- enable C++ support
- cleanup spec

* Sat Dec 13 2003 Ott Alex <ott@altlinux.ru> 6.2-alt2
- Remove .la files

* Sat Jun 28 2003 Alex Ott <ott@altlinux.ru> 6.2-alt1
- New version
- Split into static devel

* Sat Feb 08 2003 Ott Alex <ott@altlinux.ru> 6.1-alt3
- Fixing spec

* Sun Sep 15 2002 Ott Alex <ott@altlinux.ru> 6.1-alt1
- Initial build


Name: libgc
Version: 7.1
Release: alt3.1

Summary: Boehm garbage collector
Summary(ru_RU.KOI8-R): Сборщик мусора Boehm

License: See README.QUICK for Copyright notes
Group: System/Libraries
Url: http://www.hpl.hp.com/personal/Hans_Boehm/gc/

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: %url/gc_source/gc-%version.tar.bz2
Patch: %name-7.0-fixarm.patch

BuildRequires: gcc-c++

%description
The Boehm-Demers-Weiser conservative garbage collector can be used as a
garbage collecting replacement for C malloc or C++ new. Alternatively,
it may be used as a leak detector for C or C++ programs, though that is
not its primary goal.

%description -l ru_RU.KOI8-R
Консервативный сборщик мусора Boehm-Demers-Weiser, который может быть
использован как замена C malloc или C++ new, только со сборкой мусора.
Также он может быть использован как анализатор утечек памяти
для программ на C или C++, хотя это не основное его предназначение.

%package devel
Summary: Header files for libgc
Summary(ru_RU.KOI8-R): Заголовочные файлы для libgc
Group: Development/C
Requires: %name = %version-%release

%description devel
This package contain header files for Boehm garbage collector.

%description -l ru_RU.KOI8-R
Пакет содержит заголовочные файлы для сборщика мусора Boehm.

%package devel-static
Summary: Static library files libgc
Summary(ru_RU.KOI8-R): Статические библиотеки libgc
Group: Development/C
Requires: %name = %version-%release

%description devel-static
This package contain static libraries Boehm garbage collector.

%description -l ru_RU.KOI8-R
Пакет содержит статические библиотеки сборщика мусора Boehm.

%prep
%setup -q -n gc-%version
%patch

%build
%add_optflags -DUSE_LIBC_PRIVATES=1
%configure  \
	--enable-threads=pthreads \
	 --enable-shared=yes \
	 --enable-cplusplus \
	 --enable-static=yes

sed -ri 's/^(hardcode_libdir_flag_spec|runpath_var)=.*/\1=/' libtool
%make_build

%install
%makeinstall_std

mkdir -p %buildroot%_man3dir/
install -m 644 doc/gc.man %buildroot%_man3dir/gc.3

# remove docs from wrong place
rm -rf %buildroot%_datadir/gc

%files
%doc ChangeLog
%_libdir/libcord.so.*
%_libdir/libgc.so.*
%_libdir/libgccpp.so.*

%files devel
%doc doc/README* doc/*.html README.QUICK doc/barrett_diagram
%_libdir/*.so
%_includedir/gc/
%_includedir/gc.h
%_includedir/gc_cpp.h
%_man3dir/*
%_pkgconfigdir/bdw-gc.pc

%files devel-static
%_libdir/*.a

%changelog
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


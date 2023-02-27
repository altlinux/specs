# library libjvm.so not found
%set_findreq_skiplist %_libdir/swipl-*/lib/*/libjpl.so
%def_with test

Summary: Prolog interpreter and compiler
Name: swi-prolog
Version: 8.2.1
Release: alt2
License: LGPLv2+
Group: Development/Other
Requires: %name-nox
Requires: %name-xpce
Source44: import.info
# pl is not perl
AutoReq: yes,noperl
AutoProv: yes,noperl
Url: http://www.swi-prolog.org
Source0: http://www.swi-prolog.org/download/stable/src/swipl-%version.tar.gz

# Automatically added by buildreq on Sun Oct 04 2020
# optimized out: ca-trust cmake-modules fontconfig fontconfig-devel glibc-kernheaders-generic glibc-kernheaders-x86 java java-headless javazi libICE-devel libSM-devel libX11-devel libXau-devel libXrender-devel libcrypt-devel libfreetype-devel libsasl2-3 libstdc++-devel libtinfo-devel libunixODBC-devel-compat libxcb-devel pkg-config python2-base sh4 xorg-proto-devel
BuildRequires: cmake flex gcc-c++ git-core java-devel libXext-devel libXft-devel libXinerama-devel libXpm-devel libXt-devel libarchive-devel libdb6-devel libedit-devel libgmp-devel libjpeg-devel libncurses-devel libreadline-devel libssl-devel libunixODBC-devel libuuid-devel zlib-devel bzip2-devel libpng-devel libpcre-devel libbrotli-devel libexpat-devel

%if_with test
BuildRequires: ctest
%endif

%description
Edinburgh-style Prolog compiler including modules, autoload, libraries,
Garbage-collector, stack-expandor, C-interface, GNU-readline and GNU-Emacs
interface, very fast compiler.

%package nox
Group: Development/Other
Summary: SWI-Prolog without GUI components
# pl is not perl
AutoReq: yes,noperl
AutoProv: yes,noperl

%description nox
This package provide SWI-Prolog and several libraries, but without
GUI components.

%package x
Group: Development/Other
Summary: %name native GUI library
Requires: %name-nox = %version-%release
Provides: %name-xpce
# pl is not perl
AutoReq: yes,noperl
AutoProv: yes,noperl

%description x
XPCE is a toolkit for developing graphical applications in Prolog and
other interactive and dynamically typed languages.

%package java
Group: Development/Java
Summary: Java interface for %name
Requires: %name-nox = %version-%release
Provides: %name-jpl
# pl is not perl
AutoReq: yes,noperl
AutoProv: yes,noperl

%description java
JPL is a dynamic, bi-directional interface between %name and Java
runtimes. It offers two APIs: Java API (Java-calls-Prolog) and Prolog
API (Prolog-calls-Java).

%package odbc
Group: Development/Databases
Summary: ODBC interface for %name
Requires: %name-nox = %version-%release
# pl is not perl
AutoReq: yes,noperl
AutoProv: yes,noperl

%description odbc
ODBC interface for SWI-Prolog to interact with database systems.

%package doc
Group: Documentation
Summary: Documentation for %name
Requires: %name-nox = %version-%release
AutoReqProv: no

%description doc
Documentation for SWI-Prolog.

%package cmake
Group: Development/Other
Summary: CMake files for SWI Prolog

%description cmake
CMake files for SWI Prolog

%prep
%setup -n swipl-%version
sed -i '/set(SWIPL_INSTALL_PREFIX[ 	]*lib/s/ lib/ %_lib/' CMakeLists.txt

%build
%cmake -DSWIPL_VERSIONED_DIR=yes -DSWIPL_INSTALL_IN_SHARE=yes \
    -G'Unix Makefiles'
%cmake_build -t libswipl
export LD_LIBRARY_PATH=`pwd`/%_cmake__builddir/src
%cmake_build

# XXX this gone while switching to cmake
cc -g -pthread packages/xpce/src/unx/client.c -o %_cmake__builddir/xpce-client

%install
# TODO verify against swipl.so
%add_verify_elf_skiplist %_libdir/swipl-%version/*
%cmakeinstall_std
# XXX
install -D %_cmake__builddir/xpce-client %buildroot%_bindir/xpce-client
install -D packages/xpce/man/xpce-client.1 %buildroot%_man1dir/xpce-client.1
test %_lib != lib && mv %buildroot%_prefix/lib/cmake %buildroot%_libdir/
ln -rs %buildroot%_libdir/swipl-%version/lib/*/lib* %buildroot%_libdir/

%if_with test
%check
cd %_cmake__builddir
LC_ALL=ru_RU.UTF-8 LD_LIBRARY_PATH=`pwd`/src ctest -j`nproc`
%endif

%files

%files cmake
%_libdir/cmake/swipl

%files nox
%doc README.md LICENSE VERSION
%_bindir/swipl*
%_libdir/swipl-%version
%_libdir/lib*.so*
%_datadir/pkgconfig/swipl.pc
%exclude %_datadir/swipl-%version/doc
%exclude %_libdir/swipl-%version/lib/*/libjpl.so
%exclude %_libdir/swipl-%version/lib/jpl.jar
%exclude %_libdir/swipl-%version/library/jpl.pl
%exclude %_libdir/swipl-%version/xpce/*
%exclude %_libdir/swipl-%version/lib/*/odbc4pl.so
%exclude %_libdir/swipl-%version/library/odbc.pl

%files x
%_mandir/*/xpce*
%doc %_datadir/swipl-%version/doc/Manual/*xpce.html
%_bindir/xpce*
%_libdir/swipl-%version/xpce/*

%files java
%doc packages/jpl/*.md packages/jpl/*.doc packages/jpl/docs
%doc %_datadir/swipl-%version/doc/packages/examples/jpl
%doc %_datadir/swipl-%version/doc/packages/jpl.html
%_libdir/swipl-%version/lib/*/libjpl.so
%_libdir/swipl-%version/lib/jpl.jar
%_libdir/swipl-%version/library/jpl.pl

%files odbc
%doc %_datadir/swipl-%version/doc/packages/odbc.html
%_libdir/swipl-%version/lib/*/odbc4pl.so
%_libdir/swipl-%version/library/odbc.pl

%files doc
%_mandir/*/swipl*
%dir %_datadir/swipl-%version/doc
%doc %_datadir/swipl-%version/doc/Manual
%exclude %_datadir/swipl-%version/doc/Manual/*xpce.html
%doc %_datadir/swipl-%version/doc/packages
%exclude %_datadir/swipl-%version/doc/packages/examples/jpl
%exclude %_datadir/swipl-%version/doc/packages/jpl.html
%exclude %_datadir/swipl-%version/doc/packages/odbc.html

%changelog
* Mon Feb 27 2023 Igor Vlasenko <viy@altlinux.org> 8.2.1-alt2
- NMU: fixed build

* Tue Jun 01 2021 Arseny Maslennikov <arseny@altlinux.org> 8.2.1-alt1.1
- NMU: spec: adapted to new cmake macros.

* Sun Oct 25 2020 Fr. Br. George <george@altlinux.ru> 8.2.1-alt1
- Major version up

* Mon Feb 17 2020 Igor Vlasenko <viy@altlinux.ru> 7.4.2-alt2_5
- update by mgaimport

* Wed Aug 29 2018 Grigory Ustinov <grenka@altlinux.org> 7.4.2-alt2_3.1
- NMU: Rebuild with new openssl 1.1.0.

* Sat Jul 14 2018 Igor Vlasenko <viy@altlinux.ru> 7.4.2-alt2_3
- update by mgaimport

* Thu Mar 15 2018 Igor Vlasenko <viy@altlinux.ru> 7.4.2-alt2_2
- added Url:

* Sun Mar 04 2018 Igor Vlasenko <viy@altlinux.ru> 7.4.2-alt1_2
- new version; picked from orphaned as import

* Thu Aug 30 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.6.15-alt1.qa2
- Rebuilt with gmp 5.0.5

* Thu Feb 04 2010 Repocop Q. A. Robot <repocop@altlinux.org> 5.6.15-alt1.qa1
- NMU (by repocop): the following fixes applied:
  * post_ldconfig for swi-prolog
  * postun_ldconfig for swi-prolog
  * postclean-05-filetriggers for spec file

* Sun Jul 02 2006 Alexey Tourbin <at@altlinux.ru> 5.6.15-alt1
- 5.0.10 -> 5.6.15
- configured --enable-shared
- installed swi-prolog libraries under %%plbase
- built and packaged manual.pdf

* Fri Dec 30 2005 ALT QA Team Robot <qa-robot@altlinux.org> 5.0.10-alt1.1
- Rebuilt with libreadline.so.5.

* Fri Jan 24 2003 Vitaly Lugovsky <vsl@altlinux.ru> 5.0.10-alt1
- 5.0.10

* Tue Nov 27 2001 Stanislav Ievlev <inger@altlinux.ru> 4.0.10-alt1
- 4.0.10

* Tue Jan 16 2001 AEN <aen@logic.ru>
- RE adaptations

* Fri Oct 27 2000 Pixel <pixel@mandrakesoft.com> 3.4.1-1mdk
- new version

* Wed Aug 23 2000 Pixel <pixel@mandrakesoft.com> 3.3.6-6mdk
- add packager field

* Mon Aug 07 2000 Frederic Lepied <flepied@mandrakesoft.com> 3.3.6-5mdk
- automatically added BuildRequires

* Wed Jul 19 2000 Pixel <pixel@mandrakesoft.com> 3.3.6-4mdk
- BM

* Tue Jul 11 2000 Pixel <pixel@mandrakesoft.com> 3.3.6-3mdk
- and pixel changed a few other things to stef's changes

* Mon Jul 10 2000 Stefan van der Eijk <s.vandereijk@chello.nl> 3.3.6-2mdk
- makeinstall macro
- macroszifications

* Wed Jun  7 2000 Pixel <pixel@mandrakesoft.com> 3.3.6-1mdk
- change name to swi-prolog
- new version
- fix licence
- fix buildroot
- much cleanup

* Wed Jun  7 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 3.2.9-2mdk
- first package for Mandrake

* Thu Jul 29 1999 David Kuester <kuestler@zeta.org.au>
- New source build version 3.2.9
* Tue Jun 22 1999 David Kuester <kuestler@zeta.org.au>
- New source build version 3.2.8
- Split the single patch in two (emacs) and (powerpc)
* Sun Nov 15 1998 Justin Cormack <jpc1@doc.ic.ac.uk>
- added changelog
- various tidying up things
- adjusted so will build on all architectures
- previous packagers:
- David Kuestler <kuestler@zeta.org.au>
- Kjetil Wiekhorst Jørgensen <jorgens@zarhan.pvv.org>
- Adam P. Jenkins <ajenkins@cs.umass.

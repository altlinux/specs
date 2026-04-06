%define        _unpackaged_files_terminate_build 1
%def_disable   check
%define        nomen swipl

Name:          swi-prolog
Version:       10.1.5
Release:       alt1
Summary:       Prolog interpreter and compiler
License:       BSD-2-Clause
Group:         Development/Other
Url:           http://www.swi-prolog.org
Vcs:           https://github.com/SWI-Prolog/swipl-devel.git

Source:        %name-%version.tar

BuildRequires(pre): rpm-build-cmake
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: libgmp-devel
BuildRequires: libncurses-devel
BuildRequires: libreadline-devel
BuildRequires: libssl-devel
BuildRequires: zlib-devel
%if_enabled    check
BuildRequires: ctest
%endif

%add_findreq_skiplist %_libexecdir/swipl/**/*
%add_findprov_skiplist %_libexecdir/swipl/**/*

%description
Edinburgh-style Prolog compiler including modules, autoload, libraries,
Garbage-collector, stack-expandor, C-interface, GNU-readline and GNU-Emacs
interface, very fast compiler.


%package       -n lib%nomen
Group:         Development/Other
Summary:       SWI-Prolog libraries

%description   -n lib%nomen
SWI-Prolog libraries.

Edinburgh-style Prolog compiler including modules, autoload, libraries,
Garbage-collector, stack-expandor, C-interface, GNU-readline and GNU-Emacs
interface, very fast compiler.


%package       -n lib%nomen-devel
Group:         Development/Other
Summary:       SWI-Prolog libraries development module

Requires:      cmake
Requires:      gcc-c++
Requires:      libgmp-devel
Requires:      libncurses-devel
Requires:      libreadline-devel
Requires:      libssl-devel
Requires:      zlib-devel
Requires:      ctest

%description   -n lib%nomen-devel
SWI-Prolog libraries development module.

Edinburgh-style Prolog compiler including modules, autoload, libraries,
Garbage-collector, stack-expandor, C-interface, GNU-readline and GNU-Emacs
interface, very fast compiler.


%package       -n %nomen
Group:         Development/Other
Summary:       SWI-Prolog interpreter and compiler
Provides:      swi-prolog = %EVR
Obsoletes:     swi-prolog < %EVR

%description   -n %nomen
SWI-Prolog interpreter and compiler.

Edinburgh-style Prolog compiler including modules, autoload, libraries,
Garbage-collector, stack-expandor, C-interface, GNU-readline and GNU-Emacs
interface, very fast compiler.


%package       -n %nomen-stdlib
Group:         Development/Other
Summary:       SWI-Prolog standard scripts

%description   -n %nomen-stdlib
SWI-Prolog standard scripts.

Edinburgh-style Prolog compiler including modules, autoload, libraries,
Garbage-collector, stack-expandor, C-interface, GNU-readline and GNU-Emacs
interface, very fast compiler.


%prep
%setup

%ifarch loongarch64 riscv64
# try_compile with CMAKE_TRY_COMPILE_TARGET_TYPE set to STATIC_LIBARY
# does not seem to be compatible with LTO. However, currently this
# seems to break only loongarch64 and riscv64 builds
sed -i '/CMAKE_TRY_COMPILE_TARGET_TYPE.*STATIC_LIBRARY/d' cmake/*.cmake
%endif

%build
%cmake \
   -DCMAKE_BUILD_TYPE=RelWithDebInfo \
   -DCMAKE_EXECUTABLE_FORMAT=ELF \
   -DCMAKE_SKIP_BUILD_RPATH=ON \
   -DCMAKE_INSTALL_LIBDIR=lib%_libsuff \
   -DWARN_NO_DOCUMENTATION=ON \
   -DINSTALL_DOCUMENTATION=ON \
   -DSWIPL_ARCH=%_arch \
   -DSWIPL_SHARED_LIB=ON \
   -DSWIPL_VERSIONED_DIR=OFF \
   -DSWIPL_INSTALL_IN_SHARE=OFF \
   -DSWIPL_PACKAGES=OFF \
   -DSWIPL_INSTALL_PREFIX=lib/%nomen \
   -DSWIPL_INSTALL_ARCH_EXE=lib%_libsuff/%nomen/bin \
   -DSWIPL_INSTALL_ARCH_LIB=lib%_libsuff/%nomen \
   -DSWIPL_INSTALL_CMAKE_CONFIG_DIR=lib%_libsuff/cmake/swipl \
   -DSWIPL_INSTALL_PKGCONFIG=lib%_libsuff/pkgconfig \
   -DSWIPL_INSTALL_IN_LIB=ON \
   -DMULTI_THREADED=ON \
   -DBUILD_TESTING=ON \
   %nil

%cmake_build

%install
%cmake_install

%check
%ctest


%files         -n %nomen
%doc README.md LICENSE VERSION
%_bindir/%{nomen}*
%_man1dir/%{nomen}*

%files         -n %nomen-stdlib
%doc README.md LICENSE VERSION
%_libexecdir/swipl

%files         -n lib%nomen
%_libdir/lib%{nomen}.so.*

%files         -n lib%nomen-devel
%doc README.md LICENSE VERSION
%_libdir/lib%{nomen}.so
%_libdir/cmake/swipl
%_pkgconfigdir/swipl.pc


%changelog
* Mon Apr 06 2026 Pavel Skrylev <majioa@altlinux.org> 10.1.5-alt1
- ^ 9.3.25p39 -> 10.1.5

* Mon Aug 18 2025 Ivan A. Melnikov <iv@altlinux.org> 9.3.25.39-alt0.2
- NMU: avoid messing with CMAKE_TRY_COMPILE_TARGET_TYPE
  on loongarch64 and riscv64 to fix FTBFS

* Wed Jul 16 2025 Pavel Skrylev <majioa@altlinux.org> 9.3.25.39-alt0.1
- ^ 9.0.4 -> 9.3.25p39
- * rebased to plain gitflow, and repackaged
- * relicensed
- - packages disabled

* Thu May 30 2024 Michael Shigorin <mike@altlinux.org> 9.0.4-alt4
- E2K: use whatever java is there
- minor spec cleanup

* Mon Oct 23 2023 Alexey Sheplyakov <asheplyakov@altlinux.org> 9.0.4-alt3
- NMU: removed libc++-devel from build dependencies (it's impossible
  to link with two C++ runtimes). Fixes FTBFS on LoongArch.

* Mon Oct 23 2023 Denis Medvedev <nbr@altlinux.org> 9.0.4-alt2
- java reenabled

* Mon Jul 31 2023 Denis Medvedev <nbr@altlinux.org> 9.0.4-alt1
- new version

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

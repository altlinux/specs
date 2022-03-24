#set_automake_version 1.11

%define beta %nil
%def_disable static

Name: recode
Version: 3.7.12
Release: alt1

Summary: The `recode' library converts files between character sets and usages
# COPYING:              GPLv3 text
# COPYING-LIB:          LGPLv3 text
# doc/recode.info:      OFSFDL
# doc/recode.texi:      OFSFDL
# lib/error.h:              GPLv3+
# lib/strerror-override.c:  GPLv3+
# lib/vasnprintf.c:         GPLv3+
# src/ansellat1.l:      BSD
# src/lat1asci.c:       GPLv3+
# src/merged.c:         BSD
# src/recode.h:         LGPLv3+
# src/ucs.c:            LGPLv3+
## Not in any binary package
# aclocal.m4:               FSFULLR
# build-aux/bootstrap.in:   MIT or GPLv3+ (bundled gnulib-modules/bootstrap)
# build-aux/compile:        GPLv2+ with exceptions
# build-aux/config.guess:   GPLv3+ with exceptions
# build-aux/config.rpath:   FSFULLR
# build-aux/config.sub:     GPLv3+ with exceptions
# build-aux/depcomp:        GPLv2+ with exceptions
# build-aux/extract-trace:  MIT or GPLv3+ (bundled gnulib-modules/bootstrap)
# build-aux/funclib.sh:     MIT or GPLv3+ (bundled gnulib-modules/bootstrap)
# build-aux/inline-source:  MIT or GPLv3+ (bundled gnulib-modules/bootstrap)
# build-aux/install-sh:     MIT
# build-aux/ltmain.sh:      GPLv2+ with exceptions and GPLv3+ with exceptions
#                           and GPLv3+
# build-aux/mdate-sh:       GPLv2+ with exceptions
# build-aux/missing:        GPLv2+ with exceptions
# build-aux/options-parser: MIT or GPLv3+ (bundled gnulib-modules/bootstrap)
# build-aux/texinfo.tex:    GPLv3+ with exceptions
# config.rpath:         FSFULLR
# configure:            FSFUL and GPLv2+ with exceptions
# doc/Makefile.am:      GPLv3+
# doc/Makefile.in:      FSFULLR and GPLv3+
# doc/texinfo.tex:      GPLv2+ with exceptions
# INSTALL:              FSFAP
# Makefile.am:          GPLv3+
# m4/gettext.m4:        FSFULLR
# m4/gnulib-cache.m4:   GPLv3+ with exceptions
# m4/libtool.m4:        GPLv2+ with exceptions and FSFUL
# m4/mbstate_t.m4:      FSFULLR
# m4/minmax.m4:         FSFULLR
# m4/ssize_t.m4:        FSFULLR
# m4/sys_stat_h.m4:     FSFULLR
# tables.py:            GPLv3+
# tests/Makefile.am:    GPLv3+
# tests/Makefile.in:    FSFULLR and GPLv3+
# tests/Recode.pyx:     GPLv3+
License:    GPLv3+ and LGPLv3+ and BSD and OFSFDL

Group: Text tools

Url: https://github.com/rrthomas/recode/
Source: %name-%version%beta.tar.gz
Patch0: recode4python.patch
Patch1: recode-3.6-debian-boolsize.patch
Patch2: recode-3.6-alt-unicode-in-docs.patch
Patch3: recode-3.6-alt-e2k.patch
Patch5: recode-3.7.1-Rename-coliding-hash-functions.patch

Packager: Michael Shigorin <mike@altlinux.org>

Requires: lib%name = %version-%release
BuildRequires: chrpath help2man git libgpgme-devel gettext gnupg flex gcc gcc-c++ iconv

BuildRequires: python3-devel
BuildRequires: rpm-build-python3


# explicitly added texinfo for info files
BuildRequires: texinfo

Summary(ru_RU.UTF-8): Библиотека recode конвертирует файлы из разных кодировок

%description
The `recode' program is a handy front-end to the `recode' library;
it converts files between character sets and usages.

The `recode' program and library have been written by Francois Pinard.
It is an evolving package, and specifications might change in future
releases.  Option `-f' is now fairly implemented, yet not fully.

%package -n lib%name
Summary: Recode library
Group: System/Libraries

%description -n lib%name
The `recode' library converts files between character sets and usages.
The library recognises or produces nearly 150 different character sets
and is able to transliterate files between almost any pair.  When
exact transliteration are not possible, it may get rid of the
offending characters or fall back on approximations.  Most RFC 1345
character sets are supported.

%package -n lib%name-devel
Summary: Headers for developing applications with `recode' library
Group: Development/Other
Requires: lib%name = %version-%release
Provides: %name-devel = %version-%release
Obsoletes: %name-devel < 3.6-alt7

%description -n lib%name-devel
This package provides the necessary development libraries and include
files to allow you to develop applications using the `recode' libraries.

%if_enabled static
%package -n lib%name-devel-static
Summary: Static library for developing applications with `recode' library
Group: Development/Other
Requires: lib%name-devel = %version-%release

%description -n lib%name-devel-static
This package provides the necessary development libraries and include
files to allow you to develop applications using the `recode' libraries.
%endif

%prep
%setup -n %name-%version%beta
#patch0 -p1
#patch1 -p1
#patch2 -p2
%ifarch %e2k
#patch3 -p1
%endif
#patch5 -p1

%build
#rm acinclude.m4 m4/libtool.m4 m4/flex.m4
#sed -i 's/ad_AC_PROG_FLEX/AC_PROG_LEX/' configure.in
%autoreconf -fi
sed -i 's/--no-verify//' configure
#configure %{subst_enable static}
%configure \
    --without-dmalloc \
    --disable-gcc-warnings \
    --enable-largefile \
    --enable-nls \
    --disable-rpath \
    --enable-shared \
    --disable-static
%make_build

%install
%makeinstall
%find_lang %name
chrpath -d %buildroot%_bindir/%name

%files -f %name.lang
%_bindir/*
%_infodir/*
%_man1dir/*
%doc ABOUT-NLS AUTHORS COPYING COPYING-LIB ChangeLog INSTALL THANKS TODO

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so

%if_enabled static
%files -n lib%name-devel-static
%_libdir/*.a
%endif

# TODO:
# - keep an eye on 3.7 (now in beta) and eventually 4.0 // if upstream's there
# - configure.in:18: error: automatic de-ANSI-fication support has been removed

%changelog
* Fri Mar 25 2022 Ilya Mashkin <oddity@altlinux.ru> 3.7.12-alt1
- 3.7.12

* Sun Feb 13 2022 Ilya Mashkin <oddity@altlinux.ru> 3.7.11-alt1
- 3.7.11
- Update url

* Sat Jan 08 2022 Michael Shigorin <mike@altlinux.org> 3.7.9-alt2
- E2K: dropped patch (unneeded for 3.7)

* Wed Sep 08 2021 Ilya Mashkin <oddity@altlinux.ru> 3.7.9-alt1
- 3.7.9
- Add BR: python3
- Skip patches
- Copy list of licenses from FC

* Thu May 27 2021 Michael Shigorin <mike@altlinux.org> 3.6-alt13
- re-added lcc build fix by sem@ (3.6-alt11.1.1.E2K.1)
- converted spec to utf-8

* Tue Mar 09 2021 Ivan A. Melnikov <iv@altlinux.org> 3.6-alt12
- Fix build

* Thu Dec 03 2015 Igor Vlasenko <viy@altlinux.ru> 3.6-alt11.1.1
- NMU: added BR: texinfo

* Thu Nov 28 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.6-alt11.1
- Fixed build

* Thu Dec 22 2011 Michael Shigorin <mike@altlinux.org> 3.6-alt11
- drop vintage libtool (closes: #26740); thx ldv@

* Wed Dec 21 2011 Michael Shigorin <mike@altlinux.org> 3.6-alt10
- drop RPATH

* Fri Mar 04 2011 Alexey Tourbin <at@altlinux.ru> 3.6-alt9.2
- rebuilt for debuginfo

* Sun Nov 14 2010 Denis Smirnov <mithraen@altlinux.ru> 3.6-alt9.1
- rebuild (with the help of girar-nmu utility)

* Thu Mar 11 2010 Michael Shigorin <mike@altlinux.org> 3.6-alt9
- fixed FTBFS (thanks rider@ for investigation and advice)
- dropped forgotten "3.7-beta2" from 3.6-alt7 changelog record

* Mon Sep 28 2009 Michael Shigorin <mike@altlinux.org> 3.6-alt8
- x86_64 build fix (following proposal by ldv@)

* Sun Dec 07 2008 Michael Shigorin <mike@altlinux.org> 3.6-alt7
- applied repocop patch
- fixed build with an adapted Debian patch
  (http://bugs.debian.org/462004)
- removed older recode4python.patch (less complete)
- libification
- spec cleanup

* Mon Apr 16 2007 ALT QA Team Robot <qa-robot@altlinux.org> 3.6-alt6.1.0
- Automated rebuild.

* Mon Apr 24 2006 Anton Farygin <rider@altlinux.ru> 3.6-alt6.1
- NMU: fixed build for x86_64

* Fri Dec  3 2004 Maxim Tyurin <mrkooll@altlinux.ru> 3.6-alt6
- Apply patch from kota@szbk.u-szeged.hu (needed for pybliographer)

* Sun Jun 20 2004 Maxim Tyurin <mrkooll@altlinux.ru> 3.6-alt5
- added find_lang

* Thu May 13 2004 Maxim Tyurin <mrkooll@altlinux.ru> 3.6-alt4
- fix postinstall script

* Thu May 06 2004 Maxim Tyurin <mrkooll@altlinux.ru> 3.6-alt3
- rebuild without *.la files

* Fri Oct 11 2002 Rider <rider@altlinux.ru> 3.6-alt2
- gcc 3.2 rebuild

* Sat Jan 05 2002 Rider <rider@altlinux.ru> 3.6-alt1
- 3.6
- spec cleanup

* Sun Feb 18 2001 AEN <aen@logic.ru>
- group names changed
* Fri Jan 05 2001 AEN <aen@logic.ru>
- rebuild for Sisyphus
* Fri Sep 29 2000 AEN <aen@logic.ru>
- build 3.5e for RE
* Thu Jun 29 2000 David Lebel <lebel@lebel.org>
- Initial public release of this SPEC file.

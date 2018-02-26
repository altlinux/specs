%define beta %nil
%def_disable static

Name: recode
Version: 3.6
Release: alt11

Summary: The `recode' library converts files between character sets and usages
License: GPL
Group: Text tools

Url: http://recode.progiciels-bpi.ca
Source: %url/archives/%name-%version%beta.tar.gz
Patch0: recode4python.patch
Patch1: recode-3.6-debian-boolsize.patch
Packager: Michael Shigorin <mike@altlinux.org>

Requires: lib%name = %version-%release
BuildRequires: chrpath

Summary(ru_RU.KOI8-R): Библиотека recode конвертирует файлы из разных кодировок

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
%patch1 -p1

%build
rm acinclude.m4 m4/libtool.m4 m4/flex.m4
sed -i 's/ad_AC_PROG_FLEX/AC_PROG_LEX/' configure.in
%autoreconf
sed -i 's/--no-verify//' configure
%configure %{subst_enable static}
%make_build

%install
%makeinstall
%find_lang %name
chrpath -d %buildroot%_bindir/%name

%files -f %name.lang
%_bindir/*
%_infodir/*
%_man1dir/*
%doc ABOUT-NLS AUTHORS BACKLOG COPYING COPYING-LIB ChangeLog INSTALL THANKS TODO

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
# - keep an eye on 3.7 (now in beta) and eventually 4.0

%changelog
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

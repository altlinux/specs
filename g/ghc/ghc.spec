# Using -fPIC make GC 50% more slow
%set_verify_elf_method textrel=relaxed

%define _configure_target %nil

%def_without hscolour
# RPM spec file for GHC
#
# Copyright [1998..2002] Manuel M. T. Chakravarty <chak@acm.org>
# Thanks to Zoltan Vorosbaranyi <vbzoli@vbzo.li> for suggestions in
# earlier versions and Pixel <pixel@mandrakesoft.com> for coding tips.
#
# This file is subject to the same free software license as GHC.

Name: ghc
Version: 7.0.1
Release: alt1
Packager: Alexander Myltsev <avm@altlinux.ru>

Summary: Glasgow Haskell Compilation system
License: BSD style w/o adv. clause
Group: Development/Haskell
Url: http://haskell.org/ghc/

Source: %name-%version.tar
Source1: %name.macros
Requires: gmp-devel
# I think that profiling libraries must be installed by default
Requires: ghc-prof
Obsoletes: happy

Requires: haskell-filetrigger

Obsoletes: haddock <= 2.0.0.0-alt1
Provides: haddock = 2.4.2

# ghc < 6.4.2 doesn't work with gcc4.
BuildPreReq: ghc >= 6.4.2

# Automatically added by buildreq on Sun Jun 04 2006
BuildRequires: docbook-dtds docbook-style-xsl ghc libelf-devel libgmp-devel libncurses-devel libedit-devel texlive-latex-base fonts-type1-cm-super-tex time xmltex xorg-cf-files xsltproc
BuildRequires: docbook-utils-print
BuildRequires: rpm-build-haskell
BuildRequires: libbfd-devel
BuildRequires: dblatex
BuildRequires: texlive-latex-base
BuildRequires: llvm-devel

%if_with hscolour
BuildRequires: ghc(hscolour)
%endif

%description
Haskell is a standard lazy functional programming language; the
current language version is Haskell 98, agreed in December 1998.

GHC is a state-of-the-art programming suite for Haskell.  Included is
an optimising compiler generating good code for a variety of
platforms, together with an interactive system for convenient, quick
development.  The distribution includes space and time profiling
facilities, a large collection of libraries, and support for various
language extensions, including concurrency, exceptions, and foreign
language interfaces (C, C++, whatever).

A wide variety of Haskell related resources (tutorials, libraries,
specifications, documentation, compilers, interpreters, references,
contact information, links to research groups) are available from the
Haskell home page at <http://www.haskell.org/>.

%package prof
Summary: Profiling libraries for GHC
Group: Development/Haskell
Requires: ghc = %version

%description prof
Profiling libraries for Glasgow Haskell Compilation System (GHC).
They should be installed when GHC's profiling subsystem is needed.

%package libghc
Summary: GHC inside a library
Group: Development/Haskell
Requires: ghc = %version

%description libghc
Haskell is a standard lazy functional programming language;
GHC is a state-of-the-art programming suite for Haskell.

This package contains all of the GHC internal modules in a library, so
you can use parts of GHC in your own program. Install this if you intend
to do very GHC-specific development; you probably don't want this.

%package doc
Summary: Documentation for GHC
Group: Development/Haskell
BuildArch: noarch

%description doc
Preformatted documentation for the Glasgow Haskell Compiler
(GHC) and its libraries. Install it if you like to have local
access to the documentation in PostScript and HTML format.
Alternatively, the documentation is available online at

  http://haskell.org/ghc/documentation.html

%prep
%setup

%build
autoreconf -fisv
%configure
make CFLAGS=-fPIC

%install
# compress the non-html docs
dir=`pwd`
pushd docs
for i in ps dvi sgml verb idx; do
	find . -name '*.'$i -exec gzip -9 '{}' ';' -print
done
popd

# This is a cruel hack: There seems to be no way to install the Haddock
# documentation into the build directory, because DESTDIR is alway prepended.
# Furthermore, rpm removes the target documentation directory before the doc
# macros are processed. Therefore we have to copy things back into safety... :-P
make DESTDIR=%buildroot \
	HADDOCK_DOCS=YES docdir=%_defaultdocdir/%name-doc-%version \
	install 
#mkdir html-docs
cp -a %buildroot%_defaultdocdir/%name-doc-%version/html html-docs

# 'make install' installs lots of LICENSE files. Get rid of them.
rm -f %buildroot%_defaultdocdir/%name/libraries/*/LICENSE

# generate fake .pkg configs for core packages.
# haskell.prov will convert them to package provides.
for lib in %buildroot%_libdir/%name-%version/*-[0-9]*; do
	namever=`basename $lib`
	name=${namever%%-*}
	echo -e "name: $name\nversion: ${namever##*-}" >$lib/$name.pkg
done

# generate the file list for lib/ _excluding_ all files needed for profiling
# only
#
# * generating file lists in a BUILD_ROOT spec is a bit tricky: the file list
#   has to contain complete paths, _but_ without the BUILD_ROOT, we also do
#   _not_ want to have directory names in the list; furthermore, we have to make
#   sure that any leading / is removed from %%_libdir, as find has to
#   interpret the argument as a relative path; however, we have to include the
#   leading / again in the final file list (otherwise, rpm complains)
# * isn't there an easier way to do all this?
dir=`pwd`
cd %buildroot
libdir=`echo %_libdir | sed 's|^/||'`
find $libdir ! -type d ! -name '*.p_hi' \
     ! -name '*_p.a' ! -name 'package.conf*' \
     -print | sed 's|^|/|'\
     >$dir/rpm-noprof-lib-files
find $libdir ! -type d -name '*.p_hi' -print | sed 's|^|/|'\
     >$dir/rpm-prof-lib-files
find $libdir ! -type d -name '*_p.a' -print | sed 's|^|/|'\
     >>$dir/rpm-prof-lib-files
find $libdir/%name-%version -type d -print | sed 's|^|%%dir /|' >>$dir/rpm-noprof-lib-files
cd $dir

# install and fix up the macros file
%define rpmmacrosdir %_sysconfdir/rpm/macros.d
mkdir -p %buildroot%rpmmacrosdir
install %SOURCE1 %buildroot%rpmmacrosdir/%name
subst 's/@GHC_VERSION@/%version/' %buildroot%rpmmacrosdir/%name

# touch our "ghost". ghc-pkg may create him later.
touch %buildroot%_libdir/%name-%version/package.conf.old
# package-provided *.confs go in this directory:
mkdir -p %buildroot%_libdir/%name-%version/package.conf.d

%files -f rpm-noprof-lib-files
%exclude %_libdir/%name-%version/%name-%version
%rpmmacrosdir/%name
%doc ANNOUNCE README
%_bindir/*
%_man1dir/%name.1*
#%_libdir/%name-%version/package.conf
%ghost %_libdir/%name-%version/package.conf.old
%dir %_libdir/%name-%version/package.conf.d

%files libghc
%dir %_libdir/%name-%version/%name-%version
%_libdir/%name-%version/%name-%version/include
%_libdir/%name-%version/%name-%version/*[0-9].a
%_libdir/%name-%version/%name-%version/*.hi
%_libdir/%name-%version/%name-%version/*.o
%_libdir/%name-%version/%name-%version/*.pkg

%files prof -f rpm-prof-lib-files

%files doc
# Updated from ghc/ghc.spec on 19.06.2008.
# TODO
#%doc docs/docbook-cheat-sheet/docbook-cheat-sheet
%doc docs/comm
#%doc docs/users_guide/users_guide
#%doc libraries/Cabal/doc/Cabal
%doc html-docs/*

%changelog
* Mon Dec 06 2010 Denis Smirnov <mithraen@altlinux.ru> 7.0.1-alt1
- 7.0.1

* Sun Oct 24 2010 Denis Smirnov <mithraen@altlinux.ru> 6.12.3-alt5
- rebuild

* Mon Sep 13 2010 Denis Smirnov <mithraen@altlinux.ru> 6.12.3-alt4
- disable build with hscolour

* Mon Sep 13 2010 Denis Smirnov <mithraen@altlinux.ru> 6.12.3-alt3
- rebuild with new requires/provides generator
- rebuild with hscolour
- update build requires
- enable ghc-prof by default in all libraries (ghc requires ghc-prof)

* Thu Sep 09 2010 Denis Smirnov <mithraen@altlinux.ru> 6.12.3-alt2
- fix build on i586

* Wed Sep 08 2010 Denis Smirnov <mithraen@altlinux.ru> 6.12.3-alt1
- 6.12.3

* Sat Mar 13 2010 Dmitry V. Levin <ldv@altlinux.org> 6.10.4-alt2
- Fixed build with fresh autoconf.

* Thu Aug 06 2009 Alexander Myltsev <avm@altlinux.ru> 6.10.4-alt1
- 6.10.2-4: bugfix releases.

* Sat Nov 08 2008 Alexander Myltsev <avm@altlinux.ru> 6.10.1-alt1
- 6.10.1: many user-visible changes, see release notes on haskell.org.
- has haddock2 packaged inside.

* Thu Jun 19 2008 Alexander Myltsev <avm@altlinux.ru> 6.8.3-alt1
- 6.8.3: bugfix release.

* Sun Jan 13 2008 Alex V. Myltsev <avm@altlinux.ru> 6.8.2-alt2
- Include GHC core library documentation built with Haddock
- Include _ghclibdir/package.conf.d

* Sat Jan 05 2008 Alex V. Myltsev <avm@altlinux.ru> 6.8.2-alt1
- 6.8.2:
- - debugger inside ghci
- - Haskell Program Coverage in the compiler
- - better optimization
- - many more user-visible changes, see release notes
- 'ghc-extralibs' (non-core libraries) are now packaged separately

* Thu Oct 04 2007 Alex V. Myltsev <avm@altlinux.ru> 6.6.1-alt1
- 6.6.1: lots of bug fixes, new extralibs, can compile C++ files, etc.

* Sat Nov 04 2006 Alex V. Myltsev <avm@altlinux.ru> 6.6-alt1
- 6.6: many user-visible changes, see release notes on haskell.org.

* Sun Jun 04 2006 Alex V. Myltsev <avm@altlinux.ru> 6.4.2-alt2
- Build with gcc4, now that 6.4.2 is in Sisyphus.

* Mon Mar 13 2006 Alex V. Myltsev <avm@altlinux.ru> 6.4.2-alt1
- New version.

* Fri Dec 30 2005 ALT QA Team Robot <qa-robot@altlinux.org> 6.2.2-alt1.1
- Rebuilt with libreadline.so.5.

* Sun Nov 21 2004 Vitaly Lugovsky <vsl@altlinux.ru> 6.2.2-alt1
- new version

* Mon May 10 2004 Vitaly Lugovsky <vsl@altlinux.ru> 6.2.1.20040316-alt3.1
- clearance rebuild

* Mon May 10 2004 Vitaly Lugovsky <vsl@altlinux.ru> 6.2.1.20040316-alt3
- glibc2.3 rebuild

* Wed May 05 2004 Vitaly Lugovsky <vsl@altlinux.ru> 6.2.1.20040316-alt2.1
- a temporary re-bootstrap binary release

* Thu Mar 18 2004 Vitaly Lugovsky <vsl@altlinux.ru> 6.2.1.20040316-alt2
- profile .p_hi fixes

* Wed Mar 17 2004 Vitaly Lugovsky <vsl@altlinux.ru> 6.2.1.20040316-alt1
- a new version

* Wed Dec 17 2003 Vitaly Lugovsky <vsl@altlinux.ru> 6.2-alt1
New version

* Mon Oct 13 2003 Vitaly Lugovsky <vsl@altlinux.ru> 6.0.1-alt1
new version

* Sun Jun 29 2003 Vitaly Lugovsky <vsl@altlinux.ru> 6.0-alt1
- new version released

* Tue Apr 01 2003 Vitaly Lugovsky <vsl@altlinux.ru> 5.04.3-alt1
- new version released

* Fri Jan 24 2003 Vitaly Lugovsky <vsl@altlinux.ru> 5.04.2-alt1
- a new version

* Sat Dec 28 2002 Vitaly Lugovsky <vsl@altlinux.ru> 5.04.1-alt3
- spec cleanup, again

* Mon Dec 09 2002 Vitaly Lugovsky <vsl@altlinux.ru> 5.04.1-alt2
- spec cleanup

* Fri Dec 06 2002 Vitaly Lugovsky <vsl@altlinux.ru> 5.04.1-alt1
- new version

* Wed Jul 31 2002 Vitaly Lugovsky <vsl@altlinux.ru> 5.04
- New version released

* Tue May 14 2002 Vitaly Lugovsky <vsl@altlinux.ru> 5.02.3-alt4
- Get rid of virtual package 'haskell'.

*Sun May 12 2002 Vitaly Lugovsky <vsl@altlinx.ru> 5.02.3-alt3
- BuildRoot and %clean removed to conform ALTLinux packaging
  policy.

*Sat Apr 27 2002 Vitaly Lugovsky <vsl@altlinux.ru> 5.02.3-alt2
- Slightly adopted to the ALT Linux environment.

* Wed Sep 26 2001 Manuel Chakravarty
- split documentation off into a separate package
- adapt to new docbook setup in RH7.1

* Mon Apr 16 2001 Manuel Chakravarty
- revised for 5.00
- also runs autoconf automagically if no ./configure found

* Thu Jun 22 2000 Sven Panne
- removed explicit usage of hslibs/docs, it belongs to ghc/docs/set

* Sun Apr 23 2000 Manuel Chakravarty
- revised for ghc 4.07; added suggestions from Pixel <pixel@mandrakesoft.com>
- added profiling package

* Tue Dec 7 1999 Manuel Chakravarty
- version for use from CVS

* Thu Sep 16 1999 Manuel Chakravarty
- modified for GHC 4.04, patchlevel 1 (no more 62 tuple stuff); minimises use
  of patch files - instead emits a build.mk on-the-fly

* Sat Jul 31 1999 Manuel Chakravarty
- modified for GHC 4.04

* Wed Jun 30 1999 Manuel Chakravarty
- some more improvements from vbzoli

* Fri Feb 26 1999 Manuel Chakravarty
- modified for GHC 4.02

* Thu Dec 24 1998 Zoltan Vorosbaranyi
- added BuildRoot
- files located in /usr/local/bin, /usr/local/lib moved to /usr/bin, /usr/lib

* Tue Jul 28 1998 Manuel Chakravarty
- original version

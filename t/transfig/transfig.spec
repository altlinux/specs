Name: transfig
Version: 3.2.5d
Release: alt2

Packager: Victor Forsiuk <force@altlinux.org>

Summary: A utility for converting FIG files (made by xfig) to other formats
License: MIT
Group: Graphics

Url: http://www.xfig.org/
Source0: http://download.sourceforge.net/mcj/transfig.%version.tar.gz
Source1: transfig-ru_RU.KOI8-R.ps
Source2: transfig-ru_RU.CP1251.ps
Source3: transfig-uk_UA.KOI8-U.ps
Patch0: transfig-3.2.5-makefile-fig2dev_libdir.patch
Patch1: transfig-3.2.5-genps.patch

# Automatically added by buildreq on Wed Sep 22 2010
BuildRequires: imake libXpm-devel libpng-devel xorg-cf-files

# fig2dev MAY calls gs and utilities from netpbm package for some outputs:
Requires: /usr/bin/gs netpbm
# Utilities needed by fig2ps2tex:
Requires: grep awk bc

%description
The transfig utility creates a makefile which translates FIG (created by xfig)
or PIC figures into a specified LaTeX graphics language (for example,
PostScript).  Transfig is used to create TeX documents which are portable
(i.e., they can be printed in a wide variety of environments).

%prep
%setup -n %name.%version
%patch0 -p1
%patch1 -p0
chmod 644 CHANGES LATEX.AND.XFIG NOTES README

%build
# This script contains "bashism":
subst 's@/bin/sh@/bin/bash@' fig2dev/fig2ps2tex.sh.script

xmkmf
%make Makefiles
%make_build CDEBUGFLAGS="%optflags"

%install
%make_install DESTDIR=%buildroot install install.man

pushd %buildroot%_bindir
rm -f fig2ps2tex
mv fig2ps2tex.sh fig2ps2tex
popd

chmod 644 %buildroot%_datadir/xfig/bitmaps/*

install -p -m644 %SOURCE1 %buildroot%_datadir/fig2dev/ru_RU.KOI8-R.ps
install -p -m644 %SOURCE2 %buildroot%_datadir/fig2dev/ru_RU.CP1251.ps
install -p -m644 %SOURCE3 %buildroot%_datadir/fig2dev/uk_UA.KOI8-U.ps

%files
%_bindir/*
%_man1dir/*
%_datadir/fig2dev
%_datadir/xfig
%doc CHANGES LATEX.AND.XFIG NOTES README

%changelog
* Thu Sep 23 2010 Victor Forsiuk <force@altlinux.org> 3.2.5d-alt2
- Patch to fix bad hatching (closes: #19060).

* Wed Sep 22 2010 Victor Forsiuk <force@altlinux.org> 3.2.5d-alt1
- 3.2.5d
- Added requirements for packages containing utilities that fig2dev may call
  for some outputs (closes: #21930). The same for fig2ps2tex.

* Wed Aug 06 2008 Victor Forsyuk <force@altlinux.org> 3.2.5-alt1
- 3.2.5, considerable specfile cleanup.
- Fix ALT#13450.
- Fix fig2dev_libdir path.

* Sat Apr 15 2006 Yury A. Zotov <yz@altlinux.ru> 3.2.4-alt6
- man path is corrected

* Thu Feb 12 2004 Yury A. Zotov <yz@altlinux.ru> 3.2.4-alt5
- applied patch from RH to build with gcc3.3

* Mon Oct 06 2003 Yury A. Zotov <yz@altlinux.ru> 3.2.4-alt3
- BuildRequires updated for Sisyphus 20031005
- build with hasher

* Sat Mar 01 2003 Dmitry V. Levin <ldv@altlinux.org> 3.2.4-alt2
- Specfile cleanup. Fixed severe packaging error (#0002306).

* Tue Feb 25 2003 Yury A. Zotov <yz@altlinux.ru> 3.2.4-alt1
- new version

* Sun Jan 19 2003 Yury A. Zotov <yz@altlinux.ru> 3.2.3d-alt4
- added support for russian (koi8-r, cp1251) and ukrainian (koi8-u)
  languages when convert to PostScript
- language support files placement fixed
- xfig part of files installed into /usr/X11R6/lib/xfig
- changed maintainer

* Fri Oct 18 2002 Rider <rider@altlinux.ru> 3.2.3d-alt3
- Russian summary and description
- rebuild (gcc 3.2)

* Thu Oct 11 2001 Stanislav Ievlev <inger@altlinux.ru> 3.2.3d-alt2
- rebuilt with new libpng

* Wed May 30 2001 Stanislav Ievlev <inger@altlinux.ru> 3.2.3d-alt1
- 3.2.3d

* Thu Dec 14 2000 Dmitry V. Levin <ldv@fandra.org> 3.2.3c-ipl2mdk
- FHSification.

* Wed Jul 26 2000 Dmitry V. Levin <ldv@fandra.org> 3.2.3c-ipl1mdk
- 3.2.3c
- RE adaptions.

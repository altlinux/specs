Name: transfig
Version: 3.2.6a
Release: alt1

Summary: A utility for converting FIG files (made by xfig) to other formats
Group: Graphics
Url: https://sourceforge.net/projects/mcj/
License: Freeware

Source: %name-%version.tar.gz

BuildRequires: libXpm-devel libpng-devel

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
%setup -q

%build
%autoreconf
%configure --with-appdefaultdir=%_x11appconfdir

%install
%make_install DESTDIR=%buildroot install

%files
%_bindir/*
%_man1dir/*
%_datadir/fig2dev

%changelog
* Sat Feb 18 2017 Vladislav Zavjalov <slazav@altlinux.org> 3.2.6a-alt1
- 3.2.6a

* Mon Oct 08 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.2.5d-alt2.1
- Rebuilt with libpng15

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

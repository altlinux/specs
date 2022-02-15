Name: magicpoint
Version: 1.13a
Release: alt6.20140908

Summary: Presentation tool
Group: Office
License: BSD-3-Clause
Url: http://member.wide.ad.jp/wg/mgp/

# ftp://sh.wide.ad.jp/WIDE/free-ware/mgp/%name-%version.tar.bz2
Source: %name-%version.tar

Requires: ghostscript-classic, netpbm, sharutils, /bin/gunzip

BuildRequires: rpm-build-fonts
BuildRequires: flex gccmakedep imake pkg-config
BuildRequires: imlib2-devel libjpeg-devel libpng-devel libmng-devel libungif-devel
BuildRequires: fontconfig-devel libfreetype-devel
BuildRequires: libXmu-devel libXext-devel libXft-devel
BuildRequires: xorg-xextproto-devel xorg-cf-files
BuildRequires: libm17n-devel

%add_findreq_skiplist %_bindir/mgpnet

%description
MagicPoint is an X11 based presentation tool.  It is designed to make
simple presentations easy while to make complicated presentations
possible.  Its presentation file (whose suffix is typically .mgp) is
just text so that you can create presentation files quickly with your
favorite editor (e.g. Emacs).

%prep
%setup

%build
%add_optflags -D__SABER__ -DFREETYPEFONTDIR=\"%_ttffontsdir\"
export mgp_cv_path_uuencode=%_bindir/uuencode
export mgp_cv_path_uudecode=%_bindir/uudecode
%autoreconf
#	--disable-vflib \
%configure \
	--prefix=%prefix \
	--enable-xft2 \
	--enable-imlib \
	--enable-freetype \
	--enable-freetype-charset16 \
	--enable-locale \
	--enable-gif \
	--with-m17n-lib \
	--enable-debug \
	--with-x \
	#
xmkmf -a
# SMP-incompatible build.
sed -i 's|\(CDEBUGFLAGS =.*\)|\1 -g|' Makefile
%make

%install
%makeinstall install.man DESTDIR=%buildroot

%files
%_bindir/*
%_libdir/mgp
%_man1dir/*
%doc COPYRIGHT FAQ README* RELNOTES SYNTAX USAGE sample

%changelog
* Tue Feb 15 2022 Fr. Br. George <george@altlinux.org> 1.13a-alt6.20140908
- Resurrect build

* Tue Apr 13 2021 Anton Farygin <rider@altlinux.org> 1.13a-alt5.20140908
- fixed FTBFS with gcc-10

* Mon May 15 2017 Anton Farygin <rider@altlinux.ru> 1.13a-alt4.20140908
- NMU: rebuild with new libmng

* Wed Dec 09 2015 Igor Vlasenko <viy@altlinux.ru> 1.13a-alt3.20140908
- NMU: Fixed build (also - snapshot from 20151207 is the same as 20140908)

* Wed Mar 04 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.13a-alt2.20140908
- Fixed build

* Fri Sep 12 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.13a-alt1.20140908
- New snapshot

* Fri Apr 19 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 1.13a-alt1.1.qa1
- NMU: rebuilt for updated dependencies.

* Thu Jul 12 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.13a-alt1.1
- Fixed build

* Sun Dec 06 2009 Alexey Gladkov <legion@altlinux.ru> 1.13a-alt1
- New version (1.13a).
- Build with libm17n (utf8 support).

* Tue Mar 21 2006 Dmitry V. Levin <ldv@altlinux.org> 1.10a-alt3
- Fixed build on multilib platforms.
- Fixed build with XOrg in /usr.
- Updated package dependencies.

* Mon Jul 26 2004 Dmitry V. Levin <ldv@altlinux.org> 1.10a-alt2
- mgp2ps: added support for koi8-r, koi8-u and cp1251 encodings.

* Tue Feb 10 2004 Dmitry V. Levin <ldv@altlinux.org> 1.10a-alt1
- Updated to 1.10a, reviewed patches.

* Fri Sep 27 2002 Dmitry V. Levin <ldv@altlinux.org> 1.09a-alt3
- Fixed configure.
- Added preliminary i18n support (ab).

* Wed Sep 18 2002 Stanislav Ievlev <inger@altlinux.ru> 1.09a-alt2
- rebuild with new XFree86

* Sun Sep 08 2002 Dmitry V. Levin <ldv@altlinux.org> 1.09a-alt1
- Adapted for ALT Linux.

* Wed Jul 17 2002 Pixel <pixel@mandrakesoft.com> 1.09a-5mdk
- add missing quote in /etc/emacs/site-start.d/magicpoint.el

* Tue Jul 09 2002 Lenny Cartier <lenny@mandrakesoft.com> 1.09a-4mdk
- buildrequires freetype-devel

* Thu Oct 11 2001 Pixel <pixel@mandrakesoft.com> 1.09a-3mdk
- rebuilding for libpng3

* Mon Oct  8 2001 Pixel <pixel@mandrakesoft.com> 1.09a-2mdk
- better X11 font choosing (?)
- add require libjpeg-progs

* Sun Oct  7 2001 Pixel <pixel@mandrakesoft.com> 1.09a-1mdk
- fixes, cleanup, emacs mode by default...
- new version

* Mon Sep 03 2001 Yves Duret <yduret@mandrakesoft.com> 1.08a-2mdk
- added a Requires on fonts-ttf-japanese
- added -q option to %%setup

* Wed Jun 13 2001 Gwenole Beauchesne <gbeauchesne@mandrakesoft.com> 1.08a-1mdk
- 1.08a
- sanitized spec file (s/Copyright/License, etc.)

* Mon Dec 11 2000 Lenny Cartier <lenny@mandrakesoft.com> 1.07a-1mdk
- new in contribs

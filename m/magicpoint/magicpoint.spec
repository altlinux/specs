Name: magicpoint
Version: 1.13a
Release: alt1

Summary: Presentation tool
Group: Office
License: BSD-like
Url: http://member.wide.ad.jp/wg/mgp/
Packager: Alexey Gladkov <legion@altlinux.ru>

# ftp://sh.wide.ad.jp/WIDE/free-ware/mgp/%name-%version.tar.bz2
Source: %name-%version.tar

Patch1:  magicpoint-1.13a-install-path.patch
Patch2:  magicpoint-1.09a-emacs-mode--add-font-lock.patch
Patch3:  magicpoint-1.13a-alt-i18n.patch
Patch5:  magicpoint-1.13a-tffonts.patch
Patch6:  magicpoint-1.13a-sample.patch
Patch7:  magicpoint-1.13a-nonvoid.patch
Patch8:  magicpoint-1.13a-cflags.patch
Patch9:  magicpoint-1.13a-compile-warning.patch
Patch10: magicpoint-1.13a-null.patch
Patch11: magicpoint-1.13a-xft-rendering-fix.patch
Patch12: magicpoint-1.13a-lib64.patch
Patch13: magicpoint-1.13a-warnings.patch
Patch14: magicpoint-1.13a-m17n.patch

Requires: ghostscript-classic, netpbm, sharutils, /bin/gunzip

BuildRequires: rpm-build-fonts
BuildRequires: flex gccmakedep imake pkg-config
BuildRequires: imlib2-devel libjpeg-devel libpng-devel libmng-devel libungif-devel
BuildRequires: fontconfig-devel libfreetype-devel
BuildRequires: libXmu-devel libXext-devel libXft-devel
BuildRequires: xorg-xextproto-devel xorg-cf-files
BuildRequires: libm17n-devel

%description
MagicPoint is an X11 based presentation tool.  It is designed to make
simple presentations easy while to make complicated presentations
possible.  Its presentation file (whose suffix is typically .mgp) is
just text so that you can create presentation files quickly with your
favorite editor (e.g. Emacs).

%prep
%setup -q
%patch1  -p2 -b .fix1
%patch2  -p1 -b .fix2
%patch3  -p1 -b .fix3
%patch5  -p1 -b .fix5
%patch6  -p1 -b .fix6
%patch7  -p0 -b .fix7
%patch8  -p1 -b .fix8
%patch9  -p1 -b .fix9
%patch10 -p0 -b .fix10
#patch11 -p0 -b .fix11
%patch12 -p0 -b .fix12
#patch13 -p0 -b .fix13
%patch14 -p2 -b .fix14

%build
%add_optflags -D__SABER__ -DFREETYPEFONTDIR=\"%_ttffontsdir\"
export mgp_cv_path_uuencode=%_bindir/uuencode
export mgp_cv_path_uudecode=%_bindir/uudecode
%autoreconf
%configure \
	--prefix=%prefix \
	--disable-vflib \
	--enable-xft2 \
	--enable-imlib \
	--enable-freetype \
	--enable-freetype-charset16 \
	--enable-locale \
	--enable-gif \
	--with-m17n-lib \
	#
xmkmf -a
# SMP-incompatible build.
make

%install
%makeinstall install.man DESTDIR=%buildroot

%files
%_bindir/*
%_libdir/mgp
%_man1dir/*
%doc COPYRIGHT FAQ README* RELNOTES SYNTAX USAGE sample

%changelog
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

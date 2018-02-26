Name: lesstif
Version: 0.95.2
Release: alt3

Summary: LessTif - a free replacement of OSF/Motif
Group: System/Libraries
Url: http://www.lesstif.org/
Packager: Evgeny Sinelnikov <sin@altlinux.ru>
Source: http://download.sourceforge.net/%name/%name-%version.tar.bz2
License: LGPLv2+
# in Xm-2.1/
# some files are MIT
# LTV6Editres.c XpmAttrib.c XpmCrBufFrI.c XpmCrBufFrP.c XpmCrDatFrI.c
# XpmCrDatFrP.c Xpmcreate.c XpmCrIFrBuf.c XpmCrIFrDat.c XpmCrIFrP.c
# XpmCrPFrBuf.c XpmCrPFrDat.c XpmCrPFrI.c Xpmdata.c Xpmhashtab.c XpmImage.c
# XpmInfo.c Xpmmisc.c Xpmparse.c XpmRdFToBuf.c XpmRdFToDat.c XpmRdFToI.c
# XpmRdFToP.c Xpmrgb.c Xpmscan.c Xpms_popen.c XpmWrFFrBuf.c XpmWrFFrDat.c
# XpmWrFFrI.c XpmWrFFrP.c
# Transltns.c is machine generated (no license, assuming public domain)

# MIT, short version: lib/config/mxmkmf.in

# in includes
# MIT:
# XmI/LTV5EditresP.h XmI/LTV6EditresP.h XmI/XpmI.h Xm/XpmP.h

# clients/Motif-2.1/mwm/
# MIT:
# mwm.h cursors.c decorate.c desktop.c events.c functions.c menus.c misc.c
# mwm.c pan.c props.c resize.c screens.c windows.c
# no restriction
# colormaps.c icons.c move.c pager.c
# GPLV2+
# gethostname.c mwmparse.h

# clients/Motif-2.1/uil/
# no license (LGPLv2+?)
# Expression.c

Source3: mwm.xpm
Source4: mwm32.xpm

# mwm session file
Source5: mwm.desktop
# put mwm conf file in %_sysconfdir, and install Dt in %_libdir
Patch: lesstif-Makefile.in.diff
# have motif-config honor libdir
Patch1: lesstif-motif-config-use_libdir.diff
Patch5: http://ftp.debian.org/debian/pool/main/l/lesstif2/lesstif2_0.95.0-2.diff.gz

Provides: motif, %name-compat = %version
Obsoletes: %name-compat
Conflicts: openmotif < 2.2.2

# Automatically added by buildreq on Wed Oct 01 2003
BuildRequires: libXrender-devel libXext-devel libXt-devel ctags flex fontconfig-devel libfreetype-devel glibc-devel-static lynx man zlib-devel

%package devel
Summary: Include files for Lesstif development
Group: Development/C
Requires: %name = %version-%release
Provides: motif-devel, %name-devel-compat = %version
Obsoletes: %name-devel-compat
Conflicts: openmotif-devel

%package devel-static
Summary: Static libraries for Lesstif development
Group: Development/C
Requires: %name-devel = %version-%release
Provides: motif-devel-static, %name-devel-compat-static = %version
Obsoletes: %name-devel-compat-static
Conflicts: openmotif-devel-static

%package mwm
Summary: Lesstif Motif window manager clone based on fvwm
License: GPL
Group: Graphical desktop/Motif
Requires: %name = %version-%release
Provides: motif-mwm
Conflicts: openmotif-mwm

%package clients
Summary: LessTif clients
License: GPL
Group: Graphical desktop/Motif
Requires: %name = %version-%release
Provides: motif-clients
Conflicts: openmotif-clients

%package doc
Summary: LessTif Manuals
Group: Development/C
Requires: %name = %version-%release
Provides: lessdox = %version
Obsoletes: lessdox
BuildArch: noarch

%description
Lesstif is an API compatible clone of the Motif toolkit.

Most of the Motif 1.2 API is in place.
Motif 2.1 functionality is being improved.

Many Motif applications compile and run out-of-the-box with LessTif,
and we want to hear about those that don't.

%description devel
Lesstif is an API compatible clone of the Motif toolkit.

Most of the Motif 1.2 API is in place.
Motif 2.1 functionality is being improved.

Many Motif applications compile and run out-of-the-box with LessTif,
and we want to hear about those that don't.

This package contains programs, development libraries and include files
required to develop lesstif-based applications.

%description devel-static
This package contains static libraries required to develop statically
linked lesstif-based applications.

%description mwm
Lesstif is an API compatible clone of the Motif toolkit.
This package contains mwm - a window manager that adheres largely
to the Motif mwm specification.

%description clients
Lesstif is an API compatible clone of the Motif toolkit.
This package contains uil and xmbind.

%description doc
This package contains LessTif development documentation.

%prep
%setup -q
chmod a-x COPYING* doc/www.lesstif.org/BUG-HUNTING.html
%patch0 -p1
%patch1 -p1
%patch5 -p1

# and pick up some fixes from Debian
patch -p1 < debian/patches/020_xpmpipethrough.diff
patch -p1 < debian/patches/030_manpage.diff

# those substitutions are not really usefull, since the symbols are redefined
# in the Makefile, but it is clearer like that
touch -r clients/Motif-2.1/mwm/mwm.h __mwm_stamp
sed -i -e 's:"/usr/X11/include":"%_includedir":' \
  -e 's:"/usr/lib/X11/mwm":"%_sysconfdir/mwm":' clients/Motif-2.1/mwm/mwm.h
touch -r __mwm_stamp clients/Motif-2.1/mwm/mwm.h
rm __mwm_stamp

%build
CFLAGS="$RPM_OPT_FLAGS" %configure \
	--enable-shared \
	--enable-static \
	--enable-build-12 \
	--enable-build-20 \
	--enable-build-21 \
	--disable-verbose \
	--enable-production \
	--with-editres \
	--with-xdnd \
	%_configure_target

sed < libtool > libtool-2 \
	-e 's/^hardcode_libdir_flag_spec.*$/hardcode_libdir_flag_spec=" -D__LIBTOOL_IS_A_FOOL__ "/' \
	-e '/^archive_cmds="/s/"$/ \$deplibs"/'
mv libtool-2 libtool
chmod 755 libtool

%make_build

%install
%makeinstall_std \
 appdir='%_datadir/X11/app-defaults' configdir='%_datadir/X11/config' \
 INSTALL="install -p"

rm %buildroot%_libdir/*.la

# correct the paths in mxmkmf
sed -i -e 's:"\${xprefix}/lib/X11/config":"%_datadir/X11/config":' \
 -e 's:"\${lprefix}/lib/LessTif/config":"%_datadir/X11/config":' \
 %buildroot%_bindir/mxmkmf
# use .in timestamp, since the .in and resulting files are the same
touch -r lib/config/mxmkmf.in %buildroot%_bindir/mxmkmf

# will be in in %%doc
rm %buildroot%_sysconfdir/mwm/README %buildroot%_sysconfdir/mwm/alt.map

# the corresponding file is not shipped
rm %buildroot%_mandir/man*/ltversion*

# remove host.def, it lives in the imake package
rm %buildroot%_datadir/X11/config/host.def

# use ChangeLog file timestamp to have the same timestamp on all arches
# for noarch files
touch -r ChangeLog %buildroot%_datadir/X11/config/LessTif.tmpl \
%buildroot%_includedir/Xm/Xm.h

# Cleanup manpages.
find %buildroot%_mandir -type f -name '*.[1-9]' -print0 |
	xargs -r0 grep -Zl '^\.\.\.' |
	xargs -r0 sed -i -e 's/^\.\.\././g'

## Prepare docs.
mkdir -p %buildroot%_docdir/%name-%version
mv %buildroot%_x11dir/LessTif/doc %buildroot%_docdir/%name-%version/lessdox
mv %buildroot%_x11dir/LessTif/* %buildroot%_docdir/%name-%version/
rm %buildroot%_docdir/%name-%version/{COPYING*,Install} -f
install -p -m644 clients/Motif-2.1/mwm/README %buildroot%_docdir/%name-%version/mwm.README

# Icons.
install -pD -m644 %SOURCE3 %buildroot%_miconsdir/mwm.xpm
install -pD -m644 %SOURCE4 %buildroot%_niconsdir/mwm.xpm

# Install mwm xsession file.
mkdir -p %buildroot%_datadir/xsessions/
install -p -m644 %SOURCE5 %buildroot%_datadir/xsessions/

%files
%_libdir/*.so.*
%_man1dir/lesstif.*
%_man5dir/VirtualBindings.*
%doc %dir %_docdir/%name-%version
%doc %_docdir/%name-%version/[A-Z]*

%files devel
%_bindir/motif-config
%_bindir/mxmkmf
%_libdir/*.so
%_includedir/*
%_mandir/man?/*
%exclude %_man1dir/lesstif.*
%exclude %_man5dir/VirtualBindings.*
%exclude %_mandir/man?/mwm*
%exclude %_mandir/man?/uil.*
%exclude %_mandir/man?/xmbind.*
%_datadir/X11/config/*
%_datadir/aclocal/*

%files devel-static
%_libdir/*.a

%files mwm
%doc clients/Motif-2.1/mwm/README clients/Motif-2.1/mwm/alt.map
%dir %_sysconfdir/mwm/
%config(noreplace) %_sysconfdir/mwm/system.mwmrc
%_datadir/X11/app-defaults/Mwm
%_datadir/xsessions/mwm.desktop
%_bindir/mwm
%_mandir/man?/mwm*
%_niconsdir/*.xpm
%_iconsdir/hicolor/*/apps/*.xpm

%doc %dir %_docdir/%name-%version
%doc %_docdir/%name-%version/mwm.README

%files clients
%_bindir/uil
%_bindir/xmbind
%_mandir/man?/uil.*
%_mandir/man?/xmbind.*

%files doc
%doc %dir %_docdir/%name-%version
%doc %_docdir/%name-%version/lessdox

%changelog
* Tue Apr 10 2012 Lenar Shakirov <snejok@altlinux.ru> 0.95.2-alt3
- Fixed build: remove RPATH entry from libtool

* Thu Apr 14 2011 Lenar Shakirov <snejok@altlinux.ru> 0.95.2-alt2
- Fixed build:
  * xorg-x11-devel xorg-x11-libs removed from BuildReqs
  * libXrender-devel libXext-devel libXt-devel added to BuildReqs
- Spec cleaned: thanks to rpmcs script!

* Wed Nov 24 2010 Evgeny Sinelnikov <sin@altlinux.ru> 0.95.2-alt1
- Update to 0.95.2.
- Removed already applied patches in mainstream.
- Import build changes by last repocop rebuild

* Fri Jan 15 2010 Repocop Q. A. Robot <repocop@altlinux.org> 0.95-alt3.qa1
- NMU (by repocop): the following fixes applied:
  * pixmap-in-deprecated-location for lesstif
  * postclean-05-filetriggers for spec file

* Mon Jan 05 2009 Evgeny Sinelnikov <sin@altlinux.ru> 0.95-alt3
- Rebuilt with some fixes:
+ Removed deprecated post/postun_ldconfig macroses
+ Fixed filesystem conflict with openmotif-clients
+ Set doc subpackage to noarch due consists
  architecture-independent data only

* Sun Oct 28 2007 Evgeny Sinelnikov <sin@altlinux.ru> 0.95-alt2
- Merge with Fedora release:
+ Fixed build with patches from Fedora.
+ Added session desktop file.
+ Removed menu file.

* Wed Oct 24 2007 Evgeny Sinelnikov <sin@altlinux.ru> 0.95-alt1
- Updated to 0.95.
- Patch updated to 0.93.94 from Mandriva.
- Configured with mandir option.

* Thu Nov 27 2003 Dmitry V. Levin <ldv@altlinux.org> 0.93.91-alt1
- Updated to 0.93.91.
- Do not package .la files.

* Wed Oct 01 2003 Dmitry V. Levin <ldv@altlinux.org> 0.93.49-alt1
- Updated to 0.93.49.
- Updated libdir patch (mdk).

* Tue Oct 22 2002 Dmitry V. Levin <ldv@altlinux.org> 0.93.36-alt1
- Updated to 0.93.36
- Fixed libdir (mdk).
- Fixed build.

* Fri Apr 12 2002 Dmitry V. Levin <ldv@alt-linux.org> 0.93.18-alt2
- Updated conflicts (compatible with openmotif >= 2.2.2).

* Fri Mar 29 2002 Dmitry V. Levin <ldv@alt-linux.org> 0.93.18-alt1
- 0.93.18

* Tue Dec 04 2001 Dmitry V. Levin <ldv@alt-linux.org> 0.93.15-alt1
- 0.93.15

* Fri Oct 12 2001 Dmitry V. Levin <ldv@altlinux.ru> 0.93.12-alt1
- 0.93.12 (--enable-build-21).
- No compat subpackages (yet?).
- Relocated documentation.
- Added menu support and menu entries (mdk).

* Mon Mar 19 2001 Dmitry V. Levin <ldv@altlinux.ru> 0.92.6-ipl4mdk
- Moved static libraries to devel-static and devel-compat-static subpackages.

* Wed Mar 14 2001 Dmitry V. Levin <ldv@altlinux.ru> 0.92.6-ipl3mdk
- Added bunch of provides.

* Thu Feb 15 2001 Dmitry V. Levin <ldv@fandra.org> 0.92.6-ipl2mdk
- Relocated config files according to FHS.
- Used new group: Graphical desktop/Motif.

* Wed Feb 07 2001 Dmitry V. Levin <ldv@fandra.org> 0.92.6-ipl1mdk
- 0.92.6
- Fixed XltFontChooser manpage.

* Thu Dec 21 2000 Dmitry V. Levin <ldv@fandra.org> 0.92.5-ipl1mdk
- 0.92.5.
- Fixed URL.

* Mon Dec 18 2000 Dmitry V. Levin <ldv@fandra.org> 0.92.0-ipl1mdk
- 0.92.0.
- Updated groups, summaries and descriptions.
- More compatibility with openmotif.

* Mon Jun 19 2000 Dmitry V. Levin <ldv@fandra.org>
- Specfile cleanup.

* Tue May 17 2000 AEN <aen@logic.ru>
- 0.91.0
- compat & devel-compat for compatibility Lesstif-1.2 with Open Motif

* Tue May 10 2000 AEN <aen@logic.ru>
- build new lesstif for Appendix
- fix doc-files permissions

* Fri Nov 19 1999 AEN <aen@logic.ru>
- fixed bug in file list

* Tue Nov 17 1999 AEN <aen@logic.ru>
- added options for configure

* Mon Nov 08 1999 AEN <aen@logic.ru>
- build for Mandrake RE
- bzipped man-pages

* Tue Oct 23 1999 Danny Backx <danny@hungry.com>
- try to integrate Michal's stuff in lesstif.spec.in
- don't treat Xbae, Xlt separately
- compile for 2.0 as well as for 1.2
- compile Xbae, Xlt by default

* Tue Oct 19 1999 Michal Jaegermann <michal@harddata.com>              (0.89)
- Updated to version 0.89
- Reorganized spec file to follow closer its own descriptions
- Xlt does not require special make anymore.

* Thu Apr 30 1998 C. Scott Ananian <cananian@alumni.princeton.edu>      (0.83+)
- Updated to lessdoc-current.
- Removes Lessdox package (integrated into lesstif)

* Tue Mar 31 1998 C. Scott Ananian <cananian@alumni.princeton.edu>      (0.83+)
- Removed pedantic.patch
- Removed lesstif-M12 (Motif 1.2 wrapper)
- Reviewed installation and fixed %files sections.
- Added patch to fix a bug which causes mozilla to crash.
- Added patch to fix the include prefix on install.

* Sun Jul 20 1997 Tomasz K�oczko <kloczek@rudy.mif.pg.gda.pl>        (0.80-2)
- added to all %%doc %%attr macros (this allow build package from normal user
  account),
- some simplification in %files (%%doc).
* Wed Jul 9 1997 Tomasz K�oczko <kloczek@rudy.mif.pg.gda.pl>
- added using %%PACKAGE_VERSION macro in "Source:" and %files,
- added additional parameter "--enable-build-12" to runing configure,
- added %%posun and %%clear,
- in %post and %postun ldconfig is called as parameter with "-p"
  (this feature is avalable in rpm >= 2.4.3 and you must have this
  version and if you want recompile package from src.rpm you must have new
  version rpm),
- added package lesstif-M12 simpe Motif 1.2 wrapper,
- simplified %install section,
- added %%attr macros in %files sections,
- added striping shared libraries,
- added URL field,
- added Lessdox - a html development documentation to lesstif-devel,
- added lesstif-0.80public-nopedantic.patch, this allow compile lesstif on
  sparc by removing "-pedantic" from CFLAGS.

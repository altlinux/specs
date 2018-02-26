Name: fontconfig
Version: 2.9.0
Release: alt2

Summary: Font configuration and customization library and utilities
Group: System/Configuration/Other
License: MIT
Url: http://fontconfig.org/
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Source: %name-%version.tar
Patch: %name-%version-%release.patch

Provides: lib%name = %version
Obsoletes: lib%name < %version
BuildRequires: docbook-utils elinks libexpat-devel libfreetype-devel

%description
Fontconfig is designed to locate fonts within the system and
select them according to requirements specified by applications.

%package devel
Summary: Development files for font configuration and customization library
Group: Development/C
Requires: %name = %version-%release

%description devel
This package includes the fontconfig header files and developer
documentation required for development of fontconfig-based software.

%define docdir %_docdir/%name

%prep
%setup -q
%patch -p1

%build
%autoreconf
%configure \
	--disable-static \
	--with-freetype-config='pkg-config freetype2' \
	--with-default-fonts=%_datadir/fonts \
	--with-cache-dir=%_var/cache/%name \
	--docdir=%docdir

%make PDF_FILES=

%install
%make DESTDIR=%buildroot PDF_FILES= install
install -pm644 AUTHORS README %buildroot%docdir/

> %buildroot%_sysconfdir/fonts/local.conf
install -Dp -m755 fontconfig-firsttime %buildroot%_sysconfdir/firsttime.d/%name
install -Dp -m755 %name.filetrigger %buildroot%_rpmlibdir/%name.filetrigger

%post
[ -n "$DURING_INSTALL" ] || %_sysconfdir/firsttime.d/%name

%triggerin -- %name < 2.8.0-alt7
find %_datadir/fonts -depth -type f -name fonts.cache-1 -delete
find %_var/cache/%name -depth -type f -name \*.cache-\[12\] -delete

%files
%_sysconfdir/firsttime.d/%name
%dir %_sysconfdir/fonts
%dir %_sysconfdir/fonts/conf.d
%dir %_sysconfdir/fonts/conf.avail
%config %_sysconfdir/fonts/fonts.dtd
%config %_sysconfdir/fonts/fonts.conf
%config(noreplace) %_sysconfdir/fonts/conf.avail/*.conf
%_sysconfdir/fonts/conf.d/README
%_sysconfdir/fonts/conf.d/[2-9]*.conf
%ghost %_sysconfdir/fonts/conf.d/1*.conf
%ghost %config(missingok,noreplace) %_sysconfdir/fonts/local.conf
%_bindir/fc-*
%_libdir/*.so.*
%_rpmlibdir/%name.filetrigger
%_man1dir/*
%_man5dir/*
%dir %_var/cache/%name
%docdir
%exclude %docdir/%name-devel*

%files devel
%_libdir/*.so
%_pkgconfigdir/*.pc
%_includedir/*
%_man3dir/*
%dir %docdir
%docdir/%name-devel*

%changelog
* Wed Mar 28 2012 Valery Inozemtsev <shrek@altlinux.ru> 2.9.0-alt2
- updated to master git.fe6ba5e

* Mon Mar 12 2012 Valery Inozemtsev <shrek@altlinux.ru> 2.9.0-alt1
- 2.9.0

* Sat Dec 03 2011 Dmitry V. Levin <ldv@altlinux.org> 2.8.0-alt9
- Fixed build, updated build dependencies.
- Fixed %name-devel dependencies.
- Fixed packaging of documentation.
- Cleaned up specfile.

* Wed Aug 17 2011 Valery Inozemtsev <shrek@altlinux.ru> 2.8.0-alt8
- updated fontconfig.filetrigger (closes #25992)

* Thu Jul 14 2011 Valery Inozemtsev <shrek@altlinux.ru> 2.8.0-alt7
- added fontconfig.filetrigger (closes #25862)

* Thu Feb 10 2011 Alexey Tourbin <at@altlinux.ru> 2.8.0-alt6
- rebuilt for debuginfo
- disabled symbol versioning

* Thu Oct 21 2010 Valery Inozemtsev <shrek@altlinux.ru> 2.8.0-alt5
- rebuild

* Thu Dec 17 2009 Valery Inozemtsev <shrek@altlinux.ru> 2.8.0-alt4
- prefer DejaVu before Liberation (closes: #22539)

* Thu Dec 17 2009 Valery Inozemtsev <shrek@altlinux.ru> 2.8.0-alt3
- configs:
  + drop win fonts
  + added Droid

* Sun Dec 13 2009 Valery Inozemtsev <shrek@altlinux.ru> 2.8.0-alt2
- prefer Liberation before Dejavu

* Thu Nov 19 2009 Valery Inozemtsev <shrek@altlinux.ru> 2.8.0-alt1
- 2.8.0

* Mon Nov 09 2009 Valery Inozemtsev <shrek@altlinux.ru> 2.7.3-alt1
- 2.7.3

* Tue Sep 01 2009 Valery Inozemtsev <shrek@altlinux.ru> 2.7.2-alt1
- 2.7.2

* Wed Aug 26 2009 Valery Inozemtsev <shrek@altlinux.ru> 2.7.1-alt2
- fixed bug in FcLangSetContains

* Tue Jul 28 2009 Valery Inozemtsev <shrek@altlinux.ru> 2.7.1-alt1
- 2.7.1

* Wed Jun 24 2009 Valery Inozemtsev <shrek@altlinux.ru> 2.7.0-alt1
- 2.7.0

* Tue Jan 06 2009 Valery Inozemtsev <shrek@altlinux.ru> 2.6.0-alt3
- fc-conf: added lcdfilter settings

* Sat Nov 22 2008 Valery Inozemtsev <shrek@altlinux.ru> 2.6.0-alt2
- removed obsolete %%post_ldconfig/%%postun_ldconfig calls

* Sun Jun 01 2008 Valery Inozemtsev <shrek@altlinux.ru> 2.6.0-alt1
- 2.6 release

* Sun May 25 2008 Valery Inozemtsev <shrek@altlinux.ru> 2.5.93-alt1
- 2.6 RC3

* Sun May 04 2008 Valery Inozemtsev <shrek@altlinux.ru> 2.5.92-alt1
- 2.6 RC2

* Thu Jan 10 2008 Valery Inozemtsev <shrek@altlinux.ru> 2.5.91-alt1
- 2.6 RC1

* Thu Dec 13 2007 Valery Inozemtsev <shrek@altlinux.ru> 2.5.0-alt2
- FcOpNotContains should use strstr, not strcmp on strings

* Wed Nov 14 2007 Valery Inozemtsev <shrek@altlinux.ru> 2.5.0-alt1
- 2.5.0
- introduced FC_2.5 ABI interface for new functions in libfontconfig.so.1

* Tue Nov 06 2007 Valery Inozemtsev <shrek@altlinux.ru> 2.4.92-alt1
- 2.5 RC2

* Fri Oct 26 2007 Valery Inozemtsev <shrek@altlinux.ru> 2.4.91-alt1
- 2.5 RC1

* Tue Aug 07 2007 Valery Inozemtsev <shrek@altlinux.ru> 2.4.2-alt3
- added fc-conf utility, see fc-conf --help

* Mon Aug 06 2007 Valery Inozemtsev <shrek@altlinux.ru> 2.4.2-alt2
- added fontconfig-2.4.2-git-FcDirCacheUnlink-bug11756.patch:
  + Free temporary string in FcDirCacheUnlink

* Thu Aug 02 2007 Valery Inozemtsev <shrek@altlinux.ru> 2.4.2-alt1
- 2.4.2
- introduced FC_2.4 ABI interface for new functions in libfontconfig.so.1
- remove deprecated /usr/X11R6/lib/X11/fonts
- set default fonts dir to %%_datadir/fonts
- updated build dependencies

* Tue May 22 2007 Sergey V Turchin <zerg at altlinux dot org> 2.3.2-alt10
- update font aliases; thanks shrek@alt

* Fri May 18 2007 Sergey V Turchin <zerg at altlinux dot org> 2.3.2-alt9
- add font aliases for DejaVu fonts

* Mon Apr 16 2007 ALT QA Team Robot <qa-robot@altlinux.org> 2.3.2-alt8.0
- Automated rebuild.

* Mon May 15 2006 Sergey V Turchin <zerg at altlinux dot org> 2.3.2-alt8
- add patch to don't use freetype internals 

* Mon Mar 20 2006 Sergey V Turchin <zerg at altlinux dot org> 2.3.2-alt7
- add entire %%_datadir/fonts/bitmap

* Fri Dec 30 2005 Sergey V Turchin <zerg at altlinux dot org> 2.3.2-alt6
- add %%_datadir/fonts/bitmap/terminus

* Fri Dec 16 2005 Sergey V Turchin <zerg at altlinux dot org> 2.3.2-alt5
- add /usr/share/fonts/otf to search paths

* Tue Dec 13 2005 Sergey V Turchin <zerg at altlinux dot org> 2.3.2-alt4
- remove /usr/X11R6/lib/X11/fonts/urw-ttf from search paths
- add /usr/share/fonts/bitmap/misc,/usr/share/fonts/ttf,/usr/share/fonts/type1
  to search paths

* Sat Sep 10 2005 Alexey Tourbin <at@altlinux.ru> 2.3.2-alt3
- NMU: introduced FC_2.3 ABI interface for new functions in libfontconfig.so.1

* Fri Aug 05 2005 Sergey V Turchin <zerg at altlinux dot org> 2.3.2-alt2
- add Misc Fixed to monospace alias

* Thu Jun 02 2005 Sergey V Turchin <zerg at altlinux dot org> 2.3.2-alt1
- new version
- merge configuration/patches from SuSE

* Fri Mar 18 2005 Sergey V Turchin <zerg at altlinux dot org> 2.3.0-alt1
- new version

* Thu Oct 21 2004 Sergey V Turchin <zerg at altlinux dot org> 2.2.3-alt1
- new version

* Thu Jun 17 2004 Sergey V Turchin <zerg at altlinux dot org> 2.2.2-alt4
- remove /usr/X11R6/lib/X11/fonts/Type1 from fonts.conf

* Thu Jun 17 2004 Sergey V Turchin <zerg at altlinux dot org> 2.2.2-alt3
- fix %%post

* Tue May 25 2004 Sergey V Turchin <zerg at altlinux dot org> 2.2.2-alt2
- prefer XLinSans before Numbus
- prefer MS Fonts before Fixed

* Thu May 20 2004 Sergey V Turchin <zerg at altlinux dot org> 2.2.2-alt1
- new version
- merge configuration scheme from SuSE

* Mon Feb 09 2004 Sergey V Turchin <zerg at altlinux dot org> 2.2.1-alt5
- fix path to ms-fonts-ttf

* Tue Dec 02 2003 Dmitry V. Levin <ldv@altlinux.org> 2.2.1-alt4
- Ignore .fulldir entries from earlier versions 'dircache' fix (RH).
- Don't read from/write to NULL cache files (RH).
- Do not package .la files.

* Thu Oct 30 2003 AEN <aen@altlinux.ru> 2.2.1-alt3
- XLinSans is preferable Sans now

* Wed Jul 16 2003 AEN <aen@altlinux.ru> 2.2.1-alt2
- old fonts.conf restored

* Wed Jun 18 2003 AEN <aen@altlinux.ru> 2.2.1-alt1
- 2.2.1
- mhz patches & spec

* Wed Jun 11 2003 Mikhail Zabaluev <mhz@altlinux.ru> 2.2.0-alt0.1
- New version
- Patch3 gone upstream
- Use default config with known-good preconfigured paths
- Disabled doc build broken too badly
- Cleaned up filelist
- Optional devel-static subpackage

* Sat Apr 12 2003 AEN <aen@altlinux.ru> 2.1-alt2
- dircahce patch from RH

* Fri Feb 28 2003 AEN <aen@altlinux.ru> 2.1-alt1
- new version

* Fri Jan 17 2003 AEN <aen@altlinux.ru> 2.0-alt12
- desplitting

* Sun Jan 05 2003 AEN <aen@altlinux.ru> 2.0-alt11
- lib%name required %name

* Wed Nov 20 2002 AEN <aen@altlinux.ru> 2.0-alt10
- path to jdk-fonts added to fonts.conf

* Wed Nov 20 2002 Mikhail Zabaluev <mhz@altlinux.ru> 2.0-alt9.1mhz
- libification (again)
- remove src/fclang.o to rebuild just it instead of all-out make clean

* Wed Nov 13 2002 AEN <aen@altlinux.ru> 2.0-alt9
- build fixed

* Tue Oct 15 2002 AEN <aen@altlinux.ru> 2.0-alt8
- XLinSans & CourierCyr added to fonts.conf

* Fri Oct 11 2002 AEN <aen@altlinux.ru> 2.0-alt7
- fonts.conf changed again

* Thu Oct 10 2002 AEN <aen@altlinux.ru> 2.0-alt6
- ru.orth fix
- lang.h build

* Tue Oct 08 2002 AEN <aen@altlinux.ru> 2.0-alt5
- gww-ttf removed from fonts.conf

* Fri Oct 04 2002 AEN <aen@altlinux.ru> 2.0-alt4
- fonts.conf fixed

* Fri Oct 04 2002 AEN <aen@altlinux.ru> 2.0-alt3
- patches & %post from RH

* Mon Sep 23 2002 AEN <aen@altlinux.ru> 2.0-alt2
- %files fixed

* Wed Sep 18 2002 AEN <aen@altlinux.ru> 2.0-alt1
- release

* Tue Jul 02 2002 AEN <aen@logic.ru> 0.0.1-alt1
- first build for Sisyphus
- config patch (alt specific)

* Tue Jun 18 2002 Owen Taylor <otaylor@redhat.com>
- Fix crash from FcObjectSetAdd

* Tue Jun 11 2002 Owen Taylor <otaylor@redhat.com>
- make fonts.conf %%config, not %%config(noreplace)
- Another try at the CJK aliases
- Add some CJK fonts to the config
- Prefer Luxi Mono to Nimbus Mono

* Mon Jun 10 2002 Owen Taylor <otaylor@redhat.com>
- New upstream version
- Fix matching for bitmap fonts

* Mon Jun  3 2002 Owen Taylor <otaylor@redhat.com>
- New version, new upstream mega-tarball

* Tue May 28 2002 Owen Taylor <otaylor@redhat.com>
- Fix problem with FcConfigSort

* Fri May 24 2002 Owen Taylor <otaylor@redhat.com>
- Initial specfile


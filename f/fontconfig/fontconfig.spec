%ifndef xmlcatalog
%define xmlcatalog %_sysconfdir/xml/catalog
%endif
%define xmlcatalog_bin %_bindir/xmlcatalog
%define docdir %_docdir/%name
%define sover 1
%define libfontconfig libfontconfig%sover

Name: fontconfig
Version: 2.14.2
Release: alt3

Summary: Font configuration and customization utilities and library
Group: System/Configuration/Other
License: MIT
Url: http://fontconfig.org/
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Source: %name-%version.tar
Source1: fontconfig-firsttime
Source2: fontconfig.filetrigger
# FC
Patch1: fontconfig-sleep-less.patch
Patch2: fontconfig-drop-lang-from-pkgkit-format.patch
# ALT
Patch11: alt-symbols-map.patch
Patch12: alt-config.patch
Patch13: alt-fc-conf.patch
Patch14: alt-disable-postscript-aliases.patch

Provides: lib%name = %version
Obsoletes: lib%name < %version
BuildRequires(pre): rpm-build-ubt
BuildRequires: docbook-utils elinks gperf libexpat-devel libfreetype-devel libuuid-devel

%description
Fontconfig is designed to locate fonts within the system and
select them according to requirements specified by applications.

%package -n %libfontconfig
Summary: Library for Font Configuration
Group: System/Libraries
Obsoletes: fontconfig < 2.14.2
%description -n %libfontconfig
%name library.

%package devel
Summary: Development files for font configuration and customization library
Group: Development/C
Requires: %name = %version-%release

%description devel
This package includes the fontconfig header files and developer
documentation required for development of fontconfig-based software.

%prep
%setup
%patch1 -p1
%patch2 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1
%autoreconf

%build
%configure \
	--disable-static \
	--with-baseconfigdir=%_sysconfdir/fonts \
	--with-default-fonts=%_datadir/fonts \
	--with-cache-dir=%_var/cache/%name \
	--docdir=%docdir \
	--with-default-hinting=full \
	--with-default-sub-pixel-rendering=rgb \
	#

%make PDF_FILES=

%install
%make DESTDIR=%buildroot PDF_FILES= install
install -pm644 AUTHORS README %buildroot%docdir/

> %buildroot%_sysconfdir/fonts/local.conf
install -Dp -m755 %SOURCE1 %buildroot%_sysconfdir/firsttime.d/%name
install -Dp -m755 %SOURCE2 %buildroot%_rpmlibdir/%name.filetrigger

for f in $(ls %buildroot%_datadir/%name/conf.avail/1*.conf | sed -ne 's|\(.*/\)\(.*conf\)|\2|p'); do
	ln -sf ../../../%_datadir/%name/conf.avail/$f %buildroot%_sysconfdir/fonts/conf.d/$f
done

# add compatibility symlinks
find %buildroot/%_datadir/%name/conf.avail/ -type f -name \*.conf | sed -e 's|^.*/||' | \
while read CONF ; do
    ln -sr %buildroot/%_datadir/%name/conf.avail/$CONF %buildroot/%_sysconfdir/fonts/conf.avail/$CONF
done
find %buildroot/%_sysconfdir/fonts/conf.avail/ -type f -name \*.conf | sed -e 's|^.*/||' | \
while read CONF ; do
    ln -sr %buildroot/%_sysconfdir/fonts/conf.avail/$CONF %buildroot/%_datadir/%name/conf.avail/$CONF
done

%find_lang --output=%name.lang --append fontconfig fontconfig-conf

%post
XMLCATALOG_BIN=%xmlcatalog_bin
if [ -e %xmlcatalog -a -x $XMLCATALOG_BIN ]; then
  %xmlcatalog_bin --noout --add system \
    "urn:fontconfig:fonts.dtd" \
    "file://%_datadir/xml/fontconfig/fonts.dtd" \
    %xmlcatalog ||:
fi
[ -n "$DURING_INSTALL" ] || %_sysconfdir/firsttime.d/%name ||:

%postun
XMLCATALOG_BIN=%xmlcatalog_bin
if [ -e %xmlcatalog -a -x $XMLCATALOG_BIN ]; then
  %xmlcatalog_bin --noout --del system \
    "urn:fontconfig:fonts.dtd" \
    "file://%_datadir/xml/fontconfig/fonts.dtd" \
    %xmlcatalog ||:
fi

%files -f %name.lang
%_sysconfdir/firsttime.d/%name
%dir %_sysconfdir/fonts
%dir %_sysconfdir/fonts/conf.d
%dir %_sysconfdir/fonts/conf.avail
%config %_sysconfdir/fonts/fonts.conf
%config(noreplace) %_sysconfdir/fonts/conf.avail/*.conf
%_sysconfdir/fonts/conf.d/README
%_sysconfdir/fonts/conf.d/[2-9]*.conf
%config(noreplace) %_sysconfdir/fonts/conf.d/10-yes-antialias.conf
%config(noreplace) %_sysconfdir/fonts/conf.d/10-hinting.conf
%config(noreplace) %_sysconfdir/fonts/conf.d/10-hinting-full.conf
%config(noreplace) %_sysconfdir/fonts/conf.d/10-sub-pixel-rgb.conf
%config(noreplace) %_sysconfdir/fonts/conf.d/11-lcdfilter-default.conf
%ghost %_sysconfdir/fonts/conf.d/10-autohint.conf
%ghost %_sysconfdir/fonts/conf.d/10-no-antialias.conf
%ghost %_sysconfdir/fonts/conf.d/10-scale-bitmap-fonts.conf
%ghost %_sysconfdir/fonts/conf.d/10-hinting-slight.conf
%ghost %_sysconfdir/fonts/conf.d/10-hinting-medium.conf
%ghost %_sysconfdir/fonts/conf.d/10-hinting-none.conf
%ghost %_sysconfdir/fonts/conf.d/10-sub-pixel-none.conf
%ghost %_sysconfdir/fonts/conf.d/10-sub-pixel-bgr.conf
%ghost %_sysconfdir/fonts/conf.d/10-sub-pixel-vbgr.conf
%ghost %_sysconfdir/fonts/conf.d/10-sub-pixel-vrgb.conf
%ghost %_sysconfdir/fonts/conf.d/10-unhinted.conf
%ghost %_sysconfdir/fonts/conf.d/11-lcdfilter-legacy.conf
%ghost %_sysconfdir/fonts/conf.d/11-lcdfilter-light.conf
%ghost %_sysconfdir/fonts/conf.d/11-lcdfilter-none.conf
%ghost %config(missingok,noreplace) %_sysconfdir/fonts/local.conf
%_bindir/fc-*
%_rpmlibdir/%name.filetrigger
%_datadir/%name
%_datadir/xml/%name
%_man1dir/*
%_man5dir/*
%dir %_var/cache/%name
%docdir
%exclude %docdir/%name-devel*

%files -n %libfontconfig
%_libdir/libfontconfig.so.%sover
%_libdir/libfontconfig.so.*

%files devel
%_libdir/*.so
%_pkgconfigdir/*.pc
%_includedir/*
%_man3dir/*
%dir %docdir
%docdir/%name-devel*
%_datadir/gettext/its/fontconfig.*

%changelog
* Wed Mar 22 2023 Sergey V Turchin <zerg@altlinux.org> 2.14.2-alt3
- fix upgrade on x86_64-i586

* Fri Mar 03 2023 Sergey V Turchin <zerg@altlinux.org> 2.14.2-alt2
- prefer Noto fonts

* Tue Feb 07 2023 Sergey V Turchin <zerg@altlinux.org> 2.14.2-alt1
- new version
- split library into separate package

* Tue Feb 07 2023 Sergey V Turchin <zerg@altlinux.org> 2.13.1-alt5
- prefer Droid fonts

* Mon Jul 25 2022 Sergey V Turchin <zerg@altlinux.org> 2.13.1-alt4
- using grep instead of egrep for rpm filetrigger (closes: 43328)

* Wed Feb 02 2022 Sergey V Turchin <zerg@altlinux.org> 2.13.1-alt3
- register font.dtd in system xml catalog (closes: 41849)

* Wed Aug 18 2021 Sergey V Turchin <zerg@altlinux.org> 2.13.1-alt2
- fix build requires

* Wed Oct 31 2018 Sergey V Turchin <zerg@altlinux.org> 2.13.1-alt1
- new version

* Thu Sep 21 2017 Sergey V Turchin <zerg@altlinux.org> 2.12.6-alt1%ubt
- new version

* Thu Aug 10 2017 Sergey V Turchin <zerg@altlinux.org> 2.12.4-alt1%ubt
- new version

* Wed Apr 12 2017 Sergey V Turchin <zerg@altlinux.org> 2.12.1-alt2%ubt
- add fixes for new glibc and gperf

* Fri Aug 12 2016 Sergey V Turchin <zerg@altlinux.org> 2.12.1-alt1
- new version

* Tue Nov 10 2015 Sergey V Turchin <zerg@altlinux.org> 2.11.1-alt4
- increase priority of alt-post-user.conf (ALT#31462)

* Mon Aug 11 2014 Sergey V Turchin <zerg@altlinux.org> 2.11.1-alt2.M70P.1
- built for M70P

* Wed Jul 23 2014 Sergey V Turchin <zerg@altlinux.org> 2.11.1-alt3
- sync patches with FC

* Thu Jul 10 2014 Sergey V Turchin <zerg@altlinux.org> 2.11.1-alt2
- by default turn on antialias lcdfilter-default hinting style-full sub-pixel-rgb
- by default decrease ms fonts priority

* Wed Mar 26 2014 Sergey V Turchin <zerg@altlinux.org> 2.11.1-alt0.M70P.1
- built for M70P

* Wed Mar 26 2014 Sergey V Turchin <zerg@altlinux.org> 2.11.1-alt1
- new version

* Wed Mar 12 2014 Sergey V Turchin <zerg@altlinux.org> 2.11.0-alt4
- don't fail post-script with broken freetype

* Thu Feb 06 2014 Sergey V Turchin <zerg@altlinux.org> 2.11.0-alt2.M70P.1
- built for M70P

* Thu Feb 06 2014 Sergey V Turchin <zerg@altlinux.org> 2.11.0-alt3
- disable only Nimbus fonts for PostScript aliases (ALT#26768)

* Mon Nov 11 2013 Sergey V Turchin <zerg@altlinux.org> 2.11.0-alt1.M70P.1
- built for M70P

* Mon Nov 11 2013 Sergey V Turchin <zerg@altlinux.org> 2.11.0-alt2
- add patch from FC to decrease sleep in fc-cache

* Wed Oct 23 2013 Sergey V Turchin <zerg@altlinux.org> 2.11.0-alt0.M70P.1
- built for M70P

* Thu Oct 17 2013 Sergey V Turchin <zerg@altlinux.org> 2.11.0-alt1
- new version

* Thu Oct 17 2013 Sergey V Turchin <zerg@altlinux.org> 2.10.95-alt3
- fix apply patch for ALT#26768

* Mon Sep 23 2013 Sergey V Turchin <zerg@altlinux.org> 2.10.95-alt2
- disable PostScript aliases by default (ALT#26768)

* Fri Sep 13 2013 Sergey V Turchin <zerg@altlinux.org> 2.10.95-alt1
- 2.11 RC5

* Thu Jun 20 2013 Sergey V Turchin <zerg@altlinux.org> 2.10.93-alt2
- update own configs according upstream config changes

* Fri May 31 2013 Sergey V Turchin <zerg@altlinux.org> 2.10.93-alt1
- 2.11 RC3

* Mon May 06 2013 Sergey V Turchin <zerg@altlinux.org> 2.10.92-alt1
- 2.11 RC2

* Tue Apr 30 2013 Sergey V Turchin <zerg@altlinux.org> 2.10.91-alt7
- non't use assign instead of append for sub-pixel rendering
  because configs was fixed

* Thu Mar 28 2013 Sergey V Turchin <zerg@altlinux.org> 2.10.91-alt6
- add upstream fix against broken sort order with FcFontSort()

* Wed Mar 27 2013 Sergey V Turchin <zerg@altlinux.org> 2.10.91-alt5
- add upstream fix against broken 10-autohint.conf and 10-unhinted.conf (ALT#28620)

* Tue Mar 19 2013 Sergey V Turchin <zerg@altlinux.org> 2.10.91-alt4
- use assign instead of append for sub-pixel rendering default config
  to return fine fonts look

* Wed Feb 20 2013 Sergey V Turchin <zerg@altlinux.org> 2.10.91-alt3
- add compatibility config symlinks (ALT #28555)

* Wed Feb 13 2013 Valery Inozemtsev <shrek@altlinux.ru> 2.10.91-alt2
- updated to master git.72b0480

* Fri Jan 11 2013 Valery Inozemtsev <shrek@altlinux.ru> 2.10.91-alt1
- 2.11 RC1

* Wed Nov 28 2012 Valery Inozemtsev <shrek@altlinux.ru> 2.10.2-alt1
- 2.10.2

* Wed Jul 18 2012 Valery Inozemtsev <shrek@altlinux.ru> 2.10.0-alt1
- 2.10.0

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


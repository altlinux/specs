Name: grip
Version: 3.1.3
Release: alt14
Epoch: 20111008

Summary: an audio ripper/encoder front-end
License: GPL
Group: Sound

Url: http://www.nostatic.org/grip
Source0: %url/%name-%version.tar.gz
Source1: %name-icons.tar.bz2
Source2: %name.desktop
Source3: %name.1
Source4: %name-3.1.1-ru.po
Patch0: grip-2.99.2-ogg.patch.bz2
Patch1: grip-3.0.5-blind-write-fix.patch.bz2
#Patch2: grip-alt-i18n.patch.bz2
Patch3: grip-3.1.1-sf-rip_next_cd.patch
#Patch4: grip-3.1.1-alt-year-update.patch
Patch5: grip-3.1.2-alt-term.patch
Patch6: grip-3.1.2-alt-vte_2.1.patch
Patch7: grip-3.1.2-g_conv.patch
Patch10: grip-3.1.3-buffer.patch
Patch11: grip-3.1.3-alt-cdpath.patch
Packager: Michael Shigorin <mike@altlinux.org>

Summary(ru_RU.KOI8-R): графическая утилита для извлечения/сжатия треков AudioCD
Summary(uk_UA.KOI8-U): граф╕чна утил╕та для витягування/кодування AudioCD

%define id3lib_ver 3.8.1

Requires: id3lib >= %id3lib_ver
Requires: vorbis-tools

# Automatically added by buildreq on Thu May 15 2008
BuildRequires: gcc-c++ id3lib-devel libcdparanoia-devel libghttp-devel libgnomeui-devel libvte-devel

BuildRequires: libvte-devel >= 0.11.0-alt2
BuildRequires: libghttp-devel >= 1.0.9-alt3
# due to libid3, see src/cppmain.cc
BuildRequires: libstdc++-devel

%ifarch %ix86
BuildRequires: libcdparanoia-devel
Requires: libcdparanoia
%endif

BuildPreReq: id3lib-devel >= %id3lib_ver

# NOTE to the next maintainer, if any:
# grip-3.1.4 or so fixed compatibility with broken freedb spec
# (which is all fine in theory except that they've got loads of
# records in cp1251 marked as iso8859-1) -- so if you would like
# to update to latest version (dated 2005 as of 20090606), please
# do test it extensively and/or ask freedb folks if they have
# located and fixed such broken records; you might also want
# to package this version with dfo@'s charset conversion patch
# along with updated one.  Thanks for attention and patience.
# -- mike@

%description
Grip is a GNOME-based cd-player and cd-ripper. It has the ripping
capabilities of cdparanoia builtin, but can also use external
rippers (such as cdda2wav).
It also provides an automated frontend for MP3 encoders, letting
you take a disc and transform it easily straight into MP3s.
The CDDB protocol is supported for retrieving track information
from disc database servers.  Grip works with DigitalDJ to provide
a unified "computerized" version of your music collection.

%description -l ru_RU.KOI8-R
Grip - CD-проигрыватель для GNOME с возможностью извлечения и сжатия
аудиотреков.  Может использовать встроенную cdparanoia или внешний
обработчик; для сжатия можно применять несколько внешних кодеков.
Также поддерживается CDDB.

Возможна совместная работа с DigitalDJ для унификации коллекции.

%description -l uk_UA.KOI8-U
Grip - CD-прогавач та витягувач для GNOME.  Може використовувати
вбудовану cdparanoia чи зовн╕шню програму; для кодування можна
застосовувати дек╕лька зовн╕шн╕х кодек╕в.  Також п╕дтриму╓ться
CDDB.

Можлива сум╕сна робота з DigitalDJ для ун╕ф╕кац╕╖ колекц╕╖.

%prep
%setup
%patch0 -p0 -b .tv
%patch1 -p1 -b .blind-write-fix
%patch3 -p1 -b .ripnext
%patch10 -p1 -b .buffer
%patch11 -p1 -b .cdpath

%build
export CFLAGS="$CFLAGS -g"
%configure 
%make_build

%install
%makeinstall

mkdir -p %buildroot{%_miconsdir,%_niconsdir,%_liconsdir}
tar xjf %SOURCE1 -C %buildroot%_niconsdir
mv %buildroot%_iconsdir/hicolor/32x32/apps/mini/grip.xpm \
	%buildroot%_miconsdir/
mv %buildroot%_iconsdir/hicolor/32x32/apps/large/grip.xpm \
	%buildroot%_liconsdir/

install -pDm644 %SOURCE2 %buildroot%_desktopdir/%name.desktop
install -pDm644 %SOURCE3 %buildroot%_man1dir/%name.1
install -pm644 %SOURCE4 $RPM_BUILD_DIR/%name-%version/po/

%find_lang %name-2.2

%files -f %name-2.2.lang
%doc AUTHORS CREDITS ChangeLog README TODO
%_bindir/*
%_man1dir/*
%_miconsdir/*.xpm
%_niconsdir/*.xpm
%_liconsdir/*.xpm
%_desktopdir/%name.desktop
%_datadir/pixmaps/*
%_datadir/gnome/help/%name/
%_datadir/applications/*

%changelog
* Sat Oct 08 2011 Michael Shigorin <mike@altlinux.org> 20111008:3.1.3-alt14
- replaced /dev/cdrom default with /dev/sr0 (closes: #25529)

* Sun Mar 27 2011 Michael Shigorin <mike@altlinux.org> 20110327:3.1.3-alt13
- added missing BR:
- minor spec cleanup

* Sat Jun 06 2009 Michael Shigorin <mike@altlinux.org> 20090606:3.1.3-alt12
- fixed desktop file
  + taken from 3.3.1
  + dropped broken zh_* non-utf8 strings
  + added ru strings
  + fixed/added categories
- fixed pixmaps locations

* Tue Jun 02 2009 Michael Shigorin <mike@altlinux.org> 20090602:3.1.3-alt11
- rebuilt against current libvte

* Thu May 21 2009 Michael Shigorin <mike@altlinux.org> 20090521:3.1.3-alt10
- added desktop categories to stock desktop file (fixes: #20129)

* Wed May 13 2009 Michael Shigorin <mike@altlinux.org> 20090513:3.1.3-alt9
- fixed FTBFS

* Wed Dec 03 2008 Michael Shigorin <mike@altlinux.org> 20081203:3.1.3-alt8
- applied repocop patch

* Mon Sep 08 2008 Michael Shigorin <mike@altlinux.org> 20080908:3.1.3-alt7
- removed Debian menu support (#17048)

* Thu May 15 2008 Michael Shigorin <mike@altlinux.org> 20080515:3.1.3-alt6
- buildreq
- spec macro abuse cleanup

* Tue Jan 30 2007 Michael Shigorin <mike@altlinux.org> 20070130:3.1.3-alt5
- manual rebuild against current libgnome
  (thanks akhavr@ for noticing)

* Fri Oct 13 2006 Michael Shigorin <mike@altlinux.org> 20061013:3.1.3-alt4
- manual rebuild against current libvte
  (thanks dobr@ for reminding)

* Thu Jun 01 2006 Michael Shigorin <mike@altlinux.org> 20060601:3.1.3-alt3
- fixed oooold Epoch: mistake to allow auto rebuilds (#9643)
- fixed cosmetic trouble with description (#5535)
- Please Note: there seem to be no apparent updates of this package
  by me since I have little interest in it now; any future maintainer
  should carefully examine both bugzilla.altlinux.org records for grip
  and patches by dfo@.  3.2.0+ were fixed so that freedb.org's spec
  would be met but alas -- the freedb's content violates the spec itself
  thus breaking fully correct clients.  So from practical standpoint
  older grip with charset recoding was chosen over current, correct,
  but broken one.

* Fri Mar 11 2005 Michael Shigorin <mike@altlinux.ru> 20050311:3.1.3-alt2
- added fix for CDDB data buffer overflow problem
  (remote but hardly exploitable in the real world);
  thanks Dmitry Levin (ldv@) for notifying
  and Sergey Pinaev (dfo@) for backporting

* Tue Jan 18 2005 ALT QA Team Robot <qa-robot@altlinux.org> 20050118:3.1.3-alt1.1.1
- Rebuilt with libstdc++.so.6.

* Tue May 11 2004 ALT QA Team Robot <qa-robot@altlinux.org> 20040511:3.1.3-alt1.1
- Rebuilt with openssl-0.9.7d.

* Wed Nov 05 2003 Michael Shigorin <mike@altlinux.ru> 20031105:3.1.3-alt1
- 3.1.3
- patch5, patch6, patch7 merged to upstream

* Fri Oct 31 2003 Michael Shigorin <mike@altlinux.ru> 20031031:3.1.2-alt6
- new patch7, updated patch6: hopefully fixed #3204

* Mon Oct 27 2003 Michael Shigorin <mike@altlinux.ru> 20031027:3.1.2-alt5
- fixed #3201 (patch5, patch6); thanks to Dmitry Vukolov (dav@)
  for both reporting and fixing the problem, again!

* Sat Oct 25 2003 Michael Shigorin <mike@altlinux.ru> 3.1.2-alt4
- fixed buildrequires (versionized libghttp, removed superfluous
  gcc-g77); thanks to Dmitry Vukolov (dav@).

* Wed Oct 22 2003 Michael Shigorin <mike@altlinux.ru> 3.1.2-alt3
- rebuilt against libghttp-1.0.9-alt3 (=> some spec cleanup)

* Fri Oct 10 2003 Michael Shigorin <mike@altlinux.ru> 3.1.2-alt2
- rebuilt against libvte-0.11.10-alt2

* Thu Oct 09 2003 Michael Shigorin <mike@altlinux.ru> 3.1.2-alt1
- patch2, patch4 included in upstream
- patch3 *seemingly* redone in upstream too?
- updated BuildRequires

* Sun Sep 28 2003 Michael Shigorin <mike@altlinux.ru> 3.1.1-alt6
- fixed #3065; thanks to Dmitry Vukolov (dav@) for both
  report and patch

* Sun Sep 28 2003 Michael Shigorin <mike@altlinux.ru> 3.1.1-alt5
- fixed #3059

* Wed Sep 24 2003 Michael Shigorin <mike@altlinux.ru> 3.1.1-alt4
- added patch #802562 from sf.net/projects/grip page
  (should fix "rips only first CD" problem)

* Thu Sep 04 2003 Michael Shigorin <mike@altlinux.ru> 3.1.1-alt3
- updated i18n patch by Sergey Pinaev <dfo antex ru>
- includes tag recoding
- new macros substituted by data recoded to ID3 encoding specifed
  (for use with external programs):
  * %%N: The name of the track
  * %%z: The artist name for the track
  * %%Z: The artist name for the disc
  * %%D: The name of the disc

* Fri Aug 29 2003 Michael Shigorin <mike@altlinux.ru> 3.1.1-alt2
- "i18n maintenance build" :-)
  * fixed lost (renamed in upstream) .mo files
    (thanks to Sviatoslav Sviridov <svd@>)
  * added i18n patch by Sergey Pinaev <dfo antex ru>
  * somewhat updated translation
- removed obsolete "Obsoletes: gcd" (see also 2.98.7-alt1)
- spec cleanup

* Thu Aug 15 2003 Michael Shigorin <mike@altlinux.ru> 3.1.1-alt1
- 3.1.1
- merges some Cooker spec features as well as manpage and two patches
- thanks to Alexey Tourbin (at@) for robust workaround for ghttp.h :)

* Thu Apr 24 2003 Michael Shigorin <mike@altlinux.ru> 3.0.7-alt1
- 3.0.7 (minor bigfixes)

* Fri Mar 21 2003 Michael Shigorin <mike@altlinux.ru> 3.0.6-alt1
- 3.0.6
- built with new id3lib

* Fri Jan 31 2003 Stanislav Ievlev <inger@altlinux.ru> 3.0.5-alt1.1
- rebuild with new id3 lib

* Tue Jan 14 2003 Michael Shigorin <mike@altlinux.ru> 3.0.5-alt1
- 3.0.5
- ru.po patch unneeded

* Thu Jan 09 2003 Michael Shigorin <mike@altlinux.ru> 3.0.4-alt2
- ru.po got aesthetic cleanup (sent to upstream and author)

* Thu Jan 02 2003 Michael Shigorin <mike@altlinux.ru> 3.0.4-alt1
- 3.0.4
- patch1 unneeded (upstream fixed)
- small spec cleanup

* Wed Nov 20 2002 AEN <aen@altlinux.ru> 3.0.3-alt3
- ru.po fixed

* Wed Nov 13 2002 Andrey Astafiev <andrei@altlinux.ru> 3.0.3-alt2
- rebuilt with gcc3.2.
- added Packager tag.

* Mon Sep 30 2002 Michael Shigorin <mike@altlinux.ru> 3.0.3-alt1
- 3.0.3
- minor bugfixes
- lame dependency removed

* Tue Jun 18 2002 Michael Shigorin <mike@altlinux.ru> 3.0.1-alt1
- 3.0.1
- removed %_datadir/gnome/help/%name from %files (duplicated entries)

* Sat May 25 2002 Yuri N. Sedunov <aris@altlinux.ru> 3.0.0-alt1
- 3.0.0
- built with new id3lib-3.8pre2.

* Fri Apr 12 2002 Andrey Astafiev <andrei@altlinux.ru> 2.99.3-alt1
- 2.99.3.

* Tue Mar 19 2002 Andrey Astafiev <andrei@altlinux.ru> 2.99.0-alt1
- 2.99.0.

* Tue Feb 26 2002 Andrey Astafiev <andrei@altlinux.ru> 2.98.7-alt1
- 2.98.7.
- GCD removed.
- Various spec updates.

* Wed Aug 29 2001 Dmitry V. Levin <ldv@altlinux.ru> 2.96-alt2
- Merged mdk patches.

* Thu Aug 02 2001 Grigory Milev <week@altlinux.ru> 2.96-alt1
- new release
- Some spec clean up

* Thu Jan 18 2001 Dmitry V. Levin <ldv@fandra.org> 2.95-ipl3mdk
- RE adaptions.

* Wed Nov 29 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 2.95-3mdk
- recompile to s/oggvorbis/vorbis-tools

* Fri Nov 24 2000 dam's <damien@mandrakesoft.com> 2.95-2mdk
- corrected menu to make rpmlint happy.

* Tue Nov 07 2000 Thierry Vignaud <tvignaud@mandrakesoft.com> 2.95-1mdk
- new release
- fancyfication
- fix file list to prevent ownership on systemwide directories

* Thu Oct 05 2000 Daouda Lo <daouda@mandrakesoft.com> 2.94-4mdk
- provide ln icons.

* Wed Sep  6 2000 Frederic Lepied <flepied@mandrakesoft.com> 2.94-3mdk
- added oggenc support.

* Mon Aug 07 2000 Frederic Lepied <flepied@mandrakesoft.com> 2.94-2mdk
- automatically added BuildRequires

* Mon Jul 24 2000 Frederic Crozat <fcrozat@mandrakesoft.com> 2.94-1mdk
- release 2.94 (from helix)
- BM + macroszification

* Fri Jul 21 2000 dam's <damien@mandrakesoft.com> 2.93-2mdk
- BM + macrozification}

* Sun Apr 09 2000 Daouda Lo	<daouda@mandrakesoft.com> 2.93-1mdk
- release 2.93
* Wed Apr 5 2000 Lenny Cartier <lenny@mandrakesoft.com> 2.92-5mdk
- merge menu file with spec

* Tue Apr 4 2000 Warly <warly@mandrakesoft.com> 2.92-4mdk
- new icons

* Wed Mar 22 2000 Lenny Cartier <lenny@mandrakesoft.com> 2.92-3mdk
- fix permissions on archive files

* Thu Mar 21 2000 Lenny Cartier <lenny@mandrakesoft.com> 2.92-2mdk
- fix rpmlint warnings
- remove lame from grip rpm !!

* Mon Mar 20 2000 Lenny Cartier <lenny@mandrakesoft.com> 2.92-1mdk
- clean specfile
- add menu entry

* Thu Dec 30 1999 Frederic Lepied <flepied@mandrakesoft.com> 2.9-3mdk
- fix rpmlint reports.

* Wed Dec 15 1999 John Buswell <johnb@mandrakesoft.com>
- Put gcd back in
- Compressed man pages

* Mon Nov 15 1999 John Buswell <johnb@mandrakesoft.com>
- 2.9
- cleaned up spec file
- Build Release

* Mon Nov 08 1999 John Buswell <johnb@mandrakesoft.com>
- Mandrake adaptions
- Incorporated lame (mp3 encoder)
- Initial RPM
- Build Release

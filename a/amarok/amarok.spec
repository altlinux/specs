%define qtdir %_qt3dir
%define kdedir %_K3prefix

%def_disable final

Name: amarok
Version: 1.4.10
Release: alt14

Summary: Amarok is a music player for KDE.
License: GPL
Group: Sound
Url: http://amarok.kde.org/

Packager: Pavlov Konstantin <thresh@altlinux.ru>

%py_provides Publisher
Requires: %name-engine

Source0: ftp://ftp.kde.org/pub/kde/stable/amarok/%version/src/%name-%version.tar.bz2

Patch1: amarok-1.4.10-alt-ruby19.patch
Patch2: amarok-1.4.6-alt-playlist.patch
Patch3: amarok-1.4.9.1-alt-link.patch
Patch4: amarok-1.4.10-alt-ru_translation.patch
Patch5: amarok-1.4.7-alt-ru_desktop_translation.patch
Patch6: amarok-1.4.5-alt11553-collectionscanner.patch
Patch7: amarok-1.4.7-alt-player-icons.patch
Patch8: amarok-1.4.8-alt-libgpod_042.patch
Patch9: amarok-1.4.10-alt-mongrel.patch
Patch11: amarok-1.4.10-SA33505.patch
Patch10: amarok-1.4.9.1-libmtp-0.3.0-API.patch
Patch12: amarok-1.4.10-fix-FTBFS-gcc4.4.patch
Patch13: amarok-1.4.10-fix-automake-detection.patch
Patch14: 10_queuemedia.patch
Patch15: 11_bug403340_cancel_rename_when_deleting_items.diff
Patch16: 13_lastfm_crash_434835.diff
Patch17: 15_temptables_more_indices.diff
Patch18: 16_gnome_multimedia_keys.diff
Patch19: 17_xiph_audio_mimetypes.diff
Patch20: 18_add_lastfm_recommended_radio.diff
Patch22: 22_fix_wikipedia_tab.diff
Patch23: amarok-1.4.10-fix-autoconf-2.64.patch
Patch24: amarok-1.4.10-alt-gcc4.5.patch
Patch25: amarok-alt-malloc.patch
Patch26: amarok-alt-DSO.patch


BuildRequires: doxygen gcc4.5-c++ kdebase-devel libSDL-devel libXext-devel libXrender-devel libxml2-devel
BuildRequires: libXt-devel libavahi-devel libjpeg-devel libpng-devel libruby-devel
BuildRequires: libtag-devel libtunepimp-devel libusb-devel libvisual0.4-devel qt3-designer ruby xml-utils
BuildRequires: libxine-devel libmpeg4ip-devel libtunepimp-devel libgpod-devel libsqlite3-devel libmtp-devel
BuildRequires: libMySQL-devel postgresql-devel

%description
amaroK is an advanced audio player.
Excellent streaming support, audio effects, visualisations and smooth 
crossfading separate this player from existing KDE solutions. 
At the same time amaroK provides a very intuitive and quick user interface, 
with unparalleled playlist handling, optimized for very large playlists.
The built-in StreamBrowser makes finding web streams as easy as using a radio: 
you can pick your favorite program right inside of amaroK.

%description -l ru_RU.UTF-8
amaroK - передовой аудио плеер. Превосходная поддержка потокового воспроизведения, 
звуковые эффекты, визуализации. В то же самое время amaroK обеспечивает очень интуитивный
и быстрый пользовательский интерфейс. Плейлист оптимизирован для очень больших плейлистов.
Встроенный StreamBrowser делает обнаружение потоков в сети столь же легкими как и использование
радио: Вы можете выбрать и настроить их прямо в amaroK.

%package engine-xine
Summary: Xine engine for amaroK player
Group: Sound
Requires: %name = %version-%release
Provides: %name-engine

%description engine-xine
amarok-engine-xine is an engine for amaroK player.
It uses xine library for output sound stream.

%description engine-xine -l ru_RU.UTF-8
amarok-engine-xine - это движок для воспроизведения
звука для аудиоплеера amaroK. Он использует библиотеку
xine для вывода аудиопотока.

%package mediadevice-ipod
Summary: iPod plugin for amaroK player
Group: Sound
Requires: %name = %version-%release

%description mediadevice-ipod
amarok-mediadevice-ipod is a plugin for Apple iPod
player

%description mediadevice-ipod -l ru_RU.UTF-8
amarok-mediadevice-ipod - плагин, использующийся для
взаимодействия с плеером iPod от Apple

%package mediadevice-generic
Summary: VFAT plugin for amaroK player
Group: Sound
Requires: %name = %version-%release
Provides: %name-mediadevice-vfat

%description mediadevice-generic
amarok-mediadevice-generic is a generic plugin for
various devices that uses VFAT filesystem

%description mediadevice-generic -l ru_RU.UTF-8
amarok-mediadevice-generic - плагин, используемый для работы
с различного рода медиаустройствами, поддерживающими
тип файловой системы VFAT

%package mediadevice-daap
Summary: DAAP (Digital Audio Access Protocol) plugin for amaroK player
Group: Sound
Requires: %name = %version-%release

%description mediadevice-daap
amarok-mediadevice-daap is a plugin for interoperability
with various devices that uses Digital Audio Access
Protocol (DAAP)

%description mediadevice-daap -l ru_RU.UTF-8
amarok-mediadevice-daap - плагин для работы с различными
устройствами, использующими протокол Digital Audio Access
Protocol (DAAP)

%package mediadevice-mtp
Summary: MTP (Media Transfer Protocol) plugin for amaroK player
Group: Sound
Requires: %name = %version-%release

%description mediadevice-mtp
amarok-mediadevice-daap is a plugin for interoperability
with various devices that uses Media Transfer Protocol (MTP)

%description mediadevice-mtp -l ru_RU.UTF-8
amarok-mediadevice-daap - плагин для работы с различными
устройствами, использующими протокол Media Transfer Protocol (MTP)

%prep
%setup -q

%patch1 -p2
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p0
%patch11 -p1
%patch12 -p2
%patch13 -p2

%patch14 -p1
%patch15 -p1
%patch16 -p1
%patch17 -p1
%patch18 -p1
%patch19 -p1
%patch20 -p1
%patch22 -p1

%patch23 -p1
%patch24 -p2

%patch25 -p2
%patch26


cp -Rp /usr/share/libtool/aclocal/libtool.m4 admin/libtool.m4.in
cp -Rp /usr/share/libtool/config/ltmain.sh admin/ltmain.sh
%make -f admin/Makefile.common svn

%build
rm -rf %buildroot
export QTDIR=%qtdir
export KDEDIR=%kdedir

export PATH=$QTDIR/bin:$KDEDIR/bin:$PATH

export CPPFLAGS="$CPPFLAGS -I/usr/include/mpeg4 -I%_includedir/tqtinterface"

%K3configure \
	%{subst_enable final} \
	--enable-new-ldflags \
	--enable-gcc-hidden-visibility \
	--disable-debug \
	--disable-rpath \
	--with-xine \
	--with-mp4v2 \
	--with-musicbrainz \
	--with-libgpod \
	--with-libmtp \
	--with-daap \
	--with-included_sqlite \
	--without-ifp \
	--enable-postgresql \
	--enable-mysql

%make_build

%install
%K3install

rm -fr %buildroot%_K3datadir/apps/%name/scripts/templates

%K3find_lang --with-kde %name

%files -f %name.lang
%_K3bindir/amarok
%_K3bindir/amarokapp
%_K3bindir/amarok_libvisual
%_K3bindir/amarok_proxy.rb
%_K3bindir/amarokcollectionscanner
%_K3libdir/libamarok.so.*
%_K3libdir/kde3/libamarok_void-engine_plugin.so
%_K3libdir/kde3/konqsidebar_universalamarok.so
%_K3libdir/kde3/libamarok_massstorage-device.so
%_K3libdir/kde3/libamarok_nfs-device.so
%_K3libdir/kde3/libamarok_smb-device.so
/usr/share/kde/applications/kde/amarok.desktop
%dir %_K3datadir/apps/%name
%_K3datadir/apps/%name/data
%_K3datadir/apps/%name/icons
%_K3datadir/apps/%name/images
%_K3datadir/apps/%name/scripts
%_K3datadir/apps/%name/themes
%_K3datadir/apps/%name/*.rc
%_K3datadir/apps/konqueror/servicemenus/amarok_append.desktop
%_K3datadir/apps/konqueror/servicemenus/amarok_addaspodcast.desktop
%_K3datadir/apps/konqueror/servicemenus/amarok_play_audiocd.desktop
%_K3datadir/apps/konqsidebartng/add/amarok.desktop
%_K3datadir/apps/konqsidebartng/entries/amarok.desktop
%_K3datadir/apps/konqsidebartng/kicker_entries/amarok.desktop
%_K3datadir/apps/profiles/amarok.profile.xml
%_K3datadir/config/amarokrc
%_K3datadir/config.kcfg/amarok.kcfg
%_K3datadir/services/amaroklastfm.protocol
%_K3datadir/services/amarokitpc.protocol
%_K3datadir/services/amarokpcast.protocol
%_K3datadir/services/amarok_void-engine_plugin.desktop
%_K3datadir/services/amarok_massstorage-device.desktop
%_K3datadir/services/amarok_nfs-device.desktop
%_K3datadir/services/amarok_smb-device.desktop
%_K3datadir/servicetypes/amarok_plugin.desktop
%_K3datadir/servicetypes/amarok_codecinstall.desktop
%_kde3_iconsdir/*/*/apps/amarok.png
%lang(pt_BR) /usr/share/kde/doc/HTML/pt_BR/amarok

%files engine-xine
%_K3libdir/kde3/libamarok_xine-engine.so
%_K3datadir/config.kcfg/xinecfg.kcfg
%_K3datadir/services/amarok_xine-engine.desktop

%files mediadevice-ipod
%_K3libdir/kde3/libamarok_ipod-mediadevice.so
%_K3datadir/services/amarok_ipod-mediadevice.desktop

%files mediadevice-generic
%_K3libdir/kde3/libamarok_generic-mediadevice.so
%_K3datadir/services/amarok_generic-mediadevice.desktop

%files mediadevice-mtp
%_K3libdir/kde3/libamarok_mtp-mediadevice.so
%_K3datadir/services/amarok_mtp-mediadevice.desktop

%files mediadevice-daap
%_K3bindir/amarok_daapserver.rb
%_K3libdir/kde3/libamarok_daap-mediadevice.so
%_K3datadir/apps/%name/ruby_lib
%_K3datadir/services/amarok_daap-mediadevice.desktop

%changelog
* Thu May 31 2012 Roman Savochenko <rom_as@altlinux.ru> 1.4.10-alt14
- Revert to original 1.4.10 version from T6 for some bugs TDE-3.5.13 fix.

* Sun Mar 11 2012 Roman Savochenko <rom_as@altlinux.ru> 1.4.10-alt13
- Build for TDE 3.5.13 release

* Thu Feb 02 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.10-alt12.2
- Fixed build

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.4.10-alt12.1
- Rebuild with Python-2.7

* Tue Apr 19 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.4.10-alt12
- fix build

* Wed Mar 02 2011 Timur Aitov <timonbl4@altlinux.org> 1.4.10-alt11
- move to alternate place

* Wed Dec 15 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 1.4.10-alt10
- fix build
- rebuild with libmisqlclient.so.16

* Mon Mar 01 2010 Afanasov Dmitry <ender@altlinux.org> 1.4.10-alt9
- fix build with autoconf-2.64

* Tue Dec 01 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.10-alt8.1
- Rebuilt with python 2.6

* Fri Jul 31 2009 Pavlov Konstantin <thresh@altlinux.ru> 1.4.10-alt8
- Fix FTBFS with new ruby 1.9.
- Added a bunch of debian patches to address various issues.

* Thu May 28 2009 Pavlov Konstantin <thresh@altlinux.ru> 1.4.10-alt7
- Fix FTBFS with new automake and gcc4.4.

* Mon Jan 12 2009 Valery Inozemtsev <shrek@altlinux.ru> 1.4.10-alt6
- fixed SA33505 (see http://secunia.com/Advisories/33505/)

* Fri Dec 19 2008 Valery Inozemtsev <shrek@altlinux.ru> 1.4.10-alt5
- rebuild with libmtp.so.8

* Sun Nov 23 2008 Valery Inozemtsev <shrek@altlinux.ru> 1.4.10-alt4
- removed obsolete %%update_menus/%%clean_menus calls

* Tue Sep 02 2008 Valery Inozemtsev <shrek@altlinux.ru> 1.4.10-alt3
- ooops. real fix #16856

* Sun Aug 31 2008 Valery Inozemtsev <shrek@altlinux.ru> 1.4.10-alt2
- enabled daap (close #16856)

* Fri Aug 15 2008 Valery Inozemtsev <shrek@altlinux.ru> 1.4.10-alt1
- 1.4.10
- drop amarok-engine-gstreamer

* Tue Jun 17 2008 Valery Inozemtsev <shrek@altlinux.ru> 1.4.9.1-alt3
- enabled MySQL & PostgreSQL

* Sat May 17 2008 Valery Inozemtsev <shrek@altlinux.ru> 1.4.9.1-alt2
- rebuild with libgstreamer-0.10.19-alt2
- disabled daap

* Sun Apr 13 2008 Valery Inozemtsev <shrek@altlinux.ru> 1.4.9.1-alt1
- 1.4.9.1

* Wed Mar 12 2008 Valery Inozemtsev <shrek@altlinux.ru> 1.4.8-alt2
- rebuild with libmtp-0.2.6

* Wed Feb 13 2008 Valery Inozemtsev <shrek@altlinux.ru> 1.4.8-alt1.1
- rebuild with python-2.5

* Sun Dec 23 2007 Valery Inozemtsev <shrek@altlinux.ru> 1.4.8-alt0.M40.1
- build for branch 4.0

* Thu Dec 20 2007 Valery Inozemtsev <shrek@altlinux.ru> 1.4.8-alt1
- 1.4.8

* Sun Nov 11 2007 Valery Inozemtsev <shrek@altlinux.ru> 1.4.7-alt6
- rebuild with libgpod-0.6.0

* Mon Oct 08 2007 Valery Inozemtsev <shrek@altlinux.ru> 1.4.7-alt5
- added requires ruby-module-net, ruby-module-rexml (close #10278)
- fixed ru translation (close #13030)

* Fri Sep 28 2007 Valery Inozemtsev <shrek@altlinux.ru> 1.4.7-alt4
- build GStreamer engine

* Fri Aug 24 2007 Valery Inozemtsev <shrek@altlinux.ru> 1.4.7-alt3
- replace icons: player_start -> player_rew, player_end -> player_fwd

* Wed Aug 22 2007 Valery Inozemtsev <shrek@altlinux.ru> 1.4.7-alt0.M40
- build for branch 4.0
- fixed ru translation (close #12312)

* Tue Aug 21 2007 Valery Inozemtsev <shrek@altlinux.ru> 1.4.7-alt2
- rebuild with libgpod-0.5.2

* Fri Aug 17 2007 Valery Inozemtsev <shrek@altlinux.ru> 1.4.7-alt1
- 1.4.7

* Wed Jun 27 2007 Valery Inozemtsev <shrek@altlinux.ru> 1.4.6-alt2
- added amarok-1.4.6-collectiondb-br142999.patch,
	amarok-1.4.6-stars-indicating-osd-br147059.patch,
	amarok-1.4.6-show-osd-br146918.patch

* Fri Jun 22 2007 Valery Inozemtsev <shrek@altlinux.ru> 1.4.6-alt1
- 1.4.6

* Wed Jun 20 2007 Valery Inozemtsev <shrek@altlinux.ru> 1.4.5-alt7
- fixed requires

* Wed Jun 20 2007 Valery Inozemtsev <shrek@altlinux.ru> 1.4.5-alt6.M40
- rebuild for branch 4.0 (close #12080)

* Mon Jun 04 2007 Valery Inozemtsev <shrek@altlinux.ru> 1.4.5-alt6
- build with libmtp (close #11963)

* Sun Jun 03 2007 Valery Inozemtsev <shrek@altlinux.ru> 1.4.5-alt5
- bzip ChangeLog (close #11076)

* Fri Apr 27 2007 Valery Inozemtsev <shrek@altlinux.ru> 1.4.5-alt4
- fixed scanning to parse directories and files, starting with '.' (closed #11553)

* Mon Mar 26 2007 Valery Inozemtsev <shrek@altlinux.ru> 1.4.5-alt3
- rebuild with libtunepimp-0.5.3

* Thu Feb 15 2007 Valery Inozemtsev <shrek@altlinux.ru> 1.4.5-alt2
- added amarok-1.4.5-CVE-2006-6979.patch (closed #10820)

* Tue Feb 06 2007 Valery Inozemtsev <shrek@altlinux.ru> 1.4.5-alt1
- NMU:
  + update to 1.4.5
  + drop upstream patches
  + drop final compile patch

* Mon Dec 11 2006 Valery Inozemtsev <shrek@altlinux.ru> 1.4.4-alt2
- NMU:
  + replace libmusicbrainz to libtunepimp
  + added amarok-1.4.4-alt-ru_translation.patch,
          amarok-1.4.3-alt-final_compile.patch
  + build with --enable-final

* Wed Nov 08 2006 Valery Inozemtsev <shrek@altlinux.ru> 1.4.4-alt1
- NMU:
  + updated to 1.4.4
  + clenup spec file
  + updated build dependencies
  + fixed alt-ruby patch
  + added requires ruby-module-uri for %name
  + without xmms
  + removed subpackage %name-engine-gstreamer, %name-engine-arts
    (in %name-1.4.4 no such engine gstreamer, arts)
  + added amarok-1.4.4-alt-gpod_check.patch to properly detect libgpod
  + added amarok-1.4.3-alt-link_fixes.patch for clean linking
  + amarok-1.4.3-alt-playlist.patch is updated to 1.4.4 and renamed

* Wed Sep 27 2006 Stanislav Yadykin <tosick@altlinux.ru> 1.4.3-alt2
- added patches from shrek@
- fixed incorrect playlist saving

* Thu Sep 07 2006 Stanislav Yadykin <tosick@altlinux.ru> 1.4.3-alt1
- 1.4.3

* Fri Aug 25 2006 Stanislav Yadykin <tosick@altlinux.ru> 1.4.2-alt1
- 1.4.2-beta1
- enabled system sqlite by default
- added MySQL support in spec

* Mon Jul 03 2006 Stanislav Yadykin <tosick@altlinux.ru> 1.4.1-alt1
- 1.4.1

* Wed May 17 2006 Stanislav Yadykin <tosick@altlinux.ru> 1.4.0-alt1
- 1.4.0
- added macroses
- spec fixes
- removed ALT readme

* Wed May 03 2006 Stanislav Yadykin <tosick@altlinux.ru> 1.4-alt1beta3c
- 1.4-beta3c
- spec changes (beta support)

* Fri Jan 27 2006 Stanislav Yadykin <tosick@altlinux.ru> 1.3.8-alt1
- 1.3.8
- fixed BuildRequires

* Tue Jan 03 2006 Stanislav Yadykin <tosick@altlinux.ru> 1.3.7-alt2
- fixed menu generation
- fixed provides

* Mon Dec 12 2005 Stanislav Yadykin <tosick@altlinux.ru> 1.3.7-alt1
- 1.3.7
- build with libtunepimp 0.4.0

* Fri Nov 18 2005 Stanislav Yadykin <tosick@altlinux.ru> 1.3.6-alt1
- 1.3.6

* Fri Oct 28 2005 Stanislav Yadykin <tosick@altlinux.ru> 1.3.5-alt1
- 1.3.5

* Fri Oct 14 2005 Stanislav Yadykin <tosick@altlinux.ru> 1.3.3-alt1
- 1.3.3

* Tue Sep 27 2005 Stanislav Yadykin <tosick@altlinux.ru> 1.3.2-alt2
- build with system sqlite

* Thu Sep 22 2005 Stanislav Yadykin <tosick@altlinux.ru> 1.3.2-alt1
- 1.3.2

* Mon Aug 15 2005 Stanislav Yadykin <tosick@altlinux.ru> 1.3-alt2
- 1.3

* Thu Aug 11 2005 Stanislav Yadykin <tosick@altlinux.ru> 1.3-alt1beta3
- 1.3-beta3
- removed aKode engine

* Tue Aug 09 2005 Stanislav Yadykin <tosick@altlinux.ru> 1.2.4-alt2
- removed some unneeded patches (thanx zerg@)
- removed .la files (thanx zerg@)

* Wed May 25 2005 Stanislav Yadykin <tosick@altlinux.ru> 1.2.4-alt1
- 1.2.4

* Fri Apr 08 2005 Stanislav Yadykin <tosick@altlinux.ru> 1.2.3-alt2
- rebuild
- added aKode engine

* Tue Mar 29 2005 Stanislav Yadykin <tosick@altlinux.ru> 1.2.3-alt1
- 1.2.3

* Tue Mar 15 2005 Stanislav Yadykin <tosick@altlinux.ru> 1.2.2-alt1
- 1.2.2

* Thu Mar 10 2005 Stanislav Yadykin <tosick@altlinux.ru> 1.2.1-alt2
- split amarok package into base and arts-engine package
- misc spec fixes

* Thu Mar 03 2005 Stanislav Yadykin <tosick@altlinux.ru> 1.2.1-alt1
- 1.2.1
- spec fixes

* Mon Feb 14 2005 Stanislav Yadykin <tosick@altlinux.ru> 1.2-alt3
- 1.2 release

* Mon Jan 31 2005 Stanislav Yadykin <tosick@altlinux.ru> 1.2-alt2beta4
- new version
- README.ALT fix

* Thu Jan 27 2005 Stanislav Yadykin <tosick@altlinux.ru> 1.2-alt2beta3
- menu fix

* Mon Jan 10 2005 Stanislav Yadykin <tosick@altlinux.ru> 1.2-alt1beta3
- 1.2-alt1beta3 new version
- 1.2-alt1beta3 FIX #5256
- 1.2-alt1beta3 split to main app and engines for playing via gstreamer and libxine

* Tue Oct 19 2004 Dmitriy Porollo <spider@altlinux.ru> 1.1.1-alt2
- 1.1.1-alt2 Remove MAS support
- 1.1.1-alt2 Remove requires

* Mon Oct 11 2004 Dmitriy Porollo <spider@altlinux.ru> 1.1.1-alt1
- 1.1.1-alt1 new release
- 1.1.1-alt1 build bugs fixed

* Mon Oct 4 2004 Dmitriy Porollo <spider@altlinux.ru> 1.1-alt1
- 1.1-alt1 xine engine support added
- 1.1-alt1 new release

* Tue Aug 05 2004 Dmitriy Porollo <spider@altlinux.ru> 1.0.2-alt2
- 1.0.2-alt2 FIX: gstreamer requires.
- 1.0.2-alt2 ADD: README_ALT updated

* Tue Aug 05 2004 Dmitriy Porollo <spider@altlinux.ru> 1.0.2-alt1
- 1.0.2-alt1 ADD: README_ALT
- 1.0.2-alt1 ADD: xine-engine, configure --with-xine to use
- 1.0.2-alt1 FIX: aRts-engine: Compatibility with newer aRts versions improved.
- 1.0.2-alt1 FIX: aRts-engine: Streams sometimes stopping shortly after playback was started.
- 1.0.2-alt1 FIX: CHG: Increased stream connect timeout to 12 seconds.
- 1.0.2-alt1 ADD: Buld without arts engine.

* Tue Jul 13 2004 Dmitriy Porollo <spider@altlinux.ru> 1.0.1-alt3
- 1.0.1-alt3 FIX: Russian ID3v1 tag's bug fixed (see options->encoding)

* Tue Jul 07 2004 Dmitriy Porollo <spider@altlinux.ru> 1.0.1-alt2
- 1.0.1-alt2 FIX: Internatialisations fixed (invalid names of .mo files). 

* Tue Jun 29 2004 Dmitriy Porollo <spider@altlinux.ru> 1.0.1-alt1
- 1.0.1-alt1 ADD: Build with GStreamer. Use It !
- 1.0.1-alt1 FIX: Short dropouts after starting a stream with GStreamer.
- 1.0.1-alt1 FIX: amaroK starting invisible when systray icon is disabled.
- 1.0.1-alt1 FIX: Playlist analyzer looks freaky on some systems. (BR 83671)
- 1.0.1-alt1 FIX: Display filename in title column for wav files. (BR 83650)
- 1.0.1-alt1 FIX: Don't show crash dialog when no engine plugins are found.
- 1.0.1-alt1 FIX: Compile issue for KDE < 3.2.1 users.

* Wed Jun 17 2004 Dmitriy Porollo <spider@altlinux.ru> 1.0-alt1
- 1.0-alt1 Playlist orientated design with optional Player Window for XMMS junkies!
- 1.0-alt1 "Browser" tabs allow quick and shockingly easy access to media, local and streamed
- 1.0-alt1 Support for XMMS visualisations
- 1.0-alt1 Multithreaded design means the UI never hangs during complex tasks
- 1.0-alt1 Sound-engine independent design allows amaroK to run on aRts, GStreamer and NMM
           with native ALSA engine planned!
- 1.0-alt1 Highly configurable design means amaroK can be the player you want!
- 1.0-alt1 Global shortcuts and a powerful DCOP interface allow you to control amaroK in any way you want
- 1.0-alt1 Intuitive inline tag-editing

* Wed Jun 09 2004 Dmitriy Porollo <spider@altlinux.ru> 1.0-alt0.3.beta4
- 1.0-alt0.3.beta4 FIX: Fixed bug in the collection browser.

* Mon Jun 07 2004 Dmitriy Porollo <spider@altlinux.ru> 1.0-alt0.2.beta4
- 1.0-alt0.2.beta4 Translated to russian language.

* Tue Jun 03 2004 Dmitriy Porollo <spider@altlinux.ru> 1.0-alt0.1.beta4
- 1.0-alt0.1.beta4 FIX: Cover not shown in ContextBrowser, when song gets played for the first time ever.
- 1.0-alt0.1.beta4 ADD: Configure->Playback->Device && default device option for audiosinks.
- 1.0-alt0.1.beta4 FIX: Decode %-encoded characters in filenames, like %%2f for a slash.
- 1.0-alt0.1.beta4 FIX: Always show OSD (if enabled) on volume changes.
- 1.0-alt0.1.beta4 FIX: Filtering the collection using tokens with number(s) at the beginning or end failed.
- 1.0-alt0.1.beta4 FIX: "Start Scan" menu-entry gets disabled while scanning.
- 1.0-alt0.1.beta4 FIX: Display splash screen on correct desktop with Xinerama.
- 1.0-alt0.1.beta4 FIX: Not all SQL queries were "string-escaped".
- 1.0-alt0.1.beta4 ADD: Added statistics database, which keeps track of how often and when you play a specific song.
- 1.0-alt0.1.beta4 FIX: Show last playtime in localtime instead of UTC.
- 1.0-alt0.1.beta4 ADD: Allow changing volume by using the mousewheel anywhere on the toolbar.
- 1.0-alt0.1.beta4 ADD: Clear button for CollectionBrowser search.
- 1.0-alt0.1.beta4 FIX: Allow OSD still to be shown via shortcut when disabled

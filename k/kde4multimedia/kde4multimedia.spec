
%add_findpackage_path %_kde4_bindir

%define rname kdemultimedia
Name: kde4multimedia
%define major 4
%define minor 8
%define bugfix 4
Version: %major.%minor.%bugfix
Release: alt1

Group: Graphical desktop/KDE
Summary: K Desktop Environment - Multimedia
License: GPLv2
Url: http://www.kde.org

#Requires: %name-dragonplayer = %version-%release
Requires: %name-juk = %version-%release
Requires: %name-audiocd = %version-%release
Requires: %name-kmix = %version-%release
Requires: %name-kscd = %version-%release
Requires: %name-videothumbnail = %version-%release


Source00: dragon-%version.tar
Source01: juk-%version.tar
Source02: ffmpegthumbs-%version.tar
Source03: kmix-%version.tar
Source04: kscd-%version.tar
Source05: audiocd-kio-%version.tar
Source06: strigi-multimedia-%version.tar
Source100: CMakeLists.txt
Source101: ConfigureChecks.cmake
Source102: config.h.cmake
Source103: FindMusicBrainz3.cmake
Source104: FindCdparanoia.cmake
Source105: FindTunePimp.cmake

# ALT      ~/GIT/libkcddb4/altlinux
Patch2: kdemultimedia-4.8.2-alt-cflags.patch
Patch3: kdemultimedia-4.8.4-alt-audiocd-includedirs.patch

BuildRequires(pre): kde4base-workspace-devel
BuildRequires: gcc-c++ libcdparanoia-devel
BuildRequires: libmusicbrainz3-devel libtunepimp-devel libflac-devel
BuildRequires: libmad-devel libvorbis-devel libtheora-devel libspeex-devel
BuildRequires: libxine-devel >= 1.1.9
BuildRequires: libsamplerate-devel libtag-devel libfreebob-devel
BuildRequires: libjpeg-devel bzlib-devel libpulseaudio-devel glib2-devel libxine-devel
#BuildRequires: libcdda-devel
BuildRequires: libalsa-devel libcanberra-devel
BuildRequires: libavcodec-devel libavformat-devel libavutil-devel libswscale-devel
#BuildRequires: libgstreamer-plugins-base-devel
BuildRequires: kde4base-workspace-devel >= %version
BuildRequires: libkcompactdisc4-devel libkcddb4-devel

%description
* kmix: the audio mixer as a standalone program and Kicker applet
* kscd: A CD player with an interface to the internet CDDB database
* phonon-xine: A Phonon-Backend based on Xine
* kfile-plugins: provide meta information about sound files
* libkcddb: a library for retrieving and sending cddb information


%package common
Summary: %name common package
Group: Graphical desktop/KDE
Requires: kde-common >= %major.%minor
Conflicts: kdemultimedia-common <= 3.5.12-alt1
%description common
%name common package

%package core
Summary: Core files for %name
Group: Graphical desktop/KDE
Requires: %name-common = %version-%release
%description core
Core files for %name

%package dragonplayer
Group: Video
Summary: Video Player for KDE
Requires: %name-core = %version-%release
%description dragonplayer
Video Player for KDE

%package juk
Group: Sound
Summary: KDE music player, jukebox, tagger and music collection manager
Requires: %name-core = %version-%release
%description juk
Juk is well, a jukebox.  As is typical with many jukebox
applications, Juk allows you to edit the tags of the
audio files, and manage your collection and playlists.

%package audiocd
Group: Sound
Summary: KDE audiocd ioslave
Requires: %name-core = %version-%release
%description audiocd
Audiocd ioslave

%package -n libaudiocdplugins4
Group: System/Libraries
Summary: KDE 4 library
Requires: %name-common = %version-%release
%description -n libaudiocdplugins4
KDE 4 library

%package kmix
Group: Sound
Summary: KDE sound mixer applet
Requires: %name-core = %version-%release
%description kmix
A sound mixer applet for KDE.
%name allows you to control the volumes of your
sound card from a KDE panel applet.

%package kscd
Group: Sound
Summary: KDE Audio-CD player
Requires: %name-core = %version-%release
Requires: %name-audiocd
%description kscd
KSCD is an Audio-CD player for KDE

%package videothumbnail
Group: Video
Summary: Video thumbnail generator
Requires: %name-common = %version-%release
%description videothumbnail
Video thumbnail generator for all KDE file managers

%package -n libkcddb4
Group: System/Libraries
Summary: KDE 4 library
Requires: %name-common = %version-%release
%description -n libkcddb4
KDE 4 library

%package -n libkcompactdisc4
Group: System/Libraries
Summary: KDE 4 library
Requires: %name-common = %version-%release
%description -n libkcompactdisc4
KDE 4 library

%package devel
Group: Development/KDE and QT
Summary: Devel stuff for %name
Requires: kde4libs-devel
Requires: libkcompactdisc4-devel libkcddb4-devel
Requires: %name-common = %version-%release
%description devel
This package contains header files needed if you wish to build applications
based on %name.


%prep
%setup -q -cT -n %rname-%version -a0 -a1 -a2 -a3 -a4 -a5 -a6
ls -d1 * | \
while read d
do
    [ -d "$d" ] || continue
    newdirname=`echo "$d"| sed 's|-%version$||'`
    [ "$d" == "$newdirname" ] || mv $d $newdirname
done
%patch2 -p1
%patch3 -p1

mkdir -p cmake/modules/

install -m 0644 %SOURCE100 ./
install -m 0644 %SOURCE101 ./
install -m 0644 %SOURCE102 ./
install -m 0644 %SOURCE103 cmake/modules/
install -m 0644 %SOURCE104 cmake/modules/
install -m 0644 %SOURCE105 cmake/modules/
#ls -d1 * | \
#while read d
#do
#    [ "$d" == "${d#lib}" ] || continue
#    [ -d "$d" ] || continue
#    echo "add_subdirectory($d)" >> CMakeLists.txt
#done


%build
%K4build \
    -DKDE4_ENABLE_FPIE:BOOL=ON

%install
%K4install



%files
%files common
#%doc README

%files core
%_K4conf_update/*
%_K4iconsdir/oxygen/*/*/*.*
%_K4iconsdir/hicolor/*/*/*.*

%files videothumbnail
%_K4lib/ffmpegthumbs.so
%_K4srv/ffmpegthumbs.desktop

%files dragonplayer
%_K4bindir/dragon
%_K4lib/dragonpart.so
%_K4apps/dragonplayer/
%_K4apps/solid/actions/dragonplayer-opendvd.desktop
%_K4xdg_apps/dragonplayer.desktop
%_K4srv/ServiceMenus/dragonplayer_*
%_K4srv/dragonplayer_part.desktop
%_K4conf/dragonplayerrc
%_K4doc/*/dragonplayer

%files juk
%_K4bindir/juk
%_K4apps/juk/
%_K4xdg_apps/juk.desktop
%_K4srv/ServiceMenus/jukservicemenu.desktop
%_K4doc/*/juk

%files audiocd
%_K4lib/kcm_audiocd.so
%_K4lib/kio_audiocd.so
%_K4lib/libaudiocd_*
%_K4apps/konqsidebartng/virtual_folders/services/audiocd.desktop
%_K4apps/solid/actions/solid_audiocd.desktop
%_K4cfg/audiocd_*
%_K4srv/audiocd.desktop
%_K4srv/audiocd.protocol
%_K4doc/*/kioslave/audiocd/

%files kmix
%_K4bindir/kmix
%_K4bindir/kmixctrl
%_K4libdir/libkdeinit4_kmix*
%_K4lib/kded_kmixd.so
%_K4apps/kmix/
%_K4xdg_apps/kmix.desktop
%_K4start/restore_kmix_volumes.desktop
%_K4start/kmix_autostart.desktop
%_K4srv/kmixctrl_restore.desktop
%_K4srv/kded/kmixd.desktop
%_K4doc/*/kmix
#
%_K4lib/plasma_engine_mixer.so
%_K4apps/plasma/services/mixer.operations
%_K4srv/plasma-engine-mixer.desktop

%files kscd
%_K4bindir/kscd
#%_K4bindir/workman2cddb.pl
#%_K4apps/profiles/
%_K4apps/kscd/
%_K4xdg_apps/kscd.desktop
%_K4apps/solid/actions/kscd-play-audiocd.desktop
%_K4cfg/kscd.kcfg
#%_K4doc/*/kscd

%files -n libaudiocdplugins4
%_K4libdir/libaudiocdplugins.so.*

%files devel
%_K4link/lib*.so
%_K4includedir/*
%_K4dbus_interfaces/*.xml

%changelog
* Fri Jun 08 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.4-alt1
- new version

* Fri May 11 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.3-alt0.M60P.1
- build for M60P

* Thu May 03 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.3-alt1
- new version
- fix to build on arm; thanks sbolshakov@alt

* Wed Apr 11 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.2-alt0.M60P.1
- built for M60P

* Wed Apr 11 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.2-alt1
- new version

* Wed Apr 04 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.1-alt0.M60P.1
- built for M60P

* Sun Mar 11 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.1-alt1
- new version

* Tue Jan 24 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.0-alt1
- new version

* Thu Dec 29 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.4-alt1.M60P.1
- built for M60P

* Thu Dec 29 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.4-alt2
- fix kmix qt glib dispatcher detecttion in pulseaudio backend

* Mon Dec 05 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.4-alt0.M60P.1
- build for M60P

* Mon Dec 05 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.4-alt1
- new version

* Thu Nov 03 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.3-alt0.M60P.1
- built for M60P

* Tue Nov 01 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.3-alt1
- new version

* Tue Oct 18 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.2-alt0.M60T.1
- built for M60T

* Mon Oct 10 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.2-alt1
- new version

* Thu Sep 29 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.1-alt2
- rebuilt with pulse

* Tue Sep 13 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.1-alt1
- new version

* Fri Aug 12 2011 Sergey V Turchin <zerg@altlinux.org> 4.6.5-alt2
- update from 4.6 branch (fix compile with libav)

* Tue Jul 05 2011 Sergey V Turchin <zerg@altlinux.org> 4.6.5-alt1
- new version

* Wed Jun 08 2011 Sergey V Turchin <zerg@altlinux.org> 4.6.4-alt1
- new version

* Thu May 05 2011 Sergey V Turchin <zerg@altlinux.org> 4.6.3-alt1
- new version

* Thu Apr 07 2011 Sergey V Turchin <zerg@altlinux.org> 4.6.2-alt1
- new version

* Wed Mar 02 2011 Sergey V Turchin <zerg@altlinux.org> 4.6.1-alt1
- new version

* Fri Feb 25 2011 Sergey V Turchin <zerg@altlinux.org> 4.6.0-alt2
- move to standart place

* Fri Jan 28 2011 Sergey V Turchin <zerg@altlinux.org> 4.6.0-alt1
- new version

* Wed Jan 19 2011 Sergey V Turchin <zerg@altlinux.org> 4.5.5-alt1
- new version

* Wed Dec 01 2010 Sergey V Turchin <zerg@altlinux.org> 4.5.4-alt1
- new version

* Tue Nov 02 2010 Sergey V Turchin <zerg@altlinux.org> 4.5.3-alt1
- new version

* Thu Oct 07 2010 Sergey V Turchin <zerg@altlinux.org> 4.5.2-alt1
- new version

* Tue Aug 31 2010 Sergey V Turchin <zerg@altlinux.org> 4.5.1-alt1
- new version

* Thu Aug 05 2010 Sergey V Turchin <zerg@altlinux.org> 4.5.0-alt1
- new version

* Thu Jul 08 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.5-alt0.M51.1
- built for M51

* Mon Jul 05 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.5-alt1
- new version

* Thu Jun 03 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.4-alt0.M51.1
- built for M51

* Tue Jun 01 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.4-alt1
- new version

* Thu May 13 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.3-alt0.M51.1
- built for M51

* Mon May 03 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.3-alt1
- new version

* Wed Apr 21 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.2-alt0.M51.1
- built for M51

* Tue Mar 30 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.2-alt1
- new version

* Mon Mar 01 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.1-alt1
- new version

* Thu Feb 11 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.0-alt1
- new version

* Thu Jan 28 2010 Sergey V Turchin <zerg@altlinux.org> 4.3.95-alt1
- new version

* Thu Jan 21 2010 Sergey V Turchin <zerg@altlinux.org> 4.3.90-alt1
- new version

* Tue Dec 15 2009 Sergey V Turchin <zerg@altlinux.org> 4.3.4-alt0.M51.1
- built for M51

* Mon Nov 30 2009 Sergey V Turchin <zerg@altlinux.org> 4.3.4-alt1
- new version

* Mon Nov 09 2009 Sergey V Turchin <zerg@altlinux.org> 4.3.3-alt0.M51.1
- built for M51

* Tue Nov 03 2009 Sergey V Turchin <zerg@altlinux.org> 4.3.3-alt1
- new version

* Fri Oct 09 2009 Sergey V Turchin <zerg@altlinux.org> 4.3.2-alt1
- new version

* Mon Aug 31 2009 Sergey V Turchin <zerg@altlinux.org> 4.3.1-alt1
- new version

* Wed Aug 05 2009 Sergey V Turchin <zerg@altlinux.org> 4.3.0-alt1
- 4.3.0

* Thu Jul 23 2009 Sergey V Turchin <zerg@altlinux.org> 4.2.98-alt1
- 4.2.98

* Thu Jul 16 2009 Sergey V Turchin <zerg@altlinux.org> 4.2.96-alt1
- 4.2.96

* Mon Jun 22 2009 Sergey V Turchin <zerg@altlinux.org> 4.2.4-alt0.M50.1
- built for M50

* Mon Jun 08 2009 Sergey V Turchin <zerg@altlinux.org> 4.2.4-alt1
- new version

* Tue May 05 2009 Sergey V Turchin <zerg@altlinux.org> 4.2.3-alt1
- new version

* Fri Apr 17 2009 Sergey V Turchin <zerg@altlinux.org> 4.2.2-alt2
- add solid action for AudioCD
- add patch to allow turn off kmix autostart

* Fri Apr 03 2009 Sergey V Turchin <zerg@altlinux.org> 4.2.2-alt1
- new version

* Wed Mar 04 2009 Sergey V Turchin <zerg at altlinux dot org> 4.2.1-alt1
- new version

* Wed Jan 28 2009 Sergey V Turchin <zerg at altlinux dot org> 4.2.0-alt1
- new version

* Tue Jan 20 2009 Sergey V Turchin <zerg at altlinux dot org> 4.1.96-alt1
- new version
- remove deprecated macroses from specfile

* Fri Nov 07 2008 Sergey V Turchin <zerg at altlinux dot org> 4.1.3-alt1
- new version

* Tue Oct 07 2008 Sergey V Turchin <zerg at altlinux dot org> 4.1.2-alt1
- new version

* Fri Sep 05 2008 Sergey V Turchin <zerg at altlinux dot org> 4.1.1-alt1
- new version

* Sat Aug 02 2008 Sergey V Turchin <zerg at altlinux dot org> 4.1.0-alt1
- new version

* Mon Jun 02 2008 Sergey V Turchin <zerg at altlinux dot org> 4.0.80-alt1
- 4.1 beta1

* Tue May 06 2008 Sergey V Turchin <zerg at altlinux dot org> 4.0.72-alt1
- new version

* Wed Apr 02 2008 Sergey V Turchin <zerg at altlinux dot org> 4.0.3-alt1
- new version

* Tue Mar 25 2008 Sergey V Turchin <zerg at altlinux dot org> 4.0.2-alt1
- initial specfile


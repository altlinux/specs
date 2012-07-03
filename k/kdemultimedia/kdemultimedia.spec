%undefine __libtoolize
%define _optlevel s
%define _keep_libtool_files 1

%define unstable 0
%define with_kaboodle 0
%define with_noatun 0
%define with_xine 0
%define with_musicbrainz 0
%define with_arts 0

%define qtdir %_qt3dir
#%define timiddir %_datadir/timidity

%add_findpackage_path %_K3bindir
%add_findprov_lib_path %_libdir/kde3
%add_findreq_skiplist /usr/share/apps/noatun/skins/*
%add_findprov_skiplist /usr/share/apps/noatun/skins/*
%add_verify_elf_skiplist %_libdir/libmpg123.so*
%add_verify_elf_skiplist %_libdir/libmpeg-0.3.0.so*
%if %unstable
%define _optlevel 0
%endif

Name: kdemultimedia
Version: 3.5.13
Release: alt4

Group: Graphical desktop/KDE
Summary: K Desktop Environment - Multimedia
License: GPL
URL: http://www.kde.org/

%if %with_arts
Requires: %name-arts = %version-%release
Requires: %name-krec = %version-%release
%endif
Requires: %name-juk = %version-%release
%if %with_kaboodle
Requires: %name-kaboodle = %version-%release
%endif
#Requires: %name-akode = %version-%release
Requires: %name-kaudiocreator = %version-%release
Requires: %name-kfile = %version-%release
Requires: %name-kmid = %version-%release
Requires: %name-kmix = %version-%release
Requires: %name-kscd = %version-%release
Requires: %name-libs = %version-%release
%if %with_noatun
Requires: %name-noatun = %version-%release
%endif
#Requires: %name-kmidi = %version-%release


Source: kdemultimedia-%version.tar

# RH
Patch1: kdemultimedia-3.4.0-xdg.patch

# Debian
# SuSE
Patch62: fix-kscd-blocking-device.diff
Patch63: initial-preferences.diff

# ALT
Patch105: kdemultimedia-3.5.12-alt-def-kmix.patch
Patch106: kdemultimedia-3.1.4-kmid_encode_text.patch
Patch107: kmix-3.2-dev-names.patch
Patch108: kdemultimedia-3.5.10-alt-rpm-arch.patch
Patch109: kmix-3.5.10-translate-dev-names.patch
Patch110: kdemultimedia-3.5.12-alt-fix-linking.patch
Patch111: 3.5.0-libartsmidi-fix-linking.patch
Patch112: juk-3.5.0-fix-linking.patch
Patch113: kaboodle-3.5.0-fix-linking.patch
Patch114: kio_audiocd-3.4.1-alt-flac_config.patch
Patch115: mpg123_artsplugin-alt-fix-defines.patch
Patch116: kdemultimedia-3.5.6-alt-desktop-categiries.patch
Patch117: kscd-3.5.7-alt-digital-defaults.patch

# Automatically added by buildreq on Mon Apr 12 2004 (-bi)
#BuildRequires: XFree86-devel XFree86-libs cdparanoia fontconfig freetype2 gcc-c++ gcc-g77 glib2-devel kde-settings kdelibs-devel libalsa-devel libarts-devel libarts-qt-devel libaudiofile-devel libcdparanoia-devel libjpeg-devel liblame-devel libmusicbrainz-devel libogg-devel libpng-devel libqt3-devel libstdc++-devel libtag-devel libtiff-devel libvorbis-devel libxine-devel qt3-designer xml-utils zlib-devel
BuildRequires(pre): kdelibs-devel
BuildRequires: gcc-c++ glib2-devel linux-libc-headers
BuildRequires: libalsa-devel libaudiofile-devel
BuildRequires: cdparanoia libcdparanoia-devel libjpeg-devel liblame-devel
BuildRequires: libogg-devel libpng-devel libqt3-devel libstdc++-devel libtag-devel
BuildRequires: libtiff-devel libvorbis-devel
%if %with_xine
BuildRequires: libxine-devel
%endif
BuildRequires: qt3-designer xml-utils zlib-devel libacl-devel libattr-devel
BuildRequires: libflac-devel libflac++-devel liboggflac-devel libmad-devel libspeex-devel
BuildRequires: libsamplerate-devel libtheora-devel libakode libakode-devel jackit-devel
%if %with_musicbrainz
BuildRequires: libmusicbrainz-devel libtunepimp-devel
%endif
%if %with_arts
BuildRequires: libarts-qtmcop >= 1.5.1 libarts-qtmcop-devel >= 1.5.1
%endif
BuildRequires: kdelibs >= %version kdelibs-devel >= %version

%description
Multimedia tools for the K Desktop Environment.

%package common
Summary: Common empty package for %name
Group: Graphical desktop/KDE
Requires: kde-common >= 3.2
Conflicts: kdemultimedia <= 3.0
#
%description common
Common empty package for %name

%package devel
Summary: Header files for %name
Group: Development/KDE and QT
Requires: %name-common = %version-%release
Requires: %name = %version-%release
#
%description devel
Header files needed for developing kdemultimedia applications.

%package juk
Summary: Music player, jukebox, tagger and music collection manager
Group: Sound
Requires: %{get_dep kdelibs}
Requires: %name-common = %version-%release
Requires: %{get_dep libtag}
#Requires: trm
#
%description juk
Juk is well, a jukebox.  As is typical with many jukebox
applications, Juk allows you to edit the tags of the
audio files, and manage your collection and playlists.

%package akode
Summary: Sound library with IO plugins
Group: Sound
Requires: %name-common = %version-%release
#
%description akode
aKode is the sound library with several input and output plugins.

%package arts
Summary: Additional functionality for the aRts sound system
Group: Sound
Requires: %name-libs arts
Requires: %{get_dep kdelibs}
Requires: %name-common = %version-%release
#
%description arts
Additional functionality for the aRts sound system.
Among other things, this adds MIDI support, some synthesizer functionality
and artsbuilder, a frontend for connecting aRts modules to generate
synthesizers.

%package kaboodle
Summary: A KDE media player
Group: Video
Requires: %{get_dep kdelibs}
Requires: %name-common = %version-%release
#
%description kaboodle
A KDE media player. Kaboodle supports playback of Ogg, MP3 (including streaming
MP3), MP2, WAV and MOD audio files as well as MPEG video files.

%package kaudiocreator
Summary: KAudioCreator is an audio file creation solution for KDE
Group: Sound
Requires: %{get_dep kdelibs}
Requires: %name-common = %version-%release
Requires: lame vorbis-tools flac
#
%description kaudiocreator
KAudioCreator is an audio file creation solution for KDE.
Ripping the files using KDE (with CDDB support), it allows you
to use whatever encoder you wish to encode your audio files.
It also provides a job control system so you can see what
files have succeeded or failed, and stop or cancel jobs
as the application progresses. 

%package noatun
Summary: A KDE media player
Group: Sound
Requires: %name-arts
Requires: %{get_dep kdelibs}
Requires: %name-common = %version-%release
#
%description noatun
A KDE media player. Noatun supports playback of Ogg, MP3 (including streaming
MP3), MP2, WAV and MOD audio files as well as MPEG video files.

%package kfile
Summary: KFile support for audio files
Group: Sound
Requires: %{get_dep kdelibs}
Requires: %name-common = %version-%release
Provides: %name-kfile-plugins = %version-%release
#
%description kfile
Installing kdemultimedia-kfile allows all KFile aware applications (most KDE
applications) to gather, display and edit information on Ogg, MP3, WAV and M3U
files.

%package kmid
Summary: A MIDI player (using the soundcard's sequencer functionality)
Group: Sound
Requires: %{get_dep kdelibs}
Requires: %name-common = %version-%release
#
%description kmid
  A MIDI player using the soundcard's sequencer functionality.
kmid plays MIDI files through an attached MIDI device or, if your hardware
supports it, the soundcard's sequencer functionality.
  If you're looking for an application that plays MIDI files by converting
them to digital audio first (works on any soundcard and typically provides
better sound than a soundcard sequencer, but can't play to external MIDI
devices), try kmidi instead.

%package kmidi
Summary: A MIDI player (converting to digital audio)
Group: Sound
Requires: %{get_dep kdelibs}
Requires: %name-common = %version-%release
#
%description kmidi
  A MIDI player. Kmidi works by converting MIDI files to digital audio and
sending them to your soundcard's DSP. It works on every soundcard supported
by Linux and typically gives better sound quality than using the soundcard's
builtin sequencer functionality (if any), but can't send output to external
MIDI devices.
  If you're looking for an application that plays MIDI files to external
devices or your soundcard's builtin sequencer, try kmid instead.

%package kmix
Summary: KDE sound mixer applet
Group: Sound
Requires: %{get_dep kdelibs}
Requires: %name-common = %version-%release
#
%description kmix
A sound mixer applet for KDE. kmix allows you to control the volumes of your
sound card from a KDE panel applet.

%package krec
Summary: KDE based recorder app
Group: Sound
Requires: %{get_dep kdelibs}
Requires: %name-common = %version-%release
#
%description krec
This is a KDE based recorder app

%package koncd
Summary: Frontend for mastering and burning CDs
Group: Archiving/Cd burning
Requires: cdrecord mkisofs
Requires: %{get_dep kdelibs}
Requires: %name-common = %version-%release
#
%description koncd
KOnCD is a graphical frontend for mastering and burning CD-ROMs.

%package kscd
Summary: Audio-CD player for KDE
Group: Sound
Requires: %{get_dep kdelibs}
Requires: %name-common = %version-%release
#
%description kscd
KSCD is an Audio-CD player for KDE.

%package libs
Summary: Libraries used by KDE multimedia applications
Group: System/Libraries
Requires: %{get_dep kdelibs}
Requires: %name-common = %version-%release
Provides: kdemultimedia-kio-audiocd = %version-%release,	kdemultimedia-yaf = %version-%release
Provides: kdemultimedia-mpeglib = %version-%release
#
%description libs
Libraries used by KDE multimedia applications.
kdemultimedia-libs includes mpeglib.

%prep
%setup -q
cp -ar altlinux/admin ./
#sed -i admin/acinclude.m4.in -e "s,/usr/include/tqt,%{_includedir}/tqt,g"
#__cp "/usr/share/libtool/aclocal/libtool.m4" "admin/libtool.m4.in"
#__cp "/usr/share/libtool/config/ltmain.sh" "admin/ltmain.sh"
#__make -f "admin/Makefile.common"

%patch1 -p1

###%patch62 -p0
%patch63 -p0

%patch105 -p1
#%patch106 -p1
#%patch107 -p1
%patch108 -p1
%patch109 -p1
%patch110 -p1
%if %with_arts
%patch111 -p1
%endif
%patch112 -p1
#%patch113 -p1
###%patch114 -p1
%patch115 -p1
%patch116 -p1
%patch117 -p1

for f in `find -type f -name \*.mcopclass`
do
    sed -i 's/\(Library=.*\)\.la$/\1.so/' "$f"
done

rm -rf altlinux
sed -i '\|\${kdeinit}_LDFLAGS[[:space:]]=[[:space:]].*-no-undefined|s|-no-undefined|-no-undefined -Wl,--warn-unresolved-symbols|' admin/am_edit
for f in `find $PWD -type f -name Makefile.am`
do
    sed -i -e '\|_la_LDFLAGS.*[[:space:]]-module[[:space:]]|s|-module|-module \$(KDE_PLUGIN)|' $f
    #sed -i -e '\|_la_LDFLAGS.*[[:space:]]-no-undefined|s|-no-undefined|-no-undefined -Wl,--allow-shlib-undefined|' $f
    grep -q -e 'lib.*SOURCES' $f || continue
    RPATH_LINK_OPTS+=" -Wl,-rpath-link,`dirname $f`/.libs"
done
sed -i "s|\(-Wl,--as-needed\)| $RPATH_LINK_OPTS \1|g" admin/acinclude.m4.in
sed -i -e 's|\$USER_INCLUDES|-I%_includedir/tqtinterface \$USER_INCLUDES|' admin/acinclude.m4.in
make -f admin/Makefile.common cvs ||:

find ./kfile-plugins -type f -name Makefile.am | \
while read f; do
    sed -i -e '\|kfile_.*_la_LIBADD[[:space:]][[:space:]]*=|s|\(.*\)|\1 \$(LIB_KDEUI) \$(LIB_KDECORE) \$(LIB_QT)|' $f
done

find ./kioslave/audiocd/plugins -type f -name Makefile.am | \
while read f; do
    sed -i -e '\|libaudiocd_encoder_.*_la_LIBADD[[:space:]][[:space:]]*=|s|\(.*\)|\1 \$(top_builddir)/libkcddb/libkcddb.la \$(LIB_KDEUI) \$(LIB_KDECORE) \$(LIB_QT)|' $f
done

# workaround for libvorbis-devel wrong includes placement
ln -s /usr/include kfile-plugins/theora/vorbis ||:
ln -s /usr/include oggvorbis_artsplugin/vorbis ||:
ln -s /usr/include vorbis ||:

%build
%add_optflags %optflags_shared -I%_includedir/speex -I%_includedir/vorbis

export QTDIR=%qtdir
export KDEDIR=%_K3prefix

export PATH=$QTDIR/bin:$KDEDIR/bin:$PATH

export LD_LIBRARY_PATH=$QTDIR/%_lib:$KDEDIR/%_lib:$LD_LIBRARY_PATH
export LDFLAGS="-L%buildroot/%_libdir -L%buildroot/%_libdir/kde3 -L%_libdir"

%if !%with_kaboodle
DO_NOT_COMPILE="$DO_NOT_COMPILE kaboodle"
%endif
%if !%with_noatun
DO_NOT_COMPILE="$DO_NOT_COMPILE noatun"
%endif
export DO_NOT_COMPILE

#    --enable-audio=oss,nas,wav,alsa \
%K3configure \
%if %unstable
    --enable-debug=full \
%else
    --disable-debug \
%endif
    --with-alsa \
%if %with_arts
    --with-arts-alsa \
%else
    --without-arts \
%endif
    --enable-audio=oss,nas,wav \
    --disable-lametest \
    --disable-vorbistest \
    --disable-xinetest \
    --with-lame \
    --with-speex \
    --with-flac \
    --with-libmad \
    --with-libsamplerate \
    --with-jack \
    --with-taglib \
    --with-akode \
    --with-audiofile \
%if %with_musicbrainz
    --with-musicbrainz \
%else
    --without-musicbrainz \
%endif
    --with-theora \
%if %with_xine
    --with-xine \
%else
    --without-xine \
%endif
    --enable-kscd-defaults \
    --with-kscd-cdda
sed -ri 's/^(hardcode_libdir_flag_spec|runpath_var)=.*/\1=/' libtool

%make XINE_LIBS="-lxine"

%if %with_arts
%make -C oggvorbis_artsplugin
#%make -C mpg123_artsplugin
%if %with_xine
#%make -C xine_artsplugin/tools
%endif
%endif

%install
export PATH=%_bindir:$PATH
# David - 2.2-0.alpha2.4mdk - Don't strip when we are not in final release
%if %unstable
%set_strip_method none
%endif

%K3install

%if %with_arts
%K3install -C oggvorbis_artsplugin
#%K3install -C mpg123_artsplugin
%if %with_xine
#%K3install -C xine_artsplugin/tools
%endif
%endif

sed -i "s|Midi\/|Midi and |" %buildroot/%_K3xdg_apps/kmid.desktop

# add kmix to autostart
install -m 0644 %buildroot/%_K3xdg_apps/kmix.desktop %buildroot/%_K3start/kmix.desktop

# move binary
mkdir -p %buildroot/%_K3libdir/kconf_update_bin/
%if %with_noatun
mv %buildroot/%_K3apps/kconf_update/noatun20update %buildroot/%_K3libdir/kconf_update_bin/
%endif


%files
%files common

%files juk
%_K3bindir/juk
#%_K3bindir/juk-applet
%_K3iconsdir/crystalsvg/*/actions/juk_*.*
%_kde3_iconsdir/hicolor/*/apps/juk.*
%_K3apps/konqueror/servicemenus/jukservicemenu.desktop
%_K3apps/juk
%doc %_K3doc/en/juk
%_K3xdg_apps/juk.desktop

#%files akode
#%_K3libdir/libakode.so*
#%_K3libdir/libakode_*.so*

%if %with_arts
%files arts
%_K3libdir/mcop/Arts/*
%_K3libdir/mcop/arts*
%if %with_noatun
%exclude %_K3libdir/mcop/artseffects*
%endif
#%_K3libdir/mcop/akode*
%_K3libdir/mcop/*PlayObject.mcopclass
#%_K3libdir/mcop/mpg123*
%_K3libdir/mcop/ogg*
%_K3libdir/mcop/audiofile*
%_K3libdir/mcop/akodearts.*
#%_K3libdir/libmpg*.so*
%_K3libdir/libarts_*.so*
%_K3libdir/libartscontrol*.so*
%_K3libdir/libartsbuilder*.so*
%_K3libdir/libartsgui*.so*
%_K3libdir/libartsmidi*.so*
%_K3libdir/libartsmodules*.so*
#%_K3libdir/libaudiofile*.so*
%_K3libdir/libogg*.so*
%_K3bindir/arts*
%_K3bindir/midisend
%_K3bindir/mpeglibartsplay
%_K3apps/artsbuilder
%_K3apps/artscontrol
%_K3apps/kicker/applets/artscontrol*
%_kde3_iconsdir/hicolor/*/*/arts*
%_K3xdg_apps/arts*
%_K3mimelnk/*/x-arts*
#
%if %with_xine
%_K3lib/videothumbnail.so*
%_K3srv/videothumbnail.desktop
%_K3apps/videothumbnail
%endif
#
%doc %_K3doc/en/artsbuilder
%endif

%if %with_kaboodle
%files kaboodle
%_K3bindir/kaboodle
%_K3lib/libkaboodlepart*
%_kde3_iconsdir/hicolor/*/*/kaboodle.png
%_K3apps/kaboodle
%_K3xdg_apps/kaboodle.desktop
%_K3srv/kaboodleengine.desktop
%_K3srv/kaboodle_component.desktop
%doc %_K3doc/en/kaboodle
%endif

%files kaudiocreator
%_K3bindir/kaudiocreator
%_K3apps/kaudiocreator
%_K3apps/konqueror/servicemenus/audiocd_extract.desktop
%_K3conf_update/*kaudiocreator*
%_kde3_iconsdir/*/*/apps/kaudiocreator.*
%doc %_K3doc/en/kaudiocreator
%_K3xdg_apps/kaudiocreator.desktop
%_K3cfg/kaudiocreator.kcfg
%_K3cfg/kaudiocreator_encoders.kcfg

%files kfile
%_K3lib/kfile_*.so*
%_K3srv/kfile_*

%files kmid
%_K3bindir/kmid
%_K3libdir/libkmidlib.so*
%_K3lib/libkmidpart*.so*
%_K3apps/kmid
%_kde3_iconsdir/hicolor/*/apps/kmid.*
%_K3xdg_apps/kmid.desktop
%_K3mimelnk/audio/x-karaoke.desktop
%_K3srvtyp/audiomidi.desktop
%doc %_K3doc/en/kmid

%files kmix
%_K3bindir/kmix*
%_K3libdir/libkdeinit_kmix*.so*
%_K3lib/*kmix*.so*
%_kde3_iconsdir/hicolor/*/apps/kmix.*
%_K3apps/kmix
%_K3apps/kicker/applets/kmixapplet.desktop
%_K3start/restore_kmix_volumes.desktop
%_K3start/kmix.desktop
%_K3srv/kmixctrl_restore.desktop
%doc %_K3doc/en/kmix
#%doc %_K3doc/en/kcontrol/kmixcfg
%_K3xdg_apps/kmix.desktop
#%_K3xdg_apps/kmixcfg.desktop

%if %with_arts
%files krec
%_K3bindir/krec
%_K3libdir/libkdeinit_krec.so*
%_K3lib/krec*.so*
%_K3lib/kcm_krec*.so*
%_K3lib/libkrecexport_*.so*
%_K3apps/krec
%_K3srv/krec_export*
%_K3srv/kcm_krec*
%_K3srvtyp/krec_export*
%_kde3_iconsdir/hicolor/*/*/krec.*
#
%doc %_K3doc/en/krec
#
%_K3xdg_apps/krec.desktop
%endif

%files kscd
%_K3bindir/kscd
#%_K3bindir/cddaslave
%_K3bindir/workman2cddb.pl
#%_K3libdir/libworkman*.so*
%_K3apps/kscd
%_K3apps/profiles/kscd.profile.xml
%_kde3_iconsdir/hicolor/*/*/kscd.png
%_K3mimelnk/text/xmcd.desktop
%_K3apps/konqueror/servicemenus/audiocd_play.desktop
%doc %_K3doc/en/kscd
%_K3xdg_apps/kscd.desktop
%_K3cfg/kscd.kcfg

%if %with_noatun
%files noatun
%_K3apps/noatun
%_K3conf_update/noatun*
%_kde3_iconsdir/hicolor/*/*/noatun.png
%_K3libdir/kconf_update_bin/noatun*
%_K3libdir/mcop/Noatun
%_K3libdir/mcop/noatun*
%_K3libdir/mcop/ExtraStereo.mcopclass
%_K3libdir/mcop/VoiceRemoval.mcopclass
%_K3libdir/mcop/RawWriter.mcopclass
%_K3libdir/mcop/ExtraStereoGuiFactory.mcopclass
%_K3libdir/mcop/artseffects.*
%_K3libdir/mcop/winskinvis.*
#%_K3libdir/libdummy*
%_K3libdir/*noatun*.so*
%_K3libdir/libartseffects*.so*
%_K3lib/noatun*
%_K3libdir/libwinskinvis*.so*
%_K3bindir/noatun*
%_K3mimelnk/interface/x-winamp-skin.desktop
%_K3xdg_apps/noatun.desktop
%doc %_K3doc/en/noatun
%endif

%files libs
%exclude %_sysconfdir/xdg/menus/applications-merged/kde-multimedia-music.menu
%exclude %_K3xdg_dirs/kde-multimedia-music.directory
%_K3apps/kappfinder/apps/Multimedia
%_K3bindir/yaf-*
%_K3libdir/libmpeg*.so*
%_K3libdir/libkcddb.so*
%_K3libdir/libyaf*.so*
# kio
%_K3lib/kcm_cddb.so*
%_K3xdg_apps/audiocd.desktop
%_K3srv/audiocd.protocol
%_K3xdg_apps/libkcddb.desktop
%_K3libdir/libaudiocdplugins.so*
%_K3lib/libaudiocd_encoder_*.so*
%_K3lib/kcm_audiocd.so*
%_K3lib/kio_audiocd.so*
%_K3conf_update/kcmcddb-emailsettings.upd
%_K3conf_update/audiocd.upd
%_K3conf_update/upgrade-metadata.sh
%_K3cfg/audiocd_lame_encoder.kcfg
%_K3cfg/audiocd_vorbis_encoder.kcfg
%_K3cfg/libkcddb.kcfg
#%doc %_K3doc/en/kio_audiocd/
%doc %_K3doc/en/kioslave/audiocd.docbook

%files devel
%if %_keep_libtool_files
%_K3libdir/*.la
%endif
%_K3includedir/*.h
%if %with_arts
%_K3includedir/arts
%_K3includedir/mpeglib_artsplug
%endif
%_K3includedir/libkcddb
%if %with_noatun
%_K3includedir/noatun
%endif
%_K3includedir/mpeglib

%changelog
* Wed May 23 2012 Roman Savochenko <rom_as@altlinux.ru> 3.5.13-alt4
- Build fix for direct add -lkdeui -lkdecore -lDCOP -lqt-mt.

* Sun May 13 2012 Roman Savochenko <rom_as@altlinux.ru> 3.5.13-alt3
- Build require from kernel-headers-alsa is removed.

* Thu Apr 26 2012 Roman Savochenko <rom_as@altlinux.ru> 3.5.13-alt2
- Automake version is fixed to 1.11.5 detect.

* Thu Feb 23 2012 Roman Savochenko <rom_as@altlinux.ru> 3.5.13-alt1
- TDE 3.5.13 release build

* Fri Feb 10 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5.12-alt4.1
- Removed bad RPATH

* Fri Apr 15 2011 Igor Vlasenko <viy@altlinux.ru> 3.5.12-alt4
- system freedesktop menu support

* Wed Mar 23 2011 Sergey V Turchin <zerg@altlinux.org> 3.5.12-alt3
- don't show kmix window by default

* Thu Feb 24 2011 Sergey V Turchin <zerg@altlinux.org> 3.5.12-alt2
- move to alternate place

* Wed Dec 29 2010 Sergey V Turchin <zerg@altlinux.org> 3.5.12-alt1
- new version

* Thu Mar 11 2010 Sergey V Turchin <zerg@altlinux.org> 3.5.10-alt5
- fix to build with new autotools

* Thu May 14 2009 Sergey V Turchin <zerg@altlinux.org> 3.5.10-alt4
- kmix: display only one mixer for device (ALT#15259); thanks led@alt

* Tue Nov 25 2008 Sergey V Turchin <zerg at altlinux dot org> 3.5.10-alt3
- fix to determine build arch via $RPM_ARCH
- add patch from Debian to fix compile with gcc-4.3

* Tue Nov 25 2008 Sergey V Turchin <zerg at altlinux dot org> 3.5.10-alt2
- fix servicemenus/audiocd_extract.desktop placement

* Tue Aug 26 2008 Sergey V Turchin <zerg at altlinux dot org> 3.5.10-alt1
- new version

* Fri Feb 22 2008 Sergey V Turchin <zerg at altlinux dot org> 3.5.9-alt1
- new version

* Fri Jan 11 2008 Sergey V Turchin <zerg at altlinux dot org> 3.5.8-alt2
- don't build mpg123 arts plugin (#13859)

* Wed Oct 17 2007 Sergey V Turchin <zerg at altlinux dot org> 3.5.8-alt1
- new version

* Thu Aug 16 2007 Sergey V Turchin <zerg at altlinux dot org> 3.5.7-alt5
- add requires for encoders for kaudiocreator

* Thu Jul 05 2007 Sergey V Turchin <zerg at altlinux dot org> 3.5.7-alt4
- don't built noatun

* Tue Jul 03 2007 Sergey V Turchin <zerg at altlinux dot org> 3.5.7-alt3
- fix kscd digital playback defaults

* Mon Jul 02 2007 Sergey V Turchin <zerg at altlinux dot org> 3.5.7-alt2
- fix disabling kmix autostart

* Thu May 24 2007 Sergey V Turchin <zerg at altlinux dot org> 3.5.7-alt1
- new version

* Tue Mar 27 2007 Sergey V Turchin <zerg at altlinux dot org> 3.5.6-alt3
- built without libtunepimp

* Thu Feb 08 2007 Sergey V Turchin <zerg at altlinux dot org> 3.5.6-alt2
- fix desktop categories

* Fri Jan 26 2007 Sergey V Turchin <zerg at altlinux dot org> 3.5.6-alt1
- new version

* Mon Oct 16 2006 Sergey V Turchin <zerg at altlinux dot org> 3.5.5-alt1
- new version

* Mon Sep 04 2006 Sergey V Turchin <zerg at altlinux dot org> 3.5.4-alt1
- new version

* Tue Jun 13 2006 Sergey V Turchin <zerg at altlinux dot org> 3.5.3-alt2
- built without libxine

* Mon Jun 05 2006 Sergey V Turchin <zerg at altlinux dot org> 3.5.3-alt1
- new version

* Wed May 17 2006 Sergey V Turchin <zerg at altlinux dot org> 3.5.2-alt2
- rebuilt with new gcc

* Thu Mar 30 2006 Sergey V Turchin <zerg at altlinux dot org> 3.5.2-alt1
- new version
- add patch to kio_audiocd for flac config; 10x Alexey Morozov

* Fri Mar 24 2006 Sergey V Turchin <zerg at altlinux dot org> 3.5.1-alt3
- fix mpg123_artsplugin using mmx on i586
- rebuilt with new binutils

* Tue Feb 07 2006 Sergey V Turchin <zerg at altlinux dot org> 3.5.1-alt2
- fix build requires

* Wed Feb 01 2006 Sergey V Turchin <zerg at altlinux dot org> 3.5.1-alt1
- new version

* Tue Dec 06 2005 Sergey V Turchin <zerg at altlinux dot org> 3.5.0-alt1
- new version

* Fri Sep 02 2005 Sergey V Turchin <zerg at altlinux dot org> 3.4.1-alt2
- add autostart for kmix

* Mon Jun 06 2005 Sergey V Turchin <zerg at altlinux dot org> 3.4.1-alt1
- new version
- move akode to separate package

* Fri Apr 01 2005 Sergey V Turchin <zerg at altlinux dot org> 3.4.0-alt1
- new version

* Tue Jan 18 2005 Sergey V Turchin <zerg at altlinux dot org> 3.3.2-alt3
- rebuild

* Tue Jan 18 2005 Sergey V Turchin <zerg at altlinux dot org> 3.3.2-alt2
- rebuild with gcc3.4

* Tue Jan 11 2005 Sergey V Turchin <zerg at altlinux dot org> 3.3.2-alt1
- rebuild

* Tue Jan 04 2005 ZerG <zerg@altlinux.ru> 3.3.2-alt0.0.M24
- new version

* Mon Oct 25 2004 Sergey V Turchin <zerg at altlinux dot org> 3.3.1-alt2
- rebuild with libtunepimp

* Thu Oct 07 2004 Sergey V Turchin <zerg at altlinux dot org> 3.3.1-alt1
- new version

* Fri Oct 01 2004 Sergey V Turchin <zerg at altlinux dot org> 3.3.0-alt1
- new version

* Mon Jun 07 2004 Sergey V Turchin <zerg at altlinux dot org> 3.2.3-alt1
- new version
- fix kio_audiocd blocking cd with data

* Wed May 26 2004 Sergey V Turchin <zerg at altlinux dot org> 3.2.2-alt3
- rebuild with new libmusicbrainz
- don't package kaboodle

* Thu May 13 2004 Sergey V Turchin <zerg at altlinux dot org> 3.2.2-alt2
- add patches from SuSE to don't block device by kscd

* Mon Apr 12 2004 Sergey V Turchin <zerg at altlinux dot org> 3.2.2-alt1
- new version

* Wed Mar 17 2004 Sergey V Turchin <zerg at altlinux dot org> 3.2.1-alt1
- update code from KDE_3_2_BRANCH

* Wed Mar 03 2004 Sergey V Turchin <zerg at altlinux dot org> 3.2.0-alt1
- new version
- update code from KDE_3_2_BRANCH

* Wed Jan 28 2004 Sergey V Turchin <zerg at altlinux dot org> 3.1.4-alt4
- fix channel names translation in kmix
- build --without-alsa

* Tue Dec 02 2003 Sergey V Turchin <zerg at altlinux dot org> 3.1.4-alt3
- remove *.la files from package

* Wed Oct 01 2003 Sergey V Turchin <zerg at altlinux dot org> 3.1.4-alt2
- remove requires timidity
- add encode text in kmid

* Thu Sep 18 2003 Sergey V Turchin <zerg at altlinux dot org> 3.1.4-alt1
- update code from cvs

* Wed Aug 20 2003 Sergey V Turchin <zerg at altlinux dot org> 3.1.3-alt1
- update code from cvs

* Mon Jul 21 2003 Sergey V Turchin <zerg at altlinux dot org> 3.1.3-alt0.2
- rebuild

* Fri Jul 18 2003 Sergey V Turchin <zerg at altlinux dot org> 3.1.3-alt0.1
- update code from cvs

* Fri Jul 11 2003 Sergey V Turchin <zerg at altlinux dot org> 3.1.2-alt3
- update code from cvs
- don't build aktion

* Mon May 26 2003 Sergey V Turchin <zerg at altlinux dot ru> 3.1.2-alt2
- update code from cvs KDE_3_1_BRANCH
- add patch to save cddb in /var/lib/cddb

* Thu May 22 2003 Sergey V Turchin <zerg at altlinux dot ru> 3.1.2-alt1
- update code from cvs KDE_3_1_BRANCH
- add xine-arts-plugin patches 

* Tue Apr 29 2003 Sergey V Turchin <zerg at altlinux dot ru> 3.1.1-alt2
- update code from cvs KDE_3_1_BRANCH
- update xine_artsplugin

* Mon Mar 31 2003 Sergey V Turchin <zerg@altlinux.ru> 3.1.1-alt1
- update code from cvs KDE_3_1_BRANCH

* Fri Mar 14 2003 Sergey V Turchin <zerg@altlinux.ru> 3.1.1-alt0.1
- update code from cvs KDE_3_1_BRANCH
- update xine_artsplugin
- add MDK patches

* Thu Mar 13 2003 Sergey V Turchin <zerg@altlinux.ru> 3.1.0-alt6
- update code from cvs KDE_3_1_BRANCH

* Tue Feb 18 2003 Sergey V Turchin <zerg@altlinux.ru> 3.1.0-alt5
- update code from cvs KDE_3_1_BRANCH

* Fri Feb 07 2003 Sergey V Turchin <zerg@altlinux.ru> 3.1.0-alt4
- update from cvs

* Wed Jan 29 2003 Sergey V Turchin <zerg@altlinux.ru> 3.1.0-alt3
- update from cvs KDE_3_1_0_RELEASE
- build with libxine-1.0.0.beta3

* Wed Jan 22 2003 Sergey V Turchin <zerg@altlinux.ru> 3.1.0-alt2
- update code from cvs

* Mon Jan 13 2003 Sergey V Turchin <zerg@altlinux.ru> 3.1.0-alt1
- update code from cvs
- add MDK patches

* Fri Nov 22 2002 Sergey V Turchin <zerg@altlinux.ru> 3.1.0-alt0.21
- update code from cvs

* Wed Nov 06 2002 Sergey V Turchin <zerg@altlinux.ru> 3.1.0-alt0.20.rc2
- rc2

* Fri Nov 01 2002 Sergey V Turchin <zerg@altlinux.ru> 3.1.0-alt0.20.rc1
- rc1
- increase %%release to easy check dependencies

* Mon Oct 14 2002 Sergey V Turchin <zerg@altlinux.ru> 3.1.0-alt0.2
- update from cvs

* Tue Sep 10 2002 Sergey V Turchin <zerg@altlinux.ru> 3.0.3-alt3
- rebuild with gcc 3.2 & objprelink

* Mon Sep 02 2002 Sergey V Turchin <zerg@altlinux.ru> 3.0.3-alt2
- update from cvs
- add patches from cooker

* Mon Aug 19 2002 Sergey V Turchin <zerg@altlinux.ru> 3.0.3-alt1
- new version

* Wed Jul 31 2002 Sergey V Turchin <zerg@altlinux.ru> 3.0.2-alt2
- rebuild against new vorbis

* Wed Jul 03 2002 Sergey V Turchin <zerg@altlinux.ru> 3.0.2-alt1
- new version

* Mon Jun 17 2002 Sergey V Turchin <zerg@altlinux.ru> 3.0.1-alt2
- fix menu items

* Sun May 26 2002 ZerG <zerg@altlinux.ru> 3.0.1-alt1
- new version

* Wed May 15 2002 Sergey V Turchin <zerg@altlinux.ru> 3.0-alt4
- fix build with ogg vorbis libs

* Tue Apr 23 2002 Sergey V Turchin <zerg@altlinux.ru> 3.0-alt3
- move to /usr
- apply old patches
- update from cvs

* Mon Apr 08 2002 Sergey V Turchin <zerg@altlinux.ru> 3.0-alt2
- remove system catalogs from %%files

* Thu Apr 04 2002 Sergey V Turchin <zerg@altlinux.ru> 3.0-alt1
- release

* Tue Apr 02 2002 Sergey V Turchin <zerg@altlinux.ru> 3.0-alt0.2.cvs20020402
- update from cvs

* Fri Mar 29 2002 Sergey V Turchin <zerg@altlinux.ru> 3.0-alt0.1.rc3
- build for ALT

* Fri Mar 22 2002 Laurent MONTEL <lmontel@mandrakesoft.com> 3.0-0.rc3.1mdk
- RC3

* Fri Mar 01 2002 Laurent MONTEL <lmontel@mandrakesoft.com> 3.0-0.beta2.4mdk
- rebuild

* Sat Feb 09 2002 David BAUDENS <baudens@mandrakesoft.com> 3.0-0.beta2.3mdk
- Add missing files

* Fri Feb 08 2002 Laurent MONTEL <lmontel@mandrakesoft.com> 3.0-0.beta2.2mdk
- add patch1 fix compile

* Sat Feb 02 2002 Laurent MONTEL <lmontel@mandrakesoft.com> 3.0-0.beta2.1mdk
- beta2

* Sat Jan 05 2002 David BAUDENS <baudens@mandrakesoft.com> 3.0-0.beta1.4mdk
- Remove 7.2 support (too old to be easily supported)
- Don't build static libraries
- Allow KDE 2 and KDE 3 to be installed in same time
- Remove KDE 2's changelogs (KDE 2 and KDE 3 spec files have a separate life
  now)
- Add missing files
- Fix Group:

* Thu Dec 20 2001 Laurent MONTEL <lmontel@mandrakesoft.com> 3.0-0.beta1.3mdk
- Rename to allow KDE 2 and KDE 3 to be installed in same time

* Sat Dec 08 2001 Laurent MONTEL <lmontel@mandrakesoft.com> 3.0beta1-3mdk
- kde 3.0 beta1

* Thu Nov 29 2001 Laurent MONTEL <lmontel@mandrakesoft.com> 3.0-2mdk
- Improved spec file

* Sat Nov 24 2001 Laurent MONTEL <lmontel@mandrakesoft.com> 3.0-1mdk
- kde 3.0

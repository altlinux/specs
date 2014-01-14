
%define rname kid3
Name: kde4-%rname
Version: 3.0.2
Release: alt2

Group: Sound
Summary: ID3 tagger
License: GPLv2
Url: http://kid3.sourceforge.net/

Provides: %rname = %version-%release
Conflicts: kid3 <= 1.3-alt1

Source: kid3-%{version}.tar
Patch1: kid3-3.0.2-alt-desktop_ru_uk.patch
Patch2: kid3-3.0.2-alt-libdir.patch
Patch3: kid3-3.0.2-alt-cli-no-phonon.patch

BuildRequires(pre): kde4libs-devel
# Automatically added by buildreq on Mon May 21 2012 (-bi)
# optimized out: automoc cmake cmake-modules docbook-dtds docbook-style-xsl elfutils fontconfig fontconfig-devel glibc-devel-static id3lib kde-common-devel kde4libs libICE-devel libSM-devel libX11-devel libXScrnSaver-devel libXau-devel libXcomposite-devel libXcursor-devel libXdamage-devel libXdmcp-devel libXext-devel libXfixes-devel libXft-devel libXi-devel libXinerama-devel libXpm-devel libXrandr-devel libXrender-devel libXt-devel libXtst-devel libXv-devel libXxf86misc-devel libXxf86vm-devel libavcodec-devel libavutil-devel libdbus-devel libdbusmenu-qt2 libflac-devel libfreetype-devel libgpg-error libogg-devel libopencore-amrnb0 libopencore-amrwb0 libpng-devel libqt4-core libqt4-dbus libqt4-devel libqt4-gui libqt4-network libqt4-svg libqt4-xml libsoprano-devel libssl-devel libstdc++-devel libxkbfile-devel phonon-devel pkg-config python-base xml-common xml-utils xorg-kbproto-devel xorg-xf86miscproto-devel xorg-xproto-devel zlib-devel
#BuildRequires: gcc-c++ glib2-devel id3lib-devel kde4libs-devel libavdevice-devel libavformat-devel libchromaprint-devel libflac++-devel libicu libmpeg4ip-devel libqt3-devel libswscale-devel libtag-devel libvorbis-devel zlib-devel-static
BuildRequires: gcc-c++ glib2-devel id3lib-devel libavdevice-devel libavformat-devel libchromaprint-devel libflac++-devel libswscale-devel libtag-devel libvorbis-devel
# libmpeg4ip-devel
BuildRequires: phonon-devel libreadline-devel /usr/bin/xsltproc

%description
Kid3 - Efficient Audio Tagger

With Kid3 you can:

- Edit ID3v1.1 tags
- Edit all ID3v2.3 and ID3v2.4 frames
- Convert between ID3v1.1, ID3v2.3 and ID3v2.4 tags
- Edit tags in MP3, Ogg/Vorbis, FLAC, MPC, APE, MP4/AAC, MP2, Speex,
  TrueAudio, WavPack, WMA, WAV, AIFF files and tracker modules.
- Edit tags of multiple files, e.g. the artist, album, year and genre
  of all files of an album typically have the same values and can be
  set together.
- Generate tags from filenames
- Generate tags from the contents of tag fields
- Generate filenames from tags
- Rename directories from tags
- Generate playlist files
- Automatic case conversion and string translation
- Import and export album data
- Import from gnudb.org, TrackType.org, MusicBrainz, Discogs, Amazon

Authors: Urs Fleisch

%package -n %rname-common
Summary: Common empty package for %rname
Group: System/Configuration/Other
BuildArch: noarch
Conflicts: kde4-kid3 < 3.0
%description -n %rname-common
Common empty package for %rname

%package -n %rname-core
Summary: Core files needed for %rname
Group: System/Libraries
Requires: %rname-common = %EVR
%description -n %rname-core
Core files needed for %rname

%package -n %rname-ui-kde4
Summary: ID3 tagger KDE4 UI
Group: Sound
Requires: %rname-core = %EVR
Provides: %rname = %version-%release
Provides: kde4-kid3 = %EVR
Obsoletes: kde4-kid3 < %EVR
Conflicts: kid3 <= 1.3-alt1
%description -n %rname-ui-kde4
Package contains KDE4 UI.
%{description}

%package -n %rname-ui-qt4
Summary: ID3 tagger Qt4 UI
Group: Sound
Requires: %rname-core = %EVR
#Provides: %rname = %version-%release
%description -n %rname-ui-qt4
Package contains Qt4 UI.
%{description}

%package -n %rname-ui-cli
Summary: ID3 tagger CLI UI
Group: Sound
Requires: %rname-core = %EVR
#Provides: %rname = %version-%release
%description -n %rname-ui-cli
Package contains command line UI.
%{description}


%package -n libkid3-core
Summary: %name library
Group: System/Libraries
Requires: %rname-common = %EVR
%description -n libkid3-core
%name library.

%package -n libkid3-gui
Summary: %name library
Group: System/Libraries
Requires: %rname-common = %EVR
%description -n libkid3-gui
%name library.


%prep
%setup -q -n %rname-%version
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
%K4cmake \
    -DWITH_APPS="Qt;CLI;KDE" \
    -DWITH_QT4:BOOL=ON \
    -DWITH_QT5:BOOL=OFF \
    -DWITH_TAGLIB:BOOL=ON \
    -DWITH_ID3LIB:BOOL=ON \
    -DWITH_VORBIS:BOOL=ON \
    -DWITH_FLAC:BOOL=ON \
    -DWITH_CHROMAPRINT=ON \
    -DWITH_DBUS=ON \
    #
#    -DWITH_MP4V2:BOOL=ON \
%K4make


%install
%K4install
%find_lang --with-kde --with-qt %rname

%files -n %rname-common -f %rname.lang
%_K4dbus_interfaces/*id3*

%files -n %rname-core
%_libdir/kid3/plugins/lib*.so

%files -n %rname-ui-kde4
%doc AUTHORS NEWS README ChangeLog
%_K4bindir/%rname
%_K4xdg_apps/%rname.desktop
%_K4iconsdir/hicolor/*/apps/%rname.*
%_K4apps/%rname/

%files -n %rname-ui-qt4
%doc AUTHORS NEWS README ChangeLog
%_bindir/%rname-qt
%doc %_docdir/kid3-qt/
%_iconsdir/*/*/apps/kid3-qt.*
%_desktopdir/kid3-qt.desktop

%files -n %rname-ui-cli
%doc AUTHORS NEWS README ChangeLog
%_K4bindir/%rname-cli

%files -n libkid3-core
%_libdir/libkid3-core.so.*

%files -n libkid3-gui
%_libdir/libkid3-gui.so.*

%changelog
* Tue Jan 14 2014 Sergey V Turchin <zerg@altlinux.org> 3.0.2-alt2
- built CLI UI without phonon

* Thu Jan 09 2014 Sergey V Turchin <zerg@altlinux.org> 3.0.2-alt1
- new version

* Wed Sep 18 2013 Sergey V Turchin <zerg@altlinux.org> 2.3-alt0.M70P.1
- build for M70P

* Tue Sep 17 2013 Sergey V Turchin <zerg@altlinux.org> 2.3-alt1
- new version

* Mon May 21 2012 Sergey V Turchin <zerg@altlinux.org> 2.1-alt0.M60P.1
- build for M60P

* Mon May 21 2012 Sergey V Turchin <zerg@altlinux.org> 2.1-alt1
- new version

* Mon Jan 30 2012 Sergey V Turchin <zerg@altlinux.org> 2.0.1-alt0.M60P.1
- built for M60P

* Mon Dec 19 2011 Sergey V Turchin <zerg@altlinux.org> 2.0.1-alt1
- new version

* Mon Apr 25 2011 Sergey V Turchin <zerg@altlinux.org> 1.6-alt2
- fix build requires

* Thu Mar 10 2011 Sergey V Turchin <zerg@altlinux.org> 1.6-alt1
- new version
- move to standart place

* Mon Oct 18 2010 Sergey V Turchin <zerg@altlinux.org> 1.5-alt0.M51.1
- built for M51

* Mon Oct 18 2010 Sergey V Turchin <zerg@altlinux.org> 1.5-alt1
- new version

* Mon Mar 15 2010 Sergey V Turchin <zerg@altlinux.org> 1.4-alt0.M51.1
- built for M51

* Mon Mar 15 2010 Sergey V Turchin <zerg@altlinux.org> 1.4-alt1
- new version

* Mon Nov 30 2009 Sergey V Turchin <zerg@altlinux.org> 1.3-alt1.M51.1
- built for M51

* Wed Nov 25 2009 Sergey V Turchin <zerg@altlinux.org> 1.3-alt2
- fix translation files placement

* Wed Nov 25 2009 Sergey V Turchin <zerg@altlinux.org> 1.3-alt0.M51.1
- built for M51

* Tue Nov 24 2009 Sergey V Turchin <zerg@altlinux.org> 1.3-alt1
- new version

* Wed Jul 08 2009 Sergey V Turchin <zerg@altlinux.org> 1.2-alt3
- built with kde4

* Wed Aug 13 2008 Sergey V Turchin <zerg at altlinux dot org> 1.0-alt0.M41.2
- built with kde3

* Tue Aug 12 2008 Sergey V Turchin <zerg at altlinux dot org> 1.0-alt0.M40.1
- new version

* Sun Dec 23 2007 Sergey V Turchin <zerg at altlinux dot org> 0.10-alt0.M40.1
- new version

* Sat Jul 07 2007 Sergey V Turchin <zerg at altlinux dot org> 0.9-alt0.1.M30
- new version

* Sun Nov 05 2006 Zerg <zerg at altlinux dot org> 0.7-alt0.1.M30
- built for ALT


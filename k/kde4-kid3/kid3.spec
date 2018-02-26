
%define rname kid3
Name: kde4-%rname
Version: 2.1
Release: alt1

Group: Sound
Summary: ID3 tagger
License: GPLv2
Url: http://kid3.sourceforge.net/

Provides: %rname = %version-%release
Conflicts: kid3 <= 1.3-alt1

Source: kid3-%{version}.tar.gz
Patch1: kid3-2.1-alt-desktop_ru_uk.patch

BuildRequires(pre): kde4libs-devel
# Automatically added by buildreq on Mon May 21 2012 (-bi)
# optimized out: automoc cmake cmake-modules docbook-dtds docbook-style-xsl elfutils fontconfig fontconfig-devel glibc-devel-static id3lib kde-common-devel kde4libs libICE-devel libSM-devel libX11-devel libXScrnSaver-devel libXau-devel libXcomposite-devel libXcursor-devel libXdamage-devel libXdmcp-devel libXext-devel libXfixes-devel libXft-devel libXi-devel libXinerama-devel libXpm-devel libXrandr-devel libXrender-devel libXt-devel libXtst-devel libXv-devel libXxf86misc-devel libXxf86vm-devel libavcodec-devel libavutil-devel libdbus-devel libdbusmenu-qt2 libflac-devel libfreetype-devel libgpg-error libogg-devel libopencore-amrnb0 libopencore-amrwb0 libpng-devel libqt4-core libqt4-dbus libqt4-devel libqt4-gui libqt4-network libqt4-svg libqt4-xml libsoprano-devel libssl-devel libstdc++-devel libxkbfile-devel phonon-devel pkg-config python-base xml-common xml-utils xorg-kbproto-devel xorg-xf86miscproto-devel xorg-xproto-devel zlib-devel
#BuildRequires: gcc-c++ glib2-devel id3lib-devel kde4libs-devel libavdevice-devel libavformat-devel libchromaprint-devel libflac++-devel libicu libmpeg4ip-devel libqt3-devel libswscale-devel libtag-devel libvorbis-devel zlib-devel-static
BuildRequires: gcc-c++ glib2-devel id3lib-devel libavdevice-devel libavformat-devel libchromaprint-devel libflac++-devel libmpeg4ip-devel libswscale-devel libtag-devel libvorbis-devel
BuildRequires: phonon-devel


%description
Kid3 - Efficient ID3 Tagger

With Kid3 you can:

- Edit ID3v1.1 tags
- Edit all ID3v2.3 frames
- Convert between ID3v1.1 and ID3v2.3 tags
- Edit Ogg/Vorbis tags
- Edit FLAC tags
- Edit tags of multiple files, e.g. the artist, album, year and genre
  of all files of an album typically have the same values and can be
  set together.
- Generate tags from filenames
- Generate filenames from tags
- Generate playlist files
- Automatic case conversion and string translation
- Import of album data from freedb.org, MusicBrainz and other data sources
- Export of album data in various formats

Authors: Urs Fleisch


%prep
%setup -q -n %rname-%version
%patch1 -p1


%build
%K4cmake \
    -DWITH_TAGLIB:BOOL=ON \
    -DWITH_MP4V2:BOOL=ON \
    -DWITH_ID3LIB:BOOL=ON \
    -DWITH_VORBIS:BOOL=ON \
    -DWITH_FLAC:BOOL=ON \
    -DWITH_CHROMAPRINT=ON \
    -DWITH_DBUS=ON \
    -DWITH_KDE:BOOL=ON
%K4make


%install
%K4install
%K4find_lang --with-kde %rname


%files -f %rname.lang
%doc AUTHORS NEWS README ChangeLog
%_K4bindir/%rname
%_K4xdg_apps/%rname.desktop
%_K4iconsdir/hicolor/*/apps/%rname.*
%_K4dbus_interfaces/*id3*
%_K4apps/%rname/

%changelog
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


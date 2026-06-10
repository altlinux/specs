
%def_disable mp4

%define sover 3
%define libkid3_core libkid3-core%sover
%define libkid3_gui libkid3-gui%sover

%define rname kid3
Name: %rname
Version: 3.10.0
Release: alt1
%K6init

Group: Sound
Summary: ID3 tagger
License: GPL-2.0-or-later
Url: http://kid3.sourceforge.net/

Source: kid3-%{version}.tar
Source1: ru.po

BuildRequires(pre): rpm-build-kf6
BuildRequires: cmake extra-cmake-modules
BuildRequires: gettext-tools
BuildRequires: gcc-c++ glib2-devel libreadline-devel /usr/bin/xsltproc
BuildRequires: libavdevice-devel libavformat-devel libswscale-devel
# libavresample-devel
BuildRequires: libchromaprint-devel
BuildRequires: id3lib-devel taglib-devel
BuildRequires: libflac++-devel libvorbis-devel
%if_enabled mp4
BuildRequires: libmpeg4ip-devel
%endif
BuildRequires: qt6-declarative-devel qt6-multimedia-devel qt6-tools-devel qt6-phonon-devel
BuildRequires: kf6-kio-devel
BuildRequires: kf6-kdoctools kf6-kdoctools-devel
BuildRequires: kf6-kauth-devel kf6-kbookmarks-devel kf6-kcodecs-devel kf6-kcompletion-devel kf6-kconfig-devel
BuildRequires: kf6-kconfigwidgets-devel kf6-kcoreaddons-devel kf6-solid-devel kf6-kxmlgui-devel
BuildRequires: kf6-kdoctools kf6-kdoctools-devel
BuildRequires: kf6-kio-devel kf6-kitemviews-devel kf6-kjobwidgets-devel kf6-kservice-devel kf6-kwidgetsaddons-devel


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

%package common
Summary: Common empty package for %name
Group: System/Configuration/Other
BuildArch: noarch
Requires: kf6-filesystem
Provides: kde5-kid3-common = %EVR
Obsoletes: kde5-kid3-common < %EVR
%description common
Common empty package for %name

%package core
Summary: Core files needed for %name
Group: System/Libraries
Requires: %name-common = %EVR
Provides: kde5-kid3-core = %EVR
Obsoletes: kde5-kid3-core < %EVR
%description core
Core files needed for %name

%package -n %rname-ui-kde
Summary: ID3 tagger KDE UI
Group: Sound
#Provides: %rname = %version-%release
Provides: kde-kid3 = %EVR
Provides: kde5-kid3 = %EVR
Obsoletes: kde5-kid3 < %EVR
Provides: kid3-ui-kde5 = %EVR
Obsoletes: kid3-ui-kde5 < %EVR
Requires: %name-core >= %EVR
%description -n %rname-ui-kde
Package contains KDE UI.
%{description}

%package -n %rname-ui-qt
Summary: ID3 tagger Qt UI
Group: Sound
Provides: kid3-ui-qt5 = %EVR
Obsoletes: kid3-ui-qt5 < %EVR
Requires: %name-core >= %EVR
%description -n %rname-ui-qt
Package contains Qt UI.
%{description}

%package -n %rname-ui-cli
Summary: ID3 tagger CLI UI
Group: Sound
Provides: kid3-ui-cli5 = %EVR
Obsoletes: kid3-ui-cli5 < %EVR
Requires: %name-core >= %EVR
%description -n %rname-ui-cli
Package contains command line UI.
%{description}


%package -n %libkid3_core
Summary: %name library
Group: System/Libraries
Requires: %name-common >= %EVR
Obsoletes: libkid3-core5 < %EVR
%description -n %libkid3_core
%name library.

%package -n %libkid3_gui
Summary: %name library
Group: System/Libraries
Requires: %name-common >= %EVR
Obsoletes: libkid3-gui5 < %EVR
%description -n %libkid3_gui
%name library.


%prep
%setup -q -n %rname-%version

#tmp_file=`mktemp`
#msgcat --use-first translations/po/ru/kid3_qt.po %SOURCE1 >"$tmp_file"
#cat "$tmp_file" >translations/po/ru/kid3_qt.po
#rm -f "$tmp_file"

#MAJOR="6"
MAJOR=""
# setup libs names
#find -type f -name CMakeLists.txt | \
#while read f ; do
#    for l in kid3-gui kid3-core ; do
#	sed -i "s|${l}|${l}${MAJOR}|" $f
#    done
#done

# setup libs sonames
for d in core gui ; do
    echo "set_target_properties(kid3-${d}${MAJOR} PROPERTIES SOVERSION \${CPACK_PACKAGE_VERSION_MAJOR} VERSION \${KID3_VERSION})" >> src/${d}/CMakeLists.txt
done


%build
#    -DWITH_APPS="qt;qml;cli;kde" \
%K6cmake \
    -DWITH_APPS="qt;cli;kde" \
    -DWITH_BINDIR=%_K6bin \
    -DWITH_LIBDIR=%_lib \
    -DWITH_DATAROOTDIR=%_datadir \
    -DWITH_DOCDIR=%_docdir/%name \
    -DBUILD_WITH_QT6:BOOL=ON \
    -DQT_MAJOR_VERSION=6 \
    -DWITH_FFMPEG=ON \
    -DWITH_TAGLIB:BOOL=ON \
    -DWITH_ID3LIB:BOOL=ON \
    -DWITH_VORBIS:BOOL=ON \
%if_enabled mp4
    -DWITH_MP4V2:BOOL=ON \
%endif
    -DWITH_FLAC:BOOL=ON \
    -DWITH_CHROMAPRINT=ON \
    -DWITH_DBUS=ON \
    -DWITH_QML=OFF \
    #
#    -DWITH_PLUGINSDIR=%_libdir/kid3-kf6/plugins \
#    -DWITH_QMLDIR=%_datadir/kid3-kf6/qml \
#    -DWITH_TRANSLATIONSDIR=share/kid3-kf6/translations \
%K6make


%install
%K6install
%find_lang --with-kde --with-qt %rname

%files common -f %rname.lang
%dir %_datadir/kid3/
%dir %_datadir/kid3/translations

%files core
%_libdir/kid3/plugins/lib*.so

%files -n %rname-ui-kde
%doc AUTHORS NEWS README ChangeLog
%_K6bin/%rname
%_K6data/kxmlgui?/kid3/
%_K6xdgapp/*.kid3.desktop
%_K6icon/hicolor/*/apps/kid3.*
%_datadir/metainfo/*.kid3.*

%files -n %rname-ui-qt
%doc AUTHORS NEWS README ChangeLog
%_K6bin/%rname-qt
%doc %_docdir/kid3/
%_iconsdir/*/*/apps/kid3-qt.*
%_desktopdir/*.kid3-qt.desktop
%_datadir/metainfo/*.kid3-qt.*

%files -n %rname-ui-cli
%doc AUTHORS NEWS README ChangeLog
%_K6bin/%rname-cli

%files -n %libkid3_core
%_libdir/libkid3-core.so.%sover
%_libdir/libkid3-core.so.*

%files -n %libkid3_gui
%_libdir/libkid3-gui.so.%sover
%_libdir/libkid3-gui.so.*

#%files devel
#%_K6link/lib*.so
#%_K6dbus_iface/*id3*

%changelog
* Wed Jun 10 2026 Sergey V Turchin <zerg@altlinux.org> 3.10.0-alt1
- new version

* Sat Feb 07 2026 Sergey V Turchin <zerg@altlinux.org> 3.9.7-alt1
- new version

* Tue May 13 2025 Sergey V Turchin <zerg@altlinux.org> 3.9.6-alt2
- build with new taglib

* Thu Dec 05 2024 Sergey V Turchin <zerg@altlinux.org> 3.9.6-alt1
- new version

* Mon Sep 11 2023 Sergey V Turchin <zerg@altlinux.org> 3.9.4-alt1
- new version

* Wed Apr 19 2023 Sergey V Turchin <zerg@altlinux.org> 3.9.3-alt1
- new version

* Tue Aug 30 2022 Sergey V Turchin <zerg@altlinux.org> 3.9.2-alt1
- new version

* Wed Mar 02 2022 Sergey V Turchin <zerg@altlinux.org> 3.9.1-alt1
- new version
- obsolete kid3-kde4

* Thu Sep 30 2021 Sergey V Turchin <zerg@altlinux.org> 3.8.7-alt1
- new version

* Mon May 24 2021 Sergey V Turchin <zerg@altlinux.org> 3.8.6-alt1
- new version

* Wed Apr 15 2020 Sergey V Turchin <zerg@altlinux.org> 3.8.2-alt2
- fix russian GenericName in menu-item

* Wed Feb 12 2020 Sergey V Turchin <zerg@altlinux.org> 3.8.2-alt1
- new version

* Wed Dec 18 2019 Sergey V Turchin <zerg@altlinux.org> 3.8.0-alt1
- new version

* Tue Oct 09 2018 Sergey V Turchin <zerg@altlinux.org> 3.6.2-alt2
- update russian translation

* Thu Sep 13 2018 Sergey V Turchin <zerg@altlinux.org> 3.6.2-alt1
- new version

* Fri Jun 15 2018 Sergey V Turchin <zerg@altlinux.org> 3.6.1-alt1
- new version

* Wed Mar 28 2018 Sergey V Turchin <zerg@altlinux.org> 3.6.0-alt1
- new version

* Thu Dec 14 2017 Sergey V Turchin <zerg@altlinux.org> 3.5.1-alt1
- new version

* Thu Aug 10 2017 Sergey V Turchin <zerg@altlinux.org> 3.4.5-alt2
- rebuild with new chromaprint

* Tue Jun 06 2017 Sergey V Turchin <zerg@altlinux.org> 3.4.5-alt1
- new version

* Mon Jan 09 2017 Sergey V Turchin <zerg@altlinux.org> 3.4.4-alt1
- new version

* Fri Jul 15 2016 Sergey V Turchin <zerg@altlinux.org> 3.4.1-alt2
- fix load translations

* Thu Jul 14 2016 Sergey V Turchin <zerg@altlinux.org> 3.4.1-alt1
- new version

* Mon Nov 09 2015 Sergey V Turchin <zerg@altlinux.org> 3.3.0-alt1
- initial build

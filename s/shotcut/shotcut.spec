# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

%define _vstring %(echo %{version} |tr -d ".")

Name: shotcut
Version: 24.04.28
Release: alt1
Summary: A free, open source, cross-platform video editor
Summary(ru_RU.UTF-8): Свободный кросс-платформенный видеоредактор
License: GPL-3.0+
Group: Video
Url: http://www.shotcut.org/
Packager: Anton Midyukov <antohami@altlinux.org>

ExcludeArch: armh

Source: %name-%version.tar

BuildRequires(pre): cmake
BuildRequires: gcc-c++
BuildRequires: desktop-file-utils
BuildRequires: libappstream-glib
BuildRequires: pkgconfig(Qt6Charts)
BuildRequires: pkgconfig(Qt6Concurrent)
BuildRequires: pkgconfig(Qt6Core)
BuildRequires: pkgconfig(Qt6Gui)
BuildRequires: pkgconfig(Qt6Qml)
BuildRequires: pkgconfig(Qt6Multimedia)
BuildRequires: pkgconfig(Qt6Network)
BuildRequires: pkgconfig(Qt6OpenGL)
BuildRequires: pkgconfig(Qt6PrintSupport)
BuildRequires: pkgconfig(Qt6Quick)
BuildRequires: pkgconfig(Qt6WebSockets)
BuildRequires: pkgconfig(Qt6Xml)
BuildRequires: pkgconfig(Qt6Sql)
BuildRequires: pkgconfig(Qt6UiTools)
BuildRequires: qt6-linguist
BuildRequires: mlt7xx-devel
BuildRequires: pkgconfig(mlt-framework-7)
BuildRequires: libx264-devel
BuildRequires: pkgconfig(sdl2)
BuildRequires: ImageMagick-tools
BuildRequires: qt6-declarative-devel
BuildRequires: qt6-tools-devel
BuildRequires: qt6-imageformats
BuildRequires: libfftw3-devel

Requires: %name-data = %version
Requires: mlt-utils
Requires: gst-plugins-bad1.0
Requires: frei0r-plugins
Requires: ladspa_sdk
Requires: lame
Requires: ffmpeg ffprobe ffplay
Requires: libSDL2
# see bug 34876
Requires: libqt6-quickcontrols2
# see bug 34877
Requires: qt6-5compat
# Needed for timeline
Requires: libqt6-sql qt6-declarative

Provides: %name-data = %EVR
Obsoletes: %name-data < %EVR

%description
These are all currently implemented features:
 * supports oodles of audio and video formats and codecs;
 * supports many image formats as image sequences;
 * no import required - native editing;
 * frame-accurate seeking for many formats;
 * multi-format timeline;
 * screen capture (Linux only) including background capture;
 * webcam capture (Linux only);
 * audio capture (Linux only; PulseAudio, JACK, or ALSA);
 * network stream playback (HTTP, HLS, RTMP, RTSP, MMS, UDP);
 * frei0r video generator plugins (e.g. color bars and plasma);
 * Blackmagic Design SDI and HDMI for input and preview monitoring;
 * JACK transport sync;
 * deinterlacing;
 * detailed media properties panel;
 * recent files panel with search;
 * drag-n-drop files from file manager;
 * save and load trimmed clip as MLT XML file;
 * load and play complex MLT XML file as a clip;
 * audio signal level meter;
 * volume control;
 * scrubbing and transport control;
 * flexible UI through dock-able panels;
 * encode/transcode to a variety of formats and codecs;
 * capture (record);
 * stream (encode to IP) files and any capture source;
 * batch encoding with job control;
 * MLT XML playlists;
 * unlimited undo and redo for playlist edits;
 * connect to Melted servers over MVCP TCP protocol;
 * control the transport playback of Melted units;
 * edit Melted playlists including support for undo/redo;
 * OpenGL GPU-based image processing;
 * multi-core parallel image processing when not using GPU;
 * video filters;
 * audio filters;
 * 3-way color wheels for color correction and grading;
 * eye dropper tool to pick neutral color for white balancing;
 * HTML5 (sans audio and video) as video source and filters;
 * Leap Motion for jog/shuttle control;
 * DeckLink SDI keyer output - internal or external;
 * UI themes/skins: native-OS look and custom dark and light;
 * control video zoom in the player.

%prep
%setup

# Postmortem debugging tools for MinGW.
rm -rf drmingw

%build
%cmake -DCMAKE_INSTALL_LIBDIR=%_lib \
       -DSHOTCUT_VERSION="%version"
%cmake_build

%install
%cmake_install
chmod a+x %buildroot/%_datadir/shotcut/qml/export-edl/rebuild.sh

for i in 16 32 48; do
    mkdir -p %buildroot/%_iconsdir/hicolor/"$i"x"$i"/apps
    convert icons/%name-logo-64.png -resize "$i"x"$i" \
    %buildroot/%_iconsdir/hicolor/"$i"x"$i"/apps/org.shotcut.Shotcut.png
done

%files
%doc COPYING README.md
%_bindir/%name
%_libdir/*.so*
%_datadir/%name
%_desktopdir/org.shotcut.Shotcut.desktop
%_iconsdir/hicolor/*/apps/org.shotcut.Shotcut.png
%_datadir/mime/packages/org.shotcut.Shotcut.xml
%_datadir/metainfo/org.shotcut.Shotcut.metainfo.xml
%_man1dir/*

%changelog
* Mon Apr 29 2024 Andrey Cherepanov <cas@altlinux.org> 24.04.28-alt1
- New version.

* Thu Apr 18 2024 Andrey Cherepanov <cas@altlinux.org> 24.04.13-alt1
- New version.

* Fri Mar 01 2024 Andrey Cherepanov <cas@altlinux.org> 24.02.29-alt1
- New version.

* Mon Feb 19 2024 Andrey Cherepanov <cas@altlinux.org> 24.02.19-alt1
- New version.

* Mon Feb 19 2024 Andrey Cherepanov <cas@altlinux.org> 24.02.18-alt1
- New version.

* Thu Feb 01 2024 Andrey Cherepanov <cas@altlinux.org> 24.01.31-alt1
- New version.

* Mon Jan 29 2024 Andrey Cherepanov <cas@altlinux.org> 24.01.28-alt1
- New version.

* Sun Jan 14 2024 Andrey Cherepanov <cas@altlinux.org> 24.01.13-alt1
- New version.

* Fri Jan 05 2024 Andrey Cherepanov <cas@altlinux.org> 23.12.15-alt1
- New version (ALT #48666).

* Wed Sep 20 2023 Ivan A. Melnikov <iv@altlinux.org> 23.07.08-alt1.1
- NMU: Avoid build dependency on mlt 6.

* Sun Jul 09 2023 Andrey Cherepanov <cas@altlinux.org> 23.07.08-alt1
- New version.

* Thu Jun 15 2023 Andrey Cherepanov <cas@altlinux.org> 23.06.14-alt1
- New version.

* Mon May 15 2023 Andrey Cherepanov <cas@altlinux.org> 23.05.14-alt1
- New version.

* Mon May 08 2023 Andrey Cherepanov <cas@altlinux.org> 23.05.07-alt1
- New version.

* Fri Apr 21 2023 Andrey Cherepanov <cas@altlinux.org> 23.04.20-alt1
- New version.

* Mon Apr 10 2023 Leonid Znamenok <respublica@altlinux.org> 23.04.03-alt1
- New version 23.04.03.
- Updated to QT 6

* Tue Dec 27 2022 Andrey Cherepanov <cas@altlinux.org> 22.12.21-alt1
- New version.

* Thu Dec 01 2022 Andrey Cherepanov <cas@altlinux.org> 22.11.25-alt2
- Used real Shotcut version from tag (ALT #44180).

* Mon Nov 28 2022 Andrey Cherepanov <cas@altlinux.org> 22.11.25-alt1
- New version.

* Sun Oct 30 2022 Andrey Cherepanov <cas@altlinux.org> 22.10.25-alt1
- New version.

* Tue Sep 27 2022 Andrey Cherepanov <cas@altlinux.org> 22.09.23-alt1
- New version.

* Fri Sep 02 2022 Andrey Cherepanov <cas@altlinux.org> 22.09.01-alt1
- New version.

* Sun Aug 21 2022 Andrey Cherepanov <cas@altlinux.org> 22.06.23-alt1
- New version (ALT #42375).
- Joined %name-data in main package.

* Thu Oct 01 2020 Sergey V Turchin <zerg@altlinux.org> 20.09.27-alt1
- new version

* Mon Feb 17 2020 Fr. Br. George <george@altlinux.ru> 20.02.02-alt1
- new version 20.02.02

* Wed Oct 03 2018 Fr. Br. George <george@altlinux.ru> 18.10.01-alt1
- new version 18.10.01

* Tue Jul 03 2018 Anton Midyukov <antohami@altlinux.org> 18.06.02-alt1
- new version 18.07
- unpackaged files in buildroot should terminate build
- update from git
- disabled autoupdate check

* Sat May 05 2018 Anton Midyukov <antohami@altlinux.org> 18.04-alt3
- Added missing requires qt5-quickcontrols
- Added missing requires qt5-graphicaleffects

* Fri Apr 20 2018 Anton Midyukov <antohami@altlinux.org> 18.04-alt2
- Update buildrequires and requires
- Added shotcut.appdata.xml

* Sat Apr 07 2018 Cronbuild Service <cronbuild@altlinux.org> 18.04-alt1
- repocop cronbuild 20180407. At your service.

* Mon Mar 19 2018 Fr. Br. George <george@altlinux.ru> 18.03-alt2
- Patch "/bin/nice" location
- Use native .desktop
- Added missing requires ff* and melt binaries

* Sun Mar 04 2018 Cronbuild Service <cronbuild@altlinux.org> 18.03-alt1
- new version (18.03) with rpmgs script

* Tue Feb 13 2018 Cronbuild Service <cronbuild@altlinux.org> 18.02-alt1
- repocop cronbuild 20180213. At your service.

* Sun Jan 28 2018 Anton Midyukov <antohami@altlinux.org> 18.01-alt2
- Added missing requires libSDL2
- Fix make install

* Tue Jan 02 2018 Cronbuild Service <cronbuild@altlinux.org> 18.01-alt1
- new version (18.01) with rpmgs script

* Wed Dec 06 2017 Cronbuild Service <cronbuild@altlinux.org> 17.12-alt1
- new version (17.12) with rpmgs script

* Tue Nov 07 2017 Cronbuild Service <cronbuild@altlinux.org> 17.11-alt1
- repocop cronbuild 20171107. At your service.

* Sat Oct 07 2017 Cronbuild Service <cronbuild@altlinux.org> 17.10-alt1
- repocop cronbuild 20171007. At your service.

* Fri Sep 01 2017 Cronbuild Service <cronbuild@altlinux.org> 17.09-alt1
- repocop cronbuild 20170901. At your service.

* Sat Aug 05 2017 Cronbuild Service <cronbuild@altlinux.org> 17.08-alt1
- new version (17.08) with rpmgs script

* Sat Jul 08 2017 Cronbuild Service <cronbuild@altlinux.org> 17.07-alt1
- repocop cronbuild 20170708. At your service.

* Sat Jun 03 2017 Cronbuild Service <cronbuild@altlinux.org> 17.06-alt1
- new version (17.06) with rpmgs script

* Sat May 06 2017 Cronbuild Service <cronbuild@altlinux.org> 17.05-alt1
- new version (17.05) with rpmgs script

* Sat Apr 01 2017 Cronbuild Service <cronbuild@altlinux.org> 17.04-alt1
- repocop cronbuild 20170401. At your service.

* Sat Mar 04 2017 Cronbuild Service <cronbuild@altlinux.org> 17.03-alt1
- new version (17.03) with rpmgs script

* Fri Feb 17 2017 Anton Midyukov <antohami@altlinux.org> 17.02-alt1
- new version (17.02) with rpmgs script

* Thu Jan 05 2017 Anton Midyukov <antohami@altlinux.org> 17.01-alt1
- new version (17.01) with rpmgs script

* Wed Dec 07 2016 Anton Midyukov <antohami@altlinux.org> 16.12-alt1
- new version (16.12) with rpmgs script

* Thu Nov 10 2016 Anton Midyukov <antohami@altlinux.org> 16.11-alt1
- new version (16.11) with rpmgs script

* Sat Sep 17 2016 Anton Midyukov <antohami@altlinux.org> 16.09-alt1
- New version 16.09

* Sat Jul 02 2016 Anton Midyukov <antohami@altlinux.org> 16.07-alt1
- New version 16.07-alt1

* Sun Jun 12 2016 Anton Midyukov <antohami@altlinux.org> 16.06-alt1
- New version.

* Wed Mar 02 2016 Anton Midyukov <antohami@altlinux.org> 16.03-alt1
- New version.

* Fri Jan 08 2016 Anton Midyukov <antohami@altlinux.org> 16.01-alt1
- Initial build for ALT Linux Sisyphus

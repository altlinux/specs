Name: shotcut
Version: 17.12
Release: alt1
Summary: A free, open source, cross-platform video editor
Summary(ru_RU.UTF-8): Свободный кросс-платфоорменный видеоредактор
License: GPL-3.0+
Group: Video
Url: http://www.shotcut.org/
Packager: Anton Midyukov <antohami@altlinux.org>
# Source-url: https://github.com/mltframework/shotcut/archive/v%version.tar.gz
Source: %name-%version.tar
Source1: %name.desktop
BuildRequires: gcc-c++ qt5-base-devel >= 5.5.0 qt5-multimedia-devel qt5-quick1-devel qt5-webkit-devel qt5-websockets-devel qt5-x11extras-devel qt5-xmlpatterns-devel libmlt-devel libmlt++-devel qt5-tools ImageMagick-tools libX11-devel

Requires: %name-data = %version

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

%package data
Summary: Data files for %name
Group: Video
BuildArch: noarch

%description data
Data files for %name

%prep
%setup
for i in 16 32 48; do
    convert icons/%name-logo-64.png -resize "$i"x"$i" icons/%name-logo-$i.png
done


%build
%qmake_qt5
%make_build
lrelease-qt5 translations/*.ts

%install
install -Dp -m0755 src/%name %buildroot%_bindir/%name
install -d -m0755 %buildroot/%_datadir/%name
cp -a src/qml %buildroot%_datadir/%name/
install -d -m0755 %buildroot/%_datadir/%name/translations
cp -a translations/*.qm %buildroot/%_datadir/%name/translations/
install -Dp -m0644 %SOURCE1 %buildroot%_desktopdir/%name.desktop
for i in 16 32 48; do
    install -d -m755 %buildroot/%_iconsdir/hicolor/"$i"x"$i"/apps
    install -m644 icons/%name-logo-"$i".png %buildroot/%_iconsdir/hicolor/"$i"x"$i"/apps/%name.png
done
#make_install


%files
%_bindir/%name

%files data
%doc COPYING README.md
%_datadir/%name
%_desktopdir/%name.desktop
%_miconsdir/%name.png
%_niconsdir/%name.png
%_liconsdir/%name.png

%changelog
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

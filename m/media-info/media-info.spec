%define ver_major 26.10
%define rname MediaInfo
%define lname mediainfo

Name: media-info
Version: %ver_major
Release: alt10

Group: File tools
Summary: MediaInfo supplies information about a video or audio file
License: BSD-2-Clause
Url: https://github.com/MediaArea/MediaInfo
Vcs: https://github.com/MediaArea/MediaInfo.git

Source: %rname-%version.tar
Source1: %rname-translations-%version.tar

#{?_enable_kde5:BuildRequires(pre): rpm-build-kf5}
BuildRequires: gcc-c++
#BuildRequires: dos2unix
BuildRequires: zlib-devel
#BuildRequires: libpango-devel
BuildRequires: libzen-devel >= 0.4.41
BuildRequires: libmediainfo-devel >= %ver_major
BuildRequires: qt6-base-devel qt6-svg-devel qt6-tools
BuildRequires: sgml-common

%description
MediaInfo supplies technical and tag information about a video or audio file

What information can I get from MediaInfo?
General: title, author, director, album, track number, date, duration...
Video: codec, aspect, fps, bitrate...
Audio: codec, sample rate, channels, language, bitrate...
Text: language of subtitle
Chapters: number of chapters, list of chapters

What format (container) does MediaInfo support?
Video: MKV, OGM, AVI, DivX, WMV, QuickTime, Real, MPEG-1, MPEG-2,
       MPEG-4, DVD (VOB)...
(Codecs: DivX, XviD, MSMPEG4, ASP, H.264, AVC...)
Audio: OGG, MP3, WAV, RA, AC3, DTS, AAC, M4A, AU, AIFF...
Subtitles: SRT, SSA, ASS, SAMI...

This package includes the command line interface

%package gui
Group: File tools
Summary: MediaInfo supplies information about a video or audio file
Provides: mediainfo-gui = %EVR
Conflicts: mediainfo-gui
Provides: mediainfo-gui-KDE4 = %EVR
Obsoletes: mediainfo-gui-KDE4 < %EVR
Provides: mediainfo-gui-KDE5 = %EVR
Obsoletes: mediainfo-gui-KDE5 < %EVR
Provides: mediainfo-gui-KDE6 = %EVR
Obsoletes: mediainfo-gui-KDE6 < %EVR
%description gui
MediaInfo supplies technical and tag information about a video or audio file

What information can I get from MediaInfo?
General: title, author, director, album, track number, date, duration...
Video: codec, aspect, fps, bitrate...
Audio: codec, sample rate, channels, language, bitrate...
Text: language of subtitle
Chapters: number of chapters, list of chapters

What format (container) does MediaInfo support?
Video: MKV, OGM, AVI, DivX, WMV, QuickTime, Real, MPEG-1, MPEG-2,
       MPEG-4, DVD (VOB)...
(Codecs: DivX, XviD, MSMPEG4, ASP, H.264, AVC...)
Audio: OGG, MP3, WAV, RA, AC3, DTS, AAC, M4A, AU, AIFF...
Subtitles: SRT, SSA, ASS, SAMI...

This package contains the graphical user interface.

%prep
%setup -T -b 0 -a 1 -n %rname-%version
mkdir -p Source/Resource/Translations/
mv *-translations-*/*.ts Source/Resource/Translations/

%build
export PATH=%_qt6_libexecdir:%_qt6_bindir:$PATH
#pushd Project/GNU/CLI
#%autoreconf
#configure --disable-staticlibs --with-dll
#%make_build
#popd
lrelease Source/Resource/Translations/*.ts
pushd Project/QMake/GUI
%qmake_qt6 STATIC_LIBS=0
%make_build
popd

%install
#pushd Project/GNU/CLI
#%makeinstall_std
#popd
pushd Project/QMake/GUI
%makeinstall_std INSTALL_ROOT=%buildroot
popd

install -Dm 0644 Project/GNU/GUI/mediainfo-gui.desktop %buildroot/%_desktopdir/%lname-gui.desktop
install -Dm 0644 Project/GNU/GUI/mediainfo-gui.kde6.desktop %buildroot/%_datadir/kio/servicemenus/%lname-gui.desktop
install -Dm 0644 Project/GNU/GUI/mediainfo-gui.metainfo.xml %buildroot/%_datadir/metainfo/%lname-gui.metainfo.xml
install -Dm 0644 Source/Resource/Image/MediaInfo.svg %buildroot/%_iconsdir/hicolor/scalable/apps/%lname.svg

#%files
#%doc Release/ReadMe_CLI_Linux.txt
#%_bindir/%name

%files gui
%doc Release/ReadMe_GUI_Linux.txt
%_bindir/%lname-gui
%_desktopdir/%lname-gui.desktop
%_datadir/metainfo/%lname-gui.metainfo.xml
%_iconsdir/hicolor/*/apps/%lname.*
%_datadir/kio/servicemenus/%lname-gui.desktop

%changelog
* Tue Nov 03 2026 Sergey V Turchin <zerg@altlinux.org> 26.10-alt10
- build Qt GUI

* Tue Oct 06 2026 Yuri N. Sedunov <aris@altlinux.org> 26.10-alt1
- 26.10

* Tue May 12 2026 Yuri N. Sedunov <aris@altlinux.org> 26.05-alt1
- 26.05

* Tue Feb 03 2026 Yuri N. Sedunov <aris@altlinux.org> 26.01-alt1
- 26.01

* Thu Nov 06 2025 Yuri N. Sedunov <aris@altlinux.org> 25.10-alt1
- 25.10

* Wed Oct 01 2025 Yuri N. Sedunov <aris@altlinux.org> 25.09-alt1
- 25.09

* Tue Jul 29 2025 Yuri N. Sedunov <aris@altlinux.org> 25.07-alt1
- 25.07

* Thu May 01 2025 Yuri N. Sedunov <aris@altlinux.org> 25.04-alt1
- 25.04

* Sat Mar 22 2025 Yuri N. Sedunov <aris@altlinux.org> 25.03-alt1
- 25.03

* Tue Dec 10 2024 Yuri N. Sedunov <aris@altlinux.org> 24.12-alt1
- 24.12

* Sat Nov 09 2024 Yuri N. Sedunov <aris@altlinux.org> 24.11.1-alt1
- 24.11.1

* Fri Nov 08 2024 Yuri N. Sedunov <aris@altlinux.org> 24.11-alt1
- 24.11

* Sat Jun 29 2024 Yuri N. Sedunov <aris@altlinux.org> 24.06-alt1
- 24.06

* Fri May 31 2024 Yuri N. Sedunov <aris@altlinux.org> 24.05-alt1
- 24.05

* Thu Apr 18 2024 Yuri N. Sedunov <aris@altlinux.org> 24.04-alt1
- 24.04

* Fri Mar 29 2024 Yuri N. Sedunov <aris@altlinux.org> 24.03-alt1
- 24.03

* Thu Feb 01 2024 Yuri N. Sedunov <aris@altlinux.org> 24.01.1-alt1
- 24.01.1

* Thu Nov 30 2023 Yuri N. Sedunov <aris@altlinux.org> 23.11-alt1
- 23.11

* Wed Oct 04 2023 Yuri N. Sedunov <aris@altlinux.org> 23.10-alt1
- 23.10

* Thu Sep 14 2023 Yuri N. Sedunov <aris@altlinux.org> 23.09-alt1
- 23.09

* Thu Jul 13 2023 Yuri N. Sedunov <aris@altlinux.org> 23.07-alt1
- 23.07

* Wed Jun 28 2023 Yuri N. Sedunov <aris@altlinux.org> 23.06-alt1
- 23.06

* Thu Apr 27 2023 Yuri N. Sedunov <aris@altlinux.org> 23.04-alt1
- 23.04

* Wed Mar 29 2023 Yuri N. Sedunov <aris@altlinux.org> 23.03-alt1
- 23.03

* Fri Dec 23 2022 Yuri N. Sedunov <aris@altlinux.org> 22.12-alt1
- 22.12

* Wed Oct 05 2022 Yuri N. Sedunov <aris@altlinux.org> 22.09-alt1
- 22.09

* Fri Jun 24 2022 Yuri N. Sedunov <aris@altlinux.org> 22.06-alt1
- 22.06

* Thu Mar 31 2022 Yuri N. Sedunov <aris@altlinux.org> 22.03-alt1
- 22.03

* Sat Sep 25 2021 Yuri N. Sedunov <aris@altlinux.org> 21.09-alt1.1
- rebuilt with wxGTK3.0

* Sat Sep 18 2021 Yuri N. Sedunov <aris@altlinux.org> 21.09-alt1
- 21.09

* Sat Mar 27 2021 Yuri N. Sedunov <aris@altlinux.org> 21.03-alt1
- 21.03

* Mon Oct 26 2020 Yuri N. Sedunov <aris@altlinux.org> 20.09-alt1
- 20.09

* Thu Aug 20 2020 Yuri N. Sedunov <aris@altlinux.org> 20.08-alt1
- 20.08

* Fri Apr 03 2020 Yuri N. Sedunov <aris@altlinux.org> 20.03-alt1
- 20.03
- fixed License tag

* Thu Sep 12 2019 Yuri N. Sedunov <aris@altlinux.org> 19.09-alt1
- 19.09

* Wed Jul 17 2019 Yuri N. Sedunov <aris@altlinux.org> 19.07-alt1
- 19.07

* Thu Apr 25 2019 Yuri N. Sedunov <aris@altlinux.org> 19.04-alt1.1
- enabled SMP build
- disabled gui-KDE4 subpackage by default

* Wed Apr 24 2019 Yuri N. Sedunov <aris@altlinux.org> 19.04-alt1
- 19.04

* Sun Dec 23 2018 Yuri N. Sedunov <aris@altlinux.org> 18.12-alt1
- 18.12

* Sat Sep 15 2018 Yuri N. Sedunov <aris@altlinux.org> 18.08.1-alt1
- 18.08.1

* Sun Sep 02 2018 Yuri N. Sedunov <aris@altlinux.org> 18.08-alt1
- 18.08

* Fri May 11 2018 Yuri N. Sedunov <aris@altlinux.org> 18.05-alt1
- 18.05

* Tue Mar 27 2018 Yuri N. Sedunov <aris@altlinux.org> 18.03.1-alt1
- 18.03.1

* Tue Mar 20 2018 Yuri N. Sedunov <aris@altlinux.org> 18.03-alt1
- 18.03

* Thu Dec 28 2017 Yuri N. Sedunov <aris@altlinux.org> 17.12-alt1
- 17.12
- new gui-KDE5 subpackage

* Sat Nov 04 2017 Yuri N. Sedunov <aris@altlinux.org> 17.10-alt1
- 17.10

* Wed Sep 20 2017 Yuri N. Sedunov <aris@altlinux.org> 0.7.99-alt2
- removed obsolete gui-KDE3 subpackage

* Mon Sep 18 2017 Yuri N. Sedunov <aris@altlinux.org> 0.7.99-alt1
- 0.7.99

* Fri Sep 01 2017 Yuri N. Sedunov <aris@altlinux.org> 0.7.98-alt2
- fixed dependencies (ALT #33839)

* Tue Aug 22 2017 Yuri N. Sedunov <aris@altlinux.org> 0.7.98-alt1
- 0.7.98

* Sat Jul 08 2017 Yuri N. Sedunov <aris@altlinux.org> 0.7.97-alt1
- 0.7.97

* Sun Jun 04 2017 Yuri N. Sedunov <aris@altlinux.org> 0.7.96-alt1
- 0.7.96

* Sun May 07 2017 Yuri N. Sedunov <aris@altlinux.org> 0.7.95-alt1
- 0.7.95

* Tue Apr 04 2017 Yuri N. Sedunov <aris@altlinux.org> 0.7.94-alt1
- 0.7.94

* Tue Aug 25 2015 Motsyo Gennadi <drool@altlinux.ru> 0.7.76-alt1
- 0.7.76

* Wed Oct 01 2014 Motsyo Gennadi <drool@altlinux.ru> 0.7.70-alt1
- 0.7.70

* Sat Feb 18 2012 Sergei Epiphanov <serpiph@altlinux.ru> 0.7.53-alt1
- New version

* Sun Dec 04 2011 Sergei Epiphanov <serpiph@altlinux.ru> 0.7.51-alt2
- Fix build spec

* Sun Dec 04 2011 Sergei Epiphanov <serpiph@altlinux.ru> 0.7.51-alt1
- New version

* Thu Jul 21 2011 Sergei Epiphanov <serpiph@altlinux.ru> 0.7.47-alt1
- New version

* Mon Mar 07 2011 Sergei Epiphanov <serpiph@altlinux.ru> 0.7.42-alt2
- Update spec with noarch and K3/K4 macros

* Sun Mar 06 2011 Sergei Epiphanov <serpiph@altlinux.ru> 0.7.42-alt1
- New version

* Mon Feb 28 2011 Sergei Epiphanov <serpiph@altlinux.ru> 0.7.41-alt1
- New version

* Mon Oct 18 2010 Sergei Epiphanov <serpiph@altlinux.ru> 0.7.35-alt1
- New version

* Tue Mar 02 2010 Sergei Epiphanov <serpiph@altlinux.ru> 0.7.28-alt1
- New version

* Wed Feb 17 2010 Sergei Epiphanov <serpiph@altlinux.ru> 0.7.27-alt2
- Rebuild with libwxGTK
- Fix .destop files due to repocop info

* Wed Feb 10 2010 Sergei Epiphanov <serpiph@altlinux.ru> 0.7.27-alt1
- New version

* Mon Nov 23 2009 Sergei Epiphanov <serpiph@altlinux.ru> 0.7.25-alt1
- New version
- create KDE3 and KDE4 subpackages from mediainfo-gui

* Thu Nov 12 2009 Sergei Epiphanov <serpiph@altlinux.ru> 0.7.24-alt1
- initial build

Name: mediainfo
Version: 0.7.53
Release: alt1

Group: File tools
Summary: MediaInfo supplies information about a video or audio file
License: LGPL
Url: http://mediainfo.sourceforge.net
Packager: Sergei Epiphanov <serpiph@altlinux.ru>

Source0: %{name}_%{version}.tar.bz2
BuildRequires(pre): rpm-macros-kde-common-devel

BuildRequires: gcc-c++ automake autoconf libtool
BuildRequires: dos2unix
BuildRequires: pkg-config
BuildRequires: zlib-devel
BuildRequires: libpango-devel
BuildRequires: libzen-devel >= 0.4.24
BuildRequires: libmediainfo-devel >= 0.7.53
BuildRequires: libwxGTK-devel
BuildRequires: sgml-common

%package gui
Group: File tools
Summary: MediaInfo supplies information about a video or audio file

%package gui-KDE3
Group: File tools
Summary: KDE3 related MediaInfo files
BuildArch: noarch
Requires: %name-gui
Requires: kdebase-konqueror < 4.0

%package gui-KDE4
Group: File tools
Summary: KDE4 related MediaInfo files
BuildArch: noarch
Requires: %name-gui
Requires: kde4libs

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

To combine with KDE install KDE-related package

%description gui-KDE3
This package contains KDE3 related MediaInfo files for konqueror

%description gui-KDE4
This package contains KDE4 related MediaInfo files for konqueror

%prep
%setup -q -T -b 0 -n MediaInfo

%build
#dos2unix      *.txt Source/Doc/*.txt
#chmod 644    *.txt Source/Doc/*.txt
pushd Project/GNU/CLI
%autoreconf
%configure
%make
popd
#cp Source/Doc/*.txt ./
pushd Project/GNU/GUI
%autoreconf
%configure
%make
popd

%install
pushd Project/GNU/CLI
%makeinstall
popd
pushd Project/GNU/GUI
%makeinstall
popd
# Add here commands to install the package
cp Release/ReadMe_CLI_Linux.txt .
cp Release/ReadMe_GUI_Linux.txt .

install -dm 755 %buildroot%_pixmapsdir
install -m 644 Source/Resource/Image/MediaInfo.png %buildroot%_pixmapsdir/mediainfo.png
install -dm 755 %buildroot%_liconsdir
install -m 644 Source/Resource/Image/MediaInfo.png %buildroot%_liconsdir/mediainfo.png

install -dm 755 %buildroot%_desktopdir
grep -v '^Encoding=' Project/GNU/GUI/mediainfo-gui.desktop >%buildroot%_desktopdir/mediainfo-gui.desktop
#install -m 644 Project/GNU/GUI/mediainfo-gui.desktop %%buildroot%%_desktopdir
install -dm 755 %buildroot%_K3apps/konqueror/servicemenus/
grep -v '^Encoding=' Project/GNU/GUI/mediainfo-gui.kde3.desktop >%buildroot%_K3apps/konqueror/servicemenus/mediainfo-gui.desktop
#install -m 644 Project/GNU/GUI/mediainfo-gui.kde3.desktop %%buildroot%%_datadir/apps/konqueror/servicemenus/mediainfo-gui.desktop
install -dm 755 %buildroot%_K4srv/ServiceMenus/
grep -v '^Encoding=' Project/GNU/GUI/mediainfo-gui.kde4.desktop >%buildroot%_K4srv/ServiceMenus/mediainfo-gui.desktop
#install -m 644 Project/GNU/GUI/mediainfo-gui.kde4.desktop %%buildroot%%_datadir/kde4/services/ServiceMenus/mediainfo-gui.desktop

%files
%doc ReadMe_CLI_Linux.txt
%_bindir/mediainfo

%files gui
%doc ReadMe_GUI_Linux.txt
%_bindir/mediainfo-gui
%_desktopdir/mediainfo-gui.desktop
%_pixmapsdir/mediainfo.png
%_liconsdir/mediainfo.png

%files gui-KDE3
%_K3apps/konqueror/servicemenus/mediainfo-gui.desktop

%files gui-KDE4
%_K4srv/ServiceMenus/mediainfo-gui.desktop

%changelog
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

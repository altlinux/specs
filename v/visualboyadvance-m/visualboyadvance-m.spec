Name: visualboyadvance-m
Version: 2.0.1
Release: alt1

Summary: Game Boy Advance Emulator
License: GPLv2
Group: Emulators
Url: http://vba-m.com

Packager: Alexey Appolonov <alexey@altlinux.org>

# https://github.com/visualboyadvance-m/visualboyadvance-m.git v%version
Source: %name-%version.tar

Patch1: %name-2.0.1-alt-segmentation-fault-fix.patch

BuildRequires(pre): rpm-macros-cmake
BuildRequires: make
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: zlib-devel
BuildRequires: libGL-devel
BuildRequires: gettext
BuildRequires: gettext-tools
BuildRequires: libpng-devel
BuildRequires: libSDL2-devel
BuildRequires: libSFML-devel
BuildRequires: libopenal-devel
BuildRequires: libwxGTK3.0-devel
BuildRequires: libgtk+3-devel
# Optional, for 32 bit builds:
BuildRequires: nasm
# ffmpeg:
BuildRequires: libavcodec-devel libavformat-devel libswscale-devel libavutil-devel
# Not stated on developers site:
BuildRequires: zip

%description
VisualBoyAdvance-M, or simply VBA-M, is an improved fork from the inactive
VisualBoyAdvance project, adding several features as well as maintaining
an up-to-date codebase.

%prep
%setup
%patch1 -p1

%build
#mkdir build
%cmake \
	-DENABLE_LTO=OFF \
	-DENABLE_DIRECT3D=OFF
export NPROCS=1
%cmake_build

%install
%cmakeinstall_std

%files
%_bindir/%name
%_datadir/appdata/wxvbam.appdata.xml
%_datadir/applications/wxvbam.desktop
%_datadir/icons/hicolor/128x128/apps/vbam.png
%_datadir/icons/hicolor/16x16/apps/vbam.png
%_datadir/icons/hicolor/22x22/apps/vbam.png
%_datadir/icons/hicolor/24x24/apps/vbam.png
%_datadir/icons/hicolor/256x256/apps/vbam.png
%_datadir/icons/hicolor/32x32/apps/vbam.png
%_datadir/icons/hicolor/48x48/apps/vbam.png
%_datadir/icons/hicolor/64x64/apps/vbam.png
%_datadir/icons/hicolor/96x96/apps/vbam.png
%_datadir/icons/hicolor/scalable/apps/vbam.svg
%_datadir/locale/cs/LC_MESSAGES/wxvbam.mo
%_datadir/locale/de/LC_MESSAGES/wxvbam.mo
%_datadir/locale/en/LC_MESSAGES/wxvbam.mo
%_datadir/locale/es/LC_MESSAGES/wxvbam.mo
%_datadir/locale/fr/LC_MESSAGES/wxvbam.mo
%_datadir/locale/gl/LC_MESSAGES/wxvbam.mo
%_datadir/locale/ko/LC_MESSAGES/wxvbam.mo
%_datadir/locale/nb/LC_MESSAGES/wxvbam.mo
%_datadir/locale/nl/LC_MESSAGES/wxvbam.mo
%_datadir/locale/pt_BR/LC_MESSAGES/wxvbam.mo
%_datadir/locale/ru/LC_MESSAGES/wxvbam.mo
%_datadir/locale/tr/LC_MESSAGES/wxvbam.mo
%_datadir/locale/zh_TW/LC_MESSAGES/wxvbam.mo
%_mandir/man6/visualboyadvance-m.6.xz
%_datadir/vbam/vba-over.ini

%changelog
* Mon Oct 30 2017 Alexey Appolonov <alexey@altlinux.org> 2.0.1-alt1
- First ALT Linux release.
- Segmentation fault fixed in wxvbamApp::~wxvbamApp().
- Possible memory leak fixed in bin2c.c main function.
- (Closes: 31216).

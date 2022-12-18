%global shortname vbam

Name: visualboyadvance-m
Version: 2.1.5
Release: alt3

Summary: Game Boy Advance Emulator
License: GPLv2
Group: Emulators
Url: http://vba-m.com

Packager: Ilya Mashkin <oddity@altlinux.ru>

# https://github.com/visualboyadvance-m/visualboyadvance-m.git v%version
Source: %name-%version.tar
Source2: vba-translations.zip
Patch1: %name-2.0.1-alt-segmentation-fault-fix.patch


#Upstream patch:
#https://github.com/visualboyadvance-m/visualboyadvance-m/commit/af0de1c4b308ef8d9a081ecf407805b75a99d877
Patch2:         0001-xbrz-fix-inline-asm-check.patch
#https://github.com/visualboyadvance-m/visualboyadvance-m/commit/410ede543c98c8c6dd89c25484da3bffb46f4187
Patch3:         0001-Check-for-null-pointer-in-soundReset.patch
#https://github.com/visualboyadvance-m/visualboyadvance-m/commit/619a5cce683ec4b1d03f08f316ba276d8f8cd824
Patch4:         0001-SDL-Fix-build-with-SDL-2.0.14-after-KMOD_GUI-change-.patch


BuildRequires(pre): rpm-macros-cmake
BuildRequires: make
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: zlib-devel
BuildRequires: libGL-devel libGLU-devel 
BuildRequires: gettext
BuildRequires: gettext-tools
BuildRequires: libpng-devel
BuildRequires: libSDL2-devel
BuildRequires: libSFML-devel
BuildRequires: libopenal-devel
BuildRequires: libwxGTK3.2-devel libgomp-devel libwxGTK3.2 libwxGTK3.2-gl 
BuildRequires: libgtk+3-devel
# Optional, for 32 bit builds:
BuildRequires: nasm
# ffmpeg:
BuildRequires: libavcodec-devel libavformat-devel libswscale-devel libavutil-devel libswresample-devel bzlib-devel libpcre-devel libbrotli-devel libuuid-devel libexpat-devel 
# Not stated on developers site:
BuildRequires: zip bzip2

ExcludeArch: armh i586

%description
VisualBoyAdvance-M, or simply VBA-M, is an improved fork from the inactive
VisualBoyAdvance project, adding several features as well as maintaining
an up-to-date codebase.

%prep
%setup
#patch1 -p1
#patch2 -p1
#patch3 -p1
#patch4 -p1
sed -i 's/ -mtune=generic//g' CMakeLists.txt
#Some odd permission issues:
chmod -x src/wx/rpi.h

#set_gcc_version 8

%build
#mkdir build
#%cmake \
#	-DENABLE_LTO=OFF \
#	-DENABLE_DIRECT3D=OFF

%cmake \
    -DENABLE_LTO=OFF \
    -DENABLE_DIRECT3D=OFF \
    -DCMAKE_SKIP_RPATH=ON \
    -DVERSION_RELEASE=TRUE \
    -DENABLE_SDL=ON \
    -DENABLE_WX=ON \
    -DENABLE_FFMPEG=OFF \
    -DENABLE_LINK=ON

export NPROCS=1
%cmake_build

%install
%cmakeinstall_std
%find_lang wx%{shortname}

%files -f wx%{shortname}.lang
%_bindir/%name
%_datadir/appdata/%name.appdata.xml
%_datadir/applications/%name.desktop
%_datadir/icons/hicolor/128x128/apps/%name.png
%_datadir/icons/hicolor/16x16/apps/%name.png
%_datadir/icons/hicolor/22x22/apps/%name.png
%_datadir/icons/hicolor/24x24/apps/%name.png
%_datadir/icons/hicolor/256x256/apps/%name.png
%_datadir/icons/hicolor/32x32/apps/%name.png
%_datadir/icons/hicolor/48x48/apps/%name.png
%_datadir/icons/hicolor/64x64/apps/%name.png
%_datadir/icons/hicolor/96x96/apps/%name.png
%_datadir/icons/hicolor/scalable/apps/%name.svg
%_datadir/locale/cs/LC_MESSAGES/wxvbam.mo
%_datadir/locale/de/LC_MESSAGES/wxvbam.mo
#_datadir/locale/en/LC_MESSAGES/wxvbam.mo
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
%config(noreplace) %{_sysconfdir}/%{shortname}.cfg
%{_mandir}/man6/%{shortname}.*
%{_bindir}/%{shortname}


%changelog
* Sun Dec 18 2022 Ilya Mashkin <oddity@altlinux.ru> 2.1.5-alt3
- ExcludeArch: armh i586

* Sun Dec 18 2022 Ilya Mashkin <oddity@altlinux.ru> 2.1.5-alt2
- add translations

* Sun Dec 18 2022 Ilya Mashkin <oddity@altlinux.ru> 2.1.5-alt1
- 2.1.5

* Sun Oct 10 2021 Igor Vlasenko <viy@altlinux.org> 2.1.4-alt2
- NMU: excluded armh build for 2.1.4-alt2 only,
  as it consistently segfaults and prevents wxGTK3.0 rebuild

* Tue Feb 16 2021 Ilya Mashkin <oddity@altlinux.ru> 2.1.4-alt1
- 2.1.4
- Merge with deprecated VisualBoyAdvance
- Lang files added
- New BR: added

* Sun Feb 24 2019 Nazarov Denis <nenderus@altlinux.org> 2.1.0-alt2
- Rebuilt with new SFML

* Mon Oct 08 2018 Anton Farygin <rider@altlinux.ru> 2.1.0-alt1
- 2.1.0

* Mon Oct 30 2017 Alexey Appolonov <alexey@altlinux.org> 2.0.1-alt1
- First ALT Linux release.
- Segmentation fault fixed in wxvbamApp::~wxvbamApp().
- Possible memory leak fixed in bin2c.c main function.
- (Closes: 31216).

* Tue Aug 17 2010 Ilya Mashkin <oddity@altlinux.ru> 1.7.2-alt3.2
- fix build

* Tue May 27 2008 Ilya Mashkin <oddity at altlinux dot ru> 1.7.2-alt3.1
- spec cleanup

* Wed May 02 2007 Ilya Mashkin <oddity@altlinux.ru> 1.7.2-alt3
- rebuild 

* Tue Jun 15 2004 Ilya Mashkin <oddity@altlinux.ru> 1.7.2-alt2
- update spec for 1.7.2

* Sun Jun 05 2004 Ilya Mashkin <oddity@altlinux.ru> 1.7.2-alt1
- Update version to 1.7.2. Many fixes.

* Sun Feb 22 2004 Ilya Mashkin <oddity@altlinux.ru> 1.7.1-alt1
- Update version to 1.7.1. Many changes.

* Tue Nov 18 2003 Ilya Mashkin <oddity@altlinux.ru> 1.6a-alt0.1
- Initial build 

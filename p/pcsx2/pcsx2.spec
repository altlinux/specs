%define optflags_lto %nil

# git show -s --format=%ci upstream/pcsx2 | sed 's/[ :-]//g' | sed 's/\(.\{,14\}\).*/\1/'
%define svn_rev 20211210110636

%define libchdr_commit 5de1a59019815ccdbba0fe07c71b31406d023248
%define gtest_version 1.11.0

Name: pcsx2
Version: 1.7.2116
Release: alt1

Summary: Playstation 2 console emulator
License: GPLv3 and LGPLv3
Group: Emulators

Url: http://%name.net/
Packager: Nazarov Denis <nenderus@altlinux.org>

ExclusiveArch: %ix86 x86_64

BuildRequires(pre): at-spi2-atk-devel
BuildRequires(pre): bzlib-devel
BuildRequires(pre): expat-devel
BuildRequires(pre): libat-spi2-core-devel
BuildRequires(pre): libblkid-devel
BuildRequires(pre): libbrotli-devel
BuildRequires(pre): libdatrie-devel
BuildRequires(pre): libdbus-devel
BuildRequires(pre): libepoxy-devel
BuildRequires(pre): libffi-devel
BuildRequires(pre): libfribidi-devel
BuildRequires(pre): libmount-devel
BuildRequires(pre): libpcre-devel
BuildRequires(pre): libpixman-devel
BuildRequires(pre): libselinux-devel
BuildRequires(pre): libthai-devel
BuildRequires(pre): libtiff-devel
BuildRequires(pre): libuuid-devel
BuildRequires(pre): libwayland-cursor-devel
BuildRequires(pre): libwayland-egl-devel
BuildRequires(pre): wayland-protocols

# https://github.com/PCSX2/%name/archive/v%version/%name-%version.tar.gz
Source0: %name-%version.tar
# https://github.com/rtissera/libchdr/archive/%libchdr_commit/libchdr-%libchdr_commit.tar.gz
Source1: libchdr-%libchdr_commit.tar
# https://github.com/google/googletest/archive/release-%gtest_version/googletest-release-%gtest_version.tar.gz
Source2: googletest-release-%gtest_version.tar

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: libGLU-devel
BuildRequires: libSDL2-devel
BuildRequires: libXcomposite-devel
BuildRequires: libXcursor-devel
BuildRequires: libXdamage-devel
BuildRequires: libXdmcp-devel
BuildRequires: libXinerama-devel
BuildRequires: libXmu-devel
BuildRequires: libXrandr-devel
BuildRequires: libXtst-devel
BuildRequires: libaio-devel
BuildRequires: libfmt-devel
BuildRequires: libgtk+3-devel
BuildRequires: liblzma-devel
BuildRequires: libpcap-devel
BuildRequires: libportaudio2-devel
BuildRequires: libpulseaudio-devel
BuildRequires: libsamplerate-devel
BuildRequires: libsoundtouch-devel
BuildRequires: libudev-devel
BuildRequires: libwxGTK3.1-devel
BuildRequires: libxkbcommon-devel
BuildRequires: libxml2-devel
BuildRequires: libyaml-cpp-devel
BuildRequires: ninja-build

%description
PCSX2 is an emulator for the playstation 2 video game console. It is written mostly in C++, some part are in C and x86 assembly.
There is still lot of on going work to improve compatibility & speed.

%prep
%setup -b 1 -b 2

%__mv -Tf ../libchdr-%libchdr_commit 3rdparty/libchdr/libchdr
%__mv -Tf ../googletest-release-%gtest_version 3rdparty/gtest

%build
%cmake .. \
	-DCMAKE_DISABLE_PRECOMPILE_HEADERS:BOOL=TRUE \
	-DCMAKE_BUILD_PO:BOOL=TRUE \
	-DDISABLE_ADVANCE_SIMD:BOOL=TRUE \
	-DPACKAGE_MODE:BOOL=TRUE \
	-DXDG_STD:BOOL=TRUE \
	-DDISABLE_BUILD_DATE:BOOL=TRUE \
	-DUSE_SYSTEM_YAML:BOOL=TRUE \
	-DLTO_PCSX2_CORE:BOOL=TRUE \
	-GNinja

echo "#define SVN_REV $(echo %svn_rev)ll 
#define GIT_TAG \"v$(echo %version)\"
#define GIT_TAGGED_COMMIT 1
#define GIT_REV \"\"" > %_cmake__builddir/common/include/svnrev.h

%cmake_build

%install
%cmake_install
%find_lang --output=%name.lang %{name}_{Iconized,Main}

%files -f %name.lang
%_bindir/PCSX2*
%_desktopdir/PCSX2.desktop
%_man1dir/PCSX2.1.*
%dir %_datadir/PCSX2
%_datadir/PCSX2/GameIndex.yaml
%_datadir/PCSX2/cheats_ws.zip
%_pixmapsdir/PCSX2.xpm
%dir %_defaultdocdir/Pcsx2
%_defaultdocdir/Pcsx2/*.pdf

%changelog
* Fri Dec 10 2021 Nazarov Denis <nenderus@altlinux.org> 1.7.2116-alt1
- Version 1.7.2116

* Sat Nov 06 2021 Nazarov Denis <nenderus@altlinux.org> 1.7.2019-alt1
- Version 1.7.2019

* Fri Nov 05 2021 Nazarov Denis <nenderus@altlinux.org> 1.7.2016-alt1
- Version 1.7.2016

* Thu Nov 04 2021 Nazarov Denis <nenderus@altlinux.org> 1.7.2012-alt1
- Version 1.7.2012

* Wed Nov 03 2021 Nazarov Denis <nenderus@altlinux.org> 1.7.2006-alt1
- Version 1.7.2006

* Tue Nov 02 2021 Nazarov Denis <nenderus@altlinux.org> 1.7.2003-alt1
- Version 1.7.2003

* Sun Oct 11 2020 Anton Midyukov <antohami@altlinux.org> 1.6.0-alt6
- Rebuild with libwxGTK3.0

* Mon Jun 01 2020 Nazarov Denis <nenderus@altlinux.org> 1.6.0-alt5
- Use directory /usr/share/doc/PCSX2 for Configuration Guide and Readme / FAQ

* Sun May 24 2020 Nazarov Denis <nenderus@altlinux.org> 1.6.0-alt4
- Build GSdx plugin additionaly without AVX2 & SSE4 support
- Build GSdx legacy plugin
- Disable build date

* Sat May 23 2020 Nazarov Denis <nenderus@altlinux.org> 1.6.0-alt3
- Move localization files to separate subpackage
- Add requires to all plugin types

* Sat May 23 2020 Nazarov Denis <nenderus@altlinux.org> 1.6.0-alt2
- Add build pre requires
- Return XDG_STD option

* Fri May 08 2020 Nazarov Denis <nenderus@altlinux.org> 1.6.0-alt1
- Version 1.6.0

* Mon Jul 23 2018 Nazarov Denis <nenderus@altlinux.org> 1.4.0-alt2%ubt
- Rebuilt with new GLEW

* Sat Feb 20 2016 Yuri N. Sedunov <aris@altlinux.org> 1.4.0-alt1.1
- rebuilt against libSoundTouch.so.1

* Mon Jan 11 2016 Nazarov Denis <nenderus@altlinux.org> 1.4.0-alt1
- Version 1.4.0

* Tue Nov 18 2014 Nazarov Denis <nenderus@altlinux.org> 1.2.2-alt2
- Rebuild with libsoundtouch 1.8.0

* Sun Feb 16 2014 Nazarov Denis <nenderus@altlinux.org> 1.2.2-alt0.M70T.1
- Build for branch t7

* Sun Feb 16 2014 Nazarov Denis <nenderus@altlinux.org> 1.2.2-alt1
- Version 1.2.2

* Tue Feb 11 2014 Nazarov Denis <nenderus@altlinux.org> 1.2.1-alt1.M70P.1
- Build for branch p7

* Mon Feb 10 2014 Nazarov Denis <nenderus@altlinux.org> 1.2.1-alt1.M70T.1
- Build for branch t7

* Sun Feb 09 2014 Nazarov Denis <nenderus@altlinux.org> 1.2.1-alt2
- Fix language files for x64

* Sat Feb 08 2014 Nazarov Denis <nenderus@altlinux.org> 1.2.1-alt0.M70T.1
- Build for branch t7

* Fri Feb 07 2014 Nazarov Denis <nenderus@altlinux.org> 1.2.1-alt1
- Version 1.2.1

* Tue Feb 04 2014 Nazarov Denis <nenderus@altlinux.org> 1.2.0-alt1
- Version 1.2.0

* Thu Oct 17 2013 Nazarov Denis <nenderus@altlinux.org> 1.0.0-alt1.M70T.1
- Build for branch t7

* Sat Sep 28 2013 Nazarov Denis <nenderus@altlinux.org> 1.0.0-alt2
- Fix post-install unowned files
- Rebuild the ps2hw.dat file

* Fri Sep 27 2013 Nazarov Denis <nenderus@altlinux.org> 1.0.0-alt1
- Initial build for ALT Linux

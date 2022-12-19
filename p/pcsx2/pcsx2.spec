%define optflags_lto %nil

# git show -s --format=%ci upstream/pcsx2 | sed 's/[ :-]//g' | sed 's/\(.\{,14\}\).*/\1/'
%define svn_rev 20220924172107

%define libchdr_commit 5de1a59019815ccdbba0fe07c71b31406d023248
%define gtest_version 1.11.0
%define libzip_commit bdc03ab23b703fcc516436d6ebcbfb6ac4484033
%define zstd_version 1.5.2
%define vulkan_headers_version 1.3.226
%define cubeb_commit dc511c6b3597b6384d28949285b9289e009830ea
%define glslang_version 11.7.1

Name: pcsx2
Version: 1.7.3332
Release: alt1.1

Summary: Playstation 2 console emulator
License: GPLv3 and LGPLv3
Group: Emulators

Url: http://%name.net/
Packager: Nazarov Denis <nenderus@altlinux.org>

ExclusiveArch: x86_64

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
BuildRequires(pre): libjpeg-devel
BuildRequires(pre): libmount-devel
BuildRequires(pre): libpcre2-devel
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
# https://github.com/nih-at/libzip/archive/%libzip_commit/libzip-%libzip_commit.tar.gz
Source3: libzip-%libzip_commit.tar
# https://github.com/facebook/zstd/archive/v%zstd_version/zstd-%zstd_version.tar.gz
Source4: zstd-%zstd_version.tar
# https://github.com/KhronosGroup/Vulkan-Headers/archive/v%vulkan_headers_version/Vulkan-Headers-%vulkan_headers_version.tar.gz
Source5: Vulkan-Headers-%vulkan_headers_version.tar
# https://github.com/mozilla/cubeb/archive/%cubeb_commit/cubeb-%cubeb_commit.tar.gz
Source6: cubeb-%cubeb_commit.tar
# https://github.com/KhronosGroup/glslang/archive/%glslang_version/glslang-%glslang_version.tar.gz
Source7: glslang-%glslang_version.tar

BuildRequires: cmake
BuildRequires: doxygen
BuildRequires: gcc-c++
BuildRequires: graphviz
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
BuildRequires: libalsa-devel
BuildRequires: libfmt-devel
BuildRequires: libgtk+3-devel
BuildRequires: liblzma-devel
BuildRequires: libpcap-devel
BuildRequires: libpulseaudio-devel
BuildRequires: libryml-devel
BuildRequires: libsamplerate-devel
BuildRequires: libsoundtouch-devel
BuildRequires: libssl-devel
BuildRequires: libudev-devel
BuildRequires: libwxBase3.2-devel
BuildRequires: libxkbcommon-devel
BuildRequires: libzip-devel
BuildRequires: libzip-utils
BuildRequires: ninja-build

%description
PCSX2 is an emulator for the playstation 2 video game console. It is written mostly in C++, some part are in C and x86 assembly.
There is still lot of on going work to improve compatibility & speed.

%prep
%setup -b 1 -b 2 -b 3 -b 4 -b 5 -b 6 -b 7

%__mv -Tf ../libchdr-%libchdr_commit 3rdparty/libchdr/libchdr
%__mv -Tf ../googletest-release-%gtest_version 3rdparty/gtest
%__mv -Tf ../libzip-%libzip_commit 3rdparty/libzip/libzip
%__mv -Tf ../zstd-%zstd_version 3rdparty/zstd/zstd
%__mv -Tf ../Vulkan-Headers-%vulkan_headers_version 3rdparty/vulkan-headers
%__mv -Tf ../cubeb-%cubeb_commit 3rdparty/cubeb/cubeb
%__mv -Tf ../glslang-%glslang_version 3rdparty/glslang/glslang

%build
%cmake .. \
	-DCMAKE_BUILD_TYPE:STRING="RelWithDebInfo" \
	-DCMAKE_DISABLE_PRECOMPILE_HEADERS:BOOL=TRUE \
	-DCMAKE_BUILD_PO:BOOL=TRUE \
	-DDISABLE_ADVANCE_SIMD:BOOL=TRUE \
	-DDISABLE_BUILD_DATE:BOOL=TRUE \
	-DDISABLE_PCSX2_WRAPPER:BOOL=TRUE \
	-DPACKAGE_MODE:BOOL=TRUE \
	-DXDG_STD:BOOL=TRUE \
	-DLTO_PCSX2_CORE:BOOL=TRUE \
	-DSDL2_API:BOOL=TRUE \
	-GNinja \
	-Wno-dev

echo "#define SVN_REV $(echo %svn_rev)ll 
#define GIT_TAG \"v$(echo %version)\"
#define GIT_TAGGED_COMMIT 1
#define GIT_REV \"\"" > %_cmake__builddir/common/include/svnrev.h

%cmake_build

%install
%cmake_install

%files
%_bindir/%name
%_desktopdir/PCSX2.desktop
%_man1dir/PCSX2.1.*
%_datadir/PCSX2
%_pixmapsdir/PCSX2.xpm
%dir %_defaultdocdir/Pcsx2
%_defaultdocdir/Pcsx2/*.pdf

%changelog
* Mon Dec 19 2022 Nazarov Denis <nenderus@altlinux.org> 1.7.3332-alt1.1
- Fix build

* Sat Sep 24 2022 Nazarov Denis <nenderus@altlinux.org> 1.7.3332-alt1
- Version 1.7.3332

* Sun May 29 2022 Nazarov Denis <nenderus@altlinux.org> 1.7.2828-alt1
- Version 1.7.2828

* Mon May 23 2022 Nazarov Denis <nenderus@altlinux.org> 1.7.2787-alt1
- Version 1.7.2787

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

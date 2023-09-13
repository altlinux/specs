Name: ppsspp
Version: 1.16.1
Release: alt1

Summary: PlayStation Portable Emulator
License: GPL-2.0-or-later
Group: Emulators

Url: https://www.%name.org
Packager: Nazarov Denis <nenderus@altlinux.org>

ExcludeArch: ppc64le

# Source-url: https://github.com/hrydgard/%name/releases/download/v%version/%name-%version.tar.xz
Source: %name-%version.tar

Patch0: %name-alt-ffmpeg.patch
Patch1: %name-alt-git.patch

Requires: %name-common = %EVR

BuildRequires(pre): bzlib-devel
BuildRequires(pre): fontconfig-devel
BuildRequires(pre): libexpat-devel
BuildRequires(pre): libffi-devel
BuildRequires(pre): libpcre2-devel
BuildRequires(pre): libpng-devel
BuildRequires(pre): libbrotli-devel
BuildRequires(pre): zlib-devel

BuildRequires: /proc
BuildRequires: cmake
BuildRequires: libGLEW-devel
BuildRequires: libSDL2_ttf-devel
BuildRequires: libavdevice-devel
BuildRequires: libavfilter-devel
BuildRequires: libminiupnpc-devel
BuildRequires: libpostproc-devel
BuildRequires: libsnappy-devel
BuildRequires: libswresample-devel
BuildRequires: libswscale-devel
BuildRequires: libwayland-cursor-devel
BuildRequires: libwayland-egl-devel
BuildRequires: libwayland-server-devel
BuildRequires: libzip-devel
BuildRequires: libzstd-devel
BuildRequires: qt5-multimedia-devel

%description
PPSSPP is a PSP emulator written in C++, and translates PSP CPU instructions directly into optimized x86, x64 and ARM machine code, using JIT recompilers (dynarecs).

%package common
Summary: PPSSPP assets
Group: Emulators
BuildArch: noarch

%description common
Required assets for PPSSPP GUI and assorted configuration files

%package headless
Summary: PlayStation Portable Emulator (headless)
Group: Emulators
Requires: %name-common = %EVR

%description headless
PPSSPP is a PSP emulator written in C++, and translates PSP CPU instructions directly into optimized x86, x64 and ARM machine code, using JIT recompilers (dynarecs).
This build headless only.

%package qt
Summary: PlayStation Portable Emulator (Qt frontend)
Group: Emulators
Requires: %name-common = %EVR

%description qt
PPSSPP is a PSP emulator written in C++, and translates PSP CPU instructions directly into optimized x86, x64 and ARM machine code, using JIT recompilers (dynarecs).
This build using the Qt frontend.

%prep
%setup

%patch0 -p1
%patch1 -p1

%build

export CPLUS_INCLUDE_PATH=%_includedir/libzip

# Build SDL and headless versions

%define _cmake__builddir %_target_platform

%cmake \
	-DCMAKE_BUILD_TYPE:STRING=Release \
	-DUSE_SYSTEM_SNAPPY:BOOL=TRUE \
	-DUSE_SYSTEM_LIBZIP:BOOL=TRUE \
	-DUSE_SYSTEM_FFMPEG:BOOL=TRUE \
	-DUSE_SYSTEM_ZSTD:BOOL=TRUE \
	-DUSE_SYSTEM_MINIUPNPC:BOOL=TRUE \
	-DHEADLESS:BOOL=TRUE \
	-DLIBZIP_INCLUDE_DIR=%_includedir \
%ifarch %arm
	-DUSING_GLES2:BOOL=TRUE \
%else
	-DOpenGL_GL_PREFERENCE:STRING=GLVND \
%endif
	-Wno-dev

%cmake_build

# Build Qt version

%define _cmake__builddir %_target_platform-qt

%cmake \
	-DCMAKE_BUILD_TYPE:STRING=Release \
	-DUSE_SYSTEM_SNAPPY:BOOL=TRUE \
	-DUSE_SYSTEM_LIBZIP:BOOL=TRUE \
	-DUSE_SYSTEM_FFMPEG:BOOL=TRUE \
	-DUSE_SYSTEM_ZSTD:BOOL=TRUE \
	-DUSE_SYSTEM_MINIUPNPC:BOOL=TRUE \
	-DUSING_QT_UI:BOOL=TRUE \
	-DLIBZIP_INCLUDE_DIR=%_includedir \
%ifarch %arm
	-DUSING_GLES2:BOOL=TRUE \
%else
	-DOpenGL_GL_PREFERENCE:STRING=GLVND \
%endif
	-Wno-dev

%cmake_build

%install
%define _cmake__builddir %_target_platform
%cmake_install
%__install -Dp -m0755 %_target_platform/PPSSPPHeadless %buildroot%_bindir/

%define _cmake__builddir %_target_platform-qt
%cmake_install

%files
%_bindir/PPSSPPSDL
%_desktopdir/PPSSPPSDL.desktop

%files common
%doc LICENSE.TXT README.md
%_datadir/%name
%_datadir/mime/packages/%name.xml
%_iconsdir/hicolor/*/apps/%name.png
%_iconsdir/hicolor/scalable/apps/%name.svg

%files headless
%_bindir/PPSSPPHeadless

%files qt
%_bindir/PPSSPPQt
%_desktopdir/PPSSPPQt.desktop

%changelog
* Thu Sep 14 2023 Nazarov Denis <nenderus@altlinux.org> 1.16.1-alt1
- Version 1.16.1

* Thu May 25 2023 Nazarov Denis <nenderus@altlinux.org> 1.15.4-alt1
- Version 1.15.4

* Fri May 12 2023 Nazarov Denis <nenderus@altlinux.org> 1.15.3-alt1
- Version 1.15.3

* Mon Mar 27 2023 Nazarov Denis <nenderus@altlinux.org> 1.14.4-alt2
- Build with system miniupnpc and zstd (ALT #45656)

* Tue Jan 03 2023 Nazarov Denis <nenderus@altlinux.org> 1.14.4-alt1
- Version 1.14.4

* Mon Jan 02 2023 Nazarov Denis <nenderus@altlinux.org> 1.14.3-alt1
- Version 1.14.3

* Wed Dec 21 2022 Nazarov Denis <nenderus@altlinux.org> 1.14.1-alt1
- Version 1.14.1

* Sat Dec 17 2022 Nazarov Denis <nenderus@altlinux.org> 1.14-alt1
- Version 1.14

* Thu Jul 28 2022 Nazarov Denis <nenderus@altlinux.org> 1.13.1-alt1
- Version 1.13.1

* Wed Jul 27 2022 Nazarov Denis <nenderus@altlinux.org> 1.13-alt1
- Version 1.13

* Thu Nov 11 2021 Nazarov Denis <nenderus@altlinux.org> 1.12.3-alt1
- Version 1.12.3

* Sun Oct 10 2021 Nazarov Denis <nenderus@altlinux.org> 1.12.2-alt1
- Version 1.12.2

* Sat Oct 09 2021 Nazarov Denis <nenderus@altlinux.org> 1.12.1-alt1
- Version 1.12.1

* Fri Apr 16 2021 Nazarov Denis <nenderus@altlinux.org> 1.11.3-alt2
- Fix build with ffmpeg 4.4

* Sat Mar 06 2021 Nazarov Denis <nenderus@altlinux.org> 1.11.3-alt1
- Version 1.11.3

* Thu Feb 18 2021 Nazarov Denis <nenderus@altlinux.org> 1.11.2-alt2
- Fix buildrequires

* Wed Feb 17 2021 Nazarov Denis <nenderus@altlinux.org> 1.11.2-alt1
- Version 1.11.2

* Mon Feb 08 2021 Nazarov Denis <nenderus@altlinux.org> 1.11-alt3
- Build on ARMv7

* Mon Feb 08 2021 Nazarov Denis <nenderus@altlinux.org> 1.11-alt2
- Add workaround ffmpeg 3.1 or later

* Mon Feb 08 2021 Nazarov Denis <nenderus@altlinux.org> 1.11-alt1
- Version 1.11

* Sun Feb 07 2021 Nazarov Denis <nenderus@altlinux.org> 1.10.3-alt2.git5d97f3c
- Update to git d97f3c
- Use system ffmpeg
- Build also ARMv7hf

* Mon Jul 13 2020 Nazarov Denis <nenderus@altlinux.org> 1.10.3-alt1
- Version 1.10.3

* Tue Jul 07 2020 Nazarov Denis <nenderus@altlinux.org> 1.10.2-alt1
- Version 1.10.2

* Sat Jul 04 2020 Nazarov Denis <nenderus@altlinux.org> 1.10.1-alt1
- Version 1.10.1

* Sat Jun 27 2020 Nazarov Denis <nenderus@altlinux.org> 1.10-alt1
- Version 1.10

* Tue Jun 02 2020 Nazarov Denis <nenderus@altlinux.org> 1.9.4-alt4
- Don't gzip sources to speedup rpmbuild -bp

* Tue Jun 02 2020 Nazarov Denis <nenderus@altlinux.org> 1.9.4-alt3
- Build also ARMv7hf and MIPS Little Endian

* Fri May 29 2020 Nazarov Denis <nenderus@altlinux.org> 1.9.4-alt2
- Add ppsspp-ffmpeg 3dparty library
- Don't use system ffmpeg
- Don't find git package
- Use GLVND

* Thu May 28 2020 Nazarov Denis <nenderus@altlinux.org> 1.9.4-alt1
- Initial build for ALT Linux


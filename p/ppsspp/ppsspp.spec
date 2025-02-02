%define armips_commit a8d71f0f279eb0d30ecf6af51473b66ae0cf8e8d
%define discord_rpc_commit 963aa9f3e5ce81a4682c6ca3d136cddda614db33
%define glslang_commit b34f619e1c85810dcb3c578107d2e48ba4ee2b37
%define spirv_cross_commit 4212eef67ed0ca048cb726a6767185504e7695e5
%define cpu_features_commit fd4ffc1632db7b4e763bd28ffa6fc9d761cf3587
%define filesystem_commit 3f1c185ab414e764c694b8171d1c4d8c5c437517
%define ffmpeg_commit 82049cca2e4c1516ed00a77b502a21f91b7843f4
%define rcheevos_commit 32917bdddf4982e62047862c6633e7671aaaf2cb
%define libchdr_commit 26d27ca4903aaccd3ef41337b29bf5ecafb1f0ca
%define rapidjson_commit 73063f5002612c6bf64fe24f851cd5cc0d83eef9

%ifarch %ix86
%set_verify_elf_method textrel=relaxed
%endif

Name: ppsspp
Version: 1.18.1
Release: alt4

Summary: PlayStation Portable Emulator
License: GPL-2.0-or-later
Group: Emulators

Url: https://www.%name.org
Packager: Nazarov Denis <nenderus@altlinux.org>

ExcludeArch: ppc64le

# https://github.com/hrydgard/%name/releases/download/v%version/%name-%version.tar.xz
Source0: %name-%version.tar
# https://github.com/Kingcom/armips/archive/%armips_commit/armips-%armips_commit.tar.gz
Source1: armips-%armips_commit.tar
# https://github.com/discord/discord-rpc/archive/%discord_rpc_commit/discord-rpc-%discord_rpc_commit.tar.gz
Source2: discord-rpc-%discord_rpc_commit.tar
# https://github.com/hrydgard/glslang/archive/%glslang_commit/glslang-%glslang_commit.tar.gz
Source3: glslang-%glslang_commit.tar
# https://github.com/KhronosGroup/SPIRV-Cross/archive/%spirv_cross_commit/SPIRV-Cross-%spirv_cross_commit.tar.gz
Source4: SPIRV-Cross-%spirv_cross_commit.tar
# https://github.com/google/cpu_features/archive/%cpu_features_commit/cpu_features-%cpu_features_commit.tar.gz
Source5: cpu_features-%cpu_features_commit.tar
# https://github.com/Kingcom/filesystem/archive/%filesystem_commit/filesystem-%filesystem_commit.tar.gz
Source6: filesystem-%filesystem_commit.tar
# https://github.com/hrydgard/%name-ffmpeg/archive/%ffmpeg_commit/%name-ffmpeg-%ffmpeg_commit.tar.gz
Source7: %name-ffmpeg-%ffmpeg_commit.tar
# https://github.com/RetroAchievements/rcheevos/archive/%rcheevos_commit/rcheevos-%rcheevos_commit.tar.gz
Source8: rcheevos-%rcheevos_commit.tar
# https://github.com/rtissera/libchdr/archive/%libchdr_commit/libchdr-%libchdr_commit.tar.gz
Source9: libchdr-%libchdr_commit.tar
# https://github.com/Tencent/rapidjson/archive/%rapidjson_commit/rapidjson-%rapidjson_commit.tar.gz
Source10: rapidjson-%rapidjson_commit.tar

Patch0: %name-alt-git.patch
Patch1: %name-alt-miniupnpc.patch
Patch2: %name-1.18.1-alt-loongarch-always-return.patch
# https://github.com/hrydgard/ppsspp/pull/19840
Patch3: %name-1.18.1-sdl2_ttf.patch

Requires: %name-common = %EVR

BuildRequires: /proc
BuildRequires: cmake
BuildRequires: libGLEW-devel
BuildRequires: libSDL2_ttf-devel
BuildRequires: libminiupnpc-devel
BuildRequires: libsnappy-devel
BuildRequires: libwayland-cursor-devel
BuildRequires: libwayland-egl-devel
BuildRequires: libwayland-server-devel
BuildRequires: libzip-devel
BuildRequires: libzstd-devel
BuildRequires: openxr-devel
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

%package libretro
Summary: PlayStation Portable Emulator (libretro frontend)
Group: Emulators
Requires: retroarch

%description libretro
PPSSPP is a PSP emulator written in C++, and translates PSP CPU instructions directly into optimized x86, x64 and ARM machine code, using JIT recompilers (dynarecs).
This build using the libretro frontend.

%package qt
Summary: PlayStation Portable Emulator (Qt frontend)
Group: Emulators
Requires: %name-common = %EVR

%description qt
PPSSPP is a PSP emulator written in C++, and translates PSP CPU instructions directly into optimized x86, x64 and ARM machine code, using JIT recompilers (dynarecs).
This build using the Qt frontend.

%prep
%setup -b 1 -b 2 -b 3 -b 4 -b 5 -b 6 -b 7 -b 8 -b 9 -b 10

%__mv -Tf ../armips-%armips_commit ext/armips
%__mv -Tf ../discord-rpc-%discord_rpc_commit ext/discord-rpc
%__mv -Tf ../glslang-%glslang_commit ext/glslang
%__mv -Tf ../SPIRV-Cross-%spirv_cross_commit ext/SPIRV-Cross
%__mv -Tf ../cpu_features-%cpu_features_commit ext/cpu_features
%__mv -Tf ../filesystem-%filesystem_commit ext/armips/ext/filesystem
%__mv -Tf ../%name-ffmpeg-%ffmpeg_commit ffmpeg
%__mv -Tf ../rcheevos-%rcheevos_commit ext/rcheevos
%__mv -Tf ../libchdr-%libchdr_commit ext/libchdr
%__mv -Tf ../rapidjson-%rapidjson_commit ext/rapidjson

%patch0 -p1
%patch1 -p1
%patch2 -p2
%patch3 -p1

%build
%add_optflags -Wno-error=return-type

export CPLUS_INCLUDE_PATH=%_includedir/libzip

# Build SDL and headless versions

%define _cmake__builddir %_target_platform

%cmake \
	-DCMAKE_BUILD_TYPE:STRING=Release \
	-DUSE_SYSTEM_SNAPPY:BOOL=TRUE \
	-DUSE_SYSTEM_LIBZIP:BOOL=TRUE \
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

# Build libretro versions

%define _cmake__builddir %_target_platform-libretro

%cmake \
	-DCMAKE_BUILD_TYPE:STRING=Release \
	-DUSE_SYSTEM_SNAPPY:BOOL=TRUE \
	-DUSE_SYSTEM_LIBZIP:BOOL=TRUE \
	-DUSE_SYSTEM_ZSTD:BOOL=TRUE \
	-DUSE_SYSTEM_MINIUPNPC:BOOL=TRUE \
	-DLIBRETRO:BOOL=TRUE \
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
%__mkdir_p %buildroot%_libexecdir/libretro
%__install -Dp -m0644 %_target_platform-libretro/lib/%{name}_libretro.so %buildroot%_libexecdir/libretro/

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

%files libretro
%_libexecdir/libretro/%{name}_libretro.so

%files qt
%_bindir/PPSSPPQt
%_desktopdir/PPSSPPQt.desktop

%changelog
* Sun Feb 02 2025 Nazarov Denis <nenderus@altlinux.org> 1.18.1-alt4
- Switched to use .gear/tags

* Sat Feb 01 2025 Nazarov Denis <nenderus@altlinux.org> 1.18.1-alt3
- build with bundled ffmpeg (ALT #51464)

* Mon Nov 18 2024 Ilya Sorochan <k0tran@altlinux.org> 1.18.1-alt2
- add patch that fixes FTBFS on loongarch64

* Tue Nov 05 2024 Nazarov Denis <nenderus@altlinux.org> 1.18.1-alt1
- new version (1.18.1) with rpmgs script

* Mon Nov 04 2024 Nazarov Denis <nenderus@altlinux.org> 1.18-alt1
- new version (1.18) with rpmgs script

* Tue May 28 2024 Nazarov Denis <nenderus@altlinux.org> 1.17.1-alt2
- Build libretro frontend

* Thu Feb 15 2024 Nazarov Denis <nenderus@altlinux.org> 1.17.1-alt1
- new version (1.17.1) with rpmgs script

* Fri Oct 13 2023 Nazarov Denis <nenderus@altlinux.org> 1.16.6-alt1
- new version (1.16.6) with rpmgs script

* Fri Sep 29 2023 Nazarov Denis <nenderus@altlinux.org> 1.16.5-alt1
- new version (1.16.5) with rpmgs script

* Mon Sep 25 2023 Nazarov Denis <nenderus@altlinux.org> 1.16.4-alt1
- Version 1.16.4

* Sat Sep 23 2023 Nazarov Denis <nenderus@altlinux.org> 1.16.3-alt1
- Version 1.16.3

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


%define armips_commit 6719edebaae03330ee5441d9b28280672edf00d5
%define discord_rpc_commit 963aa9f3e5ce81a4682c6ca3d136cddda614db33
%define glslang_commit dc11adde23c455a24e13dd54de9b4ede8bdd7db8
%define miniupnp_commit 3a87be33e797ba947b2b2a5f8d087f6c3ff4d93e
%define spirv_cross_commit 9acb9ec31f5a8ef80ea6b994bb77be787b08d3d1
%define zstd_commit 096dccbc2d89a560db0b9892c53ea0c77eff20a1
%define filesystem_commit 3f1c185ab414e764c694b8171d1c4d8c5c437517

Name: ppsspp
Version: 1.14.4
Release: alt1

Summary: PlayStation Portable Emulator
License: GPL-2.0-or-later
Group: Emulators

Url: https://www.%name.org
Packager: Nazarov Denis <nenderus@altlinux.org>

ExcludeArch: ppc64le

# https://github.com/hrydgard/%name/archive/v%version/%name-%version.tar.gz
Source0: %name-%version.tar
# https://github.com/Kingcom/armips/archive/%armips_commit/armips-%armips_commit.tar.gz
Source1: armips-%armips_commit.tar
# https://github.com/discord/discord-rpc/archive/%discord_rpc_commit/discord-rpc-%discord_rpc_commit.tar.gz
Source2: discord-rpc-%discord_rpc_commit.tar
# https://github.com/hrydgard/glslang/archive/%glslang_commit/glslang-%glslang_commit.tar.gz
Source3: glslang-%glslang_commit.tar
# https://github.com/hrydgard/miniupnp/archive/%miniupnp_commit/miniupnp-%miniupnp_commit.tar.gz
Source4: miniupnp-%miniupnp_commit.tar
# https://github.com/KhronosGroup/SPIRV-Cross/archive/%spirv_cross_commit/SPIRV-Cross-%spirv_cross_commit.tar.gz
Source5: SPIRV-Cross-%spirv_cross_commit.tar
# https://github.com/facebook/zstd/archive/%zstd_commit/zstd-%zstd_commit.tar.gz
Source6: zstd-%zstd_commit.tar
# https://github.com/Kingcom/filesystem/archive/%filesystem_commit/filesystem-%filesystem_commit.tar.gz
Source7: filesystem-%filesystem_commit.tar

Patch0: %name-alt-ffmpeg.patch
Patch1: %name-alt-git.patch

BuildRequires: cmake
BuildRequires: pkgconfig(Qt5Multimedia)
BuildRequires: pkgconfig(RapidJSON)
BuildRequires: pkgconfig(glew)
BuildRequires: pkgconfig(libavdevice)
BuildRequires: pkgconfig(libavfilter)
BuildRequires: pkgconfig(libpng17)
BuildRequires: pkgconfig(libpostproc)
BuildRequires: pkgconfig(libswresample)
BuildRequires: pkgconfig(libswscale)
BuildRequires: pkgconfig(libzip)
BuildRequires: pkgconfig(sdl2)
BuildRequires: pkgconfig(snappy)

Requires: %name-common = %EVR

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
%setup -b 1 -b 2 -b 3 -b 4 -b 5 -b 6 -b 7

%__mv -Tf ../armips-%armips_commit ext/armips
%__mv -Tf ../discord-rpc-%discord_rpc_commit ext/discord-rpc
%__mv -Tf ../glslang-%glslang_commit ext/glslang
%__mv -Tf ../miniupnp-%miniupnp_commit ext/miniupnp
%__mv -Tf ../SPIRV-Cross-%spirv_cross_commit ext/SPIRV-Cross
%__mv -Tf ../zstd-%zstd_commit ext/zstd
%__mv -Tf ../filesystem-%filesystem_commit ext/armips/ext/filesystem

%patch0 -p1
%patch1 -p1

# Fix version string
sed s,"unknown","%{version}",g -i git-version.cmake

%build

export CPLUS_INCLUDE_PATH=%_includedir/libzip

# Build SDL and headless versions

%define _cmake__builddir %_target_platform

%cmake \
	-DCMAKE_BUILD_TYPE:STRING=Release \
	-DUSE_SYSTEM_SNAPPY:BOOL=TRUE \
	-DUSE_SYSTEM_LIBZIP:BOOL=TRUE \
	-DUSE_SYSTEM_FFMPEG:BOOL=TRUE \
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


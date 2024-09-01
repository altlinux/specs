%define optflags_lto %nil

%define git_ver 16885
%define git_commit e56164f1e321fe2873c246a268af8ce1dc9281bd

%define glslang_version 13.1.1
%define asmjit_commit 416f7356967c1f66784dc1580fe157f9406d8bff
%define hidapi_commit 8b43a97a9330f8b0035439ce9e255e4be202deca
%define yaml_cpp_commit 456c68f452da09d8ca84b375faa2b1397713eaba
%define spirv_headers_version vulkan-sdk-1.3.268.0
%define spirv_tools_version 2023.5.rc1
%define cubeb_commit 70b4e3db7822de4d534959885cda109d6edbee36
%define soundtouch_commit 394e1f58b23dc80599214d2e9b6a5e0dfd0bbe07
%define miniupnp_version miniupnpd_2_3_6
%define rtmidi_version 6.0.0
%define zstd_commit 97291fc5020a8994019ab76cf0cda83a9824374c
%define openal_version 1.23.1

Name: rpcs3
Version: 0.0.33
Release: alt1

Summary: PS3 emulator/debugger
License: GPLv2
Group: Emulators

Url: https://%name.net/
Packager: Nazarov Denis <nenderus@altlinux.org>

ExclusiveArch: x86_64 aarch64

# https://github.com/RPCS3/%name/archive/v%version/%name-%version.tar.gz
Source0: %name-%version.tar
# https://github.com/KhronosGroup/glslang/archive/%glslang_version/glslang-%glslang_version.tar.gz
Source1: glslang-%glslang_version.tar
# https://github.com/RPCS3/asmjit/archive/%asmjit_commit/asmjit-%asmjit_commit.tar.gz
Source2: asmjit-%asmjit_commit.tar
# https://github.com/RPCS3/hidapi/archive/%hidapi_commit/hidapi-%hidapi_commit.tar.gz
Source3: hidapi-%hidapi_commit.tar
# https://github.com/RPCS3/yaml-cpp/archive/%yaml_cpp_commit/yaml-cpp-%yaml_cpp_commit.tar.gz
Source4: yaml-cpp-%yaml_cpp_commit.tar
# https://github.com/KhronosGroup/SPIRV-Headers/archive/%spirv_headers_version/SPIRV-Headers-%spirv_headers_version.tar.gz
Source5: SPIRV-Headers-%spirv_headers_version.tar
# https://github.com/KhronosGroup/SPIRV-Tools/archive/v%spirv_tools_version/SPIRV-Tools-%spirv_tools_version.tar.gz
Source6: SPIRV-Tools-%spirv_tools_version.tar
# https://github.com/mozilla/cubeb/archive/%cubeb_commit/cubeb-%cubeb_commit.tar.gz
Source7: cubeb-%cubeb_commit.tar
# https://github.com/RPCS3/soundtouch/archive/%soundtouch_commit/soundtouch-%soundtouch_commit.tar.gz
Source8: soundtouch-%soundtouch_commit.tar
# https://github.com/miniupnp/miniupnp/archive/%miniupnp_version/miniupnp-%miniupnp_version.tar.gz
Source9: miniupnp-%miniupnp_version.tar
# https://github.com/thestk/rtmidi/archive/refs/tags/%rtmidi_version/rtmidi-%rtmidi_version.tar.gz
Source10: rtmidi-%rtmidi_version.tar
# https://github.com/facebook/zstd/archive/%zstd_commit/zstd-%zstd_commit.tar.gz
Source11: zstd-%zstd_commit.tar
# https://github.com/kcat/openal-soft/archive/%openal_version/openal-soft-%openal_version.tar.gz
Source12: openal-soft-%openal_version.tar

BuildRequires: /proc
BuildRequires: clang
BuildRequires: cmake
BuildRequires: doxygen
BuildRequires: glslang
BuildRequires: glslc
BuildRequires: graphviz
BuildRequires: libGLEW-devel
BuildRequires: libSDL2-devel
BuildRequires: libalsa-devel
BuildRequires: libavformat-devel
BuildRequires: libcurl-devel
BuildRequires: libedit-devel
BuildRequires: libevdev-devel
BuildRequires: libfaudio-devel
BuildRequires: libffi-devel
BuildRequires: libflatbuffers-devel
BuildRequires: libopenal-devel
BuildRequires: libpng-devel
BuildRequires: libpugixml-devel
BuildRequires: libstb-devel
BuildRequires: libswresample-devel
BuildRequires: libswscale-devel
BuildRequires: libtinfo-devel
BuildRequires: libudev-devel
BuildRequires: libusb-devel
BuildRequires: libvulkan-devel
BuildRequires: libwayland-cursor-devel
BuildRequires: libwayland-egl-devel
BuildRequires: libwayland-server-devel
BuildRequires: libwolfssl-devel
BuildRequires: libxml2-devel
BuildRequires: libxxhash-devel
BuildRequires: lld
BuildRequires: llvm
BuildRequires: llvm-devel
BuildRequires: ninja-build
BuildRequires: pipewire-jack-libs-devel
BuildRequires: qt6-multimedia-devel
BuildRequires: qt6-svg-devel

%description
The world's first free and open-source PlayStation 3 emulator/debugger, written in C++ for Windows and Linux.

%prep
%setup -b 1 -b 2 -b 3 -b 4 -b 5 -b 6 -b 7 -b 8 -b 9 -b 10 -b 11 -b 12

%__mv -Tf ../glslang-%glslang_version 3rdparty/glslang/glslang
%__mv -Tf ../asmjit-%asmjit_commit 3rdparty/asmjit/asmjit
%__mv -Tf ../hidapi-%hidapi_commit 3rdparty/hidapi/hidapi
%__mv -Tf ../yaml-cpp-%yaml_cpp_commit 3rdparty/yaml-cpp/yaml-cpp
%__mv -Tf ../SPIRV-Headers-%spirv_headers_version 3rdparty/SPIRV/SPIRV-Headers
%__mv -Tf ../SPIRV-Tools-%spirv_tools_version 3rdparty/SPIRV/SPIRV-Tools
%__mv -Tf ../cubeb-%cubeb_commit 3rdparty/cubeb/cubeb
%__mv -Tf ../soundtouch-%soundtouch_commit 3rdparty/SoundTouch/soundtouch
%__mv -Tf ../miniupnp-%miniupnp_version 3rdparty/miniupnp/miniupnp
%__mv -Tf ../rtmidi-%rtmidi_version 3rdparty/rtmidi/rtmidi
%__mv -Tf ../zstd-%zstd_commit 3rdparty/zstd/zstd
%__mv -Tf ../openal-soft-%openal_version 3rdparty/OpenAL/openal-soft

#Generate Version Strings
GIT_VERSION=$(echo %git_ver)
GIT_COMMIT=$(echo %git_commit)

echo "// This is a generated file.

#define RPCS3_GIT_VERSION \"$GIT_VERSION-${GIT_COMMIT:0:8}\"
#define RPCS3_GIT_BRANCH \"master\"
#define RPCS3_GIT_FULL_BRANCH \"RPCS3/rpcs3/master\"

// If you don't want this file to update/recompile, change to 1.
#define RPCS3_GIT_VERSION_NO_UPDATE 1
" > %name/git-version.h

%build
%add_optflags -I%_includedir/stb

%cmake \
	-DCMAKE_C_COMPILER:STRING=clang \
	-DCMAKE_CXX_COMPILER:STRING=clang++ \
	-DCMAKE_RANLIB:PATH=%_bindir/llvm-ranlib \
	-DCMAKE_AR:PATH=%_bindir/llvm-ar \
	-DCMAKE_NM:PATH=%_bindir/llvm-nm \
	-DCMAKE_EXE_LINKER_FLAGS:STRING="-fuse-ld=lld" \
	-DUSE_NATIVE_INSTRUCTIONS:BOOL=FALSE \
	-DUSE_SYSTEM_FFMPEG:BOOL=TRUE \
	-DUSE_SYSTEM_LIBPNG:BOOL=TRUE \
	-DUSE_SYSTEM_CURL:BOOL=TRUE \
	-DUSE_SYSTEM_LIBUSB:BOOL=TRUE \
	-DUSE_SYSTEM_FLATBUFFERS:BOOL=TRUE \
	-DUSE_SYSTEM_PUGIXML:BOOL=TRUE \
	-DUSE_SYSTEM_XXHASH:BOOL=TRUE \
	-DUSE_SYSTEM_WOLFSSL:BOOL=TRUE \
	-DUSE_SYSTEM_FAUDIO:BOOL=TRUE \
	-DLLVM_DIR:PATH=$(llvm-config --cmakedir) \
	-GNinja \
	-Wno-dev

%cmake_build

%install
%cmake_install

%__rm -rf %buildroot%_datadir/%name/{git,test}

%files
%doc LICENSE README.md
%_bindir/%name
%_desktopdir/%name.desktop
%_liconsdir/%name.png
%_iconsdir/hicolor/scalable/apps/%name.svg
%_datadir/%name
%_datadir/metainfo/%name.metainfo.xml

%changelog
* Sun Sep 01 2024 Nazarov Denis <nenderus@altlinux.org> 0.0.33-alt1
- Version 0.0.33

* Fri Jul 26 2024 Nazarov Denis <nenderus@altlinux.org> 0.0.32-alt2.1
- Fix FTBFS

* Sat May 04 2024 Nazarov Denis <nenderus@altlinux.org> 0.0.32-alt2
- Build with current LLVM
- Update build requires

* Wed May 01 2024 Nazarov Denis <nenderus@altlinux.org> 0.0.32-alt1
- Version 0.0.32

* Fri Mar 29 2024 Nazarov Denis <nenderus@altlinux.org> 0.0.31-alt2
- Fix build with wolfSSL 5.7.0

* Tue Mar 05 2024 Nazarov Denis <nenderus@altlinux.org> 0.0.31-alt1
- Version 0.0.31

* Wed Jan 03 2024 Nazarov Denis <nenderus@altlinux.org> 0.0.30-alt1
- Version 0.0.30

* Wed Aug 30 2023 Nazarov Denis <nenderus@altlinux.org> 0.0.29-alt1.2
- Fix FTBFS

* Sat Aug 19 2023 Nazarov Denis <nenderus@altlinux.org> 0.0.29-alt1.1
- Fix FTBFS

* Mon Jul 31 2023 Nazarov Denis <nenderus@altlinux.org> 0.0.29-alt1
- Version 0.0.29

* Mon Jun 05 2023 Nazarov Denis <nenderus@altlinux.org> 0.0.28-alt2
- Build with system LLVM

* Sat Jun 03 2023 Nazarov Denis <nenderus@altlinux.org> 0.0.28-alt1
- Version 0.0.28

* Thu Mar 02 2023 Nazarov Denis <nenderus@altlinux.org> 0.0.27-alt1
- Version 0.0.27

* Sun Jan 08 2023 Nazarov Denis <nenderus@altlinux.org> 0.0.26-alt1
- Version 0.0.26

* Wed Nov 02 2022 Nazarov Denis <nenderus@altlinux.org> 0.0.25-alt1
- Version 0.0.25

* Thu Sep 01 2022 Nazarov Denis <nenderus@altlinux.org> 0.0.24-alt1
- Version 0.0.24

* Sat Jul 02 2022 Nazarov Denis <nenderus@altlinux.org> 0.0.23-alt1
- Version 0.0.23

* Sun May 01 2022 Nazarov Denis <nenderus@altlinux.org> 0.0.22-alt1
- Version 0.0.22
- Build with Clang
- Build on AArch64

* Wed Mar 02 2022 Nazarov Denis <nenderus@altlinux.org> 0.0.21-alt1
- Version 0.0.21
- Build with GCC

* Mon Jan 10 2022 Nazarov Denis <nenderus@altlinux.org> 0.0.20-alt2
- Set ALTWRAP_LLVM_VERSION to select correct LLVM version
- Fix BR
- Build with ninja

* Mon Jan 03 2022 Nazarov Denis <nenderus@altlinux.org> 0.0.20-alt1
- Version 0.0.20

* Mon Nov 01 2021 Nazarov Denis <nenderus@altlinux.org> 0.0.19-alt1
- Version 0.0.19

* Wed Sep 01 2021 Nazarov Denis <nenderus@altlinux.org> 0.0.18-alt1
- Version 0.0.18

* Wed Aug 25 2021 Nazarov Denis <nenderus@altlinux.org> 0.0.17-alt4
- Disable LTO

* Thu Jul 08 2021 Nazarov Denis <nenderus@altlinux.org> 0.0.17-alt3
- Build with system wolfssl

* Wed Jul 07 2021 Nazarov Denis <nenderus@altlinux.org> 0.0.17-alt2
- Build with system flatbuffers, pugixml and xxhash

* Thu Jul 01 2021 Nazarov Denis <nenderus@altlinux.org> 0.0.17-alt1
- Version 0.0.17

* Sat May 01 2021 Nazarov Denis <nenderus@altlinux.org> 0.0.16-alt1
- Version 0.0.16

* Mon Mar 01 2021 Nazarov Denis <nenderus@altlinux.org> 0.0.15-alt1
- Version 0.0.15

* Mon Feb 15 2021 Nazarov Denis <nenderus@altlinux.org> 0.0.14-alt5
- Build with clang

* Thu Feb 11 2021 Nazarov Denis <nenderus@altlinux.org> 0.0.14-alt4
- Build with python3-module-Pygments

* Thu Feb 11 2021 Nazarov Denis <nenderus@altlinux.org> 0.0.14-alt3
- Remove qt5 required version patch

* Thu Feb 04 2021 Nazarov Denis <nenderus@altlinux.org> 0.0.14-alt2
- Build with system libusb

* Sat Jan 09 2021 Nazarov Denis <nenderus@altlinux.org> 0.0.14-alt1
- Version 0.0.14

* Wed Nov 04 2020 Nazarov Denis <nenderus@altlinux.org> 0.0.13-alt2
- Update build and build requires

* Mon Nov 02 2020 Nazarov Denis <nenderus@altlinux.org> 0.0.13-alt1
- Version 0.0.13

* Tue Sep 01 2020 Nazarov Denis <nenderus@altlinux.org> 0.0.12-alt1
- Version 0.0.12

* Sat Aug 29 2020 Nazarov Denis <nenderus@altlinux.org> 0.0.11.10801-alt1
- Version 0.0.11.10801

* Mon Aug 24 2020 Nazarov Denis <nenderus@altlinux.org> 0.0.11.10773-alt1
- Version 0.0.11.10773

* Fri Aug 21 2020 Nazarov Denis <nenderus@altlinux.org> 0.0.11.10768-alt1
- Version 0.0.11.10768

* Wed Aug 19 2020 Nazarov Denis <nenderus@altlinux.org> 0.0.11.10765-alt1
- Version 0.0.11.10765

* Mon Aug 17 2020 Nazarov Denis <nenderus@altlinux.org> 0.0.11-alt1
- Version 0.0.11

* Sat Aug 01 2020 Nazarov Denis <nenderus@altlinux.org> 0.0.8-alt5
- Use precompiled headers

* Tue Jun 23 2020 Nazarov Denis <nenderus@altlinux.org> 0.0.8-alt4
- Remove dirs not related to %name package

* Mon Jun 22 2020 Nazarov Denis <nenderus@altlinux.org> 0.0.8-alt3
- Don't find git package
- Remove more deprecated VK_DYNAMIC_STATE_RANGE_SIZE usage

* Sat Jan 04 2020 Nazarov Denis <nenderus@altlinux.org> 0.0.8-alt2
- Update glslang to 7.13.3496

* Fri Jan 03 2020 Nazarov Denis <nenderus@altlinux.org> 0.0.8-alt1.1
- build with python3
- don't gzip sources

* Thu Jan 02 2020 Nazarov Denis <nenderus@altlinux.org> 0.0.8-alt1
- Version 0.0.8

* Thu Dec 26 2019 Sergey V Turchin <zerg@altlinux.org> 0.0.7.9212-alt1.1
- build with python3
- don't gzip sources

* Tue Dec 24 2019 Nazarov Denis <nenderus@altlinux.org> 0.0.7.9250-alt1
- Version 0.0.7.9250

* Sat Dec 07 2019 Nazarov Denis <nenderus@altlinux.org> 0.0.7.9212-alt1
- Version 0.0.7-9212

* Wed Nov 27 2019 Nazarov Denis <nenderus@altlinux.org> 0.0.7.9180-alt1
- Version 0.0.7.9180

* Fri Nov 15 2019 Nazarov Denis <nenderus@altlinux.org> 0.0.7.9135-alt1
- Version 0.0.7.9135

* Tue Nov 12 2019 Nazarov Denis <nenderus@altlinux.org> 0.0.7.9123-alt1
- Version 0.0.7.9123

* Mon Nov 11 2019 Nazarov Denis <nenderus@altlinux.org> 0.0.7.9122-alt1
- Version 0.0.7.9122
- Remove GSL package
- Add span package in 3rdparty

* Sat Nov 09 2019 Nazarov Denis <nenderus@altlinux.org> 0.0.7.9095-alt1
- Version 0.0.7.9095

* Fri Nov 08 2019 Nazarov Denis <nenderus@altlinux.org> 0.0.7.9086-alt1
- Version 0.0.7.9086
- Change commits to version on 3rdparty packages (if possible)

* Sun Nov 03 2019 Nazarov Denis <nenderus@altlinux.org> 0.0.7.9061-alt1
- Version 0.0.7.9061
- Add FAudio in 3rdparty
- Update build requires

* Thu Oct 31 2019 Nazarov Denis <nenderus@altlinux.org> 0.0.7.9053-alt1
- Version 0.0.7.9053

* Wed Oct 23 2019 Nazarov Denis <nenderus@altlinux.org> 0.0.7.8990-alt1
- Version 0.0.7.8990
- Update LLVM to 9836c29

* Mon Oct 21 2019 Nazarov Denis <nenderus@altlinux.org> 0.0.7.8963-alt1
- Version 0.0.7.8963

* Sat Oct 19 2019 Nazarov Denis <nenderus@altlinux.org> 0.0.7.8935-alt1
- Version 0.0.7.8935

* Tue Oct 15 2019 Nazarov Denis <nenderus@altlinux.org> 0.0.7.8896-alt1
- Version 0.0.7.8896

* Mon Oct 14 2019 Nazarov Denis <nenderus@altlinux.org> 0.0.7.8886-alt1
- Version 0.0.7.8886

* Sun Oct 13 2019 Nazarov Denis <nenderus@altlinux.org> 0.0.7.8871-alt1
- Version 0.0.7.8871

* Sat Oct 12 2019 Nazarov Denis <nenderus@altlinux.org> 0.0.7.8862-alt1
- Version 0.0.7.8862
- Update asmjit to fc251c9
- Update glslang to c11e315
- Update libusb to 7cfa00e

* Wed May 22 2019 Nazarov Denis <nenderus@altlinux.org> 0.0.6.8156-alt1
- Version 0.0.6.8156

* Tue May 21 2019 Nazarov Denis <nenderus@altlinux.org> 0.0.6.8152-alt1
- Version 0.0.6.8152
- Fix post-install unowned files

* Mon May 20 2019 Nazarov Denis <nenderus@altlinux.org> 0.0.6.8147-alt1
- Initial build for ALT Linux


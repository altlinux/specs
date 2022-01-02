%define optflags_lto -flto=thin

%define clang_version 12

%define git_ver 13138
%define git_commit 61d9852632e5b417acf47299532c9f80f54d0fd5

%define glslang_version 11.7.1
%define asmjit_commit eae7197fce03fd52a6e71ca89207a88ce270fb1a
%define hidapi_commit 01f601a1509bf9c67819fbf521df39644bab52d5
%define yaml_cpp_commit 0b67821f307e8c6bf0eba9b6d3250e3cf1441450
%define llvm_commit 1c0ca194dc501ffb1674868babf8bd52658a0734
%define spirv_headers_version 1.5.3.reservations1
%define spirv_tools_version 2020.4
%define cubeb_commit d512bfa07a327e0ae7e7aef892dcce01cbeaa67c

Name: rpcs3
Version: 0.0.20
Release: alt1

Summary: PS3 emulator/debugger
License: GPLv2
Group: Emulators

Url: https://%name.net/
Packager: Nazarov Denis <nenderus@altlinux.org>

ExclusiveArch: x86_64

# https://github.com/RPCS3/%name/archive/v%version/%name-%version.tar.gz
Source0: %name-%version.tar
# https://github.com/KhronosGroup/glslang/archive/%glslang_version/glslang-%glslang_version.tar.gz
Source1: glslang-%glslang_version.tar
# https://github.com/asmjit/asmjit/archive/%asmjit_commit/asmjit-%asmjit_commit.tar.gz
Source2: asmjit-%asmjit_commit.tar
# https://github.com/RPCS3/hidapi/archive/%hidapi_commit/hidapi-%hidapi_commit.tar.gz
Source3: hidapi-%hidapi_commit.tar
# https://github.com/RPCS3/yaml-cpp/archive/%yaml_cpp_commit/yaml-cpp-%yaml_cpp_commit.tar.gz
Source4: yaml-cpp-%yaml_cpp_commit.tar
# https://github.com/RPCS3/llvm-mirror/archive/%llvm_commit/llvm-mirror-%llvm_commit.tar.gz
Source5: llvm-mirror-%llvm_commit.tar
# https://github.com/KhronosGroup/SPIRV-Headers/archive/%spirv_headers_version/SPIRV-Headers-%spirv_headers_version.tar.gz
Source6: SPIRV-Headers-%spirv_headers_version.tar
# https://github.com/KhronosGroup/SPIRV-Tools/archive/v%spirv_tools_version/SPIRV-Tools-%spirv_tools_version.tar.gz
Source7: SPIRV-Tools-%spirv_tools_version.tar
# https://github.com/mozilla/cubeb/archive/%cubeb_commit/cubeb-%cubeb_commit.tar.gz
Source8: cubeb-%cubeb_commit.tar

Patch0: %name-alt-git.patch
Patch1: %name-alt-jit-events.patch

BuildRequires: /proc
BuildRequires: clang%clang_version.0
BuildRequires: cmake >= 3.16.9
BuildRequires: git-core
BuildRequires: pkgconfig(FAudio)
BuildRequires: pkgconfig(Qt5) >= 5.15.2
BuildRequires: pkgconfig(Qt5Multimedia) >= 5.15.2
BuildRequires: pkgconfig(Qt5MultimediaWidgets) >= 5.15.2
BuildRequires: pkgconfig(Qt5Svg) >= 5.15.2
BuildRequires: pkgconfig(flatbuffers)
BuildRequires: pkgconfig(glew)
BuildRequires: pkgconfig(libavformat)
BuildRequires: pkgconfig(libcurl)
BuildRequires: pkgconfig(libevdev)
BuildRequires: pkgconfig(libffi)
BuildRequires: pkgconfig(libpng)
BuildRequires: pkgconfig(libswscale)
BuildRequires: pkgconfig(libusb-1.0)
BuildRequires: pkgconfig(libxml-2.0)
BuildRequires: pkgconfig(libxxhash)
BuildRequires: pkgconfig(openal)
BuildRequires: pkgconfig(pugixml)
BuildRequires: pkgconfig(python3)
BuildRequires: pkgconfig(sdl2)
BuildRequires: pkgconfig(wayland-cursor)
BuildRequires: pkgconfig(wayland-egl)
BuildRequires: pkgconfig(wayland-server)
BuildRequires: pkgconfig(wolfssl)
BuildRequires: llvm%clang_version.0
BuildRequires: ocaml-ctypes
BuildRequires: ocaml-findlib
BuildRequires: python3-module-yaml

BuildPreReq: pkgconfig(libswresample)
BuildPreReq: python3-module-Pygments

%description
The world's first free and open-source PlayStation 3 emulator/debugger, written in C++ for Windows and Linux.

%prep
%setup -b 1 -b 2 -b 3 -b 4 -b 5 -b 6 -b 7 -b 8

%patch0 -p1
%patch1 -p1

%__mv -Tf ../glslang-%glslang_version 3rdparty/glslang/glslang
%__mv -Tf ../asmjit-%asmjit_commit 3rdparty/asmjit/asmjit
%__mv -Tf ../hidapi-%hidapi_commit 3rdparty/hidapi/hidapi
%__mv -Tf ../yaml-cpp-%yaml_cpp_commit 3rdparty/yaml-cpp/yaml-cpp
%__mv -Tf ../llvm-mirror-%llvm_commit llvm
%__mv -Tf ../SPIRV-Headers-%spirv_headers_version 3rdparty/SPIRV/SPIRV-Headers
%__mv -Tf ../SPIRV-Tools-%spirv_tools_version 3rdparty/SPIRV/SPIRV-Tools
%__mv -Tf ../cubeb-%cubeb_commit 3rdparty/cubeb/cubeb

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
export CC="clang-%clang_version"
export CXX="clang++-%clang_version"
export LINKER="lld-%clang_version"
export AR="llvm-ar-%clang_version"
export RANLIB="llvm-ranlib-%clang_version"

%cmake \
	-DCMAKE_LINKER:STRING="$LINKER" \
	-DCMAKE_AR:STRING="$AR" \
	-DCMAKE_RANLIB:STRING="$RANLIB" \
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
	-DLLVM_USE_LINKER:STRING="$LINKER" \
	-DPython3_EXECUTABLE="%__python3" \
	-Wno-dev

%cmake_build

%install
%cmake_install

%files
%doc LICENSE README.md
%_bindir/%name
%_desktopdir/%name.desktop
%_liconsdir/%name.png
%_iconsdir/hicolor/scalable/apps/%name.svg
%_datadir/%name
%_datadir/metainfo/%name.metainfo.xml

%changelog
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


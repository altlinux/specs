%define git_ver 11506
%define git_commit 2b8eb8deb6e86deca9c677c8b300da3762532075

%define glslang_commit 3ee5f2f1d3316e228916788b300d786bb574d337
%define asmjit_commit fc251c914e77cd079e58982cdab00a47539d7fc5
%define pugixml_commit 8bf806c035373bd0723a85c0820cfd5c804bf6cd
%define hidapi_commit 8961cf86ebc4756992a7cd65c219c743e94bab19
%define yaml_cpp_commit 6a211f0bc71920beef749e6c35d7d1bcc2447715
%define xx_hash_version 0.8.0
%define llvm_commit cb7748dfa0d615e9f5ea9f31e0ce40fe9aeac595
%define cereal_commit 60c69df968d1c72c998cd5f23ba34e2e3718a84b
%define faudio_commit 9c7d2d1430c9dbe4e67c871dfe003b331f165412
%define span_commit 9d7559aabdebf569cab3480a7ea2a87948c0ae47
%define spirv_headers_version 1.5.3.reservations1
%define spirv_tools_version 2020.4
%define wolfssl_commit 39b5448601271b8d1deabde8a0d33dc64d2a94bd

Name: rpcs3
Version: 0.0.14
Release: alt2

Summary: PS3 emulator/debugger
License: GPLv2
Group: Emulators

Url: https://%name.net/
Packager: Nazarov Denis <nenderus@altlinux.org>

ExclusiveArch: x86_64

# https://github.com/RPCS3/%name/archive/v%version/%name-%version.tar.gz
Source0: %name-%version.tar
# https://github.com/KhronosGroup/glslang/archive/%glslang_commit/glslang-%glslang_commit.tar.gz
Source1: glslang-%glslang_commit.tar
# https://github.com/asmjit/asmjit/archive/%asmjit_commit/asmjit-%asmjit_commit.tar.gz
Source2: asmjit-%asmjit_commit.tar
# https://github.com/zeux/pugixml/archive/%pugixml_commit/pugixml-%pugixml_commit.tar.gz
Source3: pugixml-%pugixml_commit.tar
# https://github.com/RPCS3/hidapi/archive/%hidapi_commit/hidapi-%hidapi_commit.tar.gz
Source4: hidapi-%hidapi_commit.tar
# https://github.com/RPCS3/yaml-cpp/archive/%yaml_cpp_commit/yaml-cpp-%yaml_cpp_commit.tar.gz
Source5: yaml-cpp-%yaml_cpp_commit.tar
# https://github.com/Cyan4973/xxHash/archive/v%xx_hash_version/xxHash-%xx_hash_version.tar.gz
Source6: xxHash-%xx_hash_version.tar
# https://github.com/RPCS3/llvm-mirror/archive/%llvm_commit/llvm-mirror-%llvm_commit.tar.gz
Source7: llvm-mirror-%llvm_commit.tar
# https://github.com/RPCS3/cereal/archive/%cereal_commit/cereal-%cereal_commit.tar.gz
Source8: cereal-%cereal_commit.tar
# https://github.com/FNA-XNA/FAudio/archive/%faudio_commit/FAudio-%faudio_commit.tar.gz
Source9: FAudio-%faudio_commit.tar
# https://github.com/tcbrindle/span/archive/%span_commit/span-%span_commit.tar.gz
Source10: span-%span_commit.tar
# https://github.com/KhronosGroup/SPIRV-Headers/archive/%spirv_headers_version/SPIRV-Headers-%spirv_headers_version.tar.gz
Source11: SPIRV-Headers-%spirv_headers_version.tar
# https://github.com/KhronosGroup/SPIRV-Tools/archive/v%spirv_tools_version/SPIRV-Tools-%spirv_tools_version.tar.gz
Source12: SPIRV-Tools-%spirv_tools_version.tar
# https://github.com/RipleyTom/wolfssl/archive/%wolfssl_commit/wolfssl-%wolfssl_commit.tar.gz
Source13: wolfssl-%wolfssl_commit.tar

Patch0: %name-alt-git.patch
Patch1: %name-alt-qt5.patch
Patch2: %name-alt-string.patch

BuildRequires: cmake >= 3.14.1
BuildRequires: cvs
BuildRequires: git-core
BuildRequires: libGLEW-devel
BuildRequires: libSDL2-devel
BuildRequires: libalsa-devel
BuildRequires: libavformat-devel
BuildRequires: libcurl-devel
BuildRequires: libevdev-devel
BuildRequires: libfaudio-devel
BuildRequires: libffi-devel
BuildRequires: libflatbuffers-devel
BuildRequires: libopenal-devel
BuildRequires: libpng-devel
BuildRequires: libpulseaudio-devel
BuildRequires: libswscale-devel
BuildRequires: libudev-devel
BuildRequires: libusb-devel
BuildRequires: libwayland-cursor-devel
BuildRequires: libwayland-egl-devel
BuildRequires: libwayland-server-devel
BuildRequires: libxml2-devel
BuildRequires: ocaml-ctypes
BuildRequires: ocaml-findlib
BuildRequires: python3-dev
BuildRequires: python3-module-yaml
BuildRequires: qt5-base-devel >= 5.15.1
BuildRequires: subversion

BuildPreReq: libswresample-devel

%description
The world's first free and open-source PlayStation 3 emulator/debugger, written in C++ for Windows and Linux.

%prep
%setup -b 1 -b 2 -b 3 -b 4 -b 5 -b 6 -b 7 -b 8 -b 9 -b 10 -b 11 -b 12 -b 13

%patch0 -p1
%patch1 -p1
%patch2 -p1

%__mv -Tf ../glslang-%glslang_commit Vulkan/glslang
%__mv -Tf ../asmjit-%asmjit_commit asmjit
%__mv -Tf ../pugixml-%pugixml_commit 3rdparty/pugixml
%__mv -Tf ../hidapi-%hidapi_commit 3rdparty/hidapi
%__mv -Tf ../yaml-cpp-%yaml_cpp_commit 3rdparty/yaml-cpp
%__mv -Tf ../xxHash-%xx_hash_version 3rdparty/xxHash
%__mv -Tf ../llvm-mirror-%llvm_commit llvm
%__mv -Tf ../cereal-%cereal_commit 3rdparty/cereal
%__mv -Tf ../FAudio-%faudio_commit 3rdparty/FAudio
%__mv -Tf ../span-%span_commit 3rdparty/span
%__mv -Tf ../SPIRV-Headers-%spirv_headers_version Vulkan/spirv-headers
%__mv -Tf ../SPIRV-Tools-%spirv_tools_version Vulkan/spirv-tools
%__mv -Tf ../wolfssl-%wolfssl_commit 3rdparty/wolfssl

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
%__mkdir_p %_target_platform
pushd %_target_platform

cmake .. \
	-DCMAKE_INSTALL_PREFIX:PATH=%prefix \
	-DCMAKE_C_FLAGS:STRING='%optflags' \
	-DCMAKE_CXX_FLAGS:STRING='%optflags' \
	-DCMAKE_BUILD_TYPE:STRING=Release \
	-DCMAKE_SKIP_RPATH:BOOL=TRUE \
	-DUSE_NATIVE_INSTRUCTIONS:BOOL=FALSE \
	-DUSE_SYSTEM_FFMPEG:BOOL=TRUE \
	-DUSE_SYSTEM_LIBPNG:BOOL=TRUE \
	-DUSE_SYSTEM_CURL:BOOL=TRUE \
	-DUSE_SYS_LIBUSB:BOOL=TRUE \
	-DPython3_EXECUTABLE="%__python3" \
	-Wno-dev
popd

%make_build -C %_target_platform

%install
%makeinstall_std -C %_target_platform

%files
%doc LICENSE README.md
%_bindir/%name
%_desktopdir/%name.desktop
%_liconsdir/%name.png
%_iconsdir/hicolor/scalable/apps/%name.svg
%_datadir/%name
%_datadir/metainfo/%name.appdata.xml

%changelog
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


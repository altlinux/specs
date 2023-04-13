# git describe upstream/yuzu
%define git_descr mainline-636-9297-g03545261806

%define inih_version r52
%define cpp_httplib_commit 305a7abcb9b4e9e349843c6d563212e6c1bbbf21
%define cubeb_commit 75d9d125ee655ef80f3bfcd97ae5a805931042b8
%define dynarmic_version 6.2.3
%define sirit_commit aa292d56650bc28f2b2d75973fab2e61d0136f9c
%define mbedtls_commit 8c88150ca139e06aa2aae8349df8292a88148ea1
%define xbyak_version 5.96
%define vulkan_headers_version 1.3.213
%define enet_commit 39a72ab1990014eb399cee9d538fd529df99c6a0
%define cpp_jwt_commit e12ef06218596b52d9b5d6e1639484866a8e7067
%define sanitizers_cmake_commit aab6948fa863bc1cbe5d0850bc46b9ef02ed4c1a
%define spirv_headers_commit a3fdfe81465d57efc97cfd28ac6c8190fb31a6c8

Name: yuzu
Version: 1139
Release: alt1.1

Summary: Nintendo Switch emulator/debugger
License: GPLv2
Group: Emulators

Url: https://%name-emu.org/
Packager: Nazarov Denis <nenderus@altlinux.org>

ExclusiveArch: x86_64

# https://github.com/%name-emu/%name-mainline/archive/mainline-0-%version/%name-mainline-mainline-0-%version.tar.gz
Source0: %name-mainline-mainline-0-%version.tar
# https://github.com/benhoyt/inih/archive/r52/inih-%inih_version.tar.gz
Source1: inih-%inih_version.tar
# https://github.com/yhirose/cpp-httplib/archive/%cpp_httplib_commit/cpp-httplib-%cpp_httplib_commit.tar.gz
Source2: cpp-httplib-%cpp_httplib_commit.tar
# https://github.com/mozilla/cubeb/archive/%cubeb_commit/cubeb-%cubeb_commit.tar.gz
Source3: cubeb-%cubeb_commit.tar
# https://github.com/merryhime/dynarmic/archive/%dynarmic_version/dynarmic-%dynarmic_version.tar.gz
Source4: dynarmic-%dynarmic_version.tar
# https://github.com/ReinUsesLisp/sirit/archive/%sirit_commit/sirit-%sirit_commit.tar.gz
Source5: sirit-%sirit_commit.tar
# https://github.com/yuzu-emu/mbedtls/archive/%mbedtls_commit/mbedtls-%mbedtls_commit.tar.gz
Source6: mbedtls-%mbedtls_commit.tar
# https://github.com/herumi/xbyak/archive/v%xbyak_version/xbyak-%xbyak_version.tar.gz
Source7: xbyak-%xbyak_version.tar
# https://github.com/KhronosGroup/Vulkan-Headers/archive/v%vulkan_headers_version/Vulkan-Headers-%vulkan_headers_version.tar.gz
Source8: Vulkan-Headers-%vulkan_headers_version.tar
# https://github.com/lsalzman/enet/archive/%enet_commit/enet-%enet_commit.tar.gz
Source9: enet-%enet_commit.tar 
# https://github.com/arun11299/cpp-jwt/archive/%cpp_jwt_commit/cpp-jwt-%cpp_jwt_commit.tar.gz
Source10: cpp-jwt-%cpp_jwt_commit.tar
# https://github.com/arsenm/sanitizers-cmake/archive/%sanitizers_cmake_commit/sanitizers-cmake-%sanitizers_cmake_commit.tar.gz
Source11: sanitizers-cmake-%sanitizers_cmake_commit.tar
# https://github.com/KhronosGroup/SPIRV-Headers/archive/%spirv_headers_commit/SPIRV-Headers-%spirv_headers_commit.tar.gz
Source12: SPIRV-Headers-%spirv_headers_commit.tar

Patch0: %name-zstd.patch

BuildRequires: boost-asio-devel
BuildRequires: boost-context-devel
BuildRequires: boost-filesystem-devel
BuildRequires: catch2-devel
BuildRequires: clang-tools
BuildRequires: cmake
BuildRequires: doxygen
BuildRequires: glslang
BuildRequires: graphviz
BuildRequires: libSDL2-devel
BuildRequires: libalsa-devel
BuildRequires: libavcodec-devel
BuildRequires: libfmt-devel
BuildRequires: libjack-devel
BuildRequires: liblz4-devel
BuildRequires: libopus-devel
BuildRequires: libspeexdsp-devel
BuildRequires: libswscale-devel
BuildRequires: libusb-devel
BuildRequires: libzstd-devel
BuildRequires: ninja-build
BuildRequires: nlohmann-json-devel
BuildRequires: python-modules-encodings
BuildRequires: python3-dev
BuildRequires: python3-module-mpl_toolkits
BuildRequires: qt5-multimedia-devel
BuildRequires: qt5-tools-devel
BuildRequires: zlib-devel

%description
%name is an open source Nintendo Switch emulator/debugger.

%prep
%setup -n %name-mainline-mainline-0-%version -b 1 -b 2 -b 3 -b 4 -b 5 -b 6 -b 7 -b 8 -b 9 -b 10 -b 11 -b 12

%patch0 -p1

%__mv -Tf ../inih-%inih_version externals/inih/inih
%__mv -Tf ../cpp-httplib-%cpp_httplib_commit externals/cpp-httplib
%__mv -Tf ../cubeb-%cubeb_commit externals/cubeb
%__mv -Tf ../dynarmic-%dynarmic_version externals/dynarmic
%__mv -Tf ../sirit-%sirit_commit externals/sirit
%__mv -Tf ../mbedtls-%mbedtls_commit externals/mbedtls
%__mv -Tf ../xbyak-%xbyak_version externals/xbyak
%__mv -Tf ../Vulkan-Headers-%vulkan_headers_version externals/Vulkan-Headers
%__mv -Tf ../enet-%enet_commit externals/enet
%__mv -Tf ../cpp-jwt-%cpp_jwt_commit externals/cpp-jwt
%__mv -Tf ../sanitizers-cmake-%sanitizers_cmake_commit externals/cubeb/cmake/sanitizers-cmake
%__mv -Tf ../SPIRV-Headers-%spirv_headers_commit externals/sirit/externals/SPIRV-Headers

# Enforce package versioning in GUI
sed -i \
-e 's|@GIT_BRANCH@|HEAD|g' \
-e 's|@GIT_DESC@|%git_descr|g' \
-e 's|@TITLE_BAR_FORMAT_IDLE@|%name %version|g' \
-e 's|@TITLE_BAR_FORMAT_RUNNING@|%name %version|g' \
src/common/scm_rev.cpp.in

%__rm .gitmodules

%build
%add_optflags -I%_includedir/libzip
%cmake \
	-DENABLE_QT_TRANSLATION:BOOL=TRUE \
	-DYUZU_USE_EXTERNAL_SDL2:BOOL=FALSE \
	-DYUZU_USE_BUNDLED_OPUS:BOOL=FALSE \
	-GNinja \
	-Wno-dev
%cmake_build

%install
%cmake_install

%__rm -rf %buildroot%_libdir
%__rm -rf %buildroot%_includedir
%__rm -rf %buildroot%_datadir/cmake

%files
%doc CONTRIBUTING.md README.md
%_bindir/%name
%_bindir/%name-cmd
%_bindir/%name-room
%_desktopdir/org.%{name}_emu.%name.desktop
%_datadir/metainfo/org.%{name}_emu.%name.metainfo.xml
%_datadir/mime/packages/org.%{name}_emu.%name.xml
%_iconsdir/hicolor/scalable/apps/org.%{name}_emu.%name.svg

%changelog
* Thu Apr 13 2023 Nazarov Denis <nenderus@altlinux.org> 1139-alt1.1
- Add zstd patch

* Sun Aug 21 2022 Nazarov Denis <nenderus@altlinux.org> 1139-alt1
- Version 1139

* Thu Jun 02 2022 Nazarov Denis <nenderus@altlinux.org> 1040-alt1
- Version 1040

* Mon Jan 10 2022 Nazarov Denis <nenderus@altlinux.org> 875-alt1
- Version 875

* Wed Jan 05 2022 Nazarov Denis <nenderus@altlinux.org> 869-alt1
- Version 869

* Tue Jan 04 2022 Nazarov Denis <nenderus@altlinux.org> 868-alt1
- Version 868

* Sat Nov 06 2021 Nazarov Denis <nenderus@altlinux.org> 801-alt1
- Version 801

* Sat Nov 06 2021 Nazarov Denis <nenderus@altlinux.org> 800-alt1
- Version 800

* Mon May 31 2021 Arseny Maslennikov <arseny@altlinux.org> 620-alt1.1
- NMU: spec: adapted to new cmake macros.

* Thu May 13 2021 Nazarov Denis <nenderus@altlinux.org> 620-alt1
- Version 620

* Fri Mar 19 2021 Nazarov Denis <nenderus@altlinux.org> 567-alt1
- Version 567

* Thu Mar 11 2021 Nazarov Denis <nenderus@altlinux.org> 0.559-alt3
- Enable translations

* Thu Mar 11 2021 Nazarov Denis <nenderus@altlinux.org> 0.559-alt2
- Enforce package versioning in GUI

* Wed Mar 10 2021 Nazarov Denis <nenderus@altlinux.org> 0.559-alt1
- Initial build for ALT Linux

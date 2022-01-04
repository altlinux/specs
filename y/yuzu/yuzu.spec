# git describe upstream/yuzu
%define git_descr mainline-636-7964-ga7a5be17612

%define inih_version r52
%define cpp_httplib_commit 9648f950f5a8a41d18833cf4a85f5821b1bcac54
%define cubeb_commit 75d9d125ee655ef80f3bfcd97ae5a805931042b8
%define dynarmic_commit 28714ee75aa079cbb706e38bdabc8ee1f6c69515
%define soundtouch_commit 060181eaf273180d3a7e87349895bd0cb6ccbf4a
%define libressl_commit 8289d0d07de6553bf4b900bf60e808ea3f7f59da
%define discord_rpc_commit 963aa9f3e5ce81a4682c6ca3d136cddda614db33
%define vulkan_headers_version 1.2.202
%define sirit_commit a39596358a3a5488c06554c0c15184a6af71e433
%define mbedtls_commit 8c88150ca139e06aa2aae8349df8292a88148ea1
%define xbyak_version 5.96
%define opus_commit ad8fe90db79b7d2a135e3dfd2ed6631b0c5662ab
%define sanitizers_cmake_commit aab6948fa863bc1cbe5d0850bc46b9ef02ed4c1a
%define spirv_headers_commit a3fdfe81465d57efc97cfd28ac6c8190fb31a6c8

Name: yuzu
Version: 868
Release: alt1

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
# https://github.com/merryhime/dynarmic/archive/%dynarmic_commit/dynarmic-%dynarmic_commit.tar.gz
Source4: dynarmic-%dynarmic_commit.tar
# https://github.com/citra-emu/ext-soundtouch/archive/%soundtouch_commit/ext-soundtouch-%soundtouch_commit.tar.gz
Source5: ext-soundtouch-%soundtouch_commit.tar
# https://github.com/citra-emu/ext-libressl-portable/archive/%libressl_commit/ext-libressl-portable-%libressl_commit.tar.gz
Source6: ext-libressl-portable-%libressl_commit.tar
# https://github.com/discord/discord-rpc/archive/%discord_rpc_commit/discord-rpc-%discord_rpc_commit.tar.gz
Source7: discord-rpc-%discord_rpc_commit.tar
# https://github.com/KhronosGroup/Vulkan-Headers/archive/v%vulkan_headers_version/Vulkan-Headers-%vulkan_headers_version.tar.gz
Source8: Vulkan-Headers-%vulkan_headers_version.tar
# https://github.com/ReinUsesLisp/sirit/archive/%sirit_commit/sirit-%sirit_commit.tar.gz
Source9: sirit-%sirit_commit.tar
# https://github.com/yuzu-emu/mbedtls/archive/%mbedtls_commit/mbedtls-%mbedtls_commit.tar.gz
Source10: mbedtls-%mbedtls_commit.tar
# https://github.com/herumi/xbyak/archive/v%xbyak_version/xbyak-%xbyak_version.tar.gz
Source11: xbyak-%xbyak_version.tar
# https://github.com/xiph/opus/archive/%opus_commit/opus-%opus_commit.tar.gz
Source12: opus-%opus_commit.tar
# https://github.com/arsenm/sanitizers-cmake/archive/%sanitizers_cmake_commit/sanitizers-cmake-%sanitizers_cmake_commit.tar.gz
Source13: sanitizers-cmake-%sanitizers_cmake_commit.tar
# https://github.com/KhronosGroup/SPIRV-Headers/archive/%spirv_headers_commit/SPIRV-Headers-%spirv_headers_commit.tar.gz
Source14: SPIRV-Headers-%spirv_headers_commit.tar

BuildRequires(pre): libffi-devel
BuildRequires(pre): libspeexdsp-devel
BuildRequires(pre): libwayland-cursor-devel
BuildRequires(pre): libwayland-egl-devel

BuildRequires: boost-asio-devel
BuildRequires: boost-context-devel
BuildRequires: catch2-devel
BuildRequires: cmake
BuildRequires: doxygen
BuildRequires: glslang
BuildRequires: libSDL2-devel
BuildRequires: libXext-devel
BuildRequires: libalsa-devel
BuildRequires: libavcodec-devel
BuildRequires: libdrm-devel
BuildRequires: libesd-devel
BuildRequires: libfmt-devel
BuildRequires: libgbm-devel
BuildRequires: libjack-devel
BuildRequires: liblz4-devel
BuildRequires: libopus-devel
BuildRequires: libpulseaudio-devel
BuildRequires: libswscale-devel
BuildRequires: libusb-devel
BuildRequires: libzip-devel
BuildRequires: libzip-utils
BuildRequires: libzstd-devel
BuildRequires: llvm-common-clang-tools
BuildRequires: ninja-build
BuildRequires: nlohmann-json-devel
BuildRequires: pipewire-libs-devel
BuildRequires: python-modules-encodings
BuildRequires: python3-dev
BuildRequires: python3-module-mpl_toolkits
BuildRequires: qt5-tools-devel
BuildRequires: zlib-devel

%description
%name is an open source Nintendo Switch emulator/debugger.

%prep
%setup -n %name-mainline-mainline-0-%version -b 1 -b 2 -b 3 -b 4 -b 5 -b 6 -b 7 -b 8 -b 9 -b 10 -b 11 -b 12 -b 13 -b 14

%__mv -Tf ../inih-%inih_version externals/inih/inih
%__mv -Tf ../cpp-httplib-%cpp_httplib_commit externals/cpp-httplib
%__mv -Tf ../cubeb-%cubeb_commit externals/cubeb
%__mv -Tf ../dynarmic-%dynarmic_commit externals/dynarmic
%__mv -Tf ../ext-soundtouch-%soundtouch_commit externals/soundtouch
%__mv -Tf ../ext-libressl-portable-%libressl_commit externals/libressl
%__mv -Tf ../discord-rpc-%discord_rpc_commit externals/discord-rpc
%__mv -Tf ../Vulkan-Headers-%vulkan_headers_version externals/Vulkan-Headers
%__mv -Tf ../sirit-%sirit_commit externals/sirit
%__mv -Tf ../mbedtls-%mbedtls_commit externals/mbedtls
%__mv -Tf ../xbyak-%xbyak_version externals/xbyak
%__mv -Tf ../opus-%opus_commit externals/opus/opus
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
	-GNinja \
	-Wno-dev
%cmake_build

%install
%cmake_install

%files
%doc CONTRIBUTING.md README.md
%_bindir/%name
%_bindir/%name-cmd
%_desktopdir/%name.desktop
%_datadir/mime/packages/%name.xml
%_iconsdir/hicolor/scalable/apps/%name.svg

%changelog
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

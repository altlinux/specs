# git describe upstream/yuzu
%define git_descr mainline-636-7326-ga123fd92b03

Name: yuzu
Version: 801
Release: alt1

Summary: Nintendo Switch emulator/debugger
License: GPLv2
Group: Emulators

Url: https://%name-emu.org/
Packager: Nazarov Denis <nenderus@altlinux.org>

ExclusiveArch: x86_64

# https://github.com/yuzu-emu/yuzu-mainline.git
Source0: %name-%version.tar
# https://github.com/benhoyt/inih.git
Source1: inih.tar
# https://github.com/kinetiknz/cpp-httplib.git
Source2: cpp-httplib.tar
# https://github.com/kinetiknz/cubeb.git
Source3: cubeb.tar
# https://github.com/MerryMage/dynarmic.git
Source4: dynarmic.tar
# https://github.com/citra-emu/ext-soundtouch.git
Source5: soundtouch.tar
# https://github.com/citra-emu/ext-libressl-portable.git
Source6: libressl.tar
# https://github.com/libusb/libusb.git
Source7: libusb.tar
# https://github.com/discordapp/discord-rpc.git
Source8: discord-rpc.tar
# https://github.com/KhronosGroup/Vulkan-Headers.git
Source9: Vulkan-Headers.tar
# https://github.com/ReinUsesLisp/sirit.git
Source10: sirit.tar
# https://github.com/yuzu-emu/mbedtls.git
Source11: mbedtls.tar
# https://github.com/herumi/xbyak.git
Source12: xbyak.tar
# https://github.com/xiph/opus.git
Source13: opus.tar
# https://git.ffmpeg.org/ffmpeg.git
Source14: ffmpeg.tar
# https://github.com/libsdl-org/SDL.git
Source15: SDL.tar
# https://github.com/arsenm/sanitizers-cmake.git
Source16: sanitizers-cmake.tar
# https://github.com/KhronosGroup/SPIRV-Headers.git
Source17: SPIRV-Headers.tar

BuildRequires(pre): libffi-devel
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

BuildPreReq: libwayland-cursor-devel

%description
%name is an open source Nintendo Switch emulator/debugger.

%prep
%setup -b 1 -b 2 -b 3 -b 4 -b 5 -b 6 -b 7 -b 8 -b 9 -b 10 -b 11 -b 12 -b 13 -b 14 -b 15 -b 16 -b 17

%__mv -Tf ../inih externals/inih/inih
%__mv -Tf ../cpp-httplib externals/cpp-httplib
%__mv -Tf ../cubeb externals/cubeb
%__mv -Tf ../dynarmic externals/dynarmic
%__mv -Tf ../soundtouch externals/soundtouch
%__mv -Tf ../libressl externals/libressl
%__mv -Tf ../libusb externals/libusb/libusb
%__mv -Tf ../discord-rpc externals/discord-rpc
%__mv -Tf ../Vulkan-Headers externals/Vulkan-Headers
%__mv -Tf ../sirit externals/sirit
%__mv -Tf ../mbedtls externals/mbedtls
%__mv -Tf ../xbyak externals/xbyak
%__mv -Tf ../opus externals/opus/opus
%__mv -Tf ../ffmpeg externals/ffmpeg
%__mv -Tf ../SDL externals/SDL
%__mv -Tf ../sanitizers-cmake externals/cubeb/cmake/sanitizers-cmake
%__mv -Tf ../SPIRV-Headers externals/sirit/externals/SPIRV-Headers

%__mkdir externals/inih/inih/.git
%__mkdir externals/cpp-httplib/.git
%__mkdir externals/cubeb/.git
%__mkdir externals/dynarmic/.git
%__mkdir externals/soundtouch/.git
%__mkdir externals/libressl/.git
%__mkdir externals/libusb/libusb/.git
%__mkdir externals/discord-rpc/.git
%__mkdir externals/Vulkan-Headers/.git
%__mkdir externals/sirit/.git
%__mkdir externals/mbedtls/.git
%__mkdir externals/xbyak/.git
%__mkdir externals/opus/opus/.git
%__mkdir externals/ffmpeg/.git
%__mkdir externals/SDL/.git

# Enforce package versioning in GUI
sed -i \
-e 's|@GIT_BRANCH@|HEAD|g' \
-e 's|@GIT_DESC@|%git_descr|g' \
-e 's|@TITLE_BAR_FORMAT_IDLE@|%name %version|g' \
-e 's|@TITLE_BAR_FORMAT_RUNNING@|%name %version|g' \
src/common/scm_rev.cpp.in

%build
%add_optflags -I%_includedir/libzip
%cmake \
	-DENABLE_QT_TRANSLATION:BOOL=ON \
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

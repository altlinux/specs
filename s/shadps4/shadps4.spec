%define sirit_commit 282083a595dcca86814dedab2f2b0363ef38f1ec
%define tracy_commit 143a53d1985b8e52a7590a0daca30a0a7c653b42
%define zydis_commit 120e0e705f8e3b507dc49377ac2879979f0d545c
%define dear_imgui_commit f4d9359095eff3eb03f685921edc1cf0e37b1687
%define discord_rpc_commit 19f66e6dcabb2268965f453db9e5774ede43238f
%define libatrac9_commit ec8899dadf393f655f2871a94e0fe4b3d6220c9a
%define libusb_commit c4d237a5803900b78dcc2961d057fcc8a678d3fd
%define hwinfo_commit 351c59828a79958f74f3ccab5e7773ffd724f6f7
%define sdl3_commit 4e2fd57e77fb4a28c0eeef0670fc4121cc2cf1f9
%define sdl3_mixer_commit 4182794ea45fe28568728670c6f1583855d0e85c
%define miniz_version 3.1.0
%define aac_commit ee76460efbdb147e26d804c798949c23f174460b

Name: shadps4
Version: 0.15.0
Release: alt1

Summary: Sony PlayStation 4 emulator
License: GPL-2.0
Group: Emulators

Url: http://%name.net/
Vcs: https://github.com/%name-emu/shadPS4
Packager: Nazarov Denis <nenderus@altlinux.org>

ExclusiveArch: x86_64

# https://github.com/%name-emu/shadPS4/archive/%version/shadPS4-v.%version.tar.gz
Source0: shadPS4-v.%version.tar
# https://github.com/%name-emu/sirit/archive/%sirit_commit/sirit-%sirit_commit.tar.gz
Source1: sirit-%sirit_commit.tar
# https://github.com/%name-emu/tracy/archive/%tracy_commit/tracy-%tracy_commit.tar.gz
Source2: tracy-%tracy_commit.tar
# https://github.com/zyantific/zydis/archive/%zydis_commit/zydis-%zydis_commit.tar.gz
Source3: zydis-%zydis_commit.tar
# https://github.com/%name-emu/ext-imgui/archive/%dear_imgui_commit/ext-imgui-%dear_imgui_commit.tar.gz
Source4: ext-imgui-%dear_imgui_commit.tar
# https://github.com/%name-emu/ext-discord-rpc/archive/%discord_rpc_commit/ext-discord-rpc-%discord_rpc_commit.tar.gz
Source5: ext-discord-rpc-%discord_rpc_commit.tar
# https://github.com/%name-emu/ext-LibAtrac9/archive/%libatrac9_commit/ext-LibAtrac9-%libatrac9_commit.tar.gz
Source6: ext-LibAtrac9-%libatrac9_commit.tar
# https://github.com/%name-emu/ext-libusb/archive/%libusb_commit/ext-libusb-%libusb_commit.tar.gz
Source7: ext-libusb-%libusb_commit.tar
# https://github.com/%name-emu/ext-hwinfo/archive/%hwinfo_commit/ext-hwinfo-%hwinfo_commit.tar.gz
Source8: ext-hwinfo-%hwinfo_commit.tar
# https://github.com/shadexternals/sdl3/archive/%sdl3_commit/sdl3-%sdl3_commit.tar.gz
Source9: sdl3-%sdl3_commit.tar
# https://github.com/libsdl-org/SDL_mixer/archive/%sdl3_mixer_commit/SDL_mixer-%sdl3_mixer_commit.tar.gz
Source10: SDL_mixer-%sdl3_mixer_commit.tar
# https://github.com/richgel999/miniz/archive/%miniz_version/miniz-%miniz_version.tar.gz
Source11: miniz-%miniz_version.tar
# https://android.googlesource.com/platform/external/aac/+archive/ee76460efbdb147e26d804c798949c23f174460b.tar.gz
Source12: aac-%aac_commit.tar

Patch0: %name-0.11.0-glslang-16-alt.patch

BuildRequires: alt-os-release
BuildRequires: boost-asio-devel
BuildRequires: clang
BuildRequires: cli11-devel
BuildRequires: cmake
BuildRequires: glslang-devel
BuildRequires: libSDL3-devel
BuildRequires: libalsa-devel
BuildRequires: libavfilter-devel
BuildRequires: libavformat-devel
BuildRequires: libdecor-devel
BuildRequires: libdrm-devel
BuildRequires: libflac-devel
BuildRequires: libfluidsynth-devel
BuildRequires: libfmt-devel
BuildRequires: libfribidi-devel
BuildRequires: libgbm-devel
BuildRequires: libgme-devel
BuildRequires: libhalf-devel
BuildRequires: libmagic_enum-devel
BuildRequires: libmpg123-devel
BuildRequires: libopenal-devel
BuildRequires: libpng-devel
BuildRequires: libpugixml-devel
BuildRequires: libpulseaudio-devel
BuildRequires: libqt5-eglfskmssupport
BuildRequires: librobin-map-devel
BuildRequires: libslang2
BuildRequires: libsndio7-devel
BuildRequires: libspirv-tools-devel
BuildRequires: libssl-devel
BuildRequires: libstb-devel
BuildRequires: libstdc++-devel
BuildRequires: libswresample-devel
BuildRequires: libswscale-devel
BuildRequires: libthai-devel
BuildRequires: libtoml11-devel
BuildRequires: libudev-devel
BuildRequires: libusb-devel
BuildRequires: libuuid-devel
BuildRequires: libvorbis-devel
BuildRequires: libvulkan-memory-allocator-devel
BuildRequires: libwayland-cursor-devel
BuildRequires: libwayland-egl-devel
BuildRequires: libxbyak-devel
BuildRequires: libxkbcommon-devel
BuildRequires: libxmp-devel
BuildRequires: libxxhash-devel
BuildRequires: libzydis-devel
BuildRequires: lld
BuildRequires: llvm
BuildRequires: ninja-build
BuildRequires: nlohmann-json-devel
BuildRequires: pipewire-jack-libs-devel
BuildRequires: rapidjson-devel
BuildRequires: renderdoc-devel
BuildRequires: spirv-headers
BuildRequires: zlib-devel
BuildRequires: zlib-ng-devel

%description
shadPS4 is an early PlayStation 4 emulator for Windows, Linux and macOS written in C++

%prep
%setup -n shadPS4-v.%version -b 1 -b 2 -b 3 -b 4 -b 5 -b 6 -b 7 -b 8 -b 9 -b 10 -b 11 -b 12
%patch0 -p1

%__mv -Tf ../sirit-%sirit_commit externals/sirit
%__mv -Tf ../tracy-%tracy_commit externals/tracy
%__mv -Tf ../zydis-%zydis_commit externals/zydis
%__mv -Tf ../ext-imgui-%dear_imgui_commit externals/dear_imgui
%__mv -Tf ../ext-discord-rpc-%discord_rpc_commit externals/discord-rpc
%__mv -Tf ../ext-LibAtrac9-%libatrac9_commit externals/LibAtrac9
%__mv -Tf ../ext-libusb-%libusb_commit externals/ext-libusb
%__mv -Tf ../ext-hwinfo-%hwinfo_commit externals/hwinfo
%__mv -Tf ../sdl3-%sdl3_commit externals/sdl3
%__mv -Tf ../SDL_mixer-%sdl3_mixer_commit externals/sdl3_mixer
%__mv -Tf ../miniz-%miniz_version externals/miniz
%__mv -Tf ../aac-%aac_commit externals/aacdec/fdk-aac

%build
export CC="clang"
export CXX="clang++"
export RANLIB="llvm-ranlib"
export AR="llvm-ar"
export NM="llvm-nm"
export LDFLAGS="-fuse-ld=lld $LDFLAGS"

%cmake \
	-DCMAKE_BUILD_TYPE:STRING=RelWithDebInfo \
	-DENABLE_UPDATER:BOOL=FALSE \
	-DSIRIT_USE_SYSTEM_SPIRV_HEADERS:BOOL=TRUE \
	-GNinja \
	-Wno-dev
%cmake_build

%install
%cmake_install

%files
%doc CONTRIBUTING.md README.md
%_bindir/%name

%changelog
* Tue Mar 17 2026 Nazarov Denis <nenderus@altlinux.org> 0.15.0-alt1
- Version 0.15.0

* Sat Feb 07 2026 Nazarov Denis <nenderus@altlinux.org> 0.14.0-alt1
- Version 0.14.0

* Sat Jan 24 2026 Nazarov Denis <nenderus@altlinux.org> 0.13.0-alt1.1
- Fix FTBFS

* Wed Dec 24 2025 Nazarov Denis <nenderus@altlinux.org> 0.13.0-alt1
- Version 0.13.0

* Sat Nov 08 2025 Nazarov Denis <nenderus@altlinux.org> 0.12.5-alt1
- Version 0.12.5

* Fri Oct 31 2025 Nazarov Denis <nenderus@altlinux.org> 0.12.0-alt1
- Version 0.12.0

* Thu Oct 23 2025 Nazarov Denis <nenderus@altlinux.org> 0.11.0-alt1.2
- Fix build with Glslang 16

* Tue Sep 30 2025 Nazarov Denis <nenderus@altlinux.org> 0.11.0-alt1.1
- Fix build with fmt 12

* Thu Sep 18 2025 Nazarov Denis <nenderus@altlinux.org> 0.11.0-alt1
- Version 0.11.0

* Wed Aug 13 2025 Nazarov Denis <nenderus@altlinux.org> 0.10.0-alt3
- Build with system Vulkan headers

* Fri Jul 11 2025 Nazarov Denis <nenderus@altlinux.org> 0.10.0-alt2
- Build with system magic_enum

* Mon Jul 07 2025 Nazarov Denis <nenderus@altlinux.org> 0.10.0-alt1
- Version 0.10.0

* Sat May 24 2025 Nazarov Denis <nenderus@altlinux.org> 0.9.0-alt1
- Version 0.9.0

* Mon May 05 2025 Nazarov Denis <nenderus@altlinux.org> 0.8.0-alt2
- Add pach to restore PKG support

* Sat Apr 26 2025 Nazarov Denis <nenderus@altlinux.org> 0.8.0-alt1
- Version 0.8.0

* Wed Mar 26 2025 Nazarov Denis <nenderus@altlinux.org> 0.7.0-alt1
- Version 0.7.0

* Wed Feb 19 2025 Nazarov Denis <nenderus@altlinux.org> 0.6.0-alt1.1
- Fix FTBFS

* Tue Feb 04 2025 Nazarov Denis <nenderus@altlinux.org> 0.6.0-alt1
- Version 0.6.0

* Sun Jan 26 2025 Nazarov Denis <nenderus@altlinux.org> 0.5.0-alt2
- Build with system SDL3

* Sat Dec 28 2024 Nazarov Denis <nenderus@altlinux.org> 0.5.0-alt1
- Version 0.5.0

* Sun Dec 15 2024 Nazarov Denis <nenderus@altlinux.org> 0.4.0-alt2
- Build with Glslang 15 (ALT #52431)

* Sat Nov 02 2024 Nazarov Denis <nenderus@altlinux.org> 0.4.0-alt1
- Version 0.4.0

* Tue Sep 24 2024 Nazarov Denis <nenderus@altlinux.org> 0.3.0-alt1
- Version 0.3.0

* Fri Aug 23 2024 Nazarov Denis <nenderus@altlinux.org> 0.2.0-alt2
- Build only Qt version
- Pack desktop and icon files

* Fri Aug 16 2024 Nazarov Denis <nenderus@altlinux.org> 0.2.0-alt1
- Version 0.2.0

* Sat Jul 13 2024 Nazarov Denis <nenderus@altlinux.org> 0.1.0-alt2
- Improve Qt build

* Sat Jul 13 2024 Nazarov Denis <nenderus@altlinux.org> 0.1.0-alt1
- Initial build for ALT Linux

%define sirit_commit 282083a595dcca86814dedab2f2b0363ef38f1ec
%define tracy_commit 143a53d1985b8e52a7590a0daca30a0a7c653b42
%define zydis_commit 120e0e705f8e3b507dc49377ac2879979f0d545c
%define dear_imgui_commit f4d9359095eff3eb03f685921edc1cf0e37b1687
%define discord_rpc_commit 19f66e6dcabb2268965f453db9e5774ede43238f
%define vulkan_headers_version 1.4.329
%define libatrac9_commit ec8899dadf393f655f2871a94e0fe4b3d6220c9a
%define libusb_commit c4d237a5803900b78dcc2961d057fcc8a678d3fd
%define hwinfo_commit 351c59828a79958f74f3ccab5e7773ffd724f6f7
%define json_version 3.12.0

Name: shadps4
Version: 0.12.5
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
# https://github.com/KhronosGroup/Vulkan-Headers/archive/v%vulkan_headers_version/Vulkan-Headers-%vulkan_headers_version.tar.gz
Source6: Vulkan-Headers-%vulkan_headers_version.tar
# https://github.com/%name-emu/ext-LibAtrac9/archive/%libatrac9_commit/ext-LibAtrac9-%libatrac9_commit.tar.gz
Source7: ext-LibAtrac9-%libatrac9_commit.tar
# https://github.com/%name-emu/ext-libusb/archive/%libusb_commit/ext-libusb-%libusb_commit.tar.gz
Source8: ext-libusb-%libusb_commit.tar
# https://github.com/%name-emu/ext-hwinfo/archive/%hwinfo_commit/ext-hwinfo-%hwinfo_commit.tar.gz
Source9: ext-hwinfo-%hwinfo_commit.tar
# https://github.com/nlohmann/json/archive/v%json_version/json-%json_version.tar.gz
Source10: json-%json_version.tar

Patch0: %name-0.11.0-glslang-16-alt.patch

BuildRequires: alt-os-release
BuildRequires: boost-asio-devel
BuildRequires: clang
BuildRequires: cmake
BuildRequires: glslang-devel
BuildRequires: libSDL3-devel
BuildRequires: libavfilter-devel
BuildRequires: libavformat-devel
BuildRequires: libfmt-devel
BuildRequires: libhalf-devel
BuildRequires: libmagic_enum-devel
BuildRequires: libpng-devel
BuildRequires: libpugixml-devel
BuildRequires: librobin-map-devel
BuildRequires: libspirv-tools-devel
BuildRequires: libssl-devel
BuildRequires: libstb-devel
BuildRequires: libstdc++-devel
BuildRequires: libswresample-devel
BuildRequires: libswscale-devel
BuildRequires: libtoml11-devel
BuildRequires: libudev-devel
BuildRequires: libuuid-devel
BuildRequires: libvulkan-memory-allocator-devel
BuildRequires: libxbyak-devel
BuildRequires: libxxhash-devel
BuildRequires: libzydis-devel
BuildRequires: lld
BuildRequires: llvm
BuildRequires: ninja-build
BuildRequires: rapidjson-devel
BuildRequires: renderdoc-devel
BuildRequires: spirv-headers

%description
shadPS4 is an early PlayStation 4 emulator for Windows, Linux and macOS written in C++

%prep
%setup -n shadPS4-v.%version -b 1 -b 2 -b 3 -b 4 -b 5 -b 6 -b 7 -b 8 -b 9 -b 10
%patch0 -p1

%__mv -Tf ../sirit-%sirit_commit externals/sirit
%__mv -Tf ../tracy-%tracy_commit externals/tracy
%__mv -Tf ../zydis-%zydis_commit externals/zydis
%__mv -Tf ../ext-imgui-%dear_imgui_commit externals/dear_imgui
%__mv -Tf ../ext-discord-rpc-%discord_rpc_commit externals/discord-rpc
%__mv -Tf ../Vulkan-Headers-%vulkan_headers_version externals/vulkan-headers
%__mv -Tf ../ext-LibAtrac9-%libatrac9_commit externals/LibAtrac9
%__mv -Tf ../ext-libusb-%libusb_commit externals/ext-libusb
%__mv -Tf ../ext-hwinfo-%hwinfo_commit externals/hwinfo
%__mv -Tf ../json-%json_version externals/json

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

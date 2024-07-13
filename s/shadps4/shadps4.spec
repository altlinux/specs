%define discord_rpc_commit 4ec218155d73bcb8022f8f7ca72305d801f84beb
%define cryptopp_cmake_commit 2c384c28265a93358a2455e610e76393358794df
%define sdl3_commit b72c22340e9a3c680011e245c28492bf60f5be66
%define vulkan_headers_version 1.3.289
%define vma_commit feb11e172715011ef2a7b3b6c7c8737337b34181
%define robin_map_commit 1115dad3ffa0994e3f43b693d9b9cc99944c64c1
%define xbyak_version 7.07
%define magic_enum_commit dd6a39d0ba1852cf06907e0f0573a2a10d23c2ad
%define toml11_commit b389bbc4ebf90fa2fe7651de3046fb19f661ba3c
%define sirit_commit 505cc66a2be70b268c1700fef4d5327a5fe46494
%define tracy_commit c6d779d78508514102fbe1b8eb28bda10d95bb2a
%define cryptopp_commit 60f81a77e0c9a0e7ffc1ca1bc438ddfa2e43b78e

Name: shadps4
Version: 0.1.0
Release: alt1

Summary: Sony PlayStation 4 emulator
License: GPL-2.0
Group: Emulators

Url: http://%name.net/
Packager: Nazarov Denis <nenderus@altlinux.org>

ExclusiveArch: x86_64

# https://github.com/%name-emu/shadPS4/archive/%version/shadPS4-%version.tar.gz
Source0: shadPS4-%version.tar
# https://github.com/shadps4-emu/ext-discord-rpc/archive/%discord_rpc_commit/ext-discord-rpc-%discord_rpc_commit.tar.gz
Source1: ext-discord-rpc-%discord_rpc_commit.tar
# https://github.com/shadps4-emu/ext-cryptopp-cmake/archive/%cryptopp_cmake_commit/ext-cryptopp-cmake-%cryptopp_cmake_commit.tar.gz
Source2: ext-cryptopp-cmake-%cryptopp_cmake_commit.tar
# https://github.com/shadps4-emu/ext-SDL/archive/%sdl3_commit/ext-SDL-%sdl3_commit.tar.gz
Source3: ext-SDL-%sdl3_commit.tar
# https://github.com/KhronosGroup/Vulkan-Headers/archive/v%vulkan_headers_version/Vulkan-Headers-%vulkan_headers_version.tar.gz
Source4: Vulkan-Headers-%vulkan_headers_version.tar
# https://github.com/GPUOpen-LibrariesAndSDKs/VulkanMemoryAllocator/archive/%vma_commit/VulkanMemoryAllocator-%vma_commit.tar.gz
Source5: VulkanMemoryAllocator-%vma_commit.tar
# https://github.com/Tessil/robin-map/archive/%robin_map_commit/robin-map-%robin_map_commit.tar.gz
Source6: robin-map-%robin_map_commit.tar
# https://github.com/herumi/xbyak/archive/v%xbyak_version/xbyak-%xbyak_version.tar.gz
Source7: xbyak-%xbyak_version.tar
# https://github.com/Neargye/magic_enum/archive/%magic_enum_commit/magic_enum-%magic_enum_commit.tar.gz
Source8: magic_enum-%magic_enum_commit.tar
# https://github.com/ToruNiina/toml11/archive/%toml11_commit/toml11-%toml11_commit.tar.gz
Source9: toml11-%toml11_commit.tar
# https://github.com/shadps4-emu/sirit/archive/%sirit_commit/sirit-%sirit_commit.tar.gz
Source10: sirit-%sirit_commit.tar
# https://github.com/shadps4-emu/tracy/archive/%tracy_commit/tracy-%tracy_commit.tar.gz
Source11: tracy-%tracy_commit.tar
# https://github.com/shadps4-emu/ext-cryptopp/archive/%cryptopp_commit/ext-cryptopp-%cryptopp_commit.tar.gz
Source12: ext-cryptopp-%cryptopp_commit.tar

BuildRequires: boost-devel
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: glslang-devel
BuildRequires: libXext-devel
BuildRequires: libalsa-devel
BuildRequires: libfmt-devel
BuildRequires: libglvnd-devel
BuildRequires: libspirv-tools-devel
BuildRequires: libssl-devel
BuildRequires: libvulkan-memory-allocator-devel
BuildRequires: libxbyak-devel
BuildRequires: libxkbcommon-devel
BuildRequires: libxxhash-devel
BuildRequires: libzydis-devel
BuildRequires: python3
BuildRequires: spirv-headers
BuildRequires: zlib-ng-devel

%description
shadPS4 is an early PS4 emulator for Windows and Linux written in C++

%package cli
Summary: Sony PlayStation 4 emulator - CLI version
Group: Emulators

%description cli
shadPS4 is an early PS4 emulator for Windows and Linux written in C++

This package contains a command line interface.

%package qt
Summary: Sony PlayStation 4 emulator - Qt version
Group: Emulators

%description qt
shadPS4 is an early PS4 emulator for Windows and Linux written in C++

This package contains a graphical user interface using Qt6.

%prep
%setup -n shadPS4-%version -b 1 -b 2 -b 3 -b 4 -b 5 -b 6 -b 7 -b 8 -b 9 -b 10 -b 11 -b 12
%__mv -Tf ../ext-discord-rpc-%discord_rpc_commit externals/discord-rpc
%__mv -Tf ../ext-cryptopp-cmake-%cryptopp_cmake_commit externals/cryptopp-cmake
%__mv -Tf ../ext-SDL-%sdl3_commit externals/sdl3
%__mv -Tf ../Vulkan-Headers-%vulkan_headers_version externals/vulkan-headers
%__mv -Tf ../VulkanMemoryAllocator-%vma_commit externals/vma
%__mv -Tf ../robin-map-%robin_map_commit externals/robin-map
%__mv -Tf ../xbyak-%xbyak_version externals/xbyak
%__mv -Tf ../magic_enum-%magic_enum_commit externals/magic_enum
%__mv -Tf ../toml11-%toml11_commit externals/toml11
%__mv -Tf ../sirit-%sirit_commit externals/sirit
%__mv -Tf ../tracy-%tracy_commit externals/tracy
%__mv -Tf ../ext-cryptopp-%cryptopp_commit externals/cryptopp

%build
%add_optflags -Wno-error=return-type

# Build CLI version
%define _cmake__builddir %_target_platform
%cmake -DSIRIT_USE_SYSTEM_SPIRV_HEADERS:BOOL=TRUE
%cmake_build

# Build Qt version
%define _cmake__builddir %_target_platform-qt
%cmake -DSIRIT_USE_SYSTEM_SPIRV_HEADERS:BOOL=TRUE
%cmake_build

%install
%__mkdir_p %buildroot%_bindir
%__install -Dp -m0755 %_target_platform/%name %buildroot%_bindir/
%__install -Dp -m0755 %_target_platform-qt/%name %buildroot%_bindir/%name-qt

%files cli
%_bindir/%name

%files qt
%_bindir/%name-qt

%changelog
* Sat Jul 13 2024 Nazarov Denis <nenderus@altlinux.org> 0.1.0-alt1
- Initial build for ALT Linux

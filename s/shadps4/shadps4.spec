%define discord_rpc_commit 4ec218155d73bcb8022f8f7ca72305d801f84beb
%define cryptopp_cmake_commit 2c384c28265a93358a2455e610e76393358794df
%define sdl3_commit 4cc3410dce50cefce98d3cf3cf1bc8eca83b862a
%define vulkan_headers_version 1.3.292
%define vma_commit 871913da6a4b132b567d7b65c509600363c0041e
%define robin_map_commit 1115dad3ffa0994e3f43b693d9b9cc99944c64c1
%define xbyak_version 7.07
%define magic_enum_commit dae6bbf16c363e9ead4e628a47fdb02956a634f3
%define toml11_commit fcb1d3d7e5885edfadbbe9572991dc4b3248af58
%define sirit_commit 8db09231c448b913ae905d5237ce2eca46e3fe87
%define tracy_commit b8061982cad0210b649541016c88ff5faa90733c
%define cryptopp_commit 60f81a77e0c9a0e7ffc1ca1bc438ddfa2e43b78e
%define zydis_commit 16c6a369c193981e9cf314126589eaa8763f92c3

Name: shadps4
Version: 0.2.0
Release: alt2

Summary: Sony PlayStation 4 emulator
License: GPL-2.0
Group: Emulators

Url: http://%name.net/
Packager: Nazarov Denis <nenderus@altlinux.org>

ExclusiveArch: x86_64

# https://github.com/%name-emu/shadPS4/archive/%version/shadPS4-v.%version.tar.gz
Source0: shadPS4-v.%version.tar
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
# https://github.com/zyantific/zydis/archive/%zydis_commit/zydis-%zydis_commit.tar.gz
Source13: zydis-%zydis_commit.tar

BuildRequires: boost-asio-devel
BuildRequires: cmake
BuildRequires: glslang-devel
BuildRequires: libXext-devel
BuildRequires: libalsa-devel
BuildRequires: libfmt-devel
BuildRequires: libspirv-tools-devel
BuildRequires: libvulkan-memory-allocator-devel
BuildRequires: libxbyak-devel
BuildRequires: libxxhash-devel
BuildRequires: libzycore-devel
BuildRequires: qt6-base-devel
BuildRequires: spirv-headers
BuildRequires: zlib-ng-devel

Provides: %name-qt = %EVR
Obsoletes: %name-qt <= 0.2.0-alt1

%description
shadPS4 is an early PS4 emulator for Windows and Linux written in C++

%prep
%setup -n shadPS4-v.%version -b 1 -b 2 -b 3 -b 4 -b 5 -b 6 -b 7 -b 8 -b 9 -b 10 -b 11 -b 12 -b 13
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
%__mv -Tf ../zydis-%zydis_commit externals/zydis

%build
%add_optflags -Wno-error=return-type

%cmake \
	-DENABLE_QT_GUI:BOOL=TRUE \
	-DSIRIT_USE_SYSTEM_SPIRV_HEADERS:BOOL=TRUE \
	-Wno-dev
%cmake_build

%install
%__mkdir_p %buildroot{%_bindir,%_desktopdir,%_iconsdir/hicolor/512x512/apps}

%__install -Dp -m0755 %_target_platform/%name %buildroot%_bindir/
%__install -Dp -m0644 .github/%name.desktop %buildroot%_desktopdir/
%__install -Dp -m0644 .github/%name.png %buildroot%_iconsdir/hicolor/512x512/apps/

%files
%doc README.md
%_bindir/%name
%_desktopdir/%name.desktop
%_iconsdir/hicolor/512x512/apps/%name.png

%changelog
* Fri Aug 23 2024 Nazarov Denis <nenderus@altlinux.org> 0.2.0-alt2
- Build only Qt version
- Pack desktop and icon files

* Fri Aug 16 2024 Nazarov Denis <nenderus@altlinux.org> 0.2.0-alt1
- Version 0.2.0

* Sat Jul 13 2024 Nazarov Denis <nenderus@altlinux.org> 0.1.0-alt2
- Improve Qt build

* Sat Jul 13 2024 Nazarov Denis <nenderus@altlinux.org> 0.1.0-alt1
- Initial build for ALT Linux

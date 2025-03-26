%define cryptopp_cmake_commit 2c384c28265a93358a2455e610e76393358794df
%define vma_commit 5a53a198945ba8260fbc58fadb788745ce6aa263
%define robin_map_commit fe845fd7852ef541c5479ae23b3d36b57f8608ee
%define magic_enum_commit 1a1824df7ac798177a521eed952720681b0bf482
%define sirit_commit 8b9b12c2089505ac8b10fa56bf56b3ed49d9d7b0
%define tracy_commit 143a53d1985b8e52a7590a0daca30a0a7c653b42
%define cryptopp_commit effed0d0b865afc23ed67e0916f83734e4b9b3b7
%define zydis_commit bffbb610cfea643b98e87658b9058382f7522807
%define dear_imgui_commit 636cd4a7d623a2bc9bf59bb3acbb4ca075befba3
%define discord_rpc_commit 51b09d426a4a1bcfa6ee6d4894e57d669f4a2e65
%define vulkan_headers_version 1.4.305
%define libatrac9_commit ec8899dadf393f655f2871a94e0fe4b3d6220c9a

Name: shadps4
Version: 0.7.0
Release: alt1

Summary: Sony PlayStation 4 emulator
License: GPL-2.0
Group: Emulators

Url: http://%name.net/
Packager: Nazarov Denis <nenderus@altlinux.org>

ExclusiveArch: x86_64

# https://github.com/%name-emu/shadPS4/archive/%version/shadPS4-v.%version.tar.gz
Source0: shadPS4-v.%version.tar
# https://github.com/shadps4-emu/ext-cryptopp-cmake/archive/%cryptopp_cmake_commit/ext-cryptopp-cmake-%cryptopp_cmake_commit.tar.gz
Source1: ext-cryptopp-cmake-%cryptopp_cmake_commit.tar
# https://github.com/GPUOpen-LibrariesAndSDKs/VulkanMemoryAllocator/archive/%vma_commit/VulkanMemoryAllocator-%vma_commit.tar.gz
Source2: VulkanMemoryAllocator-%vma_commit.tar
# https://github.com/Tessil/robin-map/archive/%robin_map_commit/robin-map-%robin_map_commit.tar.gz
Source3: robin-map-%robin_map_commit.tar
# https://github.com/Neargye/magic_enum/archive/%magic_enum_commit/magic_enum-%magic_enum_commit.tar.gz
Source4: magic_enum-%magic_enum_commit.tar
# https://github.com/shadps4-emu/sirit/archive/%sirit_commit/sirit-%sirit_commit.tar.gz
Source5: sirit-%sirit_commit.tar
# https://github.com/shadps4-emu/tracy/archive/%tracy_commit/tracy-%tracy_commit.tar.gz
Source6: tracy-%tracy_commit.tar
# https://github.com/shadps4-emu/ext-cryptopp/archive/%cryptopp_commit/ext-cryptopp-%cryptopp_commit.tar.gz
Source7: ext-cryptopp-%cryptopp_commit.tar
# https://github.com/zyantific/zydis/archive/%zydis_commit/zydis-%zydis_commit.tar.gz
Source8: zydis-%zydis_commit.tar
# https://github.com/shadps4-emu/ext-imgui/archive/%dear_imgui_commit/ext-imgui-%dear_imgui_commit.tar.gz
Source9: ext-imgui-%dear_imgui_commit.tar
# https://github.com/shadps4-emu/ext-discord-rpc/archive/%discord_rpc_commit/ext-discord-rpc-%discord_rpc_commit.tar.gz
Source10: ext-discord-rpc-%discord_rpc_commit.tar
# https://github.com/KhronosGroup/Vulkan-Headers/archive/v%vulkan_headers_version/Vulkan-Headers-%vulkan_headers_version.tar.gz
Source11: Vulkan-Headers-%vulkan_headers_version.tar
# https://github.com/shadps4-emu/ext-LibAtrac9/archive/%libatrac9_commit/ext-LibAtrac9-%libatrac9_commit.tar.gz
Source12: ext-LibAtrac9-%libatrac9_commit.tar

Patch0: %name-0.6.0-vulakn-headers.patch

BuildRequires: boost-asio-devel
BuildRequires: clang
BuildRequires: glslang-devel
BuildRequires: libGLU-devel
BuildRequires: libSDL3-devel
BuildRequires: libavfilter-devel
BuildRequires: libavformat-devel
BuildRequires: libfmt-devel
BuildRequires: libhalf-devel
BuildRequires: libpng-devel
BuildRequires: libpugixml-devel
BuildRequires: libspirv-tools-devel
BuildRequires: libstb-devel
BuildRequires: libswresample-devel
BuildRequires: libswscale-devel
BuildRequires: libtoml11-devel
BuildRequires: libvulkan-memory-allocator-devel
BuildRequires: libxbyak-devel
BuildRequires: libxxhash-devel
BuildRequires: libzydis-devel
BuildRequires: lld
BuildRequires: llvm
BuildRequires: qt6-multimedia-devel
BuildRequires: qt6-tools-devel
BuildRequires: rapidjson-devel
BuildRequires: renderdoc-devel
BuildRequires: spirv-headers

Provides: %name-qt = %EVR
Obsoletes: %name-qt <= 0.2.0-alt1

%description
shadPS4 is an early PS4 emulator for Windows and Linux written in C++

%prep
%setup -n shadPS4-v.%version -b 1 -b 2 -b 3 -b 4 -b 5 -b 6 -b 7 -b 8 -b 9 -b 10 -b 11 -b 12

%patch0 -p1

%__mv -Tf ../ext-cryptopp-cmake-%cryptopp_cmake_commit externals/cryptopp-cmake
%__mv -Tf ../VulkanMemoryAllocator-%vma_commit externals/vma
%__mv -Tf ../robin-map-%robin_map_commit externals/robin-map
%__mv -Tf ../magic_enum-%magic_enum_commit externals/magic_enum
%__mv -Tf ../sirit-%sirit_commit externals/sirit
%__mv -Tf ../tracy-%tracy_commit externals/tracy
%__mv -Tf ../ext-cryptopp-%cryptopp_commit externals/cryptopp
%__mv -Tf ../zydis-%zydis_commit externals/zydis
%__mv -Tf ../ext-imgui-%dear_imgui_commit externals/dear_imgui
%__mv -Tf ../ext-discord-rpc-%discord_rpc_commit externals/discord-rpc
%__mv -Tf ../Vulkan-Headers-%vulkan_headers_version externals/vulkan-headers
%__mv -Tf ../ext-LibAtrac9-%libatrac9_commit externals/LibAtrac9

%build
%add_optflags -Wno-error=return-type

export CC="clang"
export CXX="clang++"
export RANLIB="llvm-ranlib"
export AR="llvm-ar"
export NM="llvm-nm"
export LDFLAGS="-fuse-ld=lld $LDFLAGS"

%cmake \
	-DENABLE_QT_GUI:BOOL=TRUE \
	-DSIRIT_USE_SYSTEM_SPIRV_HEADERS:BOOL=TRUE \
	-GNinja \
	-Wno-dev
%cmake_build

%install
%cmake_install

%__mkdir_p %buildroot%_libexecdir/%name

%__mv %buildroot%_bindir/%name %buildroot%_libexecdir/%name/
%__ln_s %_libexecdir/%name/%name %buildroot%_bindir/%name
%__cp -r %_target_platform/translations %buildroot%_libexecdir/%name

%files
%doc CONTRIBUTING.md README.md
%_bindir/%name
%_datadir/metainfo/net.%name.shadPS4.metainfo.xml
%_desktopdir/net.%name.shadPS4.desktop
%_iconsdir/hicolor/512x512/apps/net.%name.shadPS4.png
%_iconsdir/hicolor/scalable/apps/net.%name.shadPS4.svg
%_libexecdir/%name

%changelog
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

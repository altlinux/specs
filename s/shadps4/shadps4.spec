%define cryptopp_cmake_commit 2c384c28265a93358a2455e610e76393358794df
%define sdl3_commit 3a1d76d298db023f6cf37fb08ee766f20a4e12ab
%define vma_commit 5a53a198945ba8260fbc58fadb788745ce6aa263
%define robin_map_commit fe845fd7852ef541c5479ae23b3d36b57f8608ee
%define magic_enum_commit 1a1824df7ac798177a521eed952720681b0bf482
%define sirit_commit 1e74f4ef8d2a0e3221a4de51977663f342b53c35
%define tracy_commit 143a53d1985b8e52a7590a0daca30a0a7c653b42
%define cryptopp_commit 60f81a77e0c9a0e7ffc1ca1bc438ddfa2e43b78e
%define zydis_commit bffbb610cfea643b98e87658b9058382f7522807
%define dear_imgui_commit 636cd4a7d623a2bc9bf59bb3acbb4ca075befba3
%define discord_rpc_commit 4ec218155d73bcb8022f8f7ca72305d801f84beb
%define vulkan_headers_version 1.4.303
%define libatrac9_commit 9640129dc6f2afbca6ceeca3019856e8653a5fb2

Name: shadps4
Version: 0.5.0
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
# https://github.com/shadps4-emu/ext-SDL/archive/%sdl3_commit/ext-SDL-%sdl3_commit.tar.gz
Source2: ext-SDL-%sdl3_commit.tar
# https://github.com/GPUOpen-LibrariesAndSDKs/VulkanMemoryAllocator/archive/%vma_commit/VulkanMemoryAllocator-%vma_commit.tar.gz
Source3: VulkanMemoryAllocator-%vma_commit.tar
# https://github.com/Tessil/robin-map/archive/%robin_map_commit/robin-map-%robin_map_commit.tar.gz
Source4: robin-map-%robin_map_commit.tar
# https://github.com/Neargye/magic_enum/archive/%magic_enum_commit/magic_enum-%magic_enum_commit.tar.gz
Source5: magic_enum-%magic_enum_commit.tar
# https://github.com/shadps4-emu/sirit/archive/%sirit_commit/sirit-%sirit_commit.tar.gz
Source6: sirit-%sirit_commit.tar
# https://github.com/shadps4-emu/tracy/archive/%tracy_commit/tracy-%tracy_commit.tar.gz
Source7: tracy-%tracy_commit.tar
# https://github.com/shadps4-emu/ext-cryptopp/archive/%cryptopp_commit/ext-cryptopp-%cryptopp_commit.tar.gz
Source8: ext-cryptopp-%cryptopp_commit.tar
# https://github.com/zyantific/zydis/archive/%zydis_commit/zydis-%zydis_commit.tar.gz
Source9: zydis-%zydis_commit.tar
# https://github.com/shadps4-emu/ext-imgui/archive/%dear_imgui_commit/ext-imgui-%dear_imgui_commit.tar.gz
Source10: ext-imgui-%dear_imgui_commit.tar
# https://github.com/shadps4-emu/ext-discord-rpc/archive/%discord_rpc_commit/ext-discord-rpc-%discord_rpc_commit.tar.gz
Source11: ext-discord-rpc-%discord_rpc_commit.tar
# https://github.com/KhronosGroup/Vulkan-Headers/archive/v%vulkan_headers_version/Vulkan-Headers-%vulkan_headers_version.tar.gz
Source12: Vulkan-Headers-%vulkan_headers_version.tar
# https://github.com/shadps4-emu/ext-LibAtrac9/archive/%libatrac9_commit/ext-LibAtrac9-%libatrac9_commit.tar.gz
Source13: ext-LibAtrac9-%libatrac9_commit.tar

BuildRequires: boost-asio-devel
BuildRequires: cmake
BuildRequires: glslang-devel
BuildRequires: ilmbase-devel
BuildRequires: libXext-devel
BuildRequires: libalsa-devel
BuildRequires: libavfilter-devel
BuildRequires: libavformat-devel
BuildRequires: libdbusmenu-gtk3
BuildRequires: libdecor-devel
BuildRequires: libdrm-devel
BuildRequires: libe2fs
BuildRequires: libfmt-devel
BuildRequires: libgbm-devel
BuildRequires: libgtk-layer-shell
BuildRequires: libgtkmm3
BuildRequires: libhalf-devel
BuildRequires: libmpdclient
BuildRequires: libnl3
BuildRequires: libpng-devel
BuildRequires: libpugixml-devel
BuildRequires: libqt5-eglfskmssupport
BuildRequires: libqt5-quickshapes
BuildRequires: libspdlog1.13
BuildRequires: libspirv-tools-devel
BuildRequires: libswresample-devel
BuildRequires: libswscale-devel
BuildRequires: libtoml11-devel
BuildRequires: libunwind-devel
BuildRequires: libupower
BuildRequires: libusb-devel
BuildRequires: libvulkan-memory-allocator-devel
BuildRequires: libwayland-cursor-devel
BuildRequires: libwayland-egl-devel
BuildRequires: libxbyak-devel
BuildRequires: libxxhash-devel
BuildRequires: libzydis-devel
BuildRequires: pipewire-jack-libs-devel
BuildRequires: qt6-multimedia-devel
BuildRequires: qt6-tools-devel
BuildRequires: rapidjson-devel
BuildRequires: spirv-headers
BuildRequires: zlib-ng-devel

Provides: %name-qt = %EVR
Obsoletes: %name-qt <= 0.2.0-alt1

%description
shadPS4 is an early PS4 emulator for Windows and Linux written in C++

%prep
%setup -n shadPS4-v.%version -b 1 -b 2 -b 3 -b 4 -b 5 -b 6 -b 7 -b 8 -b 9 -b 10 -b 11 -b 12 -b 13

%__mv -Tf ../ext-cryptopp-cmake-%cryptopp_cmake_commit externals/cryptopp-cmake
%__mv -Tf ../ext-SDL-%sdl3_commit externals/sdl3
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

%cmake \
	-DENABLE_QT_GUI:BOOL=TRUE \
	-DSIRIT_USE_SYSTEM_SPIRV_HEADERS:BOOL=TRUE \
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
%_datadir/metainfo/releases/net.%name.shadPS4.releases.xml
%_datadir/metainfo/net.%name.shadPS4.metainfo.xml
%_desktopdir/net.%name.shadPS4.desktop
%_iconsdir/hicolor/512x512/apps/net.%name.shadPS4.png
%_iconsdir/hicolor/scalable/apps/net.%name.shadPS4.svg
%_libexecdir/%name

%changelog
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

%define cryptopp_cmake_commit 2c384c28265a93358a2455e610e76393358794df
%define robin_map_version 1.4.0
%define magic_enum_commit a413fcc9c46a020a746907136a384c227f3cd095
%define sirit_commit 427a42c9ed99b38204d9107bc3dc14e92458acf1
%define tracy_commit 143a53d1985b8e52a7590a0daca30a0a7c653b42
%define cryptopp_commit effed0d0b865afc23ed67e0916f83734e4b9b3b7
%define zydis_commit 120e0e705f8e3b507dc49377ac2879979f0d545c
%define dear_imgui_commit f4d9359095eff3eb03f685921edc1cf0e37b1687
%define discord_rpc_commit 19f66e6dcabb2268965f453db9e5774ede43238f
%define vulkan_headers_version 1.4.312
%define libatrac9_commit ec8899dadf393f655f2871a94e0fe4b3d6220c9a

Name: shadps4
Version: 0.8.0
Release: alt2

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
# https://github.com/Tessil/robin-map/archive/v%robin_map_version/robin-map-%robin_map_version.tar.gz
Source2: robin-map-%robin_map_version.tar
# https://github.com/Neargye/magic_enum/archive/%magic_enum_commit/magic_enum-%magic_enum_commit.tar.gz
Source3: magic_enum-%magic_enum_commit.tar
# https://github.com/shadps4-emu/sirit/archive/%sirit_commit/sirit-%sirit_commit.tar.gz
Source4: sirit-%sirit_commit.tar
# https://github.com/shadps4-emu/tracy/archive/%tracy_commit/tracy-%tracy_commit.tar.gz
Source5: tracy-%tracy_commit.tar
# https://github.com/zyantific/zydis/archive/%zydis_commit/zydis-%zydis_commit.tar.gz
Source6: zydis-%zydis_commit.tar
# https://github.com/shadps4-emu/ext-cryptopp/archive/%cryptopp_commit/ext-cryptopp-%cryptopp_commit.tar.gz
Source7: ext-cryptopp-%cryptopp_commit.tar
# https://github.com/shadps4-emu/ext-imgui/archive/%dear_imgui_commit/ext-imgui-%dear_imgui_commit.tar.gz
Source8: ext-imgui-%dear_imgui_commit.tar
# https://github.com/shadps4-emu/ext-discord-rpc/archive/%discord_rpc_commit/ext-discord-rpc-%discord_rpc_commit.tar.gz
Source9: ext-discord-rpc-%discord_rpc_commit.tar
# https://github.com/KhronosGroup/Vulkan-Headers/archive/v%vulkan_headers_version/Vulkan-Headers-%vulkan_headers_version.tar.gz
Source10: Vulkan-Headers-%vulkan_headers_version.tar
# https://github.com/shadps4-emu/ext-LibAtrac9/archive/%libatrac9_commit/ext-LibAtrac9-%libatrac9_commit.tar.gz
Source11: ext-LibAtrac9-%libatrac9_commit.tar

Patch0: %name-%version-alt-restore-pkg-support.patch

BuildRequires: boost-asio-devel
BuildRequires: clang
BuildRequires: glslang-devel
BuildRequires: libGLU-devel
BuildRequires: libSDL3-devel
BuildRequires: libavfilter-devel
BuildRequires: libavformat-devel
BuildRequires: libe2fs
BuildRequires: libfmt-devel
BuildRequires: libhalf-devel
BuildRequires: libpng-devel
BuildRequires: libpugixml-devel
BuildRequires: libqt5-eglfskmssupport
BuildRequires: libqt6-labsqmlmodels
BuildRequires: libspirv-tools-devel
BuildRequires: libstb-devel
BuildRequires: libswresample-devel
BuildRequires: libswscale-devel
BuildRequires: libtoml11-devel
BuildRequires: libusb-devel
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
%setup -n shadPS4-v.%version -b 1 -b 2 -b 3 -b 4 -b 5 -b 6 -b 7 -b 8 -b 9 -b 10 -b 11

%patch0 -p1

%__rm externals/cryptopp-cmake
%__rm externals/cryptopp

%__mv -Tf ../ext-cryptopp-cmake-%cryptopp_cmake_commit externals/cryptopp-cmake
%__mv -Tf ../robin-map-%robin_map_version externals/robin-map
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

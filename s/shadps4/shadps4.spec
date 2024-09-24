%define cryptopp_cmake_commit 2c384c28265a93358a2455e610e76393358794df
%define sdl3_commit 4cc3410dce50cefce98d3cf3cf1bc8eca83b862a
%define vma_commit e1bdbca9baf4d682fb6066b380f4aa4a7bdbb58a
%define robin_map_commit 2c48a1a50203bbaf1e3d0d64c5d726d56f8d3bb3
%define magic_enum_commit dae6bbf16c363e9ead4e628a47fdb02956a634f3
%define sirit_commit 37090c74cc6e680f2bc334cac8fd182f7634a1f6
%define tracy_commit b8061982cad0210b649541016c88ff5faa90733c
%define cryptopp_commit 60f81a77e0c9a0e7ffc1ca1bc438ddfa2e43b78e
%define zydis_commit bd73bc03b0aacaa89c9c203b9b43cd08f1b1843b
%define dear_imgui_commit 636cd4a7d623a2bc9bf59bb3acbb4ca075befba3

Name: shadps4
Version: 0.3.0
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

# https://github.com/shadps4-emu/shadPS4/pull/1039
Patch0: 0001-fixup-designator-order.patch

BuildRequires(pre): libdecor-devel

BuildRequires: boost-asio-devel
BuildRequires: cmake
BuildRequires: glslang-devel
BuildRequires: libXext-devel
BuildRequires: libalsa-devel
BuildRequires: libavfilter-devel
BuildRequires: libavformat-devel
BuildRequires: libdbusmenu-gtk3
BuildRequires: libdrm-devel
BuildRequires: libe2fs
BuildRequires: libfmt-devel
BuildRequires: libgbm-devel
BuildRequires: libgtk-layer-shell
BuildRequires: libgtkmm3
BuildRequires: libmpdclient
BuildRequires: libnl3
BuildRequires: libpugixml-devel
BuildRequires: libpulseaudio-devel
BuildRequires: libslang2
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
BuildRequires: qt6-tools-devel
BuildRequires: spirv-headers
BuildRequires: zlib-ng-devel

Provides: %name-qt = %EVR
Obsoletes: %name-qt <= 0.2.0-alt1

%description
shadPS4 is an early PS4 emulator for Windows and Linux written in C++

%prep
%setup -n shadPS4-v.%version -b 1 -b 2 -b 3 -b 4 -b 5 -b 6 -b 7 -b 8 -b 9 -b 10

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

%patch0 -p1

%build
%add_optflags -Wno-error=return-type

%cmake \
	-DENABLE_QT_GUI:BOOL=TRUE \
	-DSIRIT_USE_SYSTEM_SPIRV_HEADERS:BOOL=TRUE \
	-Wno-dev
%cmake_build

%install
%__mkdir_p %buildroot{%_bindir,%_desktopdir,%_iconsdir/hicolor/512x512/apps,%_libexecdir/%name}

%__install -Dp -m0755 %_target_platform/%name %buildroot%_libexecdir/%name/
%__ln_s %_libexecdir/%name/%name %buildroot%_bindir/%name
%__cp -r %_target_platform/translations %buildroot%_libexecdir/%name
%__install -Dp -m0644 .github/%name.desktop %buildroot%_desktopdir/
%__install -Dp -m0644 .github/%name.png %buildroot%_iconsdir/hicolor/512x512/apps/

%files
%doc README.md
%_bindir/%name
%_desktopdir/%name.desktop
%_iconsdir/hicolor/512x512/apps/%name.png
%_libexecdir/%name

%changelog
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

%define sirit_commit 282083a595dcca86814dedab2f2b0363ef38f1ec
%define tracy_commit 143a53d1985b8e52a7590a0daca30a0a7c653b42
%define zydis_commit 120e0e705f8e3b507dc49377ac2879979f0d545c
%define dear_imgui_commit f4d9359095eff3eb03f685921edc1cf0e37b1687
%define discord_rpc_commit 19f66e6dcabb2268965f453db9e5774ede43238f
%define libatrac9_commit ec8899dadf393f655f2871a94e0fe4b3d6220c9a
%define libusb_commit d087ea86539ab1f1ec42faf86e2357e2fad126a6
%define hwinfo_commit 8660006e0ca4aae5dda7a29e585968b50b0273b7
%define miniz_version 3.1.0
%define aac_commit ee76460efbdb147e26d804c798949c23f174460b
%define spdlog_commit b8944a4bcd478ee03375c9c50dc8d6c741f43f7b
%define libressl_commit b0504086dbbc186724b0cc92e6ba1832c245de0b
%define imguifiledialog_commit 6e3ddeb485e8804beefae6e6d690b7709084bacd
%define minimp3_commit 7b590fdcfa5a79c033e76eacc05d0c3e4c79f536

Name: shadps4
Version: 0.16.0
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
# https://github.com/shadexternals/libusb/archive/%libusb_commit/libusb-%libusb_commit.tar.gz
Source7: libusb-%libusb_commit.tar
# https://github.com/%name-emu/ext-hwinfo/archive/%hwinfo_commit/ext-hwinfo-%hwinfo_commit.tar.gz
Source8: ext-hwinfo-%hwinfo_commit.tar
# https://github.com/richgel999/miniz/archive/%miniz_version/miniz-%miniz_version.tar.gz
Source9: miniz-%miniz_version.tar
# https://android.googlesource.com/platform/external/aac/+archive/ee76460efbdb147e26d804c798949c23f174460b.tar.gz
Source10: aac-%aac_commit.tar
# https://github.com/gabime/spdlog/archive/%spdlog_commit/spdlog-%spdlog_commit.tar.gz
Source11: spdlog-%spdlog_commit.tar
# https://github.com/shadexternals/libressl/archive/%libressl_commit/libressl-%libressl_commit.tar.gz
Source12: libressl-%libressl_commit.tar
# https://github.com/shadexternals/ImGuiFileDialog/archive/%imguifiledialog_commit/ImGuiFileDialog-%imguifiledialog_commit.tar.gz
Source13: ImGuiFileDialog-%imguifiledialog_commit.tar
# https://github.com/lieff/minimp3/archive/%minimp3_commit/minimp3-%minimp3_commit.tar.gz
Source14: minimp3-%minimp3_commit.tar

BuildRequires: alt-os-release
BuildRequires: boost-asio-devel
BuildRequires: clang
BuildRequires: cli11-devel
BuildRequires: cmake
BuildRequires: glslang-devel
BuildRequires: libSDL3-devel
BuildRequires: libavfilter-devel
BuildRequires: libavformat-devel
BuildRequires: libfmt-devel
BuildRequires: libhalf-devel
BuildRequires: libmagic_enum-devel
BuildRequires: libnss-systemd
BuildRequires: libopenal-devel
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
BuildRequires: libzycore-devel
BuildRequires: lld
BuildRequires: llvm
BuildRequires: ninja-build
BuildRequires: nlohmann-json-devel
BuildRequires: rapidjson-devel
BuildRequires: renderdoc-devel
BuildRequires: spirv-headers
BuildRequires: zlib-devel

%description
shadPS4 is an early PlayStation 4 emulator for Windows, Linux and macOS written in C++

%prep
%setup -n shadPS4-v.%version -b 1 -b 2 -b 3 -b 4 -b 5 -b 6 -b 7 -b 8 -b 9 -b 10 -b 11 -b 12 -b 13 -b 14

%__mv -Tf ../sirit-%sirit_commit externals/sirit
%__mv -Tf ../tracy-%tracy_commit externals/tracy
%__mv -Tf ../zydis-%zydis_commit externals/zydis
%__mv -Tf ../ext-imgui-%dear_imgui_commit externals/dear_imgui
%__mv -Tf ../ext-discord-rpc-%discord_rpc_commit externals/discord-rpc
%__mv -Tf ../ext-LibAtrac9-%libatrac9_commit externals/LibAtrac9
%__mv -Tf ../libusb-%libusb_commit externals/libusb
%__mv -Tf ../ext-hwinfo-%hwinfo_commit externals/hwinfo
%__mv -Tf ../miniz-%miniz_version externals/miniz
%__mv -Tf ../aac-%aac_commit externals/aacdec/fdk-aac
%__mv -Tf ../spdlog-%spdlog_commit externals/spdlog
%__mv -Tf ../libressl-%libressl_commit externals/libressl
%__mv -Tf ../ImGuiFileDialog-%imguifiledialog_commit externals/ImGuiFileDialog
%__mv -Tf ../minimp3-%minimp3_commit externals/minimp3

sed -i 's/find_package(glslang 15 CONFIG)/find_package(glslang 16 CONFIG)/g' CMakeLists.txt

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
* Thu Jun 04 2026 Nazarov Denis <nenderus@altlinux.org> 0.16.0-alt1
- Version 0.16.0

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

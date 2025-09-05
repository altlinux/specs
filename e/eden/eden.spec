Name: eden
Version: 0.0.3
Release: alt1

Summary: Nintendo Switch Emulator
License: GPLv3+
Group: Emulators

Url: https://%name-emu.dev/
Vcs: https://git.%name-emu.dev/%name-emu/%name
Packager: Nazarov Denis <nenderus@altlinux.org>

ExcludeArch: %ix86

# https://git.%name-emu.dev/%name-emu/%name/archive/v%version.tar.gz
Source0: %name-v%version.tar
Source1: cache-cpm.tar

BuildRequires: /proc
BuildRequires: alt-os-release
BuildRequires: boost-asio-devel
BuildRequires: boost-filesystem-devel
BuildRequires: catch-devel
BuildRequires: clang
BuildRequires: clang-tools
BuildRequires: ctest
BuildRequires: git-core
BuildRequires: glslang
BuildRequires: libSDL2-devel
BuildRequires: libVulkanUtilityLibraries-devel
BuildRequires: libavfilter-devel
BuildRequires: libavformat-devel
BuildRequires: libbrotli-devel
BuildRequires: libcpp-jwt-devel
BuildRequires: libcubeb-devel
BuildRequires: libenet-devel
BuildRequires: libfmt-devel
BuildRequires: liblz4-devel
BuildRequires: libopus-devel
BuildRequires: libspirv-tools-devel
BuildRequires: libswresample-devel
BuildRequires: libswscale-devel
BuildRequires: libunordered_dense-devel
BuildRequires: libusb-devel
BuildRequires: libvulkan-memory-allocator-devel
BuildRequires: libzstd-devel
BuildRequires: libzydis-devel
BuildRequires: lld
BuildRequires: llvm
BuildRequires: python-modules-encodings
BuildRequires: python3-dev
BuildRequires: qt6-tools-devel
BuildRequires: quazip-qt6-devel
BuildRequires: spirv-headers

%description
Eden is an experimental open-source emulator for the Nintendo Switch, built with performance and stability in mind. It is written in C++ with cross-platform support for Windows, Linux, FreeBSD, Solaris, OpenBSD, and Android.

%prep
%setup -n %name -a 1

%build
sed -i -e 's/-Werror=conversion/-Wno-error=conversion/' src/input_common/CMakeLists.txt

export CC="clang"
export CXX="clang++"
export RANLIB="llvm-ranlib"
export AR="llvm-ar"
export NM="llvm-nm"
export LDFLAGS="-fuse-ld=lld $LDFLAGS"

%cmake \
	-DCMAKE_BUILD_TYPE:STRING=RelWithDebInfo \
	-DCPMUTIL_FORCE_BUNDLED:BOOL=OFF \
	-DQT_NO_PRIVATE_MODULE_WARNING:BOOL=ON \
	-DENABLE_QT_TRANSLATION:BOOL=ON \
	-DYUZU_USE_BUNDLED_QT:BOOL=OFF \
	-DYUZU_USE_EXTERNAL_SDL2:BOOL=OFF \
	-DYUZU_USE_BUNDLED_SDL2:BOOL=OFF \
	-DYUZU_USE_EXTERNAL_VULKAN_HEADERS:BOOL=OFF \
	-DYUZU_USE_EXTERNAL_VULKAN_UTILITY_LIBRARIES:BOOL=OFF \
	-DYUZU_USE_EXTERNAL_VULKAN_SPIRV_TOOLS:BOOL=OFF \
	-DYUZU_USE_BUNDLED_FFMPEG:BOOL=OFF \
	-DYUZU_USE_BUNDLED_OPENSSL:BOOL=OFF \
	-DYUZU_CHECK_SUBMODULES:BOOL=OFF \
	-DYUZU_ENABLE_LTO:BOOL=ON \
	-DYUZU_TESTS:BOOL=ON \
	-DTITLE_BAR_FORMAT_IDLE:STRING='Eden | v%version' \
	-DTITLE_BAR_FORMAT_RUNNING:STRING='Eden | v%version' \
	-GNinja \
	-Wno-dev
%cmake_build

%install
%cmake_install

%check
%ctest || :

%files
%doc CONTRIBUTING.md README.md
%_bindir/%name
%_bindir/%name-cli
%_bindir/%name-room
%_desktopdir/dev.%{name}_emu.%name.desktop
%_datadir/metainfo/dev.%{name}_emu.%name.metainfo.xml
%_datadir/mime/packages/dev.%{name}_emu.%name.xml
%_iconsdir/hicolor/scalable/apps/dev.%{name}_emu.%name.svg

%changelog
* Fri Sep 05 2025 Nazarov Denis <nenderus@altlinux.org> 0.0.3-alt1
- Stable version 0.0.3

* Mon Aug 25 2025 Nazarov Denis <nenderus@altlinux.org> 0.0.3-alt0.rc3
- Initial build for ALT Linux

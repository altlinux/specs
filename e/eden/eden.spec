Name: eden
Version: 0.2.1
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
BuildRequires: frozen-devel
BuildRequires: git-core
BuildRequires: glslang
BuildRequires: libSDL2-devel
BuildRequires: libVulkanUtilityLibraries-devel
BuildRequires: libavfilter-devel
BuildRequires: libavformat-devel
BuildRequires: libbrotli-devel
BuildRequires: libcpp-httplib-devel
BuildRequires: libcpp-jwt-devel
BuildRequires: libcubeb-devel
BuildRequires: libenet-devel
BuildRequires: libfmt-devel
BuildRequires: libgamemode-devel
BuildRequires: liblz4-devel
%ifarch aarch64
BuildRequires: liboaknut-devel
%endif
BuildRequires: libopus-devel
BuildRequires: libsimpleini-devel
BuildRequires: libswresample-devel
BuildRequires: libswscale-devel
BuildRequires: libunordered_dense-devel
BuildRequires: libusb-devel
BuildRequires: libvulkan-memory-allocator-devel
BuildRequires: libxbyak-devel
BuildRequires: libzstd-devel
BuildRequires: lld
BuildRequires: llvm
BuildRequires: llvm-devel
BuildRequires: python-modules-encodings
BuildRequires: python3-dev
BuildRequires: qt6-charts-devel
BuildRequires: qt6-tools-devel
BuildRequires: quazip-qt6-devel
BuildRequires: renderdoc-devel
BuildRequires: spirv-headers

%description
Eden is an experimental open-source emulator for the Nintendo Switch, built with performance and stability in mind. It is written in C++ with cross-platform support for Windows, Linux, FreeBSD, Solaris, OpenBSD, and Android.

%prep
%setup -n %name -a 1

%build
sed -i -e 's/-Werror=conversion/-Wno-error=conversion/' src/input_common/CMakeLists.txt

%ifarch aarch64
sed -i -e 's/-Werror=unused/-Wno-error=unused/' src/CMakeLists.txt
%endif

# Fix RenderDoc API version
sed -i -e 's/RENDERDOC_API_1_6_0/RENDERDOC_API_1_7_0/' src/core/tools/renderdoc.h

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
	-DYUZU_USE_BUNDLED_FFMPEG:BOOL=OFF \
	-DYUZU_USE_BUNDLED_OPENSSL:BOOL=OFF \
	-DYUZU_TESTS:BOOL=ON \
	-DTITLE_BAR_FORMAT_IDLE:STRING="Eden | v%version | Clang $(llvm-config --version)" \
	-DTITLE_BAR_FORMAT_RUNNING:STRING="Eden | v%version | Clang $(llvm-config --version)" \
	-Dunordered_dense_FORCE_SYSTEM:BOOL=ON \
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
* Fri Jun 12 2026 Nazarov Denis <nenderus@altlinux.org> 0.2.1-alt1
- New version 0.2.1.

* Sun May 17 2026 Nazarov Denis <nenderus@altlinux.org> 0.2.0-alt1
- New version 0.2.0.

* Sun Mar 01 2026 Nazarov Denis <nenderus@altlinux.org> 0.1.1-alt1.1
- Fix build with RenderDoc 1.43+

* Fri Jan 30 2026 Nazarov Denis <nenderus@altlinux.org> 0.1.1-alt1
- New version 0.1.1.

* Tue Jan 27 2026 Nazarov Denis <nenderus@altlinux.org> 0.1.0-alt1
- New version 0.1.0.

* Tue Dec 23 2025 Nazarov Denis <nenderus@altlinux.org> 0.0.4-alt2
- Add patch to fix dynarmic tests

* Mon Dec 22 2025 Nazarov Denis <nenderus@altlinux.org> 0.0.4-alt1
- New version 0.0.4.

* Fri Sep 05 2025 Nazarov Denis <nenderus@altlinux.org> 0.0.3-alt1
- Stable version 0.0.3

* Mon Aug 25 2025 Nazarov Denis <nenderus@altlinux.org> 0.0.3-alt0.rc3
- Initial build for ALT Linux

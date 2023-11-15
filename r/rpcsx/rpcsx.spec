%define git_date 20231111
%define git_rev 7a82602

%define xbyak_commit ce083a0dcc306c1717685a81f577a4e050193919

Name: rpcsx
Version: 20231111
Release: alt2

Summary: PS4 emulator
License: GPLv2
Group: Emulators

Url: https://%name.github.io/%name-site/
Packager: Nazarov Denis <nenderus@altlinux.org>

ExclusiveArch: x86_64

# https://github.com/RPCSX/%name/archive/%name-v%version/%name-%name-v%version.tar.gz
Source0: %name-%name-v%version.tar
# https://github.com/RPCSX/xbyak/archive/%xbyak_commit/xbyak-%xbyak_commit.tar.gz
Source1: xbyak-%xbyak_commit.tar

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: glslang
BuildRequires: glslc
BuildRequires: libglfw3-devel
BuildRequires: libsox-devel
BuildRequires: libspirv-cross-devel-static
BuildRequires: libspirv-tools-devel
BuildRequires: libunwind-devel
BuildRequires: libvulkan-devel

%description
An experimental PlayStation 4 emulator for Linux written in C++

%prep
%setup -b 1 -n %name-%name-v%version

%__rm -r 3rdparty/xbyak
%__ln_s %_builddir/xbyak-%xbyak_commit 3rdparty/xbyak

sed -e 's/find_package(Git)/#find_package(Git)/' \
	-e 's/string(SUBSTRING ${GIT_DATE} 1 8 GIT_DATE)/string(SUBSTRING %git_date 1 8 GIT_DATE)/' \
	-e 's/string(STRIP "${GIT_REV}" GIT_REV)/string(STRIP "%git_rev" GIT_REV)/' \
	-e 's/string(SUBSTRING "${GIT_REV}" 1 7 GIT_REV)/string(SUBSTRING "%git_rev" 1 7 GIT_REV)/' \
	-e 's/string(STRIP "${GIT_DIRTY}" GIT_DIRTY)/string(STRIP "0" GIT_DIRTY)/' \
	-e 's/string(STRIP "${GIT_BRANCH}" GIT_BRANCH)/string(STRIP "master" GIT_BRANCH)/' \
	-i rx/CMakeLists.txt

%build
%cmake \
	-Dspirv_cross_core_DIR:PATH=%_datadir/cmake \
	-Dspirv_cross_glsl_DIR:PATH=%_datadir/cmake \
	-Wno-dev
%cmake_build

%install
%cmake_install

%files
%doc .github/BUILDING.md .github/USAGE.md .github/readme.md
%_bindir/%name-gpu
%_bindir/%name-os

%changelog
* Wed Nov 15 2023 Nazarov Denis <nenderus@altlinux.org> 20231111-alt2
- Build with system SPIRV Cross

* Sun Nov 12 2023 Nazarov Denis <nenderus@altlinux.org> 20231111-alt1
 - Initial build for ALT Linux

%define git_date 20230916
%define git_commit d2d3741

Name: citra
Version: 1991
Release: alt1

Summary: Nintendo 3DS emulator
License: GPLv2
Group: Emulators

Url: https://%name-emu.org/
Packager: Nazarov Denis <nenderus@altlinux.org>

ExclusiveArch: x86_64 aarch64 %e2k

# Source-url: https://github.com/%name-emu/%name-nightly/releases/download/nightly-%version/%name-unified-source-%git_date-%git_commit.tar.xz
Source: %name-unified-source-%git_date-%git_commit.tar

BuildRequires: ctest
BuildRequires: doxygen
BuildRequires: git-core
BuildRequires: glslang
BuildRequires: graphviz
BuildRequires: libSDL2-devel
BuildRequires: libavfilter-devel
BuildRequires: libavformat-devel
BuildRequires: libbacktrace-devel
BuildRequires: libdbus-devel
BuildRequires: libportaudio2-devel
BuildRequires: libswresample-devel
BuildRequires: libusb-devel
BuildRequires: pipewire-jack-libs-devel
BuildRequires: python3-dev
BuildRequires: qt6-multimedia
BuildRequires: qt6-multimedia-devel
BuildRequires: qt6-tools-devel

%description
Citra is an open-source Nintendo 3DS emulator and debugger, written with portability in mind.

%prep
%setup -n %name-unified-source-%git_date-%git_commit

# Enforce package versioning in GUI
sed -i \
-e 's|@GIT_BRANCH@|HEAD|g' \
-e 's|@GIT_DESC@|%git_commit|g' \
-e 's|@BUILD_FULLNAME@|Nightly %version|g' \
src/common/scm_rev.cpp.in

%build
%add_optflags -Wno-error=deprecated-declarations

%cmake \
	-DENABLE_QT_TRANSLATION:BOOL=ON \
	-DUSE_SYSTEM_SDL2:BOOL=ON \
	-DUSE_SYSTEM_OPENSSL:BOOL=ON \
	-DUSE_SYSTEM_LIBUSB:BOOL=ON \
	-Wno-dev

%cmake_build

%install
%cmakeinstall_std

%check
cd %_cmake__builddir
ctest

%files
%_bindir/%name
%_bindir/%name-qt
%_bindir/%name-room
%_desktopdir/%name-qt.desktop
%_datadir/mime/packages/%name.xml
%_iconsdir/hicolor/scalable/apps/%name.svg
%_man6dir/%name.6*
%_man6dir/%name-qt.6*

%changelog
* Sat Sep 16 2023 Nazarov Denis <nenderus@altlinux.org> 1991-alt1
- Version Nightly 1991

* Sun Jul 23 2023 Nazarov Denis <nenderus@altlinux.org> 1953-alt1
- Version Nightly 1953

* Mon May 8 2023 Artyom Bystrov <arbars@altlinux.org> 1769-alt1.1
- Add E2K arch in ExclusiveArch

* Fri Jun 10 2022 Nazarov Denis <nenderus@altlinux.org> 1769-alt1
- Version Nightly 1769

* Thu Nov 25 2021 Nazarov Denis <nenderus@altlinux.org> 1734-alt1
- Version Nightly 1734
- Add updated russian translation

* Sat Nov 06 2021 Nazarov Denis <nenderus@altlinux.org> 1732-alt1
- Version Nightly 1732

* Sat Sep 25 2021 Nazarov Denis <nenderus@altlinux.org> 1724-alt1
- Version Nightly 1724

* Sun May 02 2021 Arseny Maslennikov <arseny@altlinux.org> 1704-alt1.1
- NMU: spec: adapted to new cmake macros.

* Thu Apr 29 2021 Nazarov Denis <nenderus@altlinux.org> 1704-alt1
- Version Nightly 1704

* Sat Apr 24 2021 Nazarov Denis <nenderus@altlinux.org> 1703-alt1
- Version Nightly 1703

* Sat Apr 03 2021 Nazarov Denis <nenderus@altlinux.org> 1697-alt1
- Version Nightly 1697

* Fri Mar 19 2021 Nazarov Denis <nenderus@altlinux.org> 1696-alt1
- Initial build for ALT Linux

# git describe --always upstream/citra
%define git_desc 3bb027ac12

%define boost_commit 36603a1e665e849d29b1735a12c0a51284a10dd0
%define nihstro_commit fd69de1a1b960ec296cc67d32257b0f9e2d89ac6
%define soundtouch_commit 060181eaf273180d3a7e87349895bd0cb6ccbf4a
%define catch_version 2.13.7
%define dynarmic_commit af0d4a7c18ee90d544866a8cf24e6a0d48d3edc4
%define xbyak_version 5.96
%define cryptopp_version CRYPTOPP_8_5_0
%define fmt_version 7.1.2
%define enet_commit 498b9e3571c2e096d7143c3c76852c5ec28d7885
%define inih_version r52
%define libressl_commit 8929f818fd748fd31a34fec7c04558399e13014a
%define libusb_version 1.0.23
%define cubeb_commit 1d66483ad2b93f0e00e175f9480c771af90003a7
%define discord_rpc_commit 963aa9f3e5ce81a4682c6ca3d136cddda614db33
%define cpp_jwt_commit 6e27aa4c8671e183f11e327a2e1f556c64fdc4a9
%define teakra_commit 01db7cdd00aabcce559a8dddce8798dabb71949b
%define lodepng_commit 31d9704fdcca0b68fb9656d4764fa0fb60e460c2
%define zstd_version 1.4.8
%define libyuv_commit 19d71f6b351fe992ae34b114eebd872c383a6bdb
%define sanitizers_cmake_commit aab6948fa863bc1cbe5d0850bc46b9ef02ed4c1a

Name: citra
Version: 1769
Release: alt1.1

Summary: Nintendo 3DS emulator
License: GPLv2
Group: Emulators

Url: https://%name-emu.org/
Packager: Nazarov Denis <nenderus@altlinux.org>

ExclusiveArch: x86_64 ppc64le %e2k

# https://github.com/%name-emu/%name-nightly/archive/nightly-%version/%name-nightly-nightly-%version.tar.gz
Source0: %name-nightly-nightly-%version.tar
# https://github.com/citra-emu/ext-boost/archive/%boost_commit/ext-boost-%boost_commit.tar.gz
Source1: ext-boost-%boost_commit.tar
# https://github.com/neobrain/nihstro/archive/%nihstro_commit/nihstro-%nihstro_commit.tar.gz
Source2: nihstro-%nihstro_commit.tar
# https://github.com/citra-emu/ext-soundtouch/archive/%soundtouch_commit/ext-soundtouch-%soundtouch_commit.tar.gz
Source3: ext-soundtouch-%soundtouch_commit.tar
# https://github.com/catchorg/Catch2/archive/v%catch_version/Catch2-%catch_version.tar.gz
Source4: Catch2-%catch_version.tar
# https://github.com/citra-emu/dynarmic/archive/%dynarmic_commit/dynarmic-%dynarmic_commit.tar.gz
Source5: dynarmic-%dynarmic_commit.tar
# https://github.com/herumi/xbyak/archive/v%xbyak_version/xbyak-%xbyak_version.tar.gz
Source6: xbyak-%xbyak_version.tar
# https://github.com/weidai11/cryptopp/archive/%cryptopp_version/cryptopp-%cryptopp_version.tar.gz
Source7: cryptopp-%cryptopp_version.tar
# https://github.com/fmtlib/fmt/archive/%fmt_version/fmt-%fmt_version.tar.gz
Source8: fmt-%fmt_version.tar
# https://github.com/lsalzman/enet/archive/%enet_commit/enet-%enet_commit.tar.gz
Source9: enet-%enet_commit.tar
# https://github.com/benhoyt/inih/archive/%inih_version/inih-%inih_version.tar.gz
Source10: inih-%inih_version.tar
# https://github.com/citra-emu/ext-libressl-portable/archive/%libressl_commit/ext-libressl-portable-%libressl_commit.tar.gz
Source11: ext-libressl-portable-%libressl_commit.tar
# https://github.com/libusb/libusb/archive/v%libusb_version/libusb-%libusb_version.tar.gz
Source12: libusb-%libusb_version.tar
# https://github.com/kinetiknz/cubeb/archive/%cubeb_commit/cubeb-%cubeb_commit.tar.gz
Source13: cubeb-%cubeb_commit.tar
# https://github.com/discord/discord-rpc/archive/%discord_rpc_commit/discord-rpc-%discord_rpc_commit.tar.gz
Source14: discord-rpc-%discord_rpc_commit.tar
# https://github.com/arun11299/cpp-jwt/archive/%cpp_jwt_commit/cpp-jwt-%cpp_jwt_commit.tar.gz
Source15: cpp-jwt-%cpp_jwt_commit.tar
# https://github.com/wwylele/teakra/archive/%teakra_commit/teakra-%teakra_commit.tar.gz
Source16: teakra-%teakra_commit.tar
# https://github.com/lvandeve/lodepng/archive/%lodepng_commit/lodepng-%lodepng_commit.tar.gz
Source17: lodepng-%lodepng_commit.tar
# https://github.com/facebook/zstd/archive/v%zstd_version/zstd-%zstd_version.tar.gz
Source18: zstd-%zstd_version.tar
# https://github.com/lemenkov/libyuv/archive/%libyuv_commit/libyuv-%libyuv_commit.tar.gz
Source19: libyuv-%libyuv_commit.tar
# https://github.com/arsenm/sanitizers-cmake/archive/%sanitizers_cmake_commit/sanitizers-cmake-%sanitizers_cmake_commit.tar.gz
Source20: sanitizers-cmake-%sanitizers_cmake_commit.tar

Source21: ru_RU.ts

BuildRequires: boost-asio-devel
BuildRequires: ctest
BuildRequires: doxygen
BuildRequires: git-core
BuildRequires: graphviz
BuildRequires: libSDL2-devel
BuildRequires: libavformat-devel
BuildRequires: libswresample-devel
BuildRequires: libswscale-devel
BuildRequires: libusb-devel
BuildRequires: qt5-multimedia-devel
BuildRequires: qt5-tools-devel

%description
Citra is an open-source Nintendo 3DS emulator and debugger, written with portability in mind.

%prep
%setup -n %name-nightly-nightly-%version -b 1 -b 2 -b 3 -b 4 -b 5 -b 6 -b 7 -b 8 -b 9 -b 10 -b 11 -b 12 -b 13 -b 14 -b 15 -b 16 -b 17 -b 18 -b 19 -b 20

%__mv -Tf ../ext-boost-%boost_commit externals/boost
%__mv -Tf ../nihstro-%nihstro_commit externals/nihstro
%__mv -Tf ../ext-soundtouch-%soundtouch_commit externals/soundtouch
%__mv -Tf ../Catch2-%catch_version externals/catch
%__mv -Tf ../dynarmic-%dynarmic_commit externals/dynarmic
%__mv -Tf ../xbyak-%xbyak_version externals/xbyak
%__mv -Tf ../cryptopp-%cryptopp_version externals/cryptopp/cryptopp
%__mv -Tf ../fmt-%fmt_version externals/fmt
%__mv -Tf ../enet-%enet_commit externals/enet
%__mv -Tf ../inih-%inih_version externals/inih/inih
%__mv -Tf ../ext-libressl-portable-%libressl_commit externals/libressl
%__mv -Tf ../libusb-%libusb_version externals/libusb/libusb
%__mv -Tf ../cubeb-%cubeb_commit externals/cubeb
%__mv -Tf ../discord-rpc-%discord_rpc_commit externals/discord-rpc
%__mv -Tf ../cpp-jwt-%cpp_jwt_commit externals/cpp-jwt
%__mv -Tf ../teakra-%teakra_commit externals/teakra
%__mv -Tf ../lodepng-%lodepng_commit externals/lodepng/lodepng
%__mv -Tf ../zstd-%zstd_version externals/zstd
%__mv -Tf ../libyuv-%libyuv_commit externals/libyuv
%__mv -Tf ../sanitizers-cmake-%sanitizers_cmake_commit externals/cubeb/cmake/sanitizers-cmake

%__mkdir externals/boost/.git
%__mkdir externals/nihstro/.git
%__mkdir externals/soundtouch/.git
%__mkdir externals/catch/.git
%__mkdir externals/dynarmic/.git
%__mkdir externals/xbyak/.git
%__mkdir externals/cryptopp/cryptopp/.git
%__mkdir externals/fmt/.git
%__mkdir externals/enet/.git
%__mkdir externals/inih/inih/.git
%__mkdir externals/libressl/.git
%__mkdir externals/libusb/libusb/.git
%__mkdir externals/cubeb/.git
%__mkdir externals/discord-rpc/.git
%__mkdir externals/cpp-jwt/.git
%__mkdir externals/teakra/.git
%__mkdir externals/lodepng/lodepng/.git
%__mkdir externals/zstd/.git
%__mkdir externals/libyuv/.git

# Enforce package versioning in GUI
sed -i \
-e 's|@GIT_BRANCH@|HEAD|g' \
-e 's|@GIT_DESC@|%git_desc|g' \
-e 's|@BUILD_FULLNAME@|Nightly %version|g' \
src/common/scm_rev.cpp.in

%__rm dist/languages/ru_RU.ts
%__cp %SOURCE20 dist/languages/

%build
%add_optflags -Wno-error=return-type

%cmake \
	-DENABLE_QT_TRANSLATION:BOOL=ON \
	-DENABLE_FFMPEG_AUDIO_DECODER:BOOL=ON \
	-DENABLE_FFMPEG_VIDEO_DUMPER:BOOL=ON \
	-DUSE_SYSTEM_BOOST:BOOL=TRUE \
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
%_desktopdir/%name.desktop
%_datadir/mime/packages/%name.xml
%_iconsdir/hicolor/scalable/apps/%name.svg
%_man6dir/%name.6*
%_man6dir/%name-qt.6*

%changelog
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

%define git_commit b92e354389bb7c0bd114a8631b8af110d3cb3a14

%define enet_commit 2a85cd64459f6ba038d233a634d9440490dbba12
%define implot_commit cc5e1daa5c7f2335a9460ae79c829011dc5cef2d
%define rcheevos_version 11.4.0
%define tinygltf_commit c5641f2c22d117da7971504591a8f6a41ece488b

Name: dolphin-emu
Version: 2407
Release: alt1

Summary: The Gamecube / Wii Emulator
License: GPLv2
Group: Emulators

Url: https://%name.org/
Packager: Nazarov Denis <nenderus@altlinux.org>

ExclusiveArch: x86_64 aarch64

# https://github.com/%name/dolphin/archive/%version/dolphin-%version.tar.gz
Source0: dolphin-%version.tar
# https://github.com/lsalzman/enet/archive/%enet_commit/enet-%enet_commit.tar.gz
Source1: enet-%enet_commit.tar
# https://github.com/epezent/implot/archive/%implot_commit/implot-%implot_commit.tar.gz
Source2: implot-%implot_commit.tar
# https://github.com/RetroAchievements/rcheevos/archive/v%rcheevos_version/rcheevos-%rcheevos_version.tar.gz
Source3: rcheevos-%rcheevos_version.tar
# https://github.com/syoyo/tinygltf/archive/%tinygltf_commit/tinygltf-%tinygltf_commit.tar.gz
Source4: tinygltf-%tinygltf_commit.tar

Patch0: dolphin-gbacore-alt.patch

BuildRequires: bzlib-devel
BuildRequires: cmake
BuildRequires: libSDL2-devel
BuildRequires: libSFML-devel
BuildRequires: libXcomposite-devel
BuildRequires: libXcursor-devel
BuildRequires: libXdamage-devel
BuildRequires: libXdmcp-devel
BuildRequires: libXft-devel
BuildRequires: libXi-devel
BuildRequires: libXinerama-devel
BuildRequires: libXmu-devel
BuildRequires: libXrandr-devel
BuildRequires: libXxf86vm-devel
BuildRequires: libalsa-devel
BuildRequires: libavformat-devel
BuildRequires: libbluez-devel
BuildRequires: libcubeb-devel
BuildRequires: libcurl-devel
BuildRequires: libedit-devel
BuildRequires: libevdev-devel
BuildRequires: libffi-devel
BuildRequires: libfmt-devel
BuildRequires: libgtest-devel
BuildRequires: libhidapi-devel
BuildRequires: liblz4-devel
BuildRequires: liblzma-devel
BuildRequires: liblzo2-devel
BuildRequires: libmbedtls-compat-devel
BuildRequires: libmgba-devel
BuildRequires: libminiupnpc-devel
BuildRequires: libminizip-ng-compat-devel
BuildRequires: libpugixml-devel
BuildRequires: libpulseaudio-devel
BuildRequires: libspng-devel
BuildRequires: libswresample-devel
BuildRequires: libswscale-devel
BuildRequires: libsystemd-devel
BuildRequires: libudev-devel
BuildRequires: libusb-devel
BuildRequires: libvulkan-memory-allocator-devel
BuildRequires: libxml2-devel
BuildRequires: libxxhash-devel
BuildRequires: libzstd-devel
BuildRequires: llvm-devel
BuildRequires: llvm17.0-gold
BuildRequires: qt6-svg-devel
BuildRequires: zlib-ng-devel

%description
Dolphin-emu is a emulator for Gamecube, Wii, Triforce that lets
you run Wii/GCN/Tri games on your Windows/Linux/Mac PC system.

%prep
%setup -n dolphin-%version -b 1 -b 2 -b 3 -b 4

%__mv -Tf ../enet-%enet_commit Externals/enet/enet
%__mv -Tf ../implot-%implot_commit Externals/implot/implot
%__mv -Tf ../rcheevos-%rcheevos_version Externals/rcheevos/rcheevos
%__mv -Tf ../tinygltf-%tinygltf_commit Externals/tinygltf/tinygltf

%patch0 -p1

%build
export LDFLAGS="-Wl,--copy-dt-needed-entries"

#Generate Version Strings
echo "#define SCM_REV_STR \"%git_commit\"
#define SCM_DESC_STR \"%version\"
#define SCM_BRANCH_STR \"heads/refs/tags/%version\"
#define SCM_COMMITS_AHEAD_MASTER 0
#define SCM_DISTRIBUTOR_STR \"ALT Linux Team\"
#define SCM_UPDATE_TRACK_STR \"\"" > Source/Core/Common/scmrev.h.in

%cmake .. \
	-DENABLE_LTO:BOOL=TRUE \
	-Wno-dev

%cmake_build

%install
%cmake_install
%__install -Dp -m0644 Data/51-usb-device.rules %buildroot%_udevrulesdir/51-%name-usb-device.rules
%find_lang %name

%files -f %name.lang
%_bindir/*
%_desktopdir/%name.desktop
%_datadir/%name
%_iconsdir/hicolor/256x256/apps/%name.png
%_iconsdir/hicolor/scalable/apps/%name.svg
%_man6dir/%{name}*
%config %_udevrulesdir/51-%name-usb-device.rules

%changelog
* Tue Jul 02 2024 Nazarov Denis <nenderus@altlinux.org> 2407-alt1
- Version 2407

* Wed Feb 14 2024 Nazarov Denis <nenderus@altlinux.org> 5.0.21088-alt1
- Version 5.0-21088

* Sun Oct 15 2023 Nazarov Denis <nenderus@altlinux.org> 5.0.19870-alt3.2
- Fix build with fmt 10

* Thu Sep 14 2023 Nazarov Denis <nenderus@altlinux.org> 5.0.19870-alt3.1
- Fix FTBFS

* Sat Sep 02 2023 Nazarov Denis <nenderus@altlinux.org> 5.0.19870-alt3
- Build with system libmgba

* Fri Sep 01 2023 Nazarov Denis <nenderus@altlinux.org> 5.0.19870-alt2
- Fix version strings

* Thu Aug 31 2023 Nazarov Denis <nenderus@altlinux.org> 5.0.19870-alt1
- Version 5.0-19870

* Tue Sep 13 2022 Nazarov Denis <nenderus@altlinux.org> 5.0.17269-alt1
- Version 5.0-17269

* Wed Aug 24 2022 Nazarov Denis <nenderus@altlinux.org> 5.0.17243-alt1
- Version 5.0-17243

* Wed May 25 2022 Nazarov Denis <nenderus@altlinux.org> 5.0.16380-alt1
- Version 5.0-16380

* Sun Apr 24 2022 Nazarov Denis <nenderus@altlinux.org> 5.0.16101-alt1.1
- Fix FTBFS

* Fri Mar 25 2022 Nazarov Denis <nenderus@altlinux.org> 5.0.16101-alt1
- Version 5.0-16101

* Wed Feb 09 2022 Nazarov Denis <nenderus@altlinux.org> 5.0.15993-alt1
- Version 5.0-15993

* Wed Nov 17 2021 Nazarov Denis <nenderus@altlinux.org> 5.0.15445-alt1
- Version 5.0-15445

* Thu Oct 07 2021 Nazarov Denis <nenderus@altlinux.org> 5.0.15260-alt1
- Version 5.0-15260

* Tue Sep 07 2021 Nazarov Denis <nenderus@altlinux.org> 5.0.15105-alt1
- Version 5.0-15105

* Mon Aug 02 2021 Nazarov Denis <nenderus@altlinux.org> 5.0.14790-alt1
- Version 5.0-14790

* Sat Jul 10 2021 Nazarov Denis <nenderus@altlinux.org> 5.0.14344-alt1.1
- Fix FTBFS

* Sun Jun 06 2021 Nazarov Denis <nenderus@altlinux.org> 5.0.14344-alt1
- Version 5.0-14344

* Fri May 28 2021 Nazarov Denis <nenderus@altlinux.org> 5.0.14095-alt1
- Version 5.0-14095

* Wed Apr 07 2021 Nazarov Denis <nenderus@altlinux.org> 5.0.13963-alt1
- Version 5.0-13963

* Sun Mar 14 2021 Nazarov Denis <nenderus@altlinux.org> 5.0.13827-alt1
- Version 5.0-13827
- Enables LLVM support

* Tue Mar 09 2021 Nazarov Denis <nenderus@altlinux.org> 5.0.13817-alt1
- Version 5.0-13817

* Wed Feb 17 2021 Nazarov Denis <nenderus@altlinux.org> 5.0.13671-alt2
- Enable Link Time Optimization
- Install udev rules for GameCube Controller Adapter, Wiimotes and DolphinBar

* Wed Feb 17 2021 Nazarov Denis <nenderus@altlinux.org> 5.0.13671-alt1
- Version 5.0-13671
- Add distributor option

* Sun Feb 14 2021 Nazarov Denis <nenderus@altlinux.org> 5.0.13653-alt1
- Version 5.0.13653
- Build with minizip-ng

* Fri Feb 12 2021 Nazarov Denis <nenderus@altlinux.org> 5.0.13633-alt1
- Version 5.0-13633
- Use system headers for Vulkan

* Wed Feb 10 2021 Nazarov Denis <nenderus@altlinux.org> 5.0.13614-alt2
- Build with cubeb

* Tue Feb 09 2021 Nazarov Denis <nenderus@altlinux.org> 5.0.13614-alt1
- Version 5.0-13614

* Sun Jan 24 2021 Nazarov Denis <nenderus@altlinux.org> 5.0-alt16.gitcaff472
- Update to git commit caff472dbf27fbcc5b3d28cbf5b1789592a9f857
- Use minizip from zlib

* Mon Oct 12 2020 Nazarov Denis <nenderus@altlinux.org> 5.0-alt15.git5a939cc
- Rebuit with minizip

* Sun Oct 11 2020 Nazarov Denis <nenderus@altlinux.org> 5.0-alt14.git5a939cc
- Update to git commit 5a939cc (ALT #39062)

* Fri Jul 03 2020 Nazarov Denis <nenderus@altlinux.org> 5.0-alt13
- Don't gzip sources to sppedup rpmbuild -bp
- Update BuildRequires and BuidPreReq
- Build for aarch64

* Mon Aug 19 2019 Anton Midyukov <antohami@altlinux.org> 5.0-alt12
- add_optflags (pkg-config --cflags pango) (Fix FTBFS)

* Sun Feb 24 2019 Nazarov Denis <nenderus@altlinux.org> 5.0-alt11
- Rebuilt with new SFML

* Tue Jan 15 2019 Nazarov Denis <nenderus@altlinux.org> 5.0-alt10
- Remove %ubt macro

* Sat Jan 12 2019 Nazarov Denis <nenderus@altlinux.org> 5.0-alt9%ubt
- Fix build

* Tue Sep 18 2018 Anton Midyukov <antohami@altlinux.org> 5.0-alt8%ubt
- Rebuilt with compat-libwxGTK3.0-gtk2-devel

* Sun Jul 22 2018 Nazarov Denis <nenderus@altlinux.org> 5.0-alt7%ubt
- Rebuilt with new mbedTLS

* Sun Jun 17 2018 Nazarov Denis <nenderus@altlinux.org> 5.0-alt6%ubt
- Rebuilt with new libva

* Fri Apr 13 2018 Nazarov Denis <nenderus@altlinux.org> 5.0-alt5%ubt
- Rebuilt with new mbedTLS

* Wed Jun 07 2017 Nazarov Denis <nenderus@altlinux.org> 5.0-alt4%ubt
- Rebuilt with ffmpeg instead libav
- Add gcc fix patch

* Tue Nov 01 2016 Nazarov Denis <nenderus@altlinux.org> 5.0-alt3.1
- Rebuilt with SFML 2.4.0

* Sun Jul 17 2016 Nazarov Denis <nenderus@altlinux.org> 5.0-alt2.M80P.1
- Build for branch p8

* Sun Jul 17 2016 Nazarov Denis <nenderus@altlinux.org> 5.0-alt3
- Rebuilt with shared enet and gtest libraries

* Wed Jul 13 2016 Nazarov Denis <nenderus@altlinux.org> 5.0-alt2
- Version 5.0

* Sat Feb 20 2016 Yuri N. Sedunov <aris@altlinux.org> 5.0-alt1.rc.1
- rebuilt against libSoundTouch.so.1

* Mon Aug 03 2015 Nazarov Denis <nenderus@altlinux.org> 5.0-alt1.rc
- Version 5.0 RC

* Thu Jul 16 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.2-alt4.git20150715
- New snapshot

* Sat Mar 14 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.2-alt3.git5fafcb6.1
- Rebuilt with wxGTK3.1 (instead of wxGTK3.0) & gtk+3 (gtk+2)

* Wed Sep 17 2014 Nazarov Denis <nenderus@altlinux.org> 4.0.2-alt3.git5fafcb6
- Version from git (commit 5fafcb6)
- Rebuild with new polarssl and GLEW

* Tue Apr 22 2014 Nazarov Denis <nenderus@altlinux.org> 4.0.2-alt2
- Rebuild with new polarssl

* Sat Feb 01 2014 Nazarov Denis <nenderus@altlinux.org> 4.0.2-alt1
- Version 4.0.2

* Wed Nov 20 2013 Nazarov Denis <nenderus@altlinux.org> 4.0.1-alt3
- Rebuild with wxGTK 3.0

* Mon Nov 11 2013 Nazarov Denis <nenderus@altlinux.org> 4.0.1-alt2
- Fix build

* Tue Nov 05 2013 Nazarov Denis <nenderus@altlinux.org> 4.0.1-alt1
- Initial build for ALT Linux

%define optflags_lto -flto=thin

%define version_hi 2
%define version_mid 0
%define version_lo 2

# git log v%version_hi.%version_mid.%version_lo -1 --format=%cd --date=local
%define git_date Sat Jul 13 06:19:16 2024
# git rev-parse v%version_hi.%version_mid.%version_lo
%define git_hash 2f46e5a8406e4832ba60c5ab1ba2fd16a074ab1f

Name: pcsx2
Version: %version_hi.%version_mid.%version_lo
Release: alt1

Summary: Playstation 2 console emulator
License: GPLv3 and LGPLv3
Group: Emulators

Url: http://%name.net/
Packager: Nazarov Denis <nenderus@altlinux.org>

ExclusiveArch: x86_64

# https://github.com/PCSX2/%name/archive/v%version/%name-%version.tar.gz
Source: %name-%version.tar

Patch0: %name-shaderc.patch

BuildRequires: bzlib-devel
BuildRequires: clang
BuildRequires: ctest
BuildRequires: extra-cmake-modules
BuildRequires: libGLU-devel
BuildRequires: libSDL2-devel
BuildRequires: libXcomposite-devel
BuildRequires: libXcursor-devel
BuildRequires: libXdamage-devel
BuildRequires: libXdmcp-devel
BuildRequires: libXft-devel
BuildRequires: libXinerama-devel
BuildRequires: libXmu-devel
BuildRequires: libXrandr-devel
BuildRequires: libXtst-devel
BuildRequires: libaio-devel
BuildRequires: libalsa-devel
BuildRequires: libavformat-devel
BuildRequires: libbacktrace-devel
BuildRequires: libcurl-devel
BuildRequires: libdbus-devel
BuildRequires: libexpat-devel
BuildRequires: libffi-devel
BuildRequires: libidn2-devel
BuildRequires: libjpeg-devel
BuildRequires: liblz4-devel
BuildRequires: liblzma-devel
BuildRequires: libpcap-devel
BuildRequires: libpcre2-devel
BuildRequires: libpulseaudio-devel
BuildRequires: libshaderc-devel
BuildRequires: libswresample-devel
BuildRequires: libswscale-devel
BuildRequires: libtiff-devel
BuildRequires: libudev-devel
BuildRequires: libwayland-egl-devel
BuildRequires: libwebp-devel
BuildRequires: libzstd-devel
BuildRequires: lld
BuildRequires: llvm
BuildRequires: ninja-build
BuildRequires: qt6-tools-devel

%description
PCSX2 is an emulator for the playstation 2 video game console. It is written mostly in C++, some part are in C and x86 assembly.
There is still lot of on going work to improve compatibility & speed.

%prep
%setup
%patch0 -p1

%build
%cmake \
	-DCMAKE_C_COMPILER:STRING=clang \
	-DCMAKE_CXX_COMPILER:STRING=clang++ \
	-DCMAKE_RANLIB:PATH=%_bindir/llvm-ranlib \
	-DCMAKE_AR:PATH=%_bindir/llvm-ar \
	-DCMAKE_NM:PATH=%_bindir/llvm-nm \
	-DCMAKE_EXE_LINKER_FLAGS:STRING="-fuse-ld=lld" \
	-DCMAKE_BUILD_TYPE:STRING="RelWithDebInfo" \
	-DCMAKE_DISABLE_PRECOMPILE_HEADERS:BOOL=TRUE \
	-DCMAKE_BUILD_PO:BOOL=TRUE \
	-DDISABLE_ADVANCE_SIMD:BOOL=TRUE \
	-DLTO_PCSX2_CORE:BOOL=TRUE \
	-GNinja \
	-Wno-dev

echo "#define GIT_TAG \"v$(echo %version)\"
#define GIT_TAGGED_COMMIT 1
#define GIT_TAG_HI  $(echo %version_hi)
#define GIT_TAG_MID $(echo %version_mid)
#define GIT_TAG_LO  $(echo %version_lo)
#define GIT_REV \"v$(echo %version)\"
#define GIT_HASH \"$(echo %git_hash)\"
#define GIT_DATE \"$(echo %git_date)\"" > %_cmake__builddir/common/include/svnrev.h

%cmake_build

%install
%__mkdir_p %buildroot%_bindir %buildroot%_libexecdir/%name
%__install -Dp -m0755 %_target_platform/bin/%name-qt %buildroot%_libexecdir/%name/%name-qt
%__ln_s %_libexecdir/%name/%name-qt %buildroot%_bindir/%name-qt
%__cp -r %_target_platform/bin/{resources,translations} %buildroot%_libexecdir/%name
%__install -Dp -m0644 %_target_platform/bin/resources/icons/AppIconLarge.png %buildroot%_iconsdir/hicolor/256x256/apps/PCSX2.png
%__install -Dp -m0644 .github/workflows/scripts/linux/%name-qt.desktop %buildroot%_desktopdir/%name-qt.desktop

%check
%ctest

%files
%doc bin/docs/*.pdf
%_bindir/%name-qt
%_desktopdir/%name-qt.desktop
%_libexecdir/%name
%_iconsdir/hicolor/256x256/apps/PCSX2.png

%changelog
* Thu Aug 22 2024 Nazarov Denis <nenderus@altlinux.org> 2.0.2-alt1
- Version 2.0.2 (ALT #50635)

* Tue May 21 2024 Nazarov Denis <nenderus@altlinux.org> 1.7.5684-alt1
- Version 1.7.5684

* Tue Apr 16 2024 Nazarov Denis <nenderus@altlinux.org> 1.7.5397-alt2
- Pack translations (ALT #49912)

* Fri Jan 05 2024 Nazarov Denis <nenderus@altlinux.org> 1.7.5397-alt1
- Version 1.7.5397

* Tue Dec 19 2023 Nazarov Denis <nenderus@altlinux.org> 1.7.5312-alt1
- Version 1.7.5312

* Wed Oct 18 2023 Nazarov Denis <nenderus@altlinux.org> 1.7.5107-alt1
- Version 1.7.5107

* Sat Jun 17 2023 Nazarov Denis <nenderus@altlinux.org> 1.7.4587-alt1
- Version 1.7.4587

* Sat May 13 2023 Nazarov Denis <nenderus@altlinux.org> 1.7.4500-alt1
- Version 1.7.4500

* Mon Apr 17 2023 Nazarov Denis <nenderus@altlinux.org> 1.7.4395-alt1
- Version 1.7.4395

* Sat Apr 15 2023 Nazarov Denis <nenderus@altlinux.org> 1.7.4383-alt1
- Version 1.7.4383

* Fri Apr 14 2023 Nazarov Denis <nenderus@altlinux.org> 1.7.4380-alt1
- Version 1.7.4380

* Thu Apr 06 2023 Nazarov Denis <nenderus@altlinux.org> 1.7.4342-alt1
- Version 1.7.4342

* Mon Dec 19 2022 Nazarov Denis <nenderus@altlinux.org> 1.7.3332-alt1.1
- Fix build

* Sat Sep 24 2022 Nazarov Denis <nenderus@altlinux.org> 1.7.3332-alt1
- Version 1.7.3332

* Sun May 29 2022 Nazarov Denis <nenderus@altlinux.org> 1.7.2828-alt1
- Version 1.7.2828

* Mon May 23 2022 Nazarov Denis <nenderus@altlinux.org> 1.7.2787-alt1
- Version 1.7.2787

* Fri Dec 10 2021 Nazarov Denis <nenderus@altlinux.org> 1.7.2116-alt1
- Version 1.7.2116

* Sat Nov 06 2021 Nazarov Denis <nenderus@altlinux.org> 1.7.2019-alt1
- Version 1.7.2019

* Fri Nov 05 2021 Nazarov Denis <nenderus@altlinux.org> 1.7.2016-alt1
- Version 1.7.2016

* Thu Nov 04 2021 Nazarov Denis <nenderus@altlinux.org> 1.7.2012-alt1
- Version 1.7.2012

* Wed Nov 03 2021 Nazarov Denis <nenderus@altlinux.org> 1.7.2006-alt1
- Version 1.7.2006

* Tue Nov 02 2021 Nazarov Denis <nenderus@altlinux.org> 1.7.2003-alt1
- Version 1.7.2003

* Sun Oct 11 2020 Anton Midyukov <antohami@altlinux.org> 1.6.0-alt6
- Rebuild with libwxGTK3.0

* Mon Jun 01 2020 Nazarov Denis <nenderus@altlinux.org> 1.6.0-alt5
- Use directory /usr/share/doc/PCSX2 for Configuration Guide and Readme / FAQ

* Sun May 24 2020 Nazarov Denis <nenderus@altlinux.org> 1.6.0-alt4
- Build GSdx plugin additionaly without AVX2 & SSE4 support
- Build GSdx legacy plugin
- Disable build date

* Sat May 23 2020 Nazarov Denis <nenderus@altlinux.org> 1.6.0-alt3
- Move localization files to separate subpackage
- Add requires to all plugin types

* Sat May 23 2020 Nazarov Denis <nenderus@altlinux.org> 1.6.0-alt2
- Add build pre requires
- Return XDG_STD option

* Fri May 08 2020 Nazarov Denis <nenderus@altlinux.org> 1.6.0-alt1
- Version 1.6.0

* Mon Jul 23 2018 Nazarov Denis <nenderus@altlinux.org> 1.4.0-alt2%ubt
- Rebuilt with new GLEW

* Sat Feb 20 2016 Yuri N. Sedunov <aris@altlinux.org> 1.4.0-alt1.1
- rebuilt against libSoundTouch.so.1

* Mon Jan 11 2016 Nazarov Denis <nenderus@altlinux.org> 1.4.0-alt1
- Version 1.4.0

* Tue Nov 18 2014 Nazarov Denis <nenderus@altlinux.org> 1.2.2-alt2
- Rebuild with libsoundtouch 1.8.0

* Sun Feb 16 2014 Nazarov Denis <nenderus@altlinux.org> 1.2.2-alt0.M70T.1
- Build for branch t7

* Sun Feb 16 2014 Nazarov Denis <nenderus@altlinux.org> 1.2.2-alt1
- Version 1.2.2

* Tue Feb 11 2014 Nazarov Denis <nenderus@altlinux.org> 1.2.1-alt1.M70P.1
- Build for branch p7

* Mon Feb 10 2014 Nazarov Denis <nenderus@altlinux.org> 1.2.1-alt1.M70T.1
- Build for branch t7

* Sun Feb 09 2014 Nazarov Denis <nenderus@altlinux.org> 1.2.1-alt2
- Fix language files for x64

* Sat Feb 08 2014 Nazarov Denis <nenderus@altlinux.org> 1.2.1-alt0.M70T.1
- Build for branch t7

* Fri Feb 07 2014 Nazarov Denis <nenderus@altlinux.org> 1.2.1-alt1
- Version 1.2.1

* Tue Feb 04 2014 Nazarov Denis <nenderus@altlinux.org> 1.2.0-alt1
- Version 1.2.0

* Thu Oct 17 2013 Nazarov Denis <nenderus@altlinux.org> 1.0.0-alt1.M70T.1
- Build for branch t7

* Sat Sep 28 2013 Nazarov Denis <nenderus@altlinux.org> 1.0.0-alt2
- Fix post-install unowned files
- Rebuild the ps2hw.dat file

* Fri Sep 27 2013 Nazarov Denis <nenderus@altlinux.org> 1.0.0-alt1
- Initial build for ALT Linux

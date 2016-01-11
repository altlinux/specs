%set_verify_elf_method textrel=relaxed

Name: pcsx2
Version: 1.4.0
Release: alt1

Summary: Playstation 2 console emulator
License: GPLv3
Group: Emulators

Url: http://pcsx2.net/
Packager: Nazarov Denis <nenderus@altlinux.org>

ExclusiveArch: %ix86

#https://codeload.github.com/PCSX2/%name/tar.gz/v%version
Source: %name-%version.tar.gz

BuildRequires: bzlib-devel
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: libGLEW-devel
BuildRequires: libSDL-devel
BuildRequires: libXmu-devel
BuildRequires: libaio-devel
BuildRequires: libalsa-devel
BuildRequires: libcggl-devel
BuildRequires: libgtk+2-devel
BuildRequires: libjpeg-devel
BuildRequires: liblzma-devel
BuildRequires: libpng++-devel
BuildRequires: libportaudio2-devel
BuildRequires: libsoundtouch-devel
BuildRequires: libwxGTK-devel

%description
PCSX2 is an emulator for the playstation 2 video game console. It is written mostly in C++, some part are in C and x86 assembly.
There is still lot of on going work to improve compatibility & speed.

%package plugin-cdvdiso
Summary: CDVDiso plugin for PCSX2
Group: Emulators
Requires: %name = %version-%release

%description plugin-cdvdiso
CDVDiso plugin for PCSX2

%package plugin-cdvdlinuz
Summary: CDVDlinuz plugin for PCSX2
Group: Emulators
Requires: %name = %version-%release

%description plugin-cdvdlinuz
CDVDlinuz plugin for PCSX2

%package plugin-cdvdnull
Summary: CDVDnull plugin for PCSX2
Group: Emulators
Requires: %name = %version-%release

%description plugin-cdvdnull
CDVDnull plugin for PCSX2

%package plugin-fwnull
Summary: FWnull plugin for PCSX2
Group: Emulators
Requires: %name = %version-%release

%description plugin-fwnull
FWnull plugin for PCSX2

%package plugin-gsdx
Summary: GSdx plugin for PCSX2
Group: Emulators
Requires: %name = %version-%release

%description plugin-gsdx
GSdx plugin for PCSX2

%package plugin-gsnull
Summary: GSnull plugin for PCSX2
Group: Emulators
Requires: %name = %version-%release

%description plugin-gsnull
GSnull plugin for PCSX2

%package plugin-lilypad
Summary: LilyPad plugin for PCSX2
Group: Emulators
Requires: %name = %version-%release

%description plugin-lilypad
LilyPad plugin for PCSX2

%package plugin-padnull
Summary: PADnull plugin for PCSX2
Group: Emulators
Requires: %name = %version-%release

%description plugin-padnull
PADnull plugin for PCSX2

%package plugin-spu2null
Summary: SPU2null plugin for PCSX2
Group: Emulators
Requires: %name = %version-%release

%description plugin-spu2null
SPU2null plugin for PCSX2

%package plugin-usbnull
Summary: USBnull plugin for PCSX2
Group: Emulators
Requires: %name = %version-%release

%description plugin-usbnull
USBnull plugin for PCSX2

%package plugin-dev9null
Summary: dev9null plugin for PCSX2
Group: Emulators
Requires: %name = %version-%release

%description plugin-dev9null
dev9null plugin for PCSX2

%package plugin-onepad
Summary: onepad plugin for PCSX2
Group: Emulators
Requires: %name = %version-%release

%description plugin-onepad
onepad plugin for PCSX2

%package plugin-spu2x
Summary: spu2x plugin for PCSX2
Group: Emulators
Requires: %name = %version-%release

%description plugin-spu2x
spu2x plugin for PCSX2

%package plugin-zzogl
Summary: zzogl plugin for PCSX2
Group: Emulators
Requires: %name = %version-%release

%description plugin-zzogl
zzogl plugin for PCSX2

%prep
%setup

%build
%__mkdir_p %_target_platform
pushd %_target_platform

cmake .. \
	-DCMAKE_INSTALL_PREFIX:PATH=%prefix \
	-DCMAKE_C_FLAGS:STRING='%optflags' \
	-DCMAKE_CXX_FLAGS:STRING='%optflags' \
	-DCMAKE_BUILD_TYPE:STRING=Release \
	-DCMAKE_BUILD_STRIP:BOOL=TRUE \
	-DCMAKE_BUILD_PO:BOOL=TRUE \
	-DPLUGIN_DIR:PATH=%_libdir/%name \
	-DGAMEINDEX_DIR:PATH=%_datadir/%name \
	-DPACKAGE_MODE:BOOL=TRUE \
	-DXDG_STD:BOOL=TRUE \
	-DSDL2_API:BOOL=FALSE \
	-DWX28_API:BOOL=TRUE \
	-DEXTRA_PLUGINS:BOOL=TRUE
popd

%make_build -C %_target_platform

%install
%makeinstall_std -C %_target_platform
%__rm -rf %buildroot%_defaultdocdir/PCSX2
%find_lang --output=%name.lang %{name}_{Iconized,Main}

%files -f %name.lang
%doc bin/docs/PCSX2_*.pdf
%_bindir/PCSX2*
%dir %_libdir/%name
%_libdir/%name/ps2hw.dat
%_desktopdir/PCSX2.desktop
%_man1dir/PCSX2.1.*
%dir %_datadir/%name
%_datadir/%name/GameIndex.dbf
%_datadir/%name/cheats_ws.zip
%_pixmapsdir/PCSX2.xpm

%files plugin-cdvdiso
%_libdir/%name/libCDVDiso.so

%files plugin-cdvdlinuz
%_libdir/%name/libCDVDlinuz.so

%files plugin-cdvdnull
%_libdir/%name/libCDVDnull.so

%files plugin-fwnull
%_libdir/%name/libFWnull-0.7.0.so

%files plugin-gsdx
%_libdir/%name/libGSdx-1.0.0.so

%files plugin-gsnull
%_libdir/%name/libGSnull.so

%files plugin-lilypad
%_libdir/%name/libLilyPad-0.11.0.so

%files plugin-padnull
%_libdir/%name/libPADnull.so

%files plugin-spu2null
%_libdir/%name/libSPU2null.so

%files plugin-usbnull
%_libdir/%name/libUSBnull-0.7.0.so

%files plugin-dev9null
%_libdir/%name/libdev9null-0.5.0.so

%files plugin-onepad
%_libdir/%name/libonepad-1.1.0.so

%files plugin-spu2x
%_libdir/%name/libspu2x-2.0.0.so

%files plugin-zzogl
%_libdir/%name/libzzogl-0.4.0.so

%changelog
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

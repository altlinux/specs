%define revision 5350

%set_verify_elf_method textrel=relaxed

Name: pcsx2
Version: 1.0.0
Release: alt1

Summary: Playstation 2 console emulator
License: GPLv3
Group: Emulators

Url: http://pcsx2.net/
Packager: Nazarov Denis <nenderus@altlinux.org>
ExclusiveArch: %ix86

Source0: https://pcsx2.googlecode.com/files/%name-%version-r%revision-sources.tar.bz2
Patch0: %name-%version-r%revision-alt-version.patch

BuildRequires: bzlib-devel
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: libSDL-devel
BuildRequires: libXmu-devel
BuildRequires: libalsa-devel
BuildRequires: libcggl-devel
BuildRequires: libglew-devel
BuildRequires: libgtk+2-devel
BuildRequires: libjpeg-devel
BuildRequires: libportaudio2-devel
BuildRequires: libsoundtouch-devel
BuildRequires: libsparsehash-devel
BuildRequires: libwxGTK-devel
BuildRequires: subversion

%description
PCSX2 is an emulator for the playstation 2 video game console. It is written mostly in C++, some part are in C and x86 assembly.
There is still lot of on going work to improve compatibility & speed.

%package -n %name-plugin-cdvdiso
Summary: CDVDiso plugin for PCSX2
Group: Emulators
Requires: %name = %version-%release

%description -n %name-plugin-cdvdiso
CDVDiso plugin for PCSX2

%package -n %name-plugin-cdvdlinuz
Summary: CDVDlinuz plugin for PCSX2
Group: Emulators
Requires: %name = %version-%release

%description -n %name-plugin-cdvdlinuz
CDVDlinuz plugin for PCSX2

%package -n %name-plugin-cdvdnull
Summary: CDVDnull plugin for PCSX2
Group: Emulators
Requires: %name = %version-%release

%description -n %name-plugin-cdvdnull
CDVDnull plugin for PCSX2

%package -n %name-plugin-fwnull
Summary: FWnull plugin for PCSX2
Group: Emulators
Requires: %name = %version-%release

%description -n %name-plugin-fwnull
FWnull plugin for PCSX2

%package -n %name-plugin-gsdx
Summary: GSdx plugin for PCSX2
Group: Emulators
Requires: %name = %version-%release

%description -n %name-plugin-gsdx
GSdx plugin for PCSX2

%package -n %name-plugin-gsnull
Summary: GSnull plugin for PCSX2
Group: Emulators
Requires: %name = %version-%release

%description -n %name-plugin-gsnull
GSnull plugin for PCSX2

%package -n %name-plugin-padnull
Summary: PADnull plugin for PCSX2
Group: Emulators
Requires: %name = %version-%release

%description -n %name-plugin-padnull
PADnull plugin for PCSX2

%package -n %name-plugin-spu2null
Summary: SPU2null plugin for PCSX2
Group: Emulators
Requires: %name = %version-%release

%description -n %name-plugin-spu2null
SPU2null plugin for PCSX2

%package -n %name-plugin-usbnull
Summary: USBnull plugin for PCSX2
Group: Emulators
Requires: %name = %version-%release

%description -n %name-plugin-usbnull
USBnull plugin for PCSX2

%package -n %name-plugin-dev9null
Summary: dev9null plugin for PCSX2
Group: Emulators
Requires: %name = %version-%release

%description -n %name-plugin-dev9null
dev9null plugin for PCSX2

%package -n %name-plugin-onepad
Summary: onepad plugin for PCSX2
Group: Emulators
Requires: %name = %version-%release

%description -n %name-plugin-onepad
onepad plugin for PCSX2

%package -n %name-plugin-spu2x
Summary: spu2x plugin for PCSX2
Group: Emulators
Requires: %name = %version-%release

%description -n %name-plugin-spu2x
spu2x plugin for PCSX2

%package -n %name-plugin-zzogl
Summary: zzogl plugin for PCSX2
Group: Emulators
Requires: %name = %version-%release

%description -n %name-plugin-zzogl
zzogl plugin for PCSX2

%package -n %name-plugin-zzogl-cg
Summary: zzogl-cg plugin for PCSX2
Group: Emulators
Requires: %name = %version-%release

%description -n %name-plugin-zzogl-cg
zzogl-cg plugin for PCSX2

%package -n %name-lang-cz
Summary: Czech language for PCSX2
Group: Emulators
Requires: %name = %version-%release

%description -n %name-lang-cz
Czech language for PCSX2

%package -n %name-lang-de
Summary: German language for PCSX2
Group: Emulators
Requires: %name = %version-%release

%description -n %name-lang-de
German language for PCSX2

%package -n %name-lang-es
Summary: Spanish language for PCSX2
Group: Emulators
Requires: %name = %version-%release

%description -n %name-lang-es
Spanish language for PCSX2

%package -n %name-lang-fi
Summary: Finnish language for PCSX2
Group: Emulators
Requires: %name = %version-%release

%description -n %name-lang-fi
Finnish language for PCSX2

%package -n %name-lang-fr
Summary: French language for PCSX2
Group: Emulators
Requires: %name = %version-%release

%description -n %name-lang-fr
French language for PCSX2

%package -n %name-lang-hu
Summary: Hungrian language for PCSX2
Group: Emulators
Requires: %name = %version-%release

%description -n %name-lang-hu
Hungrian language for PCSX2

%package -n %name-lang-id
Summary: Indonesian language for PCSX2
Group: Emulators
Requires: %name = %version-%release

%description -n %name-lang-id
Indonesian language for PCSX2

%package -n %name-lang-it
Summary: Italian language for PCSX2
Group: Emulators
Requires: %name = %version-%release

%description -n %name-lang-it
Italian language for PCSX2

%package -n %name-lang-jp
Summary: Japanese language for PCSX2
Group: Emulators
Requires: %name = %version-%release

%description -n %name-lang-jp
Japanese language for PCSX2

%package -n %name-lang-kr
Summary: Korean language for PCSX2
Group: Emulators
Requires: %name = %version-%release

%description -n %name-lang-kr
Korean language for PCSX2

%package -n %name-lang-my
Summary: Malay language for PCSX2
Group: Emulators
Requires: %name = %version-%release

%description -n %name-lang-my
Malay language for PCSX2

%package -n %name-lang-pl
Summary: Polish language for PCSX2
Group: Emulators
Requires: %name = %version-%release

%description -n %name-lang-pl
Polish language for PCSX2

%package -n %name-lang-br
Summary: Portuguese language for PCSX2
Group: Emulators
Requires: %name = %version-%release

%description -n %name-lang-br
Portuguese language for PCSX2

%package -n %name-lang-ru
Summary: Russian language for PCSX2
Group: Emulators
Requires: %name = %version-%release

%description -n %name-lang-ru
Russian language for PCSX2

%package -n %name-lang-se
Summary: Swedish language for PCSX2
Group: Emulators
Requires: %name = %version-%release

%description -n %name-lang-se
Swedish language for PCSX2

%package -n %name-lang-th
Summary: Thai language for PCSX2
Group: Emulators
Requires: %name = %version-%release

%description -n %name-lang-th
Thai language for PCSX2

%package -n %name-lang-tr
Summary: Turkish language for PCSX2
Group: Emulators
Requires: %name = %version-%release

%description -n %name-lang-tr
Turkish language for PCSX2

%package -n %name-lang-cn
Summary: Chinese language for PCSX2
Group: Emulators
Requires: %name = %version-%release

%description -n %name-lang-cn
Chenese language for PCSX2

%package -n %name-lang-tw
Summary: Chinese language for PCSX2
Group: Emulators
Requires: %name = %version-%release

%description -n %name-lang-tw
Chinese language for PCSX2

%prep
%setup -n %name-%version-r%revision-sources
%patch0 -p1

%build
%__mkdir_p %_target_platform
pushd %_target_platform

cmake .. \
	-DCMAKE_INSTALL_PREFIX:PATH=%prefix \
	-DCMAKE_C_FLAGS:STRING='%optflags' \
	-DCMAKE_CXX_FLAGS:STRING='%optflags' \
	-DPACKAGE_MODE:BOOL=TRUE \
	-DCMAKE_BUILD_TYPE:STRING=Release \
	-DPLUGIN_DIR:PATH=%_libdir/%name \
	-DGLSL_SHADER_DIR:PATH=%_gamesdatadir/%name \
	-DGAMEINDEX_DIR:PATH=%_datadir/%name \
	-DXDG_STD:BOOL=TRUE \
	-Wno-dev

popd

%make_build -C %_target_platform

%install
%makeinstall_std -C %_target_platform
%__rm -rf %buildroot%_defaultdocdir/%name

%files
%doc bin/docs/PCSX2_FAQ_%version.pdf bin/docs/PCSX2_Readme_%version.pdf
%_bindir/%{name}*
%_libdir/%name/ps2hw.dat
%_desktopdir/%name.desktop
%_gamesdatadir/%name/*.glsl
%_man1dir/%{name}*
%_datadir/%name/GameIndex.dbf
%_pixmapsdir/%name.xpm

%files -n %name-plugin-cdvdiso
%_libdir/%name/libCDVDiso.so

%files -n %name-plugin-cdvdlinuz
%_libdir/%name/libCDVDlinuz.so

%files -n %name-plugin-cdvdnull
%_libdir/%name/libCDVDnull.so

%files -n %name-plugin-fwnull
%_libdir/%name/libFWnull-0.7.0.so

%files -n %name-plugin-gsdx
%_libdir/%name/libGSdx-0.1.16.so

%files -n %name-plugin-gsnull
%_libdir/%name/libGSnull.so

%files -n %name-plugin-padnull
%_libdir/%name/libPADnull.so

%files -n %name-plugin-spu2null
%_libdir/%name/libSPU2null.so

%files -n %name-plugin-usbnull
%_libdir/%name/libUSBnull-0.7.0.so

%files -n %name-plugin-dev9null
%_libdir/%name/libdev9null-0.5.0.so

%files -n %name-plugin-onepad
%_libdir/%name/libonepad-1.1.0.so

%files -n %name-plugin-spu2x
%_libdir/%name/libspu2x-2.0.0.so

%files -n %name-plugin-zzogl
%_libdir/%name/libzzogl-0.4.0.so

%files -n %name-plugin-zzogl-cg
%_libdir/%name/libzzogl-cg-0.3.0.so

%files -n %name-lang-cz
%_datadir/locale/cs_CZ/LC_MESSAGES/%{name}*.mo

%files -n %name-lang-de
%_datadir/locale/de_DE/LC_MESSAGES/%{name}*.mo

%files -n %name-lang-es
%_datadir/locale/es_ES/LC_MESSAGES/%{name}*.mo

%files -n %name-lang-fi
%_datadir/locale/fi_FI/LC_MESSAGES/%{name}*.mo

%files -n %name-lang-fr
%_datadir/locale/fr_FR/LC_MESSAGES/%{name}*.mo

%files -n %name-lang-hu
%_datadir/locale/hu_HU/LC_MESSAGES/%{name}*.mo

%files -n %name-lang-id
%_datadir/locale/id_ID/LC_MESSAGES/%{name}*.mo

%files -n %name-lang-it
%_datadir/locale/it_IT/LC_MESSAGES/%{name}*.mo

%files -n %name-lang-jp
%_datadir/locale/ja_JP/LC_MESSAGES/%{name}*.mo

%files -n %name-lang-kr
%_datadir/locale/ko_KR/LC_MESSAGES/%{name}*.mo

%files -n %name-lang-my
%_datadir/locale/ms_MY/LC_MESSAGES/%{name}*.mo

%files -n %name-lang-pl
%_datadir/locale/pl_PL/LC_MESSAGES/%{name}*.mo

%files -n %name-lang-br
%_datadir/locale/pt_BR/LC_MESSAGES/%{name}*.mo

%files -n %name-lang-ru
%_datadir/locale/ru_RU/LC_MESSAGES/%{name}*.mo

%files -n %name-lang-se
%_datadir/locale/sv_SE/LC_MESSAGES/%{name}*.mo

%files -n %name-lang-th
%_datadir/locale/th_TH/LC_MESSAGES/%{name}*.mo

%files -n %name-lang-tr
%_datadir/locale/tr_TR/LC_MESSAGES/%{name}*.mo

%files -n %name-lang-cn
%_datadir/locale/zh_CN/LC_MESSAGES/%{name}*.mo

%files -n %name-lang-tw
%_datadir/locale/zh_TW/LC_MESSAGES/%{name}*.mo

%changelog
* Fri Sep 27 2013 Nazarov Denis <nenderus@altlinux.org> 1.0.0-alt1
- Initial build for ALT Linux

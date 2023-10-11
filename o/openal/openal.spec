%def_with pulse
%def_with qt5
%def_without bootstrap

Name: openal
Version: 1.22.2
Release: alt2

Summary: Open Audio Library

License: LGPLv2
Group: Sound
Url: http://kcat.strangesoft.net/openal.html

# Source-url: https://github.com/kcat/openal-soft/archive/refs/tags/%version.tar.gz
Source: %name-%version.tar

Patch0: openal-soft-1.17-alt-config.patch
Patch1: openal-soft-arm_neon-only-for-32bit.patch

BuildRequires: gcc-c++ cmake

BuildRequires: libalsa-devel
%{?_with_qt5:BuildRequires: qt5-base-devel}
%{?_with_pulse:BuildRequires: libpulseaudio-devel}
%if_without bootstrap
BuildRequires: libjack-devel libportaudio2-devel
BuildRequires: libavdevice-devel libswresample-devel libswscale-devel
BuildRequires: libSDL2-devel libSDL2_mixer-devel libSDL_sound-devel
BuildRequires: libdbus-devel libpostproc-devel libsndfile-devel pipewire-libs-devel
%endif

%description
OpenAL Soft is a cross-platform software implementation of the OpenAL 3D
audio API. It's built off of the open-sourced Windows version available
originally from the SVN repository at openal.org. OpenAL provides
capabilities for playing audio in a virtual 3d environment. Distance
attenuation, doppler shift, and directional sound emitters are among
the features handled by the API. More advanced effects, including air
absorption, low-pass filters, and reverb, are available through the
EFX extension. It also facilitates streaming audio, multi-channel buffers,
and audio capture.

%package -n lib%{name}1
Summary: Main library for OpenAL, a free 3D sound library
Group: Sound

%description -n lib%{name}1
This package contains the library needed to run programs dynamically
linked with OpenAL.

%package -n lib%name-devel
Summary: Headers for developing programs that will use OpenAL
Group: Development/C
Requires: lib%{name}1 = %version-%release
Obsoletes: lib%{name}1-devel < %version
Provides: lib%{name}1-devel = %version-%release

%description -n lib%name-devel
This package contains the headers that programmers will need to develop
applications which will use OpenAL, a free 3D audio library.

%package qt
Summary: Qt frontend for configuring OpenAL Soft
Group: Sound
Requires: lib%{name}1 = %EVR

%description qt
The %{name}-qt package contains alsoft-config, a Qt-based tool
for configuring OpenAL features.

%package tools
Summary: OpenAL Soft cli tools
Group: Sound
Requires: lib%{name}1 = %EVR

%description tools
The %{name}-tools package contains various OpenAL command line tools.

%prep
%setup
%ifarch %e2k
sed -i 's,-Winline,,' CMakeLists.txt
# changes "{_mm*}" to "=_mm*"
sed -i "/[{]_mm/{s|[{]_mm|=_mm|;:x;/[}]/!{N;bx};s|[}]||}" \
	alc/effects/convolution.cpp \
	core/mixer/mixer_sse*.cpp core/uhjfilter.cpp
%endif

%build
%cmake_insource \
	-DALSOFT_REQUIRE_OSS=OFF \
	-DALSOFT_CONFIG=ON \
	-DALSOFT_INSTALL_EXAMPLES=ON \
%ifarch %e2k
	-DALSOFT_CPUEXT_NEON=OFF \
%endif
	#

%make_build

%install
%makeinstall_std
#rm -f %buildroot%_bindir/%name-info
mkdir -p %buildroot%_sysconfdir/%name/
install -m0644 alsoftrc.sample %buildroot%_sysconfdir/%name/alsoft.conf

%files -n lib%{name}1
%_bindir/openal-info
%dir %_sysconfdir/%name/
%config(noreplace) %_sysconfdir/%name/alsoft.conf
%_datadir/%name/
%_libdir/*.so.1
%_libdir/*.so.1.*.*

%if_without bootstrap
%files tools
#/usr/bin/alffplay
/usr/bin/alhrtf
/usr/bin/allatency
/usr/bin/alloopback
/usr/bin/almultireverb
/usr/bin/alplay
/usr/bin/alreverb
/usr/bin/alstream

%_bindir/altonegen
%_bindir/alrecord
#_bindir/makehrtf
#_bindir/bsincgen
%endif

%files -n lib%name-devel
%_includedir/AL/
%_libdir/*.so
%_pkgconfigdir/*.pc
%_libdir/cmake/OpenAL/OpenALConfig.cmake
%_libdir/cmake/OpenAL/OpenALTargets-relwithdebinfo.cmake
%_libdir/cmake/OpenAL/OpenALTargets.cmake

%if_with qt5
%files qt
%_bindir/alsoft-config
%endif

# TODO:
# - alrecord, altonegen not packaged (really needed?)

%changelog
* Wed Oct 11 2023 Valery Inozemtsev <shrek@altlinux.ru> 1.22.2-alt2
- rebuild

* Sun Jul 17 2022 Vitaly Lipatov <lav@altlinux.ru> 1.22.2-alt1
- new version 1.22.2 (with rpmrb script)

* Wed Jun 09 2021 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 1.21.1-alt3
- fixed SSE code for Elbrus compiler

* Sat Jun 05 2021 Michael Shigorin <mike@altlinux.org> 1.21.1-alt2
- E2K: fix ftbfs by avoiding x86/arm intrinsics in a cleaner way for now

* Sat Apr 10 2021 Nazarov Denis <nenderus@altlinux.org> 1.21.1-alt1
- Version 1.21.1

* Mon Dec 10 2018 Vitaly Lipatov <lav@altlinux.ru> 1.19.1-alt1
- new version 1.19.1 (with rpmrb script)
- switch to Qt5, build tools subpackage

* Wed Oct 31 2018 Michael Shigorin <mike@altlinux.org> 1.17.2-alt2
- qt knob renamed to qt4 (still on by default)
- replaced e2k arch name with %%e2k macro (grenka@)
- minor spec cleanup
- NB: 1.19.1 available

* Wed Apr 05 2017 Michael Shigorin <mike@altlinux.org> 1.17.2-alt1.1
- BOOTSTRAP: introduce pulse, qt knobs (on by default)
- E2K: avoid lcc-unsupported option

* Sun Dec 11 2016 Vitaly Lipatov <lav@altlinux.ru> 1.17.2-alt1
- new version (1.17.2) with rpmgs script
- change upstream, update package with Fedora spec

* Mon Mar 28 2011 Valery Inozemtsev <shrek@altlinux.ru> 1.13-alt1
- 1.13

* Fri Nov 05 2010 Valery Inozemtsev <shrek@altlinux.ru> 1.11.753-alt3
- rebuild

* Tue Mar 09 2010 Valery Inozemtsev <shrek@altlinux.ru> 1.11.753-alt2
- fixed %_bindir/openal-config attribute (closes: #23099)

* Sun Feb 28 2010 Valery Inozemtsev <shrek@altlinux.ru> 1.11.753-alt1
- 1.11.753


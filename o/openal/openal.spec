%def_with pulse
%def_with qt6

%global soversion 1

Name: openal
Version: 1.25.2
Release: alt1

Summary: OpenAL Soft is a software implementation of the OpenAL 3D audio API
License: LGPL-2.0-or-later
Group: Sound
Url: https://github.com/kcat/openal-soft
Vcs: https://github.com/kcat/openal-soft.git

Source: %name-%version.tar

BuildRequires(Pre): rpm-build-cmake

BuildRequires: gcc-c++
BuildRequires: libalsa-devel
BuildRequires: libjack-devel
BuildRequires: libportaudio2-devel
BuildRequires: libavdevice-devel
BuildRequires: libswresample-devel
BuildRequires: libswscale-devel
BuildRequires: libSDL2-devel
BuildRequires: libSDL2_mixer-devel
BuildRequires: libSDL_sound-devel
BuildRequires: libdbus-devel
BuildRequires: libpostproc-devel
BuildRequires: libsndfile-devel
BuildRequires: pipewire-libs-devel
%{?_with_qt6:BuildRequires: qt6-base-devel}
%{?_with_pulse:BuildRequires: libpulseaudio-devel}

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

%package -n lib%name%soversion
Summary: Main library for OpenAL, a free 3D sound library
Group: System/Libraries
Requires: lib%{name}-common

%description -n lib%name%soversion
This package contains the library needed to run programs dynamically
linked with OpenAL.

%package -n lib%{name}-common
Summary: Common files for OpenAL
Group: System/Libraries
BuildArch: noarch

%description -n lib%{name}-common
This package contains the common files for OpenAL library and applications.

%package -n lib%{name}-devel
Summary: Headers for developing programs that will use OpenAL
Group: Development/C
Requires: lib%name%soversion
Requires: %{name}-tools
Provides: lib%name%{soversion}-devel
Obsoletes: lib%name%{soversion}-devel < %EVR

%description -n lib%{name}-devel
This package contains the headers that programmers will need to develop
applications which will use OpenAL, a free 3D audio library.

%package qt
Summary: Qt frontend for configuring OpenAL Soft
Group: Sound
Requires: lib%name%soversion

%description qt
The %{name}-qt package contains alsoft-config, a Qt-based tool
for configuring OpenAL features.

%package tools
Summary: OpenAL Soft cli tools
Group: Sound
Requires: lib%name%soversion

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
%cmake \
	-DALSOFT_REQUIRE_OSS=OFF \
	-DALSOFT_CONFIG=ON \
	-DALSOFT_INSTALL_EXAMPLES=ON \
%ifarch %e2k
	-DALSOFT_CPUEXT_NEON=OFF \
%endif
%nil

%cmake_build

%install
%cmakeinstall_std
mkdir -p %buildroot%_sysconfdir/%name/
install -Dpm 0644 alsoftrc.sample %buildroot%_sysconfdir/%name/alsoft.conf

%files -n lib%name%soversion
%_libdir/lib%name.so.%{soversion}*

%files -n lib%{name}-common
%dir %_sysconfdir/%name/
%config(noreplace) %_sysconfdir/%name/alsoft.conf
%_datadir/%name/

%files tools
%_bindir/aldebug
%_bindir/aldirect
%_bindir/alhrtf
%_bindir/allafplay
%_bindir/allatency
%_bindir/almultireverb
%_bindir/alplay
%_bindir/alrecord
%_bindir/alreverb
%_bindir/alstream
%_bindir/altonegen
%_bindir/openal-info

%files -n lib%name-devel
%_includedir/AL/
%_libdir/lib%name.so
%_libdir/cmake/OpenAL
%_pkgconfigdir/%name.pc

%if_with qt6
%files qt
%_bindir/alsoft-config
%endif

%changelog
* Fri May 15 2026 Ulysses Apokin <ulysses@altlinux.org> 1.25.2-alt1
- new version 1.25.2

* Fri Apr 24 2026 Ulysses Apokin <ulysses@altlinux.org> 1.25.1-alt1
- new version 1.25.1
- fix FTBFS
- fix to comply with shared libs policy

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


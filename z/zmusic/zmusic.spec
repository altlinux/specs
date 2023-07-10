Name:           zmusic
Version:        1.1.12
Release:        alt1
Summary:        ZDoom component library for music handling
License:        GPL-3.0 and LGPL-v2.1
Group:          Sound
URL:            https://zdoom.org/

Source:         %name-%version.tar
BuildRequires: cmake gcc-c++ rpm-macros-cmake zlib-devel glib2-devel
BuildRequires: libopenal1-devel libsndfile-devel libmpg123-devel libalsa-devel libfluidsynth-devel
Requires: timidity
Requires: timidity-eawpats

%description
This is the music playback code from gzdoom, which was separated into its own
code repository starting with gzdoom-4.4.0.

%package -n libzmusic1
Summary:        ZDoom component library for music handling
Group:          System/Libraries

%description -n libzmusic1
This is the music playback code from gzdoom, which was separated into its own
code repository starting with gzdoom-4.4.0.

%package -n libzmusiclite
Summary: Headers for the ZMusic library
Group: Sound
Requires: libzmusic1 = %version

%description -n libzmusiclite
This subpackage contains the headers for the zmusic library, which is ZDoom's
music component library.

%package devel
Summary:        Headers for the ZMusic library
Group:          System/Libraries
Requires:       libzmusic1 = %version

%description devel
This subpackage contains the headers for the zmusic library, which is ZDoom's
music component library.

%prep
%setup

%build
# There is handcrafted assembler, which LTO does not play nice with.
%define _lto_cflags %nil

%ifarch %ix86
# Allow sw to use intrinsics (functions like _mm_set_sd).
# Guarded by cpuid calls by sw.
export CFLAGS="%optflags -msse -msse2"
export CXXFLAGS="%optflags -msse -msse2"
%endif
%cmake_insource -DNO_STRIP=1 \
	-DCMAKE_SHARED_LINKER_FLAGS="" \
	-DCMAKE_EXE_LINKER_FLAGS="" -DCMAKE_MODULE_LINKER_FLAGS="" \
	-DINSTALL_DOCS_PATH="%_defaultdocdir/%name" \
	-DDYN_FLUIDSYNTH=OFF \
	-DDYN_SNDFILE=OFF -DDYN_MPG123=OFF
%make_build

%install
%makeinstall_std

%files -n libzmusic1
%_libdir/libzmusic.so.1*
%doc licenses/*

%files devel
%_includedir/*
%_libdir/libzmusic.so

%files -n libzmusiclite
%_libdir/libzmusiclite.*

%changelog
* Mon Jul 10 2023 Artyom Bystrov <arbars@altlinux.org> 1.1.12-alt1
- New version 1.1.12.

* Fri May 28 2021 Yuri N. Sedunov <aris@altlinux.org> 1.1.2-alt1.1
- rebuilt against libfluidsynth.so.3

* Thu Jul 16 2020 Artyom Bystrov <arbars@altlinux.org> 1.1.2-alt1
- initial build for ALT Sisyphus (Thanks to OpenSUSE Team!)

* Wed Jun 10 2020 Jan Engelhardt <jengelh@inai.de>
- Initial package (v1.1.2) for build.opensuse.org
- Added system-gme.patch (carryover from gzdoom.spec; modified)

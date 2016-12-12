%define oname openal-soft

Name: openal
Version: 1.17.2
Release: alt1

Summary: Open Audio Library

License: LGPLv2
Group: Sound
URL: http://kcat.strangesoft.net/openal.html

# Source-url: http://kcat.strangesoft.net/openal-releases/openal-soft-%{version}.tar.bz2
Source: %oname-%version.tar
Patch0: openal-soft-1.17-alt-config.patch
Patch1: openal-soft-arm_neon-only-for-32bit.patch

# Automatically added by buildreq on Sun Dec 11 2016
# optimized out: cmake cmake-modules fontconfig libqt4-core libqt4-devel libqt4-gui libqt4-network libqt4-opengl libqt4-qt3support libqt4-script libqt4-sql-sqlite libqt4-svg libqt4-webkit-devel libstdc++-devel pkg-config python-base python-modules python3 python3-base
BuildRequires: gcc-c++ cmake
BuildRequires: qt4-devel
BuildRequires: libalsa-devel libpulseaudio-devel libjack-devel libportaudio2-devel
BuildRequires: libfluidsynth-devel
BuildRequires: libSDL2-devel libSDL2_mixer-devel

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
Requires: lib%{name}1 = %version-%release

%description qt
The %{name}-qt package contains alsoft-config, a Qt-based tool
for configuring OpenAL features.

%prep
%setup -n %oname-%version
%patch0 -p2
%patch1 -p1

%build
%cmake_insource \
	-DALSOFT_REQUIRE_OSS=OFF \
	-DALSOFT_CONFIG=ON
%make_build

%install
%makeinstall_std
#rm -f %buildroot%_bindir/%name-info
mkdir -p %buildroot%_sysconfdir/%name/
install -m0644 alsoftrc.sample %buildroot%_sysconfdir/%name/alsoft.conf

%files -n lib%{name}1
%_bindir/altonegen
%_bindir/makehrtf
%_bindir/bsincgen
%_bindir/openal-info
%dir %_sysconfdir/%name/
%config(noreplace) %_sysconfdir/%name/alsoft.conf
%_datadir/%name/
%_libdir/*.so.1
%_libdir/*.so.1.*.*

%files -n lib%name-devel
%_includedir/AL/
%_libdir/*.so
%_pkgconfigdir/*.pc

%files qt
%_bindir/alsoft-config

%changelog
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



%define sover 1
%define libdrumstick_file libdrumstick-file%sover
%define libdrumstick_alsa libdrumstick-alsa%sover
%define libdrumstick_rt libdrumstick-rt%sover

Name: drumstick
Version: 1.0.2
Release: alt1

Group: System/Libraries
Summary: C++/Qt5 wrapper around multiple MIDI interfaces
Url: http://drumstick.sourceforge.net/
License: GPLv2+

Source: %name-%version.tar

# Automatically added by buildreq on Thu May 26 2016 (-bi)
# optimized out: cmake-modules docbook-dtds elfutils fontconfig fonts-bitmap-misc gcc-c++ libEGL-devel libGL-devel libalsa-devel libgpg-error libjson-c libqt5-core libqt5-dbus libqt5-gui libqt5-network libqt5-svg libqt5-widgets libstdc++-devel libwayland-client libwayland-server perl pkg-config python-base python-modules python3 python3-base qt5-base-devel rpm-build-python3 ruby ruby-stdlibs shared-mime-info xml-common xz
#BuildRequires: cmake docbook-style-xsl doxygen fonts-bitmap-terminus fonts-otf-stix fonts-ttf-dejavu fonts-ttf-google-droid-kufi fonts-ttf-google-droid-sans fonts-ttf-google-droid-serif fonts-ttf-java-1.6.0-sun fonts-type1-urw fonts-type1-xorg graphviz libfluidsynth-devel python-module-google python3-dev qt5-svg-devel qt5-tools-devel rpm-build-ruby xsltproc
BuildRequires: kde-common-devel
BuildRequires: cmake docbook-style-xsl doxygen graphviz xsltproc
BuildRequires: libfluidsynth-devel qt5-svg-devel qt5-tools-devel

%description
The drumstick library is a C++ wrapper around the ALSA library sequencer
interface, using Qt5 objects, idioms and style. OSS, network and Fluidsynth
interfaces are also supported by this library.

%package common
Summary: %name common package
Group: System/Configuration/Other
#BuildArch: noarch
%description common
%name common package

%package -n %libdrumstick_file
Group: System/Libraries
Summary: %name library
Requires: %name-common = %version-%release
%description -n %libdrumstick_file
%name library

%package -n %libdrumstick_alsa
Group: System/Libraries
Summary: %name library
Requires: %name-common = %version-%release
%description -n %libdrumstick_alsa
%name library

%package -n %libdrumstick_rt
Group: System/Libraries
Summary: %name library
Requires: %name-common = %version-%release
%description -n %libdrumstick_rt
%name library

%package devel
Summary: Developer files for %name
Group: Development/Other
Requires: %name-common = %version-%release
%description devel
%summary.

%package examples
Summary: Example programs for %name
Group: System/Libraries
Requires: %name-common = %version-%release
%description examples
This package contains the test/example programs for %name.

%package drumgrid
Group: Sound
Summary: Drum Grid application from %name
Requires: %name-examples = %version-%release
%description drumgrid
This package contains the drumgrid application.

%package guiplayer
Group: Sound
Summary: MIDI player from %name
Requires: %name-examples = %version-%release
%description guiplayer
This package contains the guiplayer application.

%package vpiano
Group: Sound
Summary: Virtual piano application from %name
Requires: %name-examples = %version-%release
%description vpiano
This package contains the vpiano application.

%prep
%setup -n %name-%version%{?svn}

%build
%Kbuild
pushd BUILD*
make doxygen
popd

%install
%Kinstall


%files common
%doc AUTHORS ChangeLog COPYING
%dir %_libdir/drumstick/
%_datadir/mime/packages/drumstick.xml
%_iconsdir/hicolor/*/apps/drumstick.*

%files -n %libdrumstick_file
%_libdir/libdrumstick-file.so.%sover
%_libdir/libdrumstick-file.so.*
%files -n %libdrumstick_alsa
%_libdir/libdrumstick-alsa.so.%sover
%_libdir/libdrumstick-alsa.so.*
%_libdir/drumstick/libdrumstick-rt-alsa-*.so
%files -n %libdrumstick_rt
%_libdir/libdrumstick-rt.so.%sover
%_libdir/libdrumstick-rt.so.*
%_libdir/drumstick/libdrumstick-rt-net-*.so
%_libdir/drumstick/libdrumstick-rt-oss-*.so
%_libdir/drumstick/libdrumstick-rt-synth.so

%files devel
%doc BUILD*/doc/html
%_libdir/libdrumstick-*.so
%_libdir/pkgconfig/drumstick-*.pc
%_includedir/drumstick/
%_includedir/drumstick.h

%files examples
%_bindir/drumstick-buildsmf
%_bindir/drumstick-dumpmid
%_bindir/drumstick-dumpove
%_bindir/drumstick-dumpsmf
%_bindir/drumstick-dumpwrk
%_bindir/drumstick-metronome
%_bindir/drumstick-playsmf
%_bindir/drumstick-sysinfo
%_man1dir/drumstick-buildsmf.*
%_man1dir/drumstick-dumpmid.*
%_man1dir/drumstick-dumpove.*
%_man1dir/drumstick-dumpsmf.*
%_man1dir/drumstick-dumpwrk.*
%_man1dir/drumstick-metronome.*
%_man1dir/drumstick-playsmf.*
%_man1dir/drumstick-sysinfo.*

%files drumgrid
%_bindir/drumstick-drumgrid
%_desktopdir/drumstick-drumgrid.desktop
%_man1dir/drumstick-drumgrid.*

%files guiplayer
%_bindir/drumstick-guiplayer
%_desktopdir/drumstick-guiplayer.desktop
%_man1dir/drumstick-guiplayer.*

%files vpiano
%_bindir/drumstick-vpiano
%_desktopdir/drumstick-vpiano.desktop
%_man1dir/drumstick-vpiano.*

%changelog
* Thu May 26 2016 Sergey V Turchin <zerg@altlinux.org> 1.0.2-alt1
- initial build

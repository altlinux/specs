Name: zynaddsubfx
Version: 2.4.1
Release: alt2.1

Summary: %name is a open source software synthesizer
License: GPLv2+
Group: Sound
Url: http://zynaddsubfx.sourceforge.net/

Packager: Egor Glukhov <kaman@altlinux.org>
Source: %name-%version-%release.tar

BuildRequires: cmake gcc-c++ jackit-devel libGL-devel libXScrnSaver-devel libXau-devel libXcomposite-devel libXcursor-devel libXdmcp-devel libXext-devel libXft-devel libXinerama-devel libXpm-devel libXrandr-devel libXt-devel libXtst-devel libXv-devel libalsa-devel libfftw3-devel libfltk-devel libmxml-devel libxkbfile-devel zlib-devel

BuildPreReq: libpixman-devel libcairo-devel

%description
%name is a open source software synthesizer capable of making a countless
number of instruments, from some common heard from expensive hardware to
interesting sounds that you'll boost to an amazing universe of sounds.

%package alsa
Summary: %name synthesizer with ALSA midi input
Provides: %name = %version-%release
Requires: %name-common = %version-%release
Group: Sound

%description alsa
%name is a open source software synthesizer capable of making a countless
number of instruments, from some common heard from expensive hardware to
interesting sounds that you'll boost to an amazing universe of sounds.

This package contains %name compiled with ALSA midi input and OSS output.

%package jack
Summary: %name synthesizer for using with JACK
Provides: %name = %version-%release
Requires: %name-common = %version-%release
Group: Sound

%description jack
%name is a open source software synthesizer capable of making a countless
number of instruments, from some common heard from expensive hardware to
interesting sounds that you'll boost to an amazing universe of sounds.

This package contains %name compiled for using with JACK.

%package common
Summary: Common files for %name
BuildArch: noarch
Group: Sound

%description common
%name is a open source software synthesizer capable of making a countless
number of instruments, from some common heard from expensive hardware to
interesting sounds that you'll boost to an amazing universe of sounds.

This package contains common files for %name.

%package programs
Summary: External programs from %name distribution
Group: Sound

%description programs
This package contains external programs, which can be used with %name or any
other midi device.

%prep
%setup

%build
for snd in alsa jack
do
    if [ "$snd" != "alsa" ]
    then
        sed -i -e "s/OutputModule .* CACHE/OutputModule $snd CACHE/" src/CMakeLists.txt
    fi
    mkdir build-$snd
    pushd build-$snd
    cmake ../ \
        -DCMAKE_INSTALL_PREFIX=%_prefix \
        -DCMAKE_CXX_FLAGS:STRING="%optflags" \
        -DCMAKE_BUILD_TYPE="Release" \
        -DCMAKE_SKIP_RPATH=YES
    %make_build VERBOSE=1
    popd
done

# external programs
for d in ExternalPrograms/{Controller,Spliter}; do
    pushd $d
    make
    popd
done

%install
# executables
install -pD build-alsa/src/%name %buildroot%_bindir/%name-alsa
install -pD build-jack/src/%name %buildroot%_bindir/%name-jack

# banks and examples
mkdir -p %buildroot%_datadir/%name
cp -r banks examples %buildroot%_datadir/%name

# external programs
install -pD ExternalPrograms/Controller/controller %buildroot%_bindir
install -pD ExternalPrograms/Spliter/spliter %buildroot%_bindir

# icon and desktop files
mkdir -p %buildroot%_pixmapsdir
install -pD %name.png %buildroot%_pixmapsdir
mkdir -p %buildroot%_desktopdir
install -pD %name-alsa.desktop %buildroot%_desktopdir
install -pD %name-jack.desktop %buildroot%_desktopdir

%files alsa
%_bindir/%name-alsa
%_desktopdir/%name-alsa.desktop

%files jack
%_bindir/%name-jack
%_desktopdir/%name-jack.desktop

%files common
%doc AUTHORS.txt bugs.txt ChangeLog doc/ FAQ.txt HISTORY.txt README.txt
%_datadir/%name
%_pixmapsdir/%name.png

%files programs
%_bindir/controller
%_bindir/spliter

%changelog
* Fri Apr 15 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.4.1-alt2.1
- Rebuilt with FLTK 1.3.0.r8575

* Mon Feb 28 2011 Egor Glukhov <kaman@altlinux.org> 2.4.1-alt2
- Fixed to build against fltk 1.3

* Sun Jul 18 2010 Egor Glukhov <kaman@altlinux.org> 2.4.1-alt1
- 2.4.1 from upstream tarball


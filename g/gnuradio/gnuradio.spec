%def_enable docs
%def_disable tests

%define _libexec %prefix/libexec

Name: gnuradio
Version: 3.7.11
Release: alt3
Summary: Software defined radio framework
License: GPLv2+
Group: Engineering
Url: http://www.gnuradio.org
Packager: Anton Midyukov <antohami@altlinux.org>

Source: %name-%version.tar

BuildPreReq: cmake rpm-macros-cmake rpm-build-python rpm-build-gir
BuildRequires: gcc-c++ boost-program_options-devel boost-filesystem-devel pkgconfig(sdl) pkgconfig(alsa) pkgconfig(codec2) pkgconfig(gsl) libgsm-devel pkgconfig(jack) pkgconfig(portaudio-2.0) libqt4-devel libqwt-devel pkgconfig(libusb-1.0) pkgconfig(comedilib) pkgconfig(fftw3f) pkgconfig(thrift) libzeromq-cpp-devel pkgconfig(volk) swig pkgconfig(uhd)
BuildRequires: python-devel python-module-lxml python-module-numpy python-module-cheetah python-module-pygtk python-module-PyQt4 python-module-wx
# 
%if_enabled tests
BuildRequires: cppunit-devel
%endif #tests
%if_enabled docs
BuildRequires: doxygen python-module-sphinx
%endif #docs
BuildRequires: desktop-file-utils xdg-utils
Requires: %name-data = %version-%release
Requires: lib%name = %version-%release

%description
GNU Radio is a collection of software that when combined with minimal
hardware, allows the construction of radios where the actual waveforms
transmitted and received are defined by software. What this means is
that it turns the digital modulation schemes used in today's high
performance wireless devices into software problems.

%package data
Summary: GNU Radio Data Files
Group: Engineering
Buildarch: noarch

%description data
GNU Radio Data Files.

%package docs
Summary: GNU Radio Documentation
Group: Engineering
Buildarch: noarch
Requires: %name = %version-%release

%description docs
GNU Radio Documentation.

%package examples
Summary: GNU Radio Examples
Group: Engineering
Buildarch: noarch
Requires: %name = %version-%release

%description examples
GNU Radio Examples.

%package -n lib%name
Group: Development/C++
Summary: GNU Radio Library

%description -n lib%name
GNU Radio Library.

%package -n lib%name-devel
Group: Development/C++
Summary: GNU Radio Headers
Requires: lib%name = %version-%release
Requires: cmake boost-program_options-devel

%description -n lib%name-devel
GNU Radio Headers.

%prep
%setup

%build
%cmake  -DENABLE_INTERNAL_VOLK=OFF \
        %if_enabled tests
        -DENABLE_TESTING=ON
        %else
        -DENABLE_TESTING=OFF
        %endif #tests
%cmake_build

%install
%cmakeinstall_std

# remove atsc example (bytecompilation problem)
# the examples shouldn't be probably bytecompiled,
# but selective bytecompilation would take a lot of time,
# thus letting it as is
rm -rf %buildroot%_datadir/%name/examples/atsc
rm -rf %buildroot%_datadir/%name/examples/uhd/tags_demo

# remove bundled cmake modules, upstream ticket 592
pushd %buildroot%_libdir/cmake/gnuradio && rm -f `ls | sed '/^FindUHD.cmake\|^Gr.*\|^Gnuradio.*/ d'`
popd

# install desktop file, icons, and MIME configuration to right locations
mkdir -p %buildroot%_desktopdir
desktop-file-install --dir=%buildroot%_desktopdir \
%buildroot%_datadir/%name/grc/freedesktop/gnuradio-grc.desktop
mkdir -p %buildroot%_datadir/mime/packages
mv %buildroot%_datadir/%name/grc/freedesktop/gnuradio-grc.xml %buildroot%_datadir/mime/packages
for x in 32 48 64 128 256
do
  mkdir -p %buildroot%_iconsdir/hicolor/${x}x${x}/apps
  mv %buildroot%_datadir/%name/grc/freedesktop/grc-icon-${x}.png %buildroot%_iconsdir/hicolor/${x}x${x}/apps/gnuradio-grc.png
done
rm -f %buildroot%_datadir/%name/grc/freedesktop/*
rmdir %buildroot%_datadir/%name/grc/freedesktop

# remove verify_elf problem files
rm -f %buildroot%_datadir/%name/examples/audio/dial_tone
rm -f %buildroot%_datadir/%name/examples/qt-gui/display_qt
rm -f %buildroot%_datadir/%name/examples/fcd/fcd_nfm_rx

%files
%_bindir/*
%_sysconfdir/%name
%python_sitelibdir/%name
%python_sitelibdir/grc_%name
%python_sitelibdir/pmt
%_iconsdir/hicolor/*/apps/*
%_desktopdir/*.desktop
%_datadir/mime/packages/*
%_libexec/%name

%files data
%_datadir/%name
%exclude %_datadir/%name/examples
%_docdir/%name-%version
%if_enabled docs
%exclude %_docdir/%name-%version/xml
%exclude %_docdir/%name-%version/html
%endif #docs

%if_enabled docs
%files docs
%exclude %_docdir/%name-%version/xml
%exclude %_docdir/%name-%version/html
%endif #docs

%files examples
%_datadir/%name/examples

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_libdir/*.so
%_libdir/cmake/%name
%_includedir/%name
%_includedir/pmt
%_pkgconfigdir/*.pc

%changelog
* Sun Dec 17 2017 Anton Midyukov <antohami@altlinux.org> 3.7.11-alt3
- fix build
- enable support gr-uhd

* Tue Oct 03 2017 Anton Farygin <rider@altlinux.ru> 3.7.11-alt2
- rebuilt for libcodec2 0.7

* Mon Aug 14 2017 Anton Midyukov <antohami@altlinux.org> 3.7.11-alt1
- Initial build for ALT Sisyphus.

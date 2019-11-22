# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

%def_disable docs
%def_enable tests

%define _libexec %prefix/libexec

Name: gnuradio
Version: 3.8.0.0
Release: alt1
Summary: Software defined radio framework
License: GPLv2+
Group: Engineering
Url: http://www.gnuradio.org
Packager: Anton Midyukov <antohami@altlinux.org>

Source: %name-%version.tar
Patch0: fix-gnuradio-qtgui.pc.patch
Patch1: gnuradio-3.8.0-python3-fix.patch

# upstream patch
Patch10: 0034-GRC-update-cloned-port-s-dtype.patch
Patch11: 0035-Replace-tabs-with-spaces.patch

BuildRequires(pre): rpm-macros-cmake rpm-build-python3 rpm-build-gir
BuildRequires: gcc-c++ cmake
BuildRequires: liborc-devel
BuildRequires: libgtk+3-gir-devel
BuildRequires: libgmpxx-devel
BuildRequires: boost-filesystem-devel
BuildRequires: boost-interprocess-devel
BuildRequires: boost-program_options-devel
BuildRequires: libgsm-devel
BuildRequires: qt5-base-devel
BuildRequires: liblog4cpp-devel
BuildRequires: mpir-devel
BuildRequires: libqwt6-qt5-devel
BuildRequires: libzeromq-cpp-devel
BuildRequires: pkgconfig(alsa)
BuildRequires: pkgconfig(codec2)
BuildRequires: pkgconfig(comedilib)
BuildRequires: pkgconfig(fftw3f)
BuildRequires: pkgconfig(gsl)
BuildRequires: pkgconfig(jack)
BuildRequires: pkgconfig(portaudio-2.0)
BuildRequires: pkgconfig(thrift)
BuildRequires: pkgconfig(uhd)
BuildRequires: libSDL-devel
BuildRequires: libvolk-devel
BuildRequires: python3-devel
BuildRequires: python3-module-yaml
BuildRequires: python3-module-mako
BuildRequires: python3-module-lxml
BuildRequires: python3-module-numpy
BuildRequires: python3-module-pygobject3-devel
BuildRequires: python3-module-pycairo-devel
BuildRequires: python3-module-PyQt5
BuildRequires: python3-module-click-plugins
BuildRequires: swig

%if_enabled tests
BuildRequires: pkgconfig(cppunit)
%endif #tests
%if_enabled docs
BuildRequires: doxygen python3-module-sphinx
BuildRequires: /usr/bin/latex /usr/bin/dvips tex(dvips.def)
%endif #docs
BuildRequires: desktop-file-utils xdg-utils
%add_python3_req_skip PyQt4 PyQt4.Qwt5
%add_python3_req_skip gnuradio.ctrlport.GNURadio

# skip requires on python2
%set_findreq_skiplist %_datadir/%name/modtool/templates/*

Obsoletes: gnuradio-data < 3.8
Obsoletes: libgnuradio < 3.8

%description
GNU Radio is a collection of software that when combined with minimal
hardware, allows the construction of radios where the actual waveforms
transmitted and received are defined by software. What this means is
that it turns the digital modulation schemes used in today's high
performance wireless devices into software problems.

%package docs
Summary: GNU Radio Documentation
Group: Engineering
Buildarch: noarch
Requires: %name = %EVR

%description docs
GNU Radio Documentation.

%package examples
Summary: GNU Radio Examples
Group: Engineering
Buildarch: noarch
Requires: %name = %EVR

%description examples
GNU Radio Examples.

%package devel
Group: Development/C++
Summary: GNU Radio Headers
Requires: %name = %EVR
Requires: cmake boost-program_options-devel
Provides: libgnuradio-devel = %EVR

%description devel
GNU Radio Headers.

%prep
%setup
%patch0 -p1
%patch1 -p1
%patch10 -p1
%patch11 -p1

%build
%cmake \
	-DENABLE_INTERNAL_VOLK=OFF \
	-DGR_PYTHON_DIR=%python3_sitelibdir \
	-DPYTHON_EXECUTABLE=%__python3 \
%if_enabled tests
	-DENABLE_TESTING=ON
%else
	-DENABLE_TESTING=OFF
%endif #tests
%cmake_build

%install
%cmakeinstall_std

# Remove extraneous desktop/icon/mime files
rm -r %buildroot%_datadir/%name/grc/freedesktop
rm -r %buildroot%_datadir/icons/gnome

# remove verify_elf problem files
rm %buildroot%_datadir/%name/examples/audio/dial_tone
rm %buildroot%_datadir/%name/examples/qt-gui/display_qt
rm %buildroot%_datadir/%name/examples/uhd/tags_demo

%files
%_bindir/*
%_sysconfdir/%name
%_iconsdir/hicolor/*/apps/*
%_desktopdir/*.desktop
%_datadir/mime/packages/*
%_libdir/*.so.*
%_libexec/%name
%_datadir/%name
%exclude %_datadir/%name/examples
%_docdir/%name-%version
%python3_sitelibdir/%name
%python3_sitelibdir/pmt
%if_enabled docs
%exclude %_docdir/%name-%version/xml
%exclude %_docdir/%name-%version/html
%endif #docs

%if_enabled docs
%files docs
%_docdir/%name-%version/xml
%_docdir/%name-%version/html
%endif #docs

%files examples
%_datadir/%name/examples

%files devel
%_libdir/*.so
%_libdir/cmake/%name
%_includedir/%name
%_includedir/pmt
%_pkgconfigdir/*.pc

%changelog
* Wed Dec 25 2019 Anton Midyukov <antohami@altlinux.org> 3.8.0.0-alt1
- new version 3.8.0.0
- switch to python3
- Obsoletes: gnuradio-data libgnuradio libgnuradio-devel < 3.8
- rename libgnuradio-devel to gnuradio-devel

* Thu Dec 05 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 3.7.13.4-alt2
- Rebuilt with boost-1.71.0.

* Sat Dec 29 2018 Anton Midyukov <antohami@altlinux.org> 3.7.13.4-alt1
- new version 3.7.13.4
- build with libqwt6

* Thu Aug 09 2018 Anton Farygin <rider@altlinux.ru> 3.7.12.0-alt3
- rebuilt with libcodec2-0.8.1

* Wed Jun 06 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 3.7.12.0-alt2
- NMU: rebuilt with boost-1.67.0.

* Mon Apr 23 2018 Anton Midyukov <antohami@altlinux.org> 3.7.12.0-alt1
- new version 3.7.12.0

* Fri Mar 30 2018 Anton Midyukov <antohami@altlinux.org> 3.7.11-alt5
- fix buildrequires

* Mon Mar 19 2018 Anton Midyukov <antohami@altlinux.org> 3.7.11-alt4
- rebuilt with uhd-3.11.0

* Sun Dec 17 2017 Anton Midyukov <antohami@altlinux.org> 3.7.11-alt3
- fix build
- enable support gr-uhd

* Tue Oct 03 2017 Anton Farygin <rider@altlinux.ru> 3.7.11-alt2
- rebuilt for libcodec2 0.7

* Mon Aug 14 2017 Anton Midyukov <antohami@altlinux.org> 3.7.11-alt1
- Initial build for ALT Sisyphus.

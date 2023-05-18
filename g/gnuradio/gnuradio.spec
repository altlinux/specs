# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

%def_disable docs
%def_enable tests

%define _libexec %prefix/libexec

Name: gnuradio
Version: 3.10.5.1
Release: alt1
Summary: Software defined radio framework
License: GPLv2+
Group: Engineering
Url: http://www.gnuradio.org

Source: %name-%version.tar
Patch0: fix-gnuradio-qtgui.pc.patch

# uhd not available for i586, armh
ExcludeArch: %ix86 %arm

%add_python3_path %_datadir/%name
%add_findreq_skiplist %_datadir/%name/examples/*.grc

BuildRequires(pre): rpm-macros-cmake rpm-macros-python3
BuildRequires: rpm-build-python3 rpm-build-gir
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
#BuildRequires: pkgconfig(thrift)
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
BuildRequires: python3-module-pyqtgraph
BuildRequires: python3-module-scipy-devel
BuildRequires: pybind11-devel
BuildRequires: libsndfile-devel
BuildRequires: libunwind-devel
BuildRequires: mpir-devel
BuildRequires: libgmp-devel
BuildRequires: libnumpy-py3-devel
BuildRequires: doxygen
#BuildRequires: texlive
BuildRequires: libspdlog-devel
BuildRequires: SoapySDR-devel

%if_enabled tests
BuildRequires: pkgconfig(cppunit)
%endif #tests
%if_enabled docs
BuildRequires: doxygen python3-module-sphinx
BuildRequires: /usr/bin/latex /usr/bin/dvips tex(dvips.def)
%endif #docs
BuildRequires: desktop-file-utils xdg-utils
%add_python3_req_skip PyQt5.Qwt
%add_python3_req_skip gnuradio.ctrlport.GNURadio

Obsoletes: gnuradio-data < 3.8
Obsoletes: libgnuradio < 3.8
Obsoletes: gnuradio-examples < 3.9.2.0-alt2

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

# remove verify_elf problem files
rm %buildroot%_datadir/%name/examples/audio/dial_tone
rm %buildroot%_datadir/%name/examples/qt-gui/display_qt
rm %buildroot%_datadir/%name/examples/uhd/tags_demo

# fix *.grc files permissions
find %buildroot%_datadir/ -name '*.grc' | xargs \
	chmod 644

# fix shebang
find %buildroot%_datadir/%name -name '*.py' | xargs sed -i \
	-e 's:/usr/bin/env python$:%__python3:'

%files
%_bindir/*
%_sysconfdir/%name
%_iconsdir/hicolor/*/apps/*
%_desktopdir/*.desktop
%_datadir/mime/packages/*
%_libdir/*.so.*
%_libexec/%name
%_datadir/%name
%_docdir/%name-%version
%python3_sitelibdir/%name
%python3_sitelibdir/pmt
%if_enabled docs
%exclude %_docdir/%name-%version/xml
%exclude %_docdir/%name-%version/html
%endif #docs
%_datadir/metainfo/org.gnuradio.grc.metainfo.xml
%_man1dir/*.1.*

%if_enabled docs
%files docs
%_docdir/%name-%version/xml
%_docdir/%name-%version/html
%endif #docs

%files devel
%_libdir/*.so
%_libdir/cmake/%name
%_includedir/%name
%_includedir/pmt
%_pkgconfigdir/*.pc

%changelog
* Fri Feb 24 2023 Anton Midyukov <antohami@altlinux.org> 3.10.5.1-alt1
- new version 3.10.5.1

* Fri Jan 28 2022 Anton Midyukov <antohami@altlinux.org> 3.9.5.0-alt1
- new version 3.9.5.0

* Fri Sep 24 2021 Anton Midyukov <antohami@altlinux.org> 3.9.2.0-alt2
- ExcludeArch: %ix86 %arm
- Drop examples subpackage

* Mon Jun 28 2021 Anton Midyukov <antohami@altlinux.org> 3.9.2.0-alt1
- new version 3.9.2.0

* Sat May 08 2021 Anton Midyukov <antohami@altlinux.org> 3.9.1.0-alt1
- new version 3.9.1.0
- update buildrequires

* Sat Nov 07 2020 Anton Midyukov <antohami@altlinux.org> 3.8.1.0-alt3
- Rebuilt without pkgconfig(thrift)

* Wed Jun 10 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 3.8.1.0-alt2
- Rebuilt with boost-1.73.0.

* Thu May 21 2020 Anton Midyukov <antohami@altlinux.org> 3.8.1.0-alt1
- new version 3.8.1.0

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

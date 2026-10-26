# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

%def_disable docs
%def_enable tests

Name: gnuradio
Version: 3.10.12.0
Release: alt3

Summary: Software defined radio framework
License: GPL-2.0-or-later
Group: Engineering
URL: https://www.gnuradio.org
VCS: https://github.com/gnuradio/gnuradio.git

Source: %name-%version.tar
Patch0: fix-gnuradio-qtgui.pc.patch

# https://github.com/gnuradio/gnuradio/pull/7918
Patch1: boost-1.89-system.patch

Requires: typelib(Gtk) = 3.0

%add_python3_path %_datadir/%name
%add_findreq_skiplist %_datadir/%name/examples/*.grc

BuildRequires(pre): rpm-macros-cmake
BuildRequires(pre): rpm-macros-python3
BuildRequires: rpm-build-python3
BuildRequires: rpm-build-gir
BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: liborc-devel
BuildRequires: libgtk+3-gir-devel
BuildRequires: libgmpxx-devel
BuildRequires: boost-filesystem-devel
BuildRequires: boost-interprocess-devel
BuildRequires: boost-program_options-devel
BuildRequires: libgsm-devel
BuildRequires: qt5-base-devel
BuildRequires: liblog4cpp-devel
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
BuildRequires: pkgconfig(libiio)
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
BuildRequires: python3-module-pygccxml
BuildRequires: python3-module-jsonschema
BuildRequires: pybind11-devel
BuildRequires: libsndfile-devel
BuildRequires: libunwind-devel
BuildRequires: libgmp-devel
BuildRequires: libnumpy-py3-devel
BuildRequires: doxygen
BuildRequires: graphviz
BuildRequires: mathjax
BuildRequires: xdg-utils
BuildRequires: libspdlog-devel
BuildRequires: SoapySDR-devel

%if_enabled tests
BuildRequires: ctest
BuildRequires: pkgconfig(cppunit)
BuildRequires: python3-module-zmq
%endif

%if_enabled docs
BuildRequires: doxygen
BuildRequires: python3-module-sphinx
BuildRequires: texlive
BuildRequires: /usr/bin/latex
BuildRequires: /usr/bin/dvips
BuildRequires: tex(dvips.def)
%endif

%add_python3_req_skip PyQt5.Qwt
%add_python3_req_skip gnuradio.ctrlport.GNURadio
%add_python3_req_skip Generate_LDPC_matrix_functions

Obsoletes: gnuradio-data < 3.8
Obsoletes: libgnuradio < 3.8
Obsoletes: gnuradio-examples < 3.9.2.0-alt2

%description
GNU Radio is a free & open-source signal processing runtime and signal
processing software development toolkit. Originally developed for use
with software-defined radios and for simulating wireless communications,
it's robust capabilities have led to adoption in hobbyist, academic,
and commercial environments. GNU Radio has found use in software-defined
radio, digital communications, nuclear physics, high-energy particle
physics, astrophysics, radio astronomy and more!

%package libs
Summary: GNU Radio shared libraries
Group: System/Libraries

%description libs
%summary.

%package docs
Summary: GNU Radio documentation
Group: Engineering
Buildarch: noarch
Requires: %name = %EVR

%description docs
%summary.

%package devel
Group: Development/C++
Summary: Development files for GNU Radio
Requires: %name = %EVR
Requires: cmake boost-program_options-devel
Provides: libgnuradio-devel = %EVR

%description devel
%summary.

%prep
%setup
%autopatch -p1

%build
%cmake \
	-DENABLE_INTERNAL_VOLK=OFF \
	-DGR_PYTHON_DIR=%python3_sitelibdir \
	-DPYTHON_EXECUTABLE=%__python3 \
	-DENABLE_TESTING=%{?_enable_tests:ON}%{!?_enable_tests:OFF}
%cmake_build

%install
%cmake_install

# remove verify_elf problem files
rm %buildroot%_datadir/%name/examples/audio/dial_tone
rm %buildroot%_datadir/%name/examples/qt-gui/display_qt
rm %buildroot%_datadir/%name/examples/uhd/tags_demo

# fix *.grc files permissions
find %buildroot%_datadir/ -name '*.grc' -print0 | xargs -r0 \
	chmod 644

%python3_fix_shebang %buildroot%_datadir/%name

# desktop file
desktop-file-install --dir=%buildroot%_desktopdir \
  grc/scripts/freedesktop/gnuradio-grc.desktop
# mime
install -Dp grc/scripts/freedesktop/gnuradio-grc.xml \
  %buildroot%_datadir/mime/packages/gnuradio-grc.xml
# metainfo
install -Dp grc/scripts/freedesktop/org.gnuradio.grc.metainfo.xml \
  %buildroot%_datadir/metainfo/org.gnuradio.grc.metainfo.xml
# icons
for i in 16 24 32 48 64 128 256; do
  install -Dp grc/scripts/freedesktop/grc-icon-${i}.png \
    %buildroot%_iconsdir/hicolor/${i}x${i}/apps/gnuradio-grc.png
done

%if_enabled tests
%check
# for GUI test
export QT_QPA_PLATFORM=offscreen
# Few tests hang completely on the server but run OK locally
%ctest --timeout 60 ||:
%endif

%files
%_bindir/*
%_sysconfdir/%name
%_datadir/%name
%_iconsdir/hicolor/*/apps/gnuradio-grc.png
%_desktopdir/gnuradio-grc.desktop
%_datadir/metainfo/org.gnuradio.grc.metainfo.xml
%_datadir/mime/packages/*
%_datadir/bash-completion/completions/gr_modtool
%_datadir/zsh/site-functions/_gr_modtool
%_datadir/fish/vendor_completions.d/gr_modtool.fish
%python3_sitelibdir/%name
%python3_sitelibdir/pmt
%_man1dir/*.1.*
%_docdir/%name-%version
%if_enabled docs
%exclude %_docdir/%name-%version/xml
%exclude %_docdir/%name-%version/html
%endif

%files libs
%_libdir/*.so.*

%if_enabled docs
%files docs
%_docdir/%name-%version/xml
%_docdir/%name-%version/html
%endif

%files devel
%_libdir/*.so
%_libdir/cmake/%name
%_includedir/%name
%_includedir/pmt
%_pkgconfigdir/*.pc

%changelog
* Fri Oct 23 2026 Valery Zabrovsky <brow@altlinux.org> 3.10.12.0-alt3
- Update descriptions.
- Drop ExcludeArch.
- Add check section.
- Minor spec cleanup.

* Thu Jul 23 2026 Valery Zabrovsky <brow@altlinux.org> 3.10.12.0-alt2
- Fix FTBFS with boost 1.91.0.

* Tue Jun 03 2025 Anton Midyukov <antohami@altlinux.org> 3.10.12.0-alt1
- New version 3.10.12.0.

* Sun May 11 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 3.10.11.0-alt4
- split gnuradio libraries onto own subpackage

* Sat Nov 02 2024 Anton Midyukov <antohami@altlinux.org> 3.10.11.0-alt3
- remove "BuildRequires: mpir-devel" (now for sure)

* Thu Oct 31 2024 Anton Midyukov <antohami@altlinux.org> 3.10.11.0-alt2
- remove "BuildRequires: mpir-devel"

* Mon Aug 12 2024 Anton Midyukov <antohami@altlinux.org> 3.10.11.0-alt1
- New version 3.10.11.0.

* Mon Jan 29 2024 Anton Midyukov <antohami@altlinux.org> 3.10.9.2-alt1
- New version 3.10.9.2.
- add ppc64le to ExcludeArch

* Thu Jan 04 2024 Anton Midyukov <antohami@altlinux.org> 3.10.9.1-alt1
- New version 3.10.9.1.

* Fri Nov 10 2023 Anton Midyukov <antohami@altlinux.org> 3.10.8.0-alt1
- New version 3.10.8.0.

* Mon Aug 14 2023 Anton Midyukov <antohami@altlinux.org> 3.10.7.0-alt1
- New version 3.10.7.0.

* Thu Jun 15 2023 Anton Midyukov <antohami@altlinux.org> 3.10.6.0-alt1
- New version 3.10.6.0.

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

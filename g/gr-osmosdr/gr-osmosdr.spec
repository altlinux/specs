Name: gr-osmosdr
Url: http://sdr.osmocom.org/trac/wiki/GrOsmoSDR
Version: 0.2.4
Release: alt1
License: GPL-3.0-or-later
Group: Engineering
Summary: Common software API for various radio hardware
Packager: Anton Midyukov <antohami@altlinux.org>

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake rpm-build-python3
BuildRequires: cmake gcc-c++
BuildRequires: gnuradio-devel
BuildRequires: boost-program_options-devel
BuildRequires: doxygen
BuildRequires: graphviz
BuildRequires: pybind11-devel
BuildRequires: rtl-sdr-devel
BuildRequires: uhd-devel
BuildRequires: hackrf-devel
BuildRequires: libbladerf-devel
BuildRequires: liborc-devel
BuildRequires: python3-devel
BuildRequires: python3-module-mako
BuildRequires: liblog4cpp-devel
BuildRequires: mpir-devel
BuildRequires: libgmp-devel
BuildRequires: libfftw3-devel
BuildRequires: libsndfile-devel
BuildRequires: libnumpy-py3-devel
BuildRequires: libunwind-devel

# uhd not available for %ix86 %arm
ExcludeArch: %ix86 %arm

%description
Primarily gr-osmosdr supports the OsmoSDR hardware, but it also
offers a wrapper functionality for FunCube Dongle,  Ettus UHD
and rtl-sdr radios. By using gr-osmosdr source you can take
advantage of a common software api in your application(s)
independent of the underlying radio hardware.

%package devel
Summary: Development files for gr-osmosdr
Group: Engineering
Requires: %name = %version-%release

%description devel
Development files for gr-osmosdr.

%package doc
Summary: Documentation files for gr-osmosdr
Group: Engineering
BuildArch: noarch

%description doc
Documentation files for gr-osmosdr.

%prep
%setup

# TODO fix the lib location nicer way
%__subst 's|/lib/|/%_lib/|g' CMakeLists.txt

%build
mkdir build
pushd build
%cmake_insource -DENABLE_DOXYGEN=on -DGR_PKG_DOC_DIR=%_docdir/%name ..
%make_build
popd

%install
pushd build
%makeinstall_std
popd

# Create pkgconfig .pc file
mkdir -p %buildroot%_pkgconfigdir
cat <<EOF > %buildroot%_pkgconfigdir/gnuradio-osmosdr.pc
prefix=%_prefix
exec_prefix=\${prefix}
libdir=\${exec_prefix}/%_lib
includedir=\${prefix}/include

Name: gnuradio-osmosdr
Description: GNU Radio block for various radio hardware
Url: http://sdr.osmocom.org/trac/wiki/GrOsmoSDR
Version: %version
Requires: gnuradio-runtime gnuradio-blocks
Requires.private:
Conflicts:
Cflags: -I\${includedir} -I%_includedir
Libs: -L\${libdir} -lgnuradio-osmosdr
Libs.private: -L\${libdir}
EOF

%files
%doc AUTHORS COPYING
%exclude %_docdir/%name/html
%exclude %_docdir/%name/xml
%_bindir/*
%_libdir/*.so.*
%python3_sitelibdir/*
%_datadir/gnuradio/grc/blocks/*

%files devel
%_includedir/osmosdr
%_libdir/*.so
%_libdir/cmake/osmosdr/*
%_pkgconfigdir/*.pc

%files doc
%doc %_docdir/%name/html
%doc %_docdir/%name/xml

%changelog
* Wed Mar 15 2023 Anton Midyukov <antohami@altlinux.org> 0.2.4-alt1
- New version 0.2.4.

* Fri Sep 24 2021 Anton Midyukov <antohami@altlinux.org> 0.2.3-alt2.20210129
- ExcludeArch: %ix86 %arm

* Sat May 08 2021 Anton Midyukov <antohami@altlinux.org> 0.2.3-alt1.20210129
- new snapshot

* Wed Jun 10 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 0.2.0-alt2
- Rebuilt with boost-1.73.0.

* Mon Mar 23 2020 Anton Midyukov <antohami@altlinux.org> 0.2.0-alt1
- new version 0.2.0
- generate .pc in spec as dropped upstream

* Sun Nov 24 2019 Anton Midyukov <antohami@altlinux.org> 0.1.4-alt5.20190514
- New snapshot
- Fix build with gnuradio 3.8

* Thu Feb 07 2019 Anton Midyukov <antohami@altlinux.org> 0.1.4-alt4.20180627
- New snapshot

* Thu May 31 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.1.4-alt3.20170612.S1.1
- NMU: rebuilt with boost-1.67.0

* Sun Apr 22 2018 Anton Midyukov <antohami@altlinux.org> 0.1.4-alt3.20170612.S1
- rebuilt with libvolk 1.4

* Fri Mar 30 2018 Anton Midyukov <antohami@altlinux.org> 0.1.4-alt2.20170612.1
- fix buildrequires

* Sun Oct 22 2017 Anton Midyukov <antohami@altlinux.org> 0.1.4-alt1.20170612.1
- Initial build for ALT Sisyphus.

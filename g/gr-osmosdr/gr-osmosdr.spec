Name: gr-osmosdr
Url: http://sdr.osmocom.org/trac/wiki/GrOsmoSDR
Version: 0.1.4
Release: alt5.20190514
License: GPLv3+
Group: Engineering
Summary: Common software API for various radio hardware
Packager: Anton Midyukov <antohami@altlinux.org>

Source: %name-%version.tar
Patch0: gr-osmosdr-0.1.1-pkgconfig-fix.patch
Patch1: gr-osmosdr-0.1.4-gnuradio38-blocks-fix.patch
Patch2: gr-osmosdr-0.1.4-python3-fix.patch

BuildRequires(pre): rpm-macros-cmake rpm-build-python3
BuildRequires: cmake gcc-c++
BuildRequires: gnuradio-devel
BuildRequires: boost-program_options-devel
BuildRequires: doxygen
BuildRequires: graphviz
BuildRequires: swig
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
Requires: %name = %version-%release
BuildArch: noarch

%description doc
Documentation files for gr-osmosdr.

%prep
%setup

%patch0 -p1 -b .pkgconfig-fix
%patch1 -p1 -b .gnuradio38-blocks-fix
%patch2 -p1 -b .python3-fix

# TODO fix the lib location nicer way
sed -i 's|/lib/|/%_lib/|g' CMakeLists.txt

%build
mkdir build
pushd build
%cmake_insource -DENABLE_DOXYGEN=on -DGR_PKG_DOC_DIR=%_docdir/%name ..
# parallel build is broken
make
popd

%install
pushd build
%makeinstall_std
popd

# fix docs
mkdir -p %buildroot%_docdir/%name
mv %buildroot%_docdir/gnuradio*/* %buildroot%_docdir/%name
rmdir %buildroot%_docdir/gnuradio*

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
%_pkgconfigdir/*.pc

%files doc
%doc %_docdir/%name/html
%doc %_docdir/%name/xml

%changelog
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

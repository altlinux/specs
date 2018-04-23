Name: gr-osmosdr
Url: http://sdr.osmocom.org/trac/wiki/GrOsmoSDR
Version: 0.1.4
Release: alt3.20170612.S1
License: GPLv3+
Group: Engineering
Summary: Common software API for various radio hardware
Packager: Anton Midyukov <antohami@altlinux.org>

Source: %name-%version.tar
Patch: gr-osmosdr-0.1.1-pkgconfig-fix.patch

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake gcc-c++ python-devel libgnuradio-devel boost-program_options-devel doxygen
BuildRequires: graphviz swig rtl-sdr-devel uhd-devel hackrf-devel libbladerf-devel
BuildRequires: python-module-Cheetah

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

%build
%cmake -DENABLE_DOXYGEN=on -DGR_PKG_DOC_DIR=%_docdir/%name ..
%cmake_build

%install
%cmakeinstall_std

%files
%exclude %_docdir/%name/html
%exclude %_docdir/%name/xml
%doc AUTHORS COPYING
%_bindir/*
%_libdir/*.so.*
%python_sitelibdir/*
%_datadir/gnuradio/grc/blocks/*

%files devel
%_includedir/osmosdr
%_libdir/*.so
%_pkgconfigdir/*.pc

%files doc
%doc %_docdir/%name/html
%doc %_docdir/%name/xml

%changelog
* Sun Apr 22 2018 Anton Midyukov <antohami@altlinux.org> 0.1.4-alt3.20170612.S1
- rebuilt with libvolk 1.4

* Fri Mar 30 2018 Anton Midyukov <antohami@altlinux.org> 0.1.4-alt2.20170612.1
- fix buildrequires

* Sun Oct 22 2017 Anton Midyukov <antohami@altlinux.org> 0.1.4-alt1.20170612.1
- Initial build for ALT Sisyphus.

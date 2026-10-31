%define soname 3

Name: daq
Version: 3.0.28
Release: alt1
Summary: Data Acquisition Library
License: GPL-2.0-only
Group: System/Libraries
URL: https://github.com/snort3/libdaq
# Source-url: https://github.com/snort3/libdaq/archive/v%version/libdaq-%version.tar.gz
Source: daq-%version.tar
Packager: Ilya Mashkin <oddity@altlinux.ru>

BuildRequires: gcc-c++ libpcap-devel

%description
Data Acquisition library for Snort.

This package contains daqtest, a tool to test DAQ modules.

%package -n libdaq%soname
Summary: The shared library for Snort Data Acquisition
Group: System/Libraries
# the DAQ modules in %_libdir/daq/ moved from libdaq 2.x
Obsoletes: libdaq < 3

%package -n libdaq-devel
Summary: Header files for libdaq
Summary(ru_RU.UTF-8): Заголовочные файлы для libdaq
Group: Development/C
Requires: libdaq%soname = %EVR

%description -n libdaq%soname
This package contains libdaq shared library and DAQ modules
for Snort Data Acquisition.

%description -n libdaq-devel
This package contains libdaq development files for
Snort Data Acquisition.

This package is required for development of applications that
utilize libdaq.

%prep
%setup

%build
%autoreconf
%configure --disable-static
# get rid of rpath
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
%make_build

%install
%makeinstall_std
find %buildroot -type f -name "*.la" -delete -print
# static DAQ modules for static linking into Snort: we link dynamically
rm -v %buildroot%_libdir/libdaq_static_*.a %buildroot%_pkgconfigdir/libdaq_static_*.pc
rm -v %buildroot%_bindir/daqtest-static

%files
%doc README.md ChangeLog.md
%_bindir/daqtest

%files -n libdaq%soname
%_libdir/libdaq.so.%{soname}*
%dir %_libdir/daq
%_libdir/daq/*.so

%files -n libdaq-devel
%_includedir/daq*.h
%_libdir/libdaq.so
%_pkgconfigdir/libdaq.pc

%changelog
* Fri Oct 30 2026 Vitaly Lipatov <lav@altlinux.ru> 3.0.28-alt1
- NMU: update to libdaq 3.0.28.
- removed BuildRequires: autoconf, automake, flex.
- added BuildRequires: gcc-c++ for the C++ build.

* Sat May 15 2021 Ilya Mashkin <oddity@altlinux.ru> 2.0.7-alt1
- 2.0.7

* Sat Mar 13 2021 Ilya Mashkin <oddity@altlinux.ru> 2.0.6-alt1
- 2.0.6

* Fri Dec 19 2014 Anton Farygin <rider@altlinux.ru> 2.0.4-alt1
- new version

* Tue May 27 2014 Timur Aitov <timonbl4@altlinux.org> 2.0.2-alt1
- new version

* Wed Jan 09 2013 Timur Aitov <timonbl4@altlinux.org> 2.0.0-alt1
- new version

* Tue Sep 25 2012 Anton Farygin <rider@altlinux.ru> 1.1.1-alt1
- first build for Sisyphus

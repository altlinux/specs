# TODO: add pybind11

Name: libbroker
Version: 2.2.0
Release: alt1

Summary: Zeek's Messaging Library 

Group: Networking/Other
License: BSD
Url: https://github.com/zeek/broker

# Source-url: https://github.com/zeek/broker/archive/v%version.tar.gz
Source: %name-%version.tar

Patch1: libbroker-external-sqlite.patch

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake gcc-c++
BuildRequires: libcaf-devel
BuildRequires: libsqlite3-devel
BuildRequires: libssl-devel

BuildRequires: zeek-cmake >= 20210717
# for doc
#BuildRequires: python-module-sphinx

%description
The Broker library implements Bro's high-level communication patterns:

* remote logging
* remote events
* distributed data stores

%package devel
Summary: Development file for %name
Requires: %name = %EVR
Group: Development/C++

%description devel
This package contains the header files for %name.

%package -n broker-tools
Summary: Tools for broker
Group: Networking/Other

%description -n broker-tools
%summary.

%prep
%setup
#patch1 -p2

# use cmake file from zeek-cmake package
rm -rf cmake/
ln -s %_datadir/zeek-cmake/ cmake

# use system lib
#rm -rv src/3rdparty/caf/ aux/libbrokerker/3rdparty/caf/

# TODO
#find -name CMakeLists.txt | xargs sed -i "s|DESTINATION lib|DESTINATION %_lib|"
#sed -i "s|INSTALL_LIB_DIR lib|INSTALL_LIB_DIR %_lib|" CMakeLists.txt
#sed -i "s|{CMAKE_INSTALL_PREFIX}/lib|{CMAKE_INSTALL_PREFIX}/%_lib|" CMakeLists.txt
#sed -i "s|CMAKE_CURRENT_BINARY_DIR}/lib|CMAKE_CURRENT_BINARY_DIR}/%_lib|" CMakeLists.txt
#sed -i "s|.{BROKER_VERSION_MAJOR}\..{BROKER_VERSION_MINOR}|0.%version|" CMakeLists.txt

%build
%cmake \
	-DCMAKE_BUILD_TYPE:STRING=RelWithDebInfo \
	-DBROKER_DISABLE_DOCS:BOOL=true \
	-DCAF_ROOT:PATH=/ \
	-DBROKER_EXTERNAL_SQLITE_TARGET=sqlite3 

%cmake_build
#make doc

%install
%cmakeinstall_std

%files
%doc CHANGES COPYING README VERSION
%_libdir/libbroker.so.*

%files devel
%_includedir/broker/
%_libdir/libbroker.so

%files -n broker-tools
%_bindir/broker-*

%changelog
* Sun Apr 03 2022 Vitaly Lipatov <lav@altlinux.ru> 2.2.0-alt1
- new version 2.2.0 (with rpmrb script)

* Mon Oct 25 2021 Alexey Shabalin <shaba@altlinux.org> 2.1.0-alt1
- new version 2.1.0
- add broker-tools package
- build without rocksdb support (upstream drop)

* Sat Sep 25 2021 Vitaly Lipatov <lav@altlinux.ru> 2.0.2-alt1
- new version 2.0.2 (with rpmrb script)

* Sun Jun 09 2019 Vitaly Lipatov <lav@altlinux.ru> 1.1.2-alt1
- new version 1.1.2 (with rpmrb script)
- build with external zeek-cmake scripts

* Sun Dec 16 2018 Vitaly Lipatov <lav@altlinux.ru> 1.1.1-alt1
- initial build for ALT Sisyphus

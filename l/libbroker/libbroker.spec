# TODO: add pybind11

Name: libbroker
Version: 1.1.1
Release: alt1

Summary: Zeek's Messaging Library 

Group: Networking/Other
License: BSD
Url: https://github.com/zeek/broker

# Source-url: https://github.com/zeek/broker/archive/v%version.tar.gz
Source: %name-%version.tar

# CMake scripts used in Zeek
# Source1-url: https://github.com/zeek/cmake/archive/master.zip
Source1: cmake.tar

Patch1: libbroker-external-sqlite.patch

BuildRequires: cmake gcc-c++
BuildRequires: libcaf-devel
BuildRequires: librocksdb-devel
BuildRequires: libsqlite3-devel
BuildRequires: libssl-devel
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
Group: Networking/Other

%description devel
This package contains the header files for %name.

%prep
%setup -a1
%patch1 -p2

# use system lib
rm -rf src/3rdparty/caf/ aux/libbrokerker/3rdparty/caf/
# disable rpath
%__subst "s|.*SetupRPATH.*||" cmake/CommonCMakeConfig.cmake

# TODO
#find -name CMakeLists.txt | xargs sed -i "s|DESTINATION lib|DESTINATION %_lib|"
#sed -i "s|INSTALL_LIB_DIR lib|INSTALL_LIB_DIR %_lib|" CMakeLists.txt
#sed -i "s|{CMAKE_INSTALL_PREFIX}/lib|{CMAKE_INSTALL_PREFIX}/%_lib|" CMakeLists.txt
#sed -i "s|CMAKE_CURRENT_BINARY_DIR}/lib|CMAKE_CURRENT_BINARY_DIR}/%_lib|" CMakeLists.txt
sed -i "s|.{BROKER_VERSION_MAJOR}\..{BROKER_VERSION_MINOR}|0.%version|" CMakeLists.txt

%build
./configure \
    --prefix=%prefix \
    --libdir=%_libdir \
    --with-caf=%prefix \
    --enable-debug \
    --disable-docs \
    --with-rocksdb=%prefix
%make_build
#make doc

%install
%makeinstall_std
# DESTDIR=%buildroot INSTALL="install -p"

%files
%doc CHANGES COPYING README VERSION
%_libdir/libbroker.so.*

%files devel
%_includedir/broker/
%_libdir/libbroker.so

%changelog
* Sun Dec 16 2018 Vitaly Lipatov <lav@altlinux.ru> 1.1.1-alt1
- initial build for ALT Sisyphus

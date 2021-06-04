Name: sysdig
Version: 0.27.1
Release: alt1

Summary: A system exploration and troubleshooting tool

Group: File tools
License: GPLv2
Url: https://github.com/draios/sysdig

# Source-url: https://github.com/draios/sysdig/archive/%version.tar.gz
Source: %name-%version.tar

ExclusiveArch: x86_64 %ix86

# manually removed: python3 ruby ruby-stdlibs 
# Automatically added by buildreq on Sat Jul 18 2015
# optimized out: cmake cmake-modules libstdc++-devel libtinfo-devel python3-base zlib-devel
BuildRequires: cmake gcc-c++ jsoncpp-devel libdb4-devel libluajit-devel libncurses-devel zlib-devel
BuildRequires: libjq-devel libb64-devel libssl-devel libcurl-devel libelf-devel
BuildRequires: pkgconfig(grpc) grpc-plugins
BuildRequires: pkgconfig(protobuf)
BuildRequires: pkgconfig(gtest)
BuildRequires: libcares-devel
BuildRequires: tbb-devel
BuildRequires: liblua5.1-devel

%description
An open source system-level exploration and troubleshooting tool.

%prep
%setup
%__subst "/option(BUILD_DRIVER/s|ON|OFF|g" driver/CMakeLists.txt

# fix build with recent curl, see https://github.com/draios/sysdig/issues/895
sed 's|curl/curlbuild\.h|curl/system.h|' -i \
	userspace/libsinsp/marathon_http.cpp \
	userspace/libsinsp/mesos_http.cpp

%build
# hack for userspace/libscap/scap.c:34:40: fatal error: ../../driver/driver_config.h
cd driver
cmake . || :
cd -

%cmake -DUSE_BUNDLED_LUAJIT:BOOL=off \
       -DUSE_BUNDLED_JSONCPP:BOOL=off \
       -DUSE_BUNDLED_ZLIB:BOOL=off \
       -DUSE_BUNDLED_TBB:BOOL=off \
       -DUSE_BUNDLED_PROTOBUF:BOOL=off \
       -DUSE_BUNDLED_NCURSES:BOOL=off \
       -DUSE_BUNDLED_OPENSSL:BOOL=off \
       -DUSE_BUNDLED_GTEST:BOOL=off \
       -DUSE_BUNDLED_GRPC:BOOL=off \
       -DUSE_BUNDLED_CURL:BOOL=off \
       -DUSE_BUNDLED_CARES:BOOL=off \
       -DUSE_BUNDLED_B64:BOOL=off \
       -DUSE_BUNDLED_JQ:BOOL=off
%cmake_build

%install
%cmake_install
rm -rf %buildroot/%_datadir/zsh/
rm -rf %buildroot/usr/etc/
rm -rf %buildroot/%_prefix/src/sysdig

%files
%_bindir/%name
%_bindir/c%name
%_bindir/sysdig-probe-loader
%_man8dir/*
%_datadir/%name/

%changelog
* Thu Jun 03 2021 Arseny Maslennikov <arseny@altlinux.org> 0.27.1-alt1
- new version 0.27.1 (with rpmrb script)

* Thu Sep 13 2018 Vitaly Lipatov <lav@altlinux.ru> 0.23.1-alt1
- new version 0.23.1 (with rpmrb script)

* Sat Apr 21 2018 Vitaly Lipatov <lav@altlinux.ru> 0.21.0-alt1
- new version 0.21.0 (with rpmrb script)

* Tue Nov 07 2017 Vitaly Lipatov <lav@altlinux.ru> 0.19.1-alt1
- new version 0.19.1 (with rpmrb script)

* Fri Aug 11 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.17.0-alt1
- Updated to upstream version 0.17.0.

* Thu Jan 05 2017 Vitaly Lipatov <lav@altlinux.ru> 0.13.0-alt1
- new version 0.13.0 (with rpmrb script)

* Mon Aug 01 2016 Vitaly Lipatov <lav@altlinux.ru> 0.11.0-alt1
- new version 0.11.0 (with rpmrb script)

* Thu Jul 28 2016 Vitaly Lipatov <lav@altlinux.ru> 0.8.0-alt1
- new version 0.8.0 (with rpmrb script)

* Fri Jul 17 2015 Vitaly Lipatov <lav@altlinux.ru> 0.1.101-alt1
- new version 0.1.101 (with rpmrb script)

* Thu Jun 04 2015 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.1.89-alt2
- rebuild with c++11 ABI

* Sun Sep 28 2014 Vitaly Lipatov <lav@altlinux.ru> 0.1.89-alt1
- initial build for ALT Linux Sisyphus

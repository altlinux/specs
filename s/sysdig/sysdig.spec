%define clang_ver 17
%define clang_version 17.0

Name: sysdig
Version: 0.39.0
Release: alt2

Summary: A system exploration and troubleshooting tool

Group: File tools
License: GPL-2.0
Url: https://github.com/draios/sysdig

# Source-url: https://github.com/draios/sysdig/archive/%version.tar.gz
Source: %name-%version.tar
Source1: 0.18.1.tar.gz
Source2: 0.8.0.tar.gz
Source3: 7.3.0+driver.tar.gz

ExcludeArch: %ix86 armh ppc64le

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: clang%clang_version
BuildRequires: libstdc++-devel
BuildRequires: grpc-plugins
BuildRequires: jsoncpp-devel
BuildRequires: libb64-devel
BuildRequires: libcares-devel
BuildRequires: libcurl-devel
BuildRequires: libdb4-devel
BuildRequires: libelf-devel
BuildRequires: libelf-devel-static
BuildRequires: libjq-devel
BuildRequires: liblua5.1-devel
BuildRequires: libluajit-devel
BuildRequires: libncurses-devel
BuildRequires: libssl-devel
BuildRequires: pkgconfig(grpc++)
BuildRequires: pkgconfig(gtest)
BuildRequires: pkgconfig(protobuf)
BuildRequires: tbb-devel
BuildRequires: zlib-devel
BuildRequires: bpftool
BuildRequires: libbpf-devel
BuildRequires: libre2-devel
BuildRequires: libuthash-devel
BuildRequires: libyaml-cpp-devel
BuildRequires: nlohmann-json-devel
BuildRequires: valijson-devel
BuildRequires: kernel-build-tools

%description
An open source system-level exploration and troubleshooting tool.

%package -n kernel-source-sysdig
Summary: Sources for build sysdig-probe kernel module for sysdig
Group: Development/Kernel
License: GPL-2.0
Version: 7.3.0

%description -n kernel-source-sysdig
%summary

%prep
%setup
# Use bindled tarballs
subst 's|URL ".*/|URL "file://%_sourcedir/|' `find . -name CMakeLists.txt`

%build
%define optflags_lto %nil
%cmake \
       -DMODERN_CLANG_EXE="/usr/bin/clang-%clang_ver" \
       -DCMAKE_CXX_COMPILER="clang++-%clang_ver" \
       -DUSE_BUNDLED_CARES:BOOL=off \
       -DUSE_BUNDLED_CURL:BOOL=off \
       -DUSE_BUNDLED_DEPS:BOOL=off \
       -DUSE_BUNDLED_GRPC:BOOL=off \
       -DUSE_BUNDLED_JSONCPP:BOOL=off \
       -DUSE_BUNDLED_LIBBPF:BOOL=off \
       -DUSE_BUNDLED_LIBELF:BOOL=off \
       -DUSE_BUNDLED_LUAJIT:BOOL=off \
       -DUSE_BUNDLED_NCURSES:BOOL=off \
       -DUSE_BUNDLED_OPENSSL:BOOL=off \
       -DUSE_BUNDLED_PROTOBUF:BOOL=off \
       -DUSE_BUNDLED_RE2:BOOL=off \
       -DUSE_BUNDLED_TBB:BOOL=off \
       -DUSE_BUNDLED_UTHASH:BOOL=off \
       -DUSE_BUNDLED_VALIJSON:BOOL=off \
       -DUSE_BUNDLED_YAMLCPP:BOOL=off \
       -DUSE_BUNDLED_ZLIB:BOOL=off

# Remove kernel module target all and install
cp "%_cmake__builddir/driver/src/Makefile" driver_Makefile
subst '/$(MAKE)/d' "%_cmake__builddir/driver/src/Makefile"
subst 's/^all:.*/all: ;/' "%_cmake__builddir/driver/src/Makefile"
subst 's/^clean:.*/clean: ;/' "%_cmake__builddir/driver/src/Makefile"
subst 's/^install:.*/install: ;/' "%_cmake__builddir/driver/src/Makefile"
subst '/scap.ko/d' "%_cmake__builddir/driver/CMakeFiles/driver.dir/build.make"

%cmake_build

%install
%cmake_install
rm -rf %buildroot/%_datadir/zsh/
mv %buildroot/%_prefix/etc %buildroot
rm -rf %buildroot/%_prefix/src/sysdig
# Remove static libraries
rm -rf %buildroot%_libdir/*.a
rm -rf %buildroot%_includedir
rm -rf %buildroot%_libdir/pkgconfig
# Restore cleaned Makefile
cp driver_Makefile %buildroot/usr/src/scap-7.3.0+driver/Makefile

# Package kernel module
mkdir -p %kernel_srcdir
cd %buildroot%_usrsrc
tar -cjf %kernel_srcdir/%name-%version.tar.bz2 scap-*
rm -rf scap-*

# Remove scap-driver-loader because scap module is building as RPM package
rm -f %buildroot%_bindir/scap-driver-loader

%files
%_bindir/%name
%_bindir/c%name
%_sysconfdir/bash_completion.d/sysdig
%_man8dir/*
%_datadir/%name/

%files -n kernel-source-sysdig
%attr(0644,root,root) %kernel_src/%name-%version.tar.bz2

%changelog
* Fri Feb 07 2025 Andrey Cherepanov <cas@altlinux.org> 0.39.0-alt2
- Disabled lto support.
- Remove scap-driver-loader because there is kernel module as RPM package.

* Thu Feb 06 2025 Andrey Cherepanov <cas@altlinux.org> 0.39.0-alt1
- New version.
- Package kernel-source-sysdig.

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

%global _unpackaged_files_terminate_build 1
%def_disable check

Name: fluent-bit
Version: 2.0.6
Release: alt1
Summary: Fast data collector for Linux
License: Apache-2.0 and BSD-2-Clause and BSD-3-Clause and MIT
Group: Monitoring
Url: https://github.com/fluent/fluent-bit

Source: %name-%version.tar
# Remove -Werror in mbedtls build. Not upstream
Patch: 0001-mbedtls-disable-Werror-in-prod-build.patch
# Fix up some install paths in CMake. Not upstream
Patch1: 0002-CMake-fix-up-install-paths.patch
# Add -fPIC to jemalloc build. Not upstream
Patch2: 0003-jemalloc-add-fPIC-to-CFLAGS.patch

%if_enabled check
BuildRequires: ctest
%endif
# libudev-devel BR is needed for systemd input plugin
BuildRequires: libudev-devel
BuildRequires: gcc-c++ binutils
BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake
BuildRequires: flex
BuildRequires: bison
BuildRequires: libpq-devel
BuildRequires: zlib-devel libzstd-devel liblz4-devel
BuildRequires: libssl-devel
BuildRequires: libsasl2-devel
BuildRequires: libyaml-devel
BuildRequires: libsystemd-devel
BuildRequires: libcares-devel
# temporarily in-source (by upstream)
# BuildRequires: libsqlite3-devel

ExcludeArch: armh ppc64le

%description
Fluent Bit is a fast Log Processor and Forwarder.
Its part of the Fluentd Ecosystem and a CNCF sub-project.
Fluent Bit allows to collect log events or metrics from different sources,
process them and deliver them to different backends such as
Fluentd, Elasticsearch, NATS, InfluxDB or any custom HTTP end-point within others.
In addition, Fluent Bit comes with full Stream Processing capabilities:
data manipulation and analytics using SQL queries.

%prep
%setup
#patch -p1
%patch1 -p1
%patch2 -p1
sed -i 's|c-ares|cares|' \
    src/CMakeLists.txt
sed -i '/FLB_PATH_LIB_CARES/d' \
    CMakeLists.txt \
    cmake/headers.cmake \
    cmake/libraries.cmake
sed -i '/include(ExternalProject)/i include(CheckIncludeFiles)' \
    CMakeLists.txt

%build
%cmake \
    -DCMAKE_BUILD_TYPE=RelWithDebInfo \
    -DFLB_EXAMPLES=Off \
    -DFLB_OUT_SLACK=Off \
    -DFLB_IN_SYSTEMD=On \
    -DFLB_OUT_TD=Off \
    -DFLB_OUT_ES=On \
    -DFLB_OUT_PGSQL=On \
    -DFLB_OUT_KAFKA=On \
    -DFLB_IN_KAFKA=Off \
    -DFLB_SHARED_LIB=Off \
    -DFLB_TESTS_RUNTIME=On \
    -DFLB_TESTS_INTERNAL=Off \
    -DFLB_RELEASE=On \
    -DFLB_DEBUG=Off \
    -DFLB_TLS=On \
    -DFLB_LUAJIT=Off \
    -DFLB_FILTER_LUA=Off \
    -DFLB_HTTP_SERVER=On \
    -DFLB_CONFIG_YAML=On \
#

%cmake_build

%install
%cmake_install
# We don't ship headers and shared library for plugins (yet)
rm -rvf %buildroot%_includedir

%check
cd %_target_alias
ctest

%post
%post_service %name.service

%preun
%preun_service %name.service

%files
%doc LICENSE README.md MAINTAINERS.md CODE_OF_CONDUCT.md CONTRIBUTING.md GOLANG_OUTPUT_PLUGIN.md GOVERNANCE.md
%doc conf
%dir %_sysconfdir/%name
%config(noreplace) %_sysconfdir/%name/*.conf
%_bindir/%name
%_unitdir/%name.service

%changelog
* Mon Nov 28 2022 Leontiy Volodin <lvol@altlinux.org> 2.0.6-alt1
- New version.

* Mon Nov 21 2022 Leontiy Volodin <lvol@altlinux.org> 2.0.5-alt1
- New version.
- Updated the patches.
- Disabled in_kafka module.
- Excluded armh and ppc64le.

* Mon Oct 03 2022 Leontiy Volodin <lvol@altlinux.org> 1.9.9-alt1
- New version.
- Built with external c-ares instead built-in (ALT #43888).

* Mon Sep 26 2022 Alexey Shabalin <shaba@altlinux.org> 1.9.8-alt1
- new version 1.9.8

* Fri Jul 01 2022 Alexey Shabalin <shaba@altlinux.org> 1.9.5-alt2
- Build with ElasticSearch support.
- Disable build shared lib.
- Cleanup BR:.

* Fri Jun 24 2022 Leontiy Volodin <lvol@altlinux.org> 1.9.5-alt1
- New version.
- Enabled yaml support by default.

* Thu Jun 09 2022 Leontiy Volodin <lvol@altlinux.org> 1.9.4-alt1
- New version.
- Disabled luajit and filter_lua support (ALT #42618).

* Thu Mar 03 2022 Nikolay Burykin <bne@altlinux.org> 1.8.12-alt2
- Add build option -DFLB_OUT_KAFKA=On

* Tue Feb 15 2022 Leontiy Volodin <lvol@altlinux.org> 1.8.12-alt1
- Initial build for ALT Sisyphus (thanks fedora for the spec).

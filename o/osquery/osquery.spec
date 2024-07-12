%define _unpackaged_files_terminate_build 1                                                    
%global llvm_version 18.1
%global gcc_version 13

Name:    osquery
Version: 5.13.0
Release: alt1

Summary: SQL powered operating system instrumentation, monitoring, and analytics
License: Apache-2.0 and GPL-2.0
Group:   Other
Url:     https://github.com/osquery/osquery

Packager: Andrey Cherepanov <cas@altlinux.org>

Source: %name-%version.tar
Source1: submodules.tar
Patch0: osquery-unbundle-libraries.patch
Patch1: osquery-disable-expiremental.patch
Patch2: osquery-disable-dpkg.patch
Patch3: osquery-use-cstdint.patch
Patch4: osquery-new-boost.patch
Patch5: osquery-fix-std-functions.patch
Patch6: osquery-fix-audit_rule_syscall_data.patch
Patch7: osquery-sysctl.h.patch
Patch8: osquery-no-lvm2app.h.patch
Patch9: osquery-enable_yara_string.patch
Patch10: osquery-no-__secure_getenv.patch
Patch11: osquery-no-sysctl.patch
Patch12: osquery-fix-docker-networks.patch
Patch13: osquery-no-experiments.patch
Patch14: osquery-link-system-libraries.patch
Patch15: osquery-no-examples-build.patch
Patch16: osquery-lenses-install-dir.patch
Patch17: osquery-bindir.patch

ExcludeArch: armh %ix86 ppc64le

BuildRequires(pre): cmake
BuildRequires(pre): rpm-build-ninja
BuildRequires: gcc-c++
BuildRequires: libstdc++-devel
BuildRequires: git-core
BuildRequires: python3-base
BuildRequires: ccache
BuildRequires: clang%{llvm_version}
BuildRequires: clang%{llvm_version}-devel
BuildRequires: llvm%{llvm_version}-devel
BuildRequires: lld%{llvm_version}-devel
BuildRequires: clang-tools
BuildRequires: liblz4-devel
BuildRequires: libzstd-devel
BuildRequires: libexpat-devel
BuildRequires: libudev-devel
BuildRequires: liblzma-devel
BuildRequires: libsqlite3-devel
BuildRequires: rapidjson-devel
BuildRequires: libmagic-devel
BuildRequires: libgcrypt-devel
BuildRequires: libpopt-devel
BuildRequires: libaudit-devel
BuildRequires: libdbus-devel
BuildRequires: boost-devel
BuildRequires: zlib-devel
BuildRequires: libdevmapper-devel
BuildRequires: libcap-devel
BuildRequires: libiptables-devel
BuildRequires: libuuid-devel
BuildRequires: boost-filesystem-devel
BuildRequires: boost-context-devel
BuildRequires: libgtest-devel
BuildRequires: libgflags-devel
BuildRequires: libglog-devel
BuildRequires: boost-asio-devel
BuildRequires: librocksdb-devel
BuildRequires: libssl-devel
BuildRequires: thrift-devel
BuildRequires: boost-beast-devel
BuildRequires: libtsk-devel
BuildRequires: liblinenoise-devel
BuildRequires: librdkafka-devel
BuildRequires: libarchive-devel
BuildRequires: libyara-devel
BuildRequires: libaugeas-devel
BuildRequires: librpm-devel
BuildRequires: libblkid-devel
BuildRequires: libcryptsetup-devel
BuildRequires: libxml2-devel
BuildRequires: libc++-devel
BuildRequires: libc++abi-devel

%description
%summary

%prep
%setup
tar xf %SOURCE1
%autopatch -p1
# Remove bundled libraries
#ls -1 libraries/cmake/source | grep -vE 'sleuthkit|linenoise-ng' | xargs -n1 -i{} rm -rf 'libraries/cmake/source/{}' ';'
#s/thirdparty_glog/glog/;
subst '
      s/thirdparty_boost$/boost_system/;
      s/thirdparty_gflags$/gflags/;
      s/thirdparty_sqlite/sqlite3/;
      s/thirdparty_zlib/z/;
      /osquery_utils_linux$/d;
      s/thirdparty_googletest_headers/gtest/' `grep -l thirdparty_ $(find . -name CMakeLists.txt)`
# Fix broken linking
subst 's/-stdlib=libc++//' cmake/flags.cmake

%build
%add_optflags -I%_includedir/c++/%gcc_version -I%_includedir/c++/%gcc_version/%_arch-alt-linux
%add_optflags -I%_includedir/dbus-1.0 -I%_libdir/dbus-1.0/include -I%_includedir/libxml2
%add_optflags -I%_includedir/linux-default/include
export CC="clang"
export CXX="clang++"
export AR="llvm-ar"
export NM="llvm-nm"
export RANLIB="llvm-ranlib"
export LLVM_PROFDATA="llvm-profdata"
%cmake -GNinja -Wno-dev \
       -DOSQUERY_VERSION=%version \
       -DOSQUERY_BUILD_TESTS=OFF \
       -DOSQUERY_BUILD_BPF=OFF \
       -DOSQUERY_BUILD_AWS=OFF \
       -DOSQUERY_BUILD_DPKG=OFF \
       -DOSQUERY_BUILD_ETW=OFF \
       -DOSQUERY_BUILD_EXPERIMENTS=OFF
%ninja_build -C "%_cmake__builddir"

%install
%ninja_install -C "%_cmake__builddir"
install -Dpm0644 %buildroot/control/rpm/etc/sysconfig/osqueryd %buildroot%_sysconfdir/sysconfig/osqueryd
install -Dpm0644 tools/deployment/linux_packaging/rpm/osqueryd.service %buildroot%_unitdir/osqueryd.service
rm -rf %buildroot/control
mkdir -p %buildroot%_sysconfdir/osquery
touch %buildroot%_sysconfdir/osquery/osquery.flags %buildroot%_sysconfdir/osquery/osquery.conf
mkdir -p %buildroot%_logdir/osquery

%preun
%preun_service osqueryd

%post
%post_service osqueryd

%files
%doc *.md
%_bindir/osquery*
%config(noreplace) %_sysconfdir/sysconfig/osqueryd
%config(noreplace) %_sysconfdir/osquery/osquery.flags
%config(noreplace) %_sysconfdir/osquery/osquery.conf
%_unitdir/osqueryd.service
%_datadir/osquery
%dir %_logdir/osquery

%changelog
* Fri Jul 12 2024 Andrey Cherepanov <cas@altlinux.org> 5.13.0-alt1
- New version.

* Sat Jun 01 2024 Andrey Cherepanov <cas@altlinux.org> 5.12.2-alt1
- Initial build for Sisyphus (ALT #39251).

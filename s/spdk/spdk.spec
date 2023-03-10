%set_verify_elf_skiplist %_libdir/libspdk*

%define dpdk_build_path "dpdk/build"
%define dpdk_path "dpdk"
%define llvm_ver 15
%define gcc_ver 12

%def_disable dpdk_internal
%def_disable static
%def_disable tests
# configure file is not a GNU autoconf script
%def_enable clang

Name: spdk
Version: 23.01
Release: alt1

Summary: Storage Performance Development Kit
License: BSD-3-Clause
Group: Development/Tools
Url: https://spdk.io
ExcludeArch: i586 ppc64le armh

Source: spdk-%version.tar.gz
Patch: spdk-21.10-alt-scripts-syntax.patch
Patch1: spdk-21.10-alt-scripts-startup.patch
Patch2: spdk-23.01-alpinelinux-use-system-isal.patch

# This is a minimal set of requirements needed for SPDK apps to run when built with
# default configuration. These are also predetermined by rpmbuild. Extra requirements
# can be defined through a comma-separated list passed via $requirements when building
# the spec.
#Requires: glibc
#Requires: libaio
#Requires: libgcc
#Requires: libstdc++
#Requires: libuuid
#Requires: ncurses-libs
#Requires: numactl-libs
#Requires: openssl-libs
#Requires: zlib

%add_python3_req_skip common spdk.rpc spdk.rpc.client spdk.rpc.helpers spdk.sma spdk.sma.proto.nvmf_tcp_pb2 spdk.sma.proto.nvmf_tcp_pb2_grpc spdk.sma.proto.sma_pb2 spdk.sma.proto.sma_pb2_grpc spdk.spdkcli
%filter_from_requires /apt*/d
# %%filter_from_requires /bpftrace/d

Requires: systemd-utils
BuildPreReq: libfuse3-devel
%if_enabled clang
#BuildRequires(pre): rpm-macros-llvm-common
BuildRequires: clang%llvm_ver.0-devel
BuildRequires: lld%llvm_ver.0-devel
BuildRequires: llvm%llvm_ver.0-devel
%else
BuildRequires: gcc%gcc_ver-c++
%endif
BuildRequires: libstdc++%gcc_ver-devel
BuildRequires: glibc-devel rpm-build-python3 libuuid-devel libssl-devel libaio-devel libncurses-devel libisal-devel
BuildRequires: rdma-core-devel libbpf-devel libelf-devel zlib-devel libpcap-devel libjansson-devel
BuildRequires: libzstd-devel
# BuildPreReq: libpmem-devel rdma-core-devel libiscsi-devel liburing-devel librbd-devel libpmem-devel
%if_enabled dpdk_internal
BuildPreReq: libnuma-devel libfdt-devel
BuildPreReq: libarchive-devel libbsd-devel libjansson-devel libpcap-devel
BuildPreReq: doxygen python3-module-sphinx-sphinx-build-symlink
BuildRequires: meson rpm-build-ninja python3-module-elftools
%else
BuildRequires: dpdk-devel
%endif
%if_enabled tests
BuildRequires: CUnit-devel
%endif

%description
The Storage Performance Development Kit (SPDK) provides a set of tools and
libraries for writing high performance, scalable, user-mode storage
applications. It achieves high performance by moving all of the necessary
drivers into userspace and operating in a polled mode instead of relying
on interrupts, which avoids kernel context switches and eliminates interrupt
handling overhead.

%package devel
Summary: SPDK development libraries and headers
Group: Development/C

%description devel
SPDK development libraries and headers

%package libs
Summary: SPDK libraries
Group: System/Libraries

%description libs
SPDK libraries

%if_enabled static
%package devel-static
Summary: SPDK static libraries
Group: System/Libraries

%description devel-static
SPDK devel libraries
%endif

%prep
%setup
%patch -p1
%patch1 -p1
%patch2 -p1

sed -i 's|__bitwise__|__bitwise|' include/linux/virtio_types.h

sed -i 's|/etc/lsb-release|/etc/os-release|' \
  scripts/vagrant/update.sh

sed -i 's|/usr/lib64/iscsi|%_libdir|' \
  configure \
  mk/spdk.modules.mk

sed -i 's|/lib|/%_lib|; s|/include|/include/spdk|' \
  scripts/pc.sh

sed -i 's|libdir?=$(CONFIG_PREFIX)/lib|libdir?=$(CONFIG_PREFIX)/%_lib|' \
  mk/spdk.common.mk

sed -i 's|/usr/local/bin/pip|%_bindir/pip3|' \
  scripts/pkgdep/*.sh

sed -i 's|/usr/local/bin/|%_prefix/libexec/spdk/bin/|' \
  docker/build_base/post-install \
  docker/traffic-generator/init

# Remove illegal absolute entry from RPATH.
sed -i '/-Wl,-rpath=$(DESTDIR)\/$(libdir)/d' \
	mk/spdk.common.mk

%build
%if_enabled clang
%define optflags_lto %nil
export CC=clang-%llvm_ver
export CXX=clang++-%llvm_ver
export LDFLAGS="-fuse-ld=lld-%llvm_ver $LDFLAGS"
%else
export CC=gcc-%gcc_ver
export CXX=g++-%gcc_ver
%endif
export CONFIG_DPDK_LIB_DIR=%_libdir
export CONFIG_DPDK_INC_DIR=%_includedir/dpdk
export DPDK_ABS_DIR=%_prefix
export DPDK_INC_DIR=%_includedir/dpdk
export DPDK_LIB_DIR=%_libdir
export SPDK_ROOT_DIR=$PWD
/usr/bin/ld -v
%_configure_script \
	--prefix=%prefix \
%if_disabled clang
	--cross-prefix=%_target_alias \
%endif
	--with-system-isal \
	--without-crypto \
	--with-fuse \
%if_enabled dpdk_internal
	--without-dpdk \
%else
	--with-dpdk=%_libdir \
%endif
%if_disabled static
%if_disabled clang
	--enable-lto \
%else
  --disable-lto \
%endif
	--with-shared \
%endif
%if_disabled tests
	--disable-tests \
	--disable-unit-tests \
%endif
%nil

%make_build

%install
export CONFIG_DPDK_LIB_DIR=%_libdir
export CONFIG_DPDK_INC_DIR=%_includedir/dpdk

%makeinstall_std

# And some useful setup scripts SPDK uses
mkdir -p %buildroot%_prefix/libexec/spdk
mkdir -p %buildroot%_prefix/libexec/spdk/bin
mkdir -p %buildroot%_prefix/libexec/spdk/examples
mkdir -p %buildroot%_sysconfdir/bash_completion.d
mkdir -p %buildroot%_sysconfdir/profile.d
mkdir -p %buildroot%_sysconfdir/ld.so.conf.d

%if_enabled dpdk_internal
# Include DPDK libs in case --with-shared is in use.
mkdir -p %buildroot%_libdir/
cp -a %dpdk_build_path/lib/* %buildroot%_libdir/
%endif
# Special case for SPDK_RUN_EXTERNAL_DPDK setup
[[ -e %dpdk_path/intel-ipsec-mb ]] && find %dpdk_path/intel-ipsec-mb/ -name '*.so*' -exec cp -a {} %buildroot%_libdir/ ';'
[[ -e %dpdk_path/isa-l/build/lib ]] && cp -a %dpdk_path/isa-l/build/lib/*.so* %buildroot%_libdir/

# Try to include all the binaries that were potentially built
[[ -e build/examples ]] && cp -a build/examples/* %buildroot%_prefix/libexec/spdk/examples/
[[ -e build/bin ]] && cp -a build/bin/* %buildroot%_prefix/libexec/spdk/bin/
#[[ -e build/fio ]] && cp -a build/fio %%buildroot%%_prefix/libexec/spdk/fio

cat <<-'EOF' > %buildroot%_sysconfdir/ld.so.conf.d/spdk.conf
%_libdir
EOF

cat <<-'EOF' > %buildroot%_sysconfdir/profile.d/spdk_path.sh
PATH=$PATH:%_prefix/libexec/spdk
PATH=$PATH:%_prefix/libexec/spdk/scripts
PATH=$PATH:%_prefix/libexec/spdk/scripts/vagrant
PATH=$PATH:%_prefix/libexec/spdk/test/common/config
PATH=$PATH:%_prefix/libexec/spdk/bin
PATH=$PATH:%_prefix/libexec/spdk/include
PATH=$PATH:%_prefix/libexec/spdk/examples
export PATH
EOF

cp -a scripts %buildroot%_prefix/libexec/spdk/scripts
ln -s %_prefix/libexec/spdk/scripts/bash-completion/spdk %buildroot%_sysconfdir/bash_completion.d/spdk

# We need to take into the account the fact that most of the scripts depend on being
# run directly from the repo. To workaround it, create common root space under dir
# like /usr/libexec/spdk and link all potential relative paths the script may try
# to reference.

# setup.sh uses pci_ids.h
ln -s %_includedir/spdk %buildroot%_prefix/libexec/spdk/include

mv -f %buildroot%_bindir/* %buildroot%_prefix/libexec/spdk/bin/

# libspdk_ut_mock.so.3.0 statically linked?!
rm -f %buildroot%_libdir/libspdk_ut_mock.so*
rm -f %buildroot%_pkgconfigdir/spdk_ut_mock.pc

%if_disabled static
# remove static libraries
rm -f %buildroot%_libdir/*.a
%endif

%files
%_sysconfdir/profile.d/*
%_sysconfdir/bash_completion.d/spdk
%dir %_prefix/libexec/spdk/
%_prefix/libexec/spdk/*

%files devel
%dir %_includedir/spdk/
%_includedir/spdk/*
%_libdir/lib*.so
%_pkgconfigdir/*.pc

%files libs
%_sysconfdir/ld.so.conf.d/*
%_libdir/lib*.so.*

%if_enabled static
%files devel-static
%_libdir/lib*.a
%endif

%changelog
* Fri Mar 10 2023 Leontiy Volodin <lvol@altlinux.org> 23.01-alt1
- New version (23.01).
- Built with system isa-l (thanks alpinelinux for the patch).
- Built using clang instead gcc.
- Updated syntax patch.

* Mon May 30 2022 Leontiy Volodin <lvol@altlinux.org> 22.05-alt1
- New version (22.05).

* Mon May 30 2022 Leontiy Volodin <lvol@altlinux.org> 22.01.1-alt2
- Fixed FTBFS.

* Mon May 16 2022 Leontiy Volodin <lvol@altlinux.org> 22.01.1-alt1
- New version (22.01.1).

* Tue Mar 15 2022 Leontiy Volodin <lvol@altlinux.org> 22.01-alt3
- Fix setup.sh startup (ALT #42131).

* Wed Mar 02 2022 Leontiy Volodin <lvol@altlinux.org> 22.01-alt2
- Fixed build on p10 branch.

* Wed Feb 16 2022 Leontiy Volodin <lvol@altlinux.org> 22.01-alt1
- New version (22.01).
- Changed group.
- Skipped elf check for spdk libs.

* Thu Jan 27 2022 Leontiy Volodin <lvol@altlinux.org> 21.10-alt1
- Initial build for ALT Sisyphus (ALT #41663).

* Tue Feb 16 2021 Michal Berger <michalx.berger@intel.com>
- Initial RPM .spec for the SPDK

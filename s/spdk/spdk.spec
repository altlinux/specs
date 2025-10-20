%define dpdk_build_path "dpdk/build"
%define dpdk_path "dpdk"

%def_disable static
%def_disable tests
%def_enable clang

Name: spdk
Version: 25.05.1
Release: alt1

Summary: Storage Performance Development Kit

License: BSD-3-Clause
Group: Development/Tools
Url: https://spdk.io
VCS: https://github.com/spdk/spdk

ExcludeArch: i586 ppc64le armh

Source: spdk-%version.tar
Patch0: spdk-%version-%release.patch
Patch1: spdk-25.05-alt-scripts-syntax.patch
Patch2: spdk-24.09-alpinelinux-use-system-isal.patch
Patch3: spdk-23.09-alpinelinux-remove-stupid.patch
# python module
Patch4: spdk-25.05-upstream-python-1.patch
Patch5: spdk-25.05-upstream-python-2.patch
Patch6: spdk-25.05-upstream-python-3.patch
Patch7: spdk-25.05-upstream-python-4.patch
# ---
Patch8: spdk-25.05-alt-fix-symbols.patch

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
%filter_from_requires /\%_prefix\/libexec\/spdk\/scripts\/pkgdep/d
%filter_from_requires /\%_sysconfdir\/opt\/spdk-pkgdep\/paths\/export.sh/d
%filter_from_requires /apt*/d
%filter_from_requires /pacman/d
# %%filter_from_requires /bpftrace/d

Requires: systemd-utils

# Automatically added by buildreq on Mon Oct 16 2023
# optimized out: bash5 bashrc glibc-kernheaders-generic glibc-kernheaders-x86 libgpg-error libncurses-devel libstdc++-devel libtinfo-devel pkg-config python3 python3-base python3-dev sh5
BuildRequires: libaio-devel libfuse3-devel libisal-devel libisal_crypto-devel libssl-devel libuuid-devel libsystemd-devel libncurses-devel patchelf python3-devel libcap-devel
BuildRequires: rdma-core-devel zlib-devel libpcap-devel libdbus-devel libelf-devel libzstd-devel libjansson-devel dpdk-devel
BuildRequires: python3-module-pyproject-installer python3-module-wheel python3-module-setuptools python3-module-hatchling
%if_enabled clang
#BuildRequires(pre): rpm-macros-llvm-common
BuildRequires: clang-devel
BuildRequires: lld-devel
BuildRequires: llvm-devel
BuildRequires: libstdc++-devel
%else
BuildRequires: gcc-c++
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
Requires: libdpdk

%description libs
SPDK libraries

%if_enabled static
%package devel-static
Summary: SPDK static libraries
Group: System/Libraries

%description devel-static
SPDK devel libraries
%endif

%package -n python3-module-%name
Summary: Python3 module for %name
Group: Development/Python3
BuildArch: noarch

%description -n python3-module-%name
This package provides python3 module for %name.

%prep
%setup
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1 -R
%patch5 -p1 -R
%patch6 -p1 -R
%patch7 -p1 -R
%patch8 -p1

sed -i '/CONFIG_PREFIX=/s|/usr/local|%_prefix|' CONFIG

sed -i 's|__bitwise__|__bitwise|' include/linux/virtio_types.h

sed -i 's|/etc/lsb-release|/etc/os-release|' \
  scripts/vagrant/update.sh

sed -i 's|/usr/lib64/iscsi|%_libdir|g' \
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

sed -i '/setup_cmd/d' python/Makefile

sed -i 's/isa-l\/include/isa-l/' \
  lib/util/crc16.c \
  lib/util/crc64.c \
  lib/util/crc_internal.h \
  lib/util/xor.c

sed -i 's/\.\.\/isa-l\/include/isa-l/' \
  lib/accel/accel_sw.c

# Remove illegal absolute entry from RPATH.
sed -i '/-Wl,-rpath=$(DESTDIR)\/$(libdir)/d' \
  mk/spdk.common.mk
sed -i 's| -Wl,-rpath=$(DPDK_LIB_DIR)||' \
  lib/env_dpdk/env.mk
sed -i 's|-rpath=$(SPDK_LIB_DIR),||' \
  test/external_code/hello_world/Makefile
sed -i 's|-rpath=$(SPDK_LIB_DIR)||' \
  test/external_code/nvme/Makefile

# fix startup scripts
sed -i 's|include/spdk/pci_ids.h|include/pci_ids.h|' \
  scripts/common.sh \
  test/vmd/vmd.sh

%build
%if_enabled clang
%define optflags_lto %nil
export CC=clang
export CXX=clang++
export LDFLAGS="-fuse-ld=lld $LDFLAGS"
%else
export CC=gcc
export CXX=g++
%endif
export CONFIG_DPDK_LIB_DIR=%_libdir
export CONFIG_DPDK_INC_DIR=%_includedir/dpdk
export DPDK_ABS_DIR=%_prefix
export DPDK_INC_DIR=%_includedir/dpdk
export DPDK_LIB_DIR=%_libdir
export SPDK_ROOT_DIR=$PWD
%_configure_script \
	--prefix=%prefix \
%if_disabled clang
	--cross-prefix=%_target_alias \
%endif
	--with-system-isal \
	--without-crypto \
	--with-fuse \
	--with-dpdk=%_libdir \
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
#

%make_build
cd python/
%pyproject_build
cd -

%install
export CONFIG_DPDK_LIB_DIR=%_libdir
export CONFIG_DPDK_INC_DIR=%_includedir/dpdk

%makeinstall_std
cd python/
%pyproject_install
cd -

# And some useful setup scripts SPDK uses
mkdir -p %buildroot%_prefix/libexec/spdk
mkdir -p %buildroot%_prefix/libexec/spdk/bin
mkdir -p %buildroot%_prefix/libexec/spdk/examples
mkdir -p %buildroot%_sysconfdir/bash_completion.d
mkdir -p %buildroot%_sysconfdir/profile.d

# Special case for SPDK_RUN_EXTERNAL_DPDK setup
[[ -e %dpdk_path/intel-ipsec-mb ]] && find %dpdk_path/intel-ipsec-mb/ -name '*.so*' -exec cp -a {} %buildroot%_libdir/ ';'
[[ -e %dpdk_path/isa-l/build/lib ]] && cp -a %dpdk_path/isa-l/build/lib/*.so* %buildroot%_libdir/

# Try to include all the binaries that were potentially built
[[ -e build/examples ]] && cp -a build/examples/* %buildroot%_prefix/libexec/spdk/examples/
[[ -e build/bin ]] && cp -a build/bin/* %buildroot%_prefix/libexec/spdk/bin/

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

# fix undefined symbols
patchelf %buildroot%_libdir/libspdk_env_dpdk_rpc.so.6.0 --add-needed libspdk_env_dpdk.so.15.1
patchelf %buildroot%_libdir/libspdk_scheduler_dpdk_governor.so.4.0 --add-needed libspdk_env_dpdk.so.15.1
#patchelf %buildroot%_libdir/libspdk_accel_dpdk_cryptodev.so.3.0 --add-needed librte_cryptodev.so.24.0
patchelf %buildroot%_libdir/libspdk_scheduler_gscheduler.so.4.0 --add-needed libspdk_env_dpdk.so.15.1
patchelf %buildroot%_libdir/libspdk_scheduler_dynamic.so.4.0 --add-needed libspdk_env_dpdk.so.15.1
patchelf %buildroot%_libdir/libspdk_sock_posix.so.6.0 --add-needed libspdk_env_dpdk.so.15.1
patchelf %buildroot%_libdir/libspdk_event_nvmf.so.6.0 --add-needed libspdk_env_dpdk.so.15.1
patchelf %buildroot%_libdir/libspdk_event_vmd.so.6.0 --add-needed libspdk_env_dpdk.so.15.1
patchelf %buildroot%_libdir/libspdk_accel_ioat.so.6.0 --add-needed libspdk_env_dpdk.so.15.1
patchelf %buildroot%_libdir/libspdk_blobfs_bdev.so.6.0 --add-needed libspdk_env_dpdk.so.15.1
patchelf %buildroot%_libdir/libspdk_bdev.so.17.0 --add-needed libspdk_env_dpdk.so.15.1
patchelf %buildroot%_libdir/libspdk_bdev_virtio.so.6.0 --add-needed libspdk_env_dpdk.so.15.1
patchelf %buildroot%_libdir/libspdk_bdev_raid.so.6.0 --add-needed libspdk_env_dpdk.so.15.1
patchelf %buildroot%_libdir/libspdk_bdev_nvme.so.7.1 --add-needed libspdk_env_dpdk.so.15.1
patchelf %buildroot%_libdir/libspdk_bdev_null.so.6.0 --add-needed libspdk_env_dpdk.so.15.1
patchelf %buildroot%_libdir/libspdk_bdev_malloc.so.6.0 --add-needed libspdk_env_dpdk.so.15.1
patchelf %buildroot%_libdir/libspdk_bdev_gpt.so.6.0 --add-needed libspdk_env_dpdk.so.15.1
patchelf %buildroot%_libdir/libspdk_bdev_delay.so.6.0 --add-needed libspdk_env_dpdk.so.15.1
patchelf %buildroot%_libdir/libspdk_fuse_dispatcher.so.1.0 --add-needed libspdk_env_dpdk.so.15.1
patchelf %buildroot%_libdir/libspdk_fsdev.so.2.0 --add-needed libspdk_env_dpdk.so.15.1
patchelf %buildroot%_libdir/libspdk_virtio.so.7.0 --add-needed libspdk_env_dpdk.so.15.1
patchelf %buildroot%_libdir/libspdk_vhost.so.8.0 --add-needed libspdk_env_dpdk.so.15.1
patchelf %buildroot%_libdir/libspdk_vfio_user.so.5.0 --add-needed libspdk_env_dpdk.so.15.1
patchelf %buildroot%_libdir/libspdk_ftl.so.9.0 --add-needed libspdk_env_dpdk.so.15.1
patchelf %buildroot%_libdir/libspdk_nbd.so.7.0 --add-needed libspdk_env_dpdk.so.15.1
patchelf %buildroot%_libdir/libspdk_iscsi.so.8.0 --add-needed libspdk_env_dpdk.so.15.1
patchelf %buildroot%_libdir/libspdk_ioat.so.7.0 --add-needed libspdk_env_dpdk.so.15.1
patchelf %buildroot%_libdir/libspdk_nvmf.so.20.0 --add-needed libspdk_env_dpdk.so.15.1
patchelf %buildroot%_libdir/libspdk_vmd.so.6.0 --add-needed libspdk_env_dpdk.so.15.1
patchelf %buildroot%_libdir/libspdk_nvme.so.15.0 --add-needed libspdk_env_dpdk.so.15.1
patchelf %buildroot%_libdir/libspdk_event.so.14.0 --add-needed libspdk_env_dpdk.so.15.1
patchelf %buildroot%_libdir/libspdk_init.so.6.0 --add-needed libspdk_env_dpdk.so.15.1
patchelf %buildroot%_libdir/libspdk_blobfs.so.11.0 --add-needed libspdk_env_dpdk.so.15.1
patchelf %buildroot%_libdir/libspdk_blob.so.12.0 --add-needed libspdk_env_dpdk.so.15.1
patchelf %buildroot%_libdir/libspdk_thread.so.11.0 --add-needed libspdk_env_dpdk.so.15.1
patchelf %buildroot%_libdir/libspdk_trace.so.11.0 --add-needed libspdk_env_dpdk.so.15.1
patchelf %buildroot%_libdir/libspdk_scsi.so.9.0 --add-needed libspdk_env_dpdk.so.15.1
patchelf %buildroot%_libdir/libspdk_util.so.10.1 --add-needed libspdk_blobfs_bdev.so.6.0
patchelf %buildroot%_libdir/libspdk_util.so.10.1 --add-needed libspdk_env_dpdk.so.15.1

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
%_libdir/lib*.so.*

%if_enabled static
%files devel-static
%_libdir/lib*.a
%endif

%files -n python3-module-%name
%python3_sitelibdir_noarch/%name/
%python3_sitelibdir_noarch/%{name}-*

%changelog
* Mon Oct 20 2025 Leontiy Volodin <lvol@altlinux.org> 25.05.1-alt1
- New version 25.05.1 (Fixes: CVE-2025-57275).
- Fixed build with libsystemd 258.1.

* Wed Jun 11 2025 Leontiy Volodin <lvol@altlinux.org> 25.05-alt1
- New version 25.05.
- Added VCS tag.
- Fixed undefined symbols.

* Tue Jan 14 2025 Leontiy Volodin <lvol@altlinux.org> 23.09-alt1.1
- Fixed FTBFS.

* Mon Oct 16 2023 Leontiy Volodin <lvol@altlinux.org> 23.09-alt1
- New version 23.09.
- Fixed build with python 3.11.6.
- Cleanup BRs.

* Wed Sep 06 2023 Leontiy Volodin <lvol@altlinux.org> 23.05-alt2.1
- Removed pacman from requires (ALT #47071).

* Mon Aug 07 2023 Leontiy Volodin <lvol@altlinux.org> 23.05-alt2
- Fixed links with some system libraries.
- Removed unneeded requires for pkgdep scripts (ALT #47071).

* Tue Jul 04 2023 Leontiy Volodin <lvol@altlinux.org> 23.05-alt1
- New version 23.05.
- Built with system isa-l (thanks alpinelinux for the patch).

* Thu Jun 22 2023 Leontiy Volodin <lvol@altlinux.org> 23.01.1-alt3
- Rebuilt with new libstdc++-devel.

* Wed Jun 21 2023 Leontiy Volodin <lvol@altlinux.org> 23.01.1-alt2
- Fixed FTBFS.

* Tue May 02 2023 Leontiy Volodin <lvol@altlinux.org> 23.01.1-alt1
- New version 23.01.1.

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

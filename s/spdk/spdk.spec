%define _libexecdir /usr/libexec

%def_disable tests
%def_enable clang
%def_enable shared
# system libs or built-in
%def_without dpdk
%def_without isal
%def_without vfio_user

Name: spdk
Version: 26.01
Release: alt1

Summary: Storage Performance Development Kit

License: BSD-3-Clause
Group: Development/Tools
Url: https://spdk.io
VCS: https://github.com/spdk/spdk

ExcludeArch: i586 ppc64le armh aarch64

Source0: spdk-%version.tar
Source1: dpdk.tar
Source2: intel-ipsec-mb.tar
Source3: isa-l.tar
Source4: ocf.tar
Source5: libvfio-user.tar
Source6: xnvme.tar
Source7: isa-l-crypto.tar
Patch0: spdk-%version-%release.patch
Patch1: spdk-25.05-alt-scripts-syntax.patch
Patch2: spdk-26.01-alt-use-system-isal.patch
Patch3: spdk-23.09-alpinelinux-remove-stupid.patch
Patch4: spdk-26.01-alt-fix-symbols.patch

%add_python3_req_skip common spdk.rpc spdk.rpc.client spdk.rpc.helpers spdk.sma spdk.sma.proto.nvmf_tcp_pb2 spdk.sma.proto.nvmf_tcp_pb2_grpc spdk.sma.proto.sma_pb2 spdk.sma.proto.sma_pb2_grpc spdk.spdkcli gdb gdb.printing
%filter_from_requires /\%_prefix\/libexec\/spdk\/scripts\/pkgdep/d
%filter_from_requires /\%_sysconfdir\/opt\/spdk-pkgdep\/paths\/export.sh/d
%filter_from_requires /apt*/d
%filter_from_requires /pacman/d
# TODO: find all python2 requires.
%filter_from_requires /python-base/d

Requires: systemd-utils

# Automatically added by buildreq on Mon Oct 16 2023
# optimized out: bash5 bashrc glibc-kernheaders-generic glibc-kernheaders-x86 libgpg-error libncurses-devel libstdc++-devel libtinfo-devel pkg-config python3 python3-base python3-dev sh5
BuildRequires: libaio-devel libfuse3-devel libssl-devel libuuid-devel libsystemd-devel libncurses-devel patchelf python3-devel libcap-devel nasm libfdt-devel
BuildRequires: rdma-core-devel zlib-devel libpcap-devel libdbus-devel libelf-devel libzstd-devel libjansson-devel
%if_with isal
BuildRequires: libisal-devel libisal_crypto-devel
%endif
%if_with dpdk
BuildRequires: dpdk-devel
%endif
BuildRequires: python3-module-pyproject-installer python3-module-wheel python3-module-setuptools python3-module-hatchling
BuildRequires: meson python3-module-elftools libnuma-devel
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

# find libraries
%add_findprov_lib_path %_libdir/spdk/lib

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
%if_with dpdk
Requires: libdpdk
%endif

%description libs
SPDK libraries

%package libs-dpdk
Summary: DPDK libraries for SPDK
Group: System/Libraries
# Requires: libdpdk

%description libs-dpdk
DPDK libraries for SPDK

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
%setup -a1 -a2 -a3 -a4 -a5 -a6 -a7
%patch0 -p1
%patch1 -p1
%if_with isal
%patch2 -p1
%endif
%patch3 -p1
%patch4 -p2

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

sed -i 's|/bin/pip|%_bindir/pip3|' \
  scripts/pkgdep/*.sh

sed -i 's|/usr/local/bin/|%_libexecdir/spdk/bin/|' \
  docker/build_base/post-install \
  docker/traffic-generator/init

sed -i 's|/usr/local/lib/sysctl.d/|%_sysctldir/|' \
  scripts/setup.sh

%if_without isal
sed -i \
  -e 's|-Wl,-rpath=$(ISAL_CRYPTO_DIR)/.libs|-Wl,-rpath=%_libdir/spdk/lib|;' \
  -e 's|-Wl,-rpath=$(ISAL_DIR)/.libs|-Wl,-rpath=%_libdir/spdk/lib|;' \
  mk/spdk.common.mk
%else
sed -i '/isal/s|SYS_LIBS|LOCAL_SYS_LIBS|g' \
  $(find ./ -name 'Makefile')
%endif

# Remove illegal absolute entry from RPATH.
sed -i '/-Wl,-rpath=$(DESTDIR)\/$(libdir)/d' \
  mk/spdk.common.mk
sed -i 's|-rpath=$(SPDK_LIB_DIR),||' \
  $(find ./test/external_code/ -name 'Makefile') \
  $(find ./examples -name 'Makefile')

# fix startup scripts
sed -i 's|include/spdk/pci_ids.h|include/pci_ids.h|' \
  scripts/common.sh \
  test/vmd/vmd.sh

# fix python shebangs
sed -i \
  -e 's|/usr/bin/env python3|%__python3|;' \
  -e 's|/usr/bin/env python|%__python3|;' \
  $(find ./ -name '*.py')
sed -i '1i #!%__python3' \
  dpdk/usertools/telemetry-endpoints/*.py \
  scripts/gdb_macros.py \
  scripts/perf/nvmf/common.py

# disable python buildings via uv using Makefile
sed -i '/python/d' Makefile

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

%if_with dpdk
export CONFIG_DPDK_LIB_DIR=%_libdir
export CONFIG_DPDK_INC_DIR=%_includedir/dpdk
export DPDK_ABS_DIR=%_prefix
export DPDK_INC_DIR=%_includedir/dpdk
export DPDK_LIB_DIR=%_libdir
%endif

%_configure_script \
  --prefix=%_prefix \
  --libdir=%_libdir \
%if_with dpdk
  --with-dpdk=%_libdir \
%endif
%if_disabled clang
  --cross-prefix=%_target_alias \
%endif
%if_with isal
  --with-system-isal \
%endif
  --without-crypto \
%if_enabled shared
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
%make all
%pyproject_build
cd -

%install
%if_with dpdk
export CONFIG_DPDK_LIB_DIR=%_libdir
export CONFIG_DPDK_INC_DIR=%_includedir/dpdk
%else
export DPDK_LIB_DIR=%_libdir/spdk/lib
%endif

%makeinstall_std
cd python/
%pyproject_install
cd -

cfs() {
  (($# > 1)) || return 0
  local dst=$1 f
  mkdir -p "$dst"
  shift; for f; do [[ -e $f ]] && cp -a "$f" "$dst"; done
}

cl() {
  [[ -e $2 ]] || return 0
  cfs "$1" $(find "$2" -name '*.so*' -type f -o -type l | grep -v .symbols)
}

# We need to take into the account the fact that most of the scripts depend on being
# run directly from the repo. To workaround it, create common root space under dir
# like /usr/libexec/spdk and link all potential relative paths the script may try
# to reference.

mkdir -p %buildroot%_libdir/spdk/lib/
mkdir -p %buildroot%_libexecdir/spdk/bin/
mkdir -p %buildroot%_includedir/spdk/dpdk/
mv -f %buildroot%_includedir/{cmdline*.h,generic,rte*.h} %buildroot%_includedir/spdk/dpdk/
mv -f %buildroot%_bindir/{iscsi_tgt,nvmf_tgt,vhost,spdk*} %buildroot%_libexecdir/spdk/bin/

# DPDK always builds both static and shared, so we need to remove one or the other
# SPDK always builds static, so remove it if we want shared.

%if_without isal
mv -f %buildroot%_includedir/isa-l* %buildroot%_includedir/spdk/dpdk/
rm -f %buildroot%_prefix/lib/pkgconfig/libisal*.pc
%if_enabled shared
rm -f %buildroot%_prefix/lib/libisal*.a
mv -f %buildroot%_prefix/lib/libisal*.so* %buildroot%_libdir/spdk/lib/
%else
rm -f %buildroot%_prefix/lib/libisal*.so*
mv -f %buildroot%_prefix/lib/libisal*.a %buildroot%_libdir/spdk/lib/
%endif
%endif

%if_enabled shared
mv -f %buildroot%_prefix/lib/librte*.so* %buildroot%_libdir/spdk/lib/
mv -f %buildroot%_prefix/lib/dpdk/pmds*/librte*.so* %buildroot%_libdir/spdk/lib/
rm -f %buildroot%_libdir/*.a
rm -rf %buildroot%_prefix/lib/lib*.a
%else
mv -f %buildroot%_libdir/librte*.a %buildroot%_libdir/spdk/lib/
mv -f %buildroot%_prefix/lib/dpdk/pmds*/librte*.a %buildroot%_libdir/spdk/lib/
rm -f %buildroot%_libdir/lib*.so*
%endif

%if_with dpdk
# DPDK also installs some python scripts to bin that we do not want to package here
rm -f %buildroot%_bindir/dpdk-*.py
# DPDK examples do not need to be packaged in our RPMs
rm -rf %buildroot%_datadir/dpdk
# In case sphinx-build is available, DPDK will leave some files we don't need
rm -rf %buildroot%_datadir/doc/dpdk
%else
mkdir -p %buildroot%_libexecdir/spdk/scripts/dpdk/
mv -f %buildroot%_bindir/dpdk-*.py %buildroot%_libexecdir/spdk/scripts/dpdk/
mv -f %buildroot%_datadir/dpdk/telemetry-endpoints/ %buildroot%_libexecdir/spdk/scripts/dpdk/
rm -rf %buildroot%_prefix/lib/pkgconfig/libdpdk*.pc
rm -rf %buildroot%_datadir/dpdk/examples/
%endif

# The ISA-L install may have installed some binaries that we do not want to package
rm -f %buildroot%_bindir/igzip
rm -rf %buildroot%_datadir/man

# Include libvfio-user libs in case --with-vfio-user is in use together with --with-shared
%if_with vfio_user && %if_enabled shared
cl %buildroot%_libdir/libvfio-user build/libvfio-user/
%endif

# And some useful setup scripts SPDK uses
mkdir -p %buildroot%_libexecdir/spdk
mkdir -p %buildroot%_sysconfdir/bash_completion.d
mkdir -p %buildroot%_sysconfdir/profile.d
# mkdir -p %buildroot%_sysconfdir/ld.so.conf.d

# %if_enabled shared
# cat <<-EOF > %buildroot%_sysconfdir/ld.so.conf.d/spdk.conf
# %_libdir/spdk/lib
# EOF
# %endif

cat <<-'EOF' > %buildroot%_sysconfdir/profile.d/spdk_path.sh
PATH=$PATH:%_libexecdir/spdk/scripts
PATH=$PATH:%_libexecdir/spdk/scripts/vagrant
PATH=$PATH:%_libexecdir/spdk/test/common/config
PATH=$PATH:%_libexecdir/spdk/bin
PATH=$PATH:%_libexecdir/spdk/include
PATH=$PATH:%_libexecdir/spdk/examples
export PATH
EOF

cfs %buildroot%_libexecdir/spdk scripts
cfs %buildroot%_libexecdir/spdk build/examples
ln -s %_libexecdir/spdk/scripts/bash-completion/spdk %buildroot%_sysconfdir/bash_completion.d/

# setup.sh uses pci_ids.h
ln -s %_includedir/spdk %buildroot%_prefix/libexec/spdk/include

# Remove obloleted scripts
rm -rf %buildroot%_libexecdir/spdk/scripts/*.orig

%if_enabled shared
# libspdk_ut_mock.so.3.0 statically linked?!
rm -f %buildroot%_libdir/libspdk_ut_mock.so*
rm -f %buildroot%_pkgconfigdir/spdk_ut_mock.pc

# fix undefined symbols
patchelf %buildroot%_libdir/libspdk_env_dpdk.so.16.1 --add-needed librte_eal.so.26.0
patchelf %buildroot%_libdir/libspdk_env_dpdk.so.16.1 --add-needed librte_mempool.so.26.0
patchelf %buildroot%_libdir/libspdk_env_dpdk.so.16.1 --add-needed librte_ring.so.26.0
patchelf %buildroot%_libdir/libspdk_env_dpdk.so.16.1 --add-needed librte_mbuf.so.26.0
patchelf %buildroot%_libdir/libspdk_env_dpdk.so.16.1 --add-needed librte_bus_pci.so.26.0
patchelf %buildroot%_libdir/libspdk_env_dpdk.so.16.1 --add-needed librte_pci.so.26.0
patchelf %buildroot%_libdir/libspdk_env_dpdk.so.16.1 --add-needed librte_mempool_ring.so.26.0
patchelf %buildroot%_libdir/libspdk_env_dpdk.so.16.1 --add-needed librte_telemetry.so.26.0
patchelf %buildroot%_libdir/libspdk_env_dpdk.so.16.1 --add-needed librte_kvargs.so.26.0
patchelf %buildroot%_libdir/libspdk_env_dpdk.so.16.1 --add-needed librte_rcu.so.26.0
patchelf %buildroot%_libdir/libspdk_env_dpdk.so.16.1 --add-needed librte_power.so.26.0
patchelf %buildroot%_libdir/libspdk_env_dpdk.so.16.1 --add-needed librte_ethdev.so.26.0
patchelf %buildroot%_libdir/libspdk_env_dpdk.so.16.1 --add-needed librte_vhost.so.26.0
patchelf %buildroot%_libdir/libspdk_env_dpdk.so.16.1 --add-needed librte_net.so.26.0
patchelf %buildroot%_libdir/libspdk_env_dpdk.so.16.1 --add-needed librte_dmadev.so.26.0
patchelf %buildroot%_libdir/libspdk_env_dpdk.so.16.1 --add-needed librte_cryptodev.so.26.0
patchelf %buildroot%_libdir/libspdk_env_dpdk_rpc.so.7.0 --add-needed libspdk_env_dpdk.so.16.1
patchelf %buildroot%_libdir/libspdk_scheduler_dpdk_governor.so.5.0 --add-needed libspdk_env_dpdk.so.16.1
patchelf %buildroot%_libdir/libspdk_scheduler_dpdk_governor.so.5.0 --add-needed librte_power.so.26
patchelf %buildroot%_libdir/libspdk_scheduler_gscheduler.so.5.0 --add-needed libspdk_env_dpdk.so.16.1
patchelf %buildroot%_libdir/libspdk_scheduler_dynamic.so.5.0 --add-needed libspdk_env_dpdk.so.16.1
patchelf %buildroot%_libdir/libspdk_sock_posix.so.7.0 --add-needed libspdk_env_dpdk.so.16.1
patchelf %buildroot%_libdir/libspdk_event_nvmf.so.7.0 --add-needed libspdk_env_dpdk.so.16.1
patchelf %buildroot%_libdir/libspdk_event_vmd.so.7.0 --add-needed libspdk_env_dpdk.so.16.1
patchelf %buildroot%_libdir/libspdk_accel.so.17.0 --add-needed libisal.so.2.0.31
patchelf %buildroot%_libdir/libspdk_accel.so.17.0 --add-needed libisal_crypto.so.2.0.26
patchelf %buildroot%_libdir/libspdk_accel_ioat.so.7.0 --add-needed libspdk_env_dpdk.so.16.1
patchelf %buildroot%_libdir/libspdk_bdev.so.19.0 --add-needed libspdk_env_dpdk.so.16.1
patchelf %buildroot%_libdir/libspdk_bdev_virtio.so.7.0 --add-needed libspdk_env_dpdk.so.16.1
patchelf %buildroot%_libdir/libspdk_bdev_raid.so.7.0 --add-needed libspdk_env_dpdk.so.16.1
patchelf %buildroot%_libdir/libspdk_bdev_nvme.so.8.0 --add-needed libspdk_env_dpdk.so.16.1
patchelf %buildroot%_libdir/libspdk_bdev_null.so.7.0 --add-needed libspdk_env_dpdk.so.16.1
patchelf %buildroot%_libdir/libspdk_bdev_malloc.so.7.0 --add-needed libspdk_env_dpdk.so.16.1
patchelf %buildroot%_libdir/libspdk_bdev_gpt.so.7.0 --add-needed libspdk_env_dpdk.so.16.1
patchelf %buildroot%_libdir/libspdk_bdev_delay.so.7.0 --add-needed libspdk_env_dpdk.so.16.1
patchelf %buildroot%_libdir/libspdk_fuse_dispatcher.so.2.0 --add-needed libspdk_env_dpdk.so.16.1
patchelf %buildroot%_libdir/libspdk_fsdev.so.3.0 --add-needed libspdk_env_dpdk.so.16.1
patchelf %buildroot%_libdir/libspdk_virtio.so.8.0 --add-needed libspdk_env_dpdk.so.16.1
patchelf %buildroot%_libdir/libspdk_vhost.so.9.0 --add-needed libspdk_env_dpdk.so.16.1
patchelf %buildroot%_libdir/libspdk_vfio_user.so.6.0 --add-needed libspdk_env_dpdk.so.16.1
patchelf %buildroot%_libdir/libspdk_ftl.so.10.0 --add-needed libspdk_env_dpdk.so.16.1
patchelf %buildroot%_libdir/libspdk_nbd.so.8.0 --add-needed libspdk_env_dpdk.so.16.1
patchelf %buildroot%_libdir/libspdk_iscsi.so.9.0 --add-needed libspdk_env_dpdk.so.16.1
patchelf %buildroot%_libdir/libspdk_ioat.so.8.0 --add-needed libspdk_env_dpdk.so.16.1
patchelf %buildroot%_libdir/libspdk_nvmf.so.22.0 --add-needed libspdk_env_dpdk.so.16.1
patchelf %buildroot%_libdir/libspdk_vmd.so.7.0 --add-needed libspdk_env_dpdk.so.16.1
patchelf %buildroot%_libdir/libspdk_nvme.so.17.0 --add-needed libspdk_env_dpdk.so.16.1
patchelf %buildroot%_libdir/libspdk_event.so.15.1 --add-needed libspdk_env_dpdk.so.16.1
patchelf %buildroot%_libdir/libspdk_init.so.7.0 --add-needed libspdk_env_dpdk.so.16.1
patchelf %buildroot%_libdir/libspdk_blob.so.13.1 --add-needed libspdk_env_dpdk.so.16.1
patchelf %buildroot%_libdir/libspdk_thread.so.12.0 --add-needed libspdk_env_dpdk.so.16.1
patchelf %buildroot%_libdir/libspdk_trace.so.12.0 --add-needed libspdk_env_dpdk.so.16.1
patchelf %buildroot%_libdir/libspdk_scsi.so.10.0 --add-needed libspdk_env_dpdk.so.16.1
patchelf %buildroot%_libdir/libspdk_util.so.11.0 --add-needed libspdk_env_dpdk.so.16.1
patchelf %buildroot%_libdir/libspdk_util.so.11.0 --add-needed libisal.so.2.0.31
patchelf %buildroot%_libexecdir/spdk/bin/spdk_trace_record --add-rpath %_libdir/spdk/lib
patchelf %buildroot%_libexecdir/spdk/bin/spdk_trace --add-rpath %_libdir/spdk/lib
patchelf %buildroot%_libexecdir/spdk/bin/spdk_top --add-rpath %_libdir/spdk/lib
patchelf %buildroot%_libexecdir/spdk/bin/spdk_tgt --add-rpath %_libdir/spdk/lib
patchelf %buildroot%_libexecdir/spdk/bin/spdk_nvme_perf --add-rpath %_libdir/spdk/lib
patchelf %buildroot%_libexecdir/spdk/bin/spdk_nvme_identify --add-rpath %_libdir/spdk/lib
patchelf %buildroot%_libexecdir/spdk/bin/spdk_nvme_discover --add-rpath %_libdir/spdk/lib
patchelf %buildroot%_libexecdir/spdk/bin/spdk_lspci --add-rpath %_libdir/spdk/lib
patchelf %buildroot%_libexecdir/spdk/bin/spdk_dd --add-rpath %_libdir/spdk/lib
patchelf %buildroot%_libexecdir/spdk/bin/vhost --add-rpath %_libdir/spdk/lib
patchelf %buildroot%_libexecdir/spdk/bin/nvmf_tgt --add-rpath %_libdir/spdk/lib
patchelf %buildroot%_libexecdir/spdk/bin/iscsi_tgt --add-rpath %_libdir/spdk/lib
patchelf %buildroot%_libdir/spdk/lib/*.so --add-rpath %_libdir/spdk/lib
patchelf %buildroot%_libexecdir/spdk/examples/* --shrink-rpath --allowed-rpath-prefixes %_libdir/spdk/lib
patchelf %buildroot%_libexecdir/spdk/examples/* --add-rpath %_libdir/spdk/lib
%endif

%files
# %_sysconfdir/ld.so.conf.d/spdk.conf
%_sysconfdir/profile.d/*
%_sysconfdir/bash_completion.d/spdk
%dir %_libexecdir/spdk/
%_libexecdir/spdk/*

%files devel
%dir %_includedir/spdk/
%_includedir/spdk/*
%_pkgconfigdir/*.pc
%if_enabled shared
%_libdir/lib*.so
%files libs
%_libdir/lib*.so.*
%else
%files devel-static
%_libdir/lib*.a
%endif

%if_without dpdk
%files libs-dpdk
%dir %_libdir/spdk/
%_libdir/spdk/lib/
%endif

%files -n python3-module-%name
%python3_sitelibdir_noarch/%name/
%python3_sitelibdir_noarch/%{name}-*

%changelog
* Tue Mar 24 2026 Leontiy Volodin <lvol@altlinux.org> 26.01-alt1
- New version 26.01.
- Built on built-in dpdk (ALT #58136).
- Excluded build on aarch64.

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

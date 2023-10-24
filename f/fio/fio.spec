%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
# unresolved=relaxed because of DSOs.
%set_verify_elf_method strict,unresolved=relaxed

%def_enable gfio
%def_enable http
%def_enable libblkio
%def_enable libiscsi
%def_enable libnbd
%def_enable libnfs
%def_enable numa
%def_enable rdmacm
%ifarch %ix86 %arm %mips32 ppc
%def_disable rbd
%else
%def_enable rbd
%endif
%ifarch armh
%def_disable gfapi
%else
%def_enable gfapi
%endif
%ifarch x86_64 aarch64 ppc64le
%def_enable libpmem
%else
%def_disable libpmem
%endif

Name: fio
Version: 3.36
Release: alt2
Summary: Flexible I/O Tester
License: GPL-2.0
Group: System/Kernel and hardware
Url: https://git.kernel.dk/cgit/fio/
# Backup: https://github.com/axboe/fio
Obsoletes: fio-tools < %EVR

Conflicts: python3-module-fiona
%add_python3_req_skip pandas
# Instead of Recommends.
Provides: fio-engine-libaio

Source0: %name-%version.tar
BuildRequires(pre): rpm-build-python3
BuildRequires: libaio-devel
BuildRequires: zlib-devel
%{?_enable_gfapi:BuildRequires: libglusterfs-devel}
%{?_enable_gfio:BuildRequires: libgtk+2-devel}
%{?_enable_http:BuildRequires: libcurl-devel libssl-devel}
%{?_enable_libblkio:BuildRequires: libblkio-devel}
%{?_enable_libiscsi:BuildRequires: libiscsi-devel}
%{?_enable_libnbd:BuildRequires: libnbd-devel}
%{?_enable_libnfs:BuildRequires: libnfs-devel}
%{?_enable_numa:BuildRequires: libnuma-devel }
%{?_enable_rbd:BuildRequires: ceph-devel}
%{?_enable_rdmacm:BuildRequires: librdmacm-devel}
%{?_enable_libpmem:BuildRequires: libpmem-devel}
%{?!_without_check:%{?!_disable_check:
BuildRequires: CUnit-devel
}}

%description
fio is a tool that will spawn a number of threads or processes doing a
particular type of io action as specified by the user. fio takes a
number of global parameters, each inherited by the thread unless
otherwise parameters given to them overriding that setting is given.
The typical use of fio is to write a job file matching the io load
one wants to simulate.

%package engine-http
Summary: HTTP engine for fio
Requires: %name = %EVR
Group: %group

%description engine-http
%summary (based on libcurl).

%package engine-libblkio
Summary: libblkio engine for fio
Requires: %name = %EVR
Group: %group

%description engine-libblkio
%summary.

%package engine-libiscsi
Summary: iSCSI engine for fio
Requires: %name = %EVR
Group: %group

%description engine-libiscsi
%summary.

%package engine-nbd
Summary: Network Block Device engine for fio
Requires: %name = %EVR
Group: %group

%description engine-nbd
%summary.

%package engine-pmdk
Summary: PMDK engines for fio
Requires: %name = %EVR
Group: %group
Provides: fio-engine-dev-dax
Provides: fio-engine-libpmem

%description engine-pmdk
%summary: dev-dax and libpmem.

%package engine-rados
Summary: Rados engines for fio
Requires: %name = %EVR
Group: %group
Provides: fio-engine-rbd

%description engine-rados
%summary: rados and rbd (Rados Block Device).

%package engine-rdma
Summary: RDMA engine for fio
Requires: %name = %EVR
Group: %group

%description engine-rdma
%summary.

%package -n gfio
Summary: GTK frontend for %name
Group: System/Kernel and hardware
Requires: %name = %version-%release

%description -n gfio
fio is a tool that will spawn a number of threads or processes doing a
particular type of io action as specified by the user. fio takes a
number of global parameters, each inherited by the thread unless
otherwise parameters given to them overriding that setting is given.
The typical use of fio is to write a job file matching the io load
one wants to simulate.

This package contains GTK frontend for %name.

%package checkinstall
Summary: CI test for %name
Group: Development/Other
BuildArch: noarch
Requires(post): fio-engine-nbd = %EVR
# Attempt to solve package ambiguity due to pve-qemu-img.
Requires(post): qemu-img /usr/bin/qemu-nbd
Requires(post): /usr/bin/time

%description checkinstall
%summary.

%prep
%setup
find  -name '*.py' | xargs sed -i '1s|#!/usr/bin/env python3|#!%__python3|'
sed -i '\!FIO_EXT_ENG_DIR!s!".*"!"%_libdir/fio"!' os/os-linux.h

%build
./configure \
	--prefix=%_prefix \
	--disable-native \
	--dynamic-libengines \
	--disable-optimizations \
	%{subst_enable gfio} \
	%{subst_enable libiscsi} \
	%{subst_enable libnbd} \
	--extra-cflags="%optflags"
%make_build V=1

%install
%makeinstall_std mandir=%_mandir libdir=%_libdir/fio

%check
unittests/unittest
%make test
./fio -i

%post checkinstall
set -ex
fio -i
fio -i | grep -w libaio
fio -i'aio'
%if_enabled libnbd
cd $(mktemp -d)
truncate -s 256M disk.img
qemu-nbd -t -k $PWD/socket -f raw disk.img &
sleep 1
time fio --ioengine=nbd --rw=randrw --time_based --runtime=3 --uri=nbd+unix:///?socket=socket --name=job
kill %%
rm disk.img
rmdir $PWD
%endif

%files
%define _customdocdir %_docdir/%name
%doc HOWTO* README* REPORTING-BUGS examples
%doc COPYING CITATION.cff MORAL-LICENSE
%_bindir/*
%dir %_libdir/fio
%_libdir/fio/fio-libaio.so
%exclude %_bindir/gfio
%_datadir/%name
%_man1dir/*.1*

%if_enabled http
%files engine-http
%_libdir/fio/fio-http.so
%endif

%files engine-libblkio
%_libdir/fio/fio-libblkio.so

%if_enabled libiscsi
%files engine-libiscsi
%_libdir/fio/fio-libiscsi.so
%endif

%if_enabled libnbd
%files engine-nbd
%_libdir/fio/fio-nbd.so
%endif

%if_enabled libpmem
%files engine-pmdk
%_libdir/fio/fio-dev-dax.so
%_libdir/fio/fio-libpmem.so
%endif

%if_enabled rbd
%files engine-rados
%_libdir/fio/fio-rados.so
%_libdir/fio/fio-rbd.so
%endif

%if_enabled rdmacm
%files engine-rdma
%_libdir/fio/fio-rdma.so
%endif

%if_enabled gfio
%files -n gfio
%_bindir/gfio
%endif

%files checkinstall

%changelog
* Tue Oct 24 2023 Vitaly Chikunov <vt@altlinux.org> 3.36-alt2
- Split external I/O engine into separate packages.
- spec: Add checkinstall package.
- spec: Update Summary.

* Mon Oct 23 2023 Vitaly Chikunov <vt@altlinux.org> 3.36-alt1
- Update to fio-3.36 (2023-10-20).
- Enable nbd and nfs engines.
- Merge fio-tools into fio package.
- spec: Run unit tests in %%check.

* Thu Jul 20 2023 Vitaly Chikunov <vt@altlinux.org> 3.35-alt1
- Update to fio-3.35 (2023-05-23).
- Do not package html docs (there are .rst docs already).
- Add libblkio, libiscsi, and pmem/dev-dax engines.
- spec: Run (smoke) tests in %%check.

* Tue Aug 31 2021 Vitaly Lipatov <lav@altlinux.ru> 3.27-alt1
- new version 3.27
- add upstream fix: remove raw device support

* Tue Mar 16 2021 Vitaly Lipatov <lav@altlinux.ru> 3.26-alt1
- new version 3.26

* Thu Sep 10 2020 Vitaly Lipatov <lav@altlinux.ru> 3.23-alt1
- new version 3.23 (with rpmrb script)

* Wed Feb 05 2020 Vitaly Lipatov <lav@altlinux.ru> 3.17-alt1.1
- NMU: real drop python2 deps

* Wed Feb 05 2020 Vitaly Lipatov <lav@altlinux.ru> 3.17-alt1
- NMU: build new version
- use libglusterfs-devel instead of libglusterfs3-devel
- use python3 only

* Sat Feb 23 2019 Alexey Shabalin <shaba@altlinux.org> 3.13-alt1
- 3.13
- disable support ceph on 32-bit arch
- build with http support for WebDAV and S3

* Tue Aug 29 2017 Terechkov Evgenii <evg@altlinux.org> 3.0-alt2
- Build documentation

* Tue Aug 29 2017 Terechkov Evgenii <evg@altlinux.org> 3.0-alt1
- 3.0

* Tue Jun 14 2016 Alexey Shabalin <shaba@altlinux.ru> 2.12-alt1
- 2.12
- build with support numa, ceph, gluster, rdmacm

* Sun Jan 19 2014 Alexey Shabalin <shaba@altlinux.ru> 2.1.4-alt1
- 2.1.4
- add packages fio-tools and gfio

* Thu Dec 13 2012 Slava Dubrovskiy <dubrsl@altlinux.org> 2.0.11-alt1
- 2.0.11

* Fri Nov 30 2012 Slava Dubrovskiy <dubrsl@altlinux.org> 2.0.10-alt1
- 2.0.10

* Sun Apr 15 2012 Victor Forsiuk <force@altlinux.org> 2.0.7-alt1
- 2.0.7

* Sun Mar 25 2012 Victor Forsiuk <force@altlinux.org> 2.0.6-alt1
- 2.0.6

* Sat Oct 08 2011 Michael Shigorin <mike@altlinux.org> 1.59-alt1
- 1.59

* Fri Jul 22 2011 Victor Forsiuk <force@altlinux.org> 1.57-alt1
- 1.57

* Sun Jun 12 2011 Victor Forsiuk <force@altlinux.org> 1.55-alt1
- 1.55

* Sun Mar 14 2010 Igor Zubkov <icesik@altlinux.org> 1.37-alt1
- 1.36 -> 1.37

* Wed Dec 16 2009 Igor Zubkov <icesik@altlinux.org> 1.36-alt1
- 1.34 -> 1.36

* Thu Oct 01 2009 Igor Zubkov <icesik@altlinux.org> 1.34-alt1
- 1.24 -> 1.34

* Wed Mar 25 2009 Igor Zubkov <icesik@altlinux.org> 1.24-alt1
- 1.23 -> 1.24

* Tue Dec 02 2008 Igor Zubkov <icesik@altlinux.org> 1.23-alt1
- 1.21 -> 1.23

* Sat Jul 19 2008 Igor Zubkov <icesik@altlinux.org> 1.21-alt1
- 1.17.2 -> 1.21

* Thu Nov 01 2007 Igor Zubkov <icesik@altlinux.org> 1.17.2-alt1
- build for Sisyphus


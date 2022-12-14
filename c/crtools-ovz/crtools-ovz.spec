%def_without check
%define optflags_lto %nil

Name: crtools-ovz
Version: 3.15.4.16
Release: alt1

Summary: Utility to checkpoint/restore tasks for OpenVZ containers
License: GPL-2.0-only
Group: System/Configuration/Other
Url: http://criu.org
Vcs: https://src.openvz.org/scm/ovz/criu.git

Packager: Andrew A. Vasilyev <andy@altlinux.org>

Source: criu-%version.tar

Provides: criu-ovz = %EVR
Conflicts: crtools
Conflicts: python3-module-criu
ExclusiveArch: x86_64

BuildRequires: libnet2-devel
BuildRequires: libprotobuf-c-devel %_bindir/protoc-c
BuildRequires: libprotobuf-devel protobuf-compiler
BuildRequires: asciidoc xmlto %_bindir/a2x
BuildRequires: libnftables-devel
BuildRequires: libgnutls-devel
BuildRequires: glibc-devel
BuildRequires: libnl-devel
BuildRequires: libcap-devel
BuildRequires: python3-base
# BuildRequires: python3-devel
# BuildRequires: libselinux-devel
BuildRequires(pre): rpm-build-python3

%if_with check
BuildRequires: rpm-build-vm-run
BuildRequires: vzkernel
BuildRequires: libaio-devel
BuildRequires: python3-module-future python3-module-yaml python3-module-protobuf
BuildRequires: libbsd-devel
BuildRequires: iproute2 iptables iputils openvswitch
%endif

Requires: nftables util-linux ipset

%add_python3_self_prov_path %buildroot%python3_sitelibdir/pycriu
%add_python3_self_prov_path %buildroot%python3_sitelibdir/pycriu/images
%add_findprov_skiplist %python3_sitelibdir/pycriu/*
%add_findprov_skiplist %python3_sitelibdir/pycriu/*/*
%add_python3_req_skip core_aarch64_pb2 core_arm_pb2 core_mips_pb2 core_pb2 core_ppc64_pb2 core_s390_pb2 core_x86_pb2
%add_python3_req_skip creds_pb2 eventfd_pb2 eventpoll_pb2 ext_file_pb2 fh_pb2 fifo_pb2 fown_pb2 fsnotify_pb2 ipc_desc_pb2
%add_python3_req_skip macvlan_pb2 memfd_pb2 ns_pb2 openvswitch_pb2 opts_pb2 packet_sock_pb2 pipe_pb2 regfile_pb2 rlimit_pb2
%add_python3_req_skip sa_pb2 siginfo_pb2 signalfd_pb2 sit_pb2 sk_inet_pb2 sk_netlink_pb2 sk_opts_pb2 sk_unix_pb2 sysctl_pb2
%add_python3_req_skip time_pb2 timerfd_pb2 timer_pb2 tty_pb2 tun_pb2 vma_pb2 vxlan_pb2 bpfmap_file_pb2

%description
An utility to checkpoint/restore tasks for OpenVZ containers.

%prep
%setup -n criu-%version

%build
# Upstream claims that stack protection break criu
# https://github.com/checkpoint-restore/criu/issues/1744#issuecomment-1031605370
%add_optflags -fno-stack-protector -fno-stack-clash-protection
export CFLAGS="%optflags -fcommon -Wno-stringop-overflow"
export PYTHON=python3
%make_build \
	PREFIX=%prefix V=1 all docs

%install
export PYTHON=python3
%makeinstall_std \
	PREFIX=%prefix LIBDIR=%_libdir LIBEXECDIR=%_libexecdir SYSTEMDUNITDIR=%_unitdir

mv %buildroot%_sbindir/criu{,-ovz}
ln -s criu-ovz %buildroot%_sbindir/criu
ln -s criu-ovz %buildroot%_sbindir/crtools
ln -s criu.8 %buildroot%_man8dir/crtools.8

find %buildroot -name 'lib*.a' -delete

rm -f %buildroot%_bindir/crit
# rm -rf %%buildroot%%python3_sitelibdir_noarch
mkdir -p %buildroot%_libdir/python3/
mv %buildroot{%python3_sitelibdir_noarch,%_libdir/python3}
rmdir %buildroot%_usr/lib/python3 ||:

rm -f %buildroot%_man1dir/crit.1*
rm -f %buildroot%_libdir/libcriu.so.2*
rm -f %buildroot%_libdir/libcompel.so.1*
rm -rf %buildroot%_includedir/criu
rm -rf %buildroot%_includedir/compel
rm -f %buildroot%_libdir/*.so
rm -f %buildroot%_pkgconfigdir/criu.pc

%check
vm-run --kvm=cond --sbin --udevd make test || :

%files
%doc README.md COPYING CREDITS
%_sbindir/criu
%_sbindir/criu-ovz
%_sbindir/crtools
%_bindir/compel
%_libexecdir/criu
%_libexecdir/compel
%_man1dir/compel.1*
%_man8dir/criu.8*
%_man8dir/crtools.8*
%python3_sitelibdir/pycriu
%python3_sitelibdir/crit-*.egg-info

%changelog
* Sun Dec 11 2022 Andrew A. Vasilyev <andy@altlinux.org> 3.15.4.16-alt1
- 3.15.4.16
- add python libs for p.haul-ovz (instead of python3-module-criu)

* Mon Nov 14 2022 Andrew A. Vasilyev <andy@altlinux.org> 3.15.4.14-alt1
- 3.15.4.14
- build without stack protection

* Wed Oct 26 2022 Andrew A. Vasilyev <andy@altlinux.org> 3.15.4.13-alt1
- 3.15.4.13

* Wed Jun 08 2022 Andrew A. Vasilyev <andy@altlinux.org> 3.15.4.9-alt1
- 3.15.4.9

* Wed Jun 01 2022 Andrew A. Vasilyev <andy@altlinux.org> 3.15.4.8-alt1
- 3.15.4.8
- fix build with GCC 12

* Thu May 12 2022 Andrew A. Vasilyev <andy@altlinux.org> 3.15.4.7-alt1
- 3.15.4.7

* Mon May 09 2022 Andrew A. Vasilyev <andy@altlinux.org> 3.15.4.6-alt1
- 3.15.4.6

* Wed Apr 27 2022 Andrew A. Vasilyev <andy@altlinux.org> 3.15.4.5-alt1
- 3.15.4.5

* Tue Mar 01 2022 Andrew A. Vasilyev <andy@altlinux.org> 3.15.4.3-alt1
- 3.15.4.3

* Fri Jan 21 2022 Andrew A. Vasilyev <andy@altlinux.org> 3.15.4.1-alt1
- 3.15.4.1

* Tue Dec 21 2021 Andrew A. Vasilyev <andy@altlinux.org> 3.15.3.11-alt1
- 3.15.3.11

* Wed Nov 10 2021 Andrew A. Vasilyev <andy@altlinux.org> 3.15.3.6-alt1
- 3.15.3.6

* Wed Sep 22 2021 Andrew A. Vasilyev <andy@altlinux.org> 3.15.2.9-alt4
- FTBFS: gcc11: false stringop-overflow

* Mon Sep 20 2021 Andrew A. Vasilyev <andy@altlinux.org> 3.15.2.9-alt3
- protobuf: remove leading underscores from protobuf structs (from criu upstream)

* Thu Sep 16 2021 Andrew A. Vasilyev <andy@altlinux.org> 3.15.2.9-alt2
- FTBFS: remove leading underscores in structs

* Tue Aug 24 2021 Andrew A. Vasilyev <andy@altlinux.org> 3.15.2.9-alt1
- 3.15.2.9
- disable LTO

* Fri Aug 06 2021 Andrew A. Vasilyev <andy@altlinux.org> 3.15.2.6-alt1
- 3.15.2.6

* Thu Jul 08 2021 Andrew A. Vasilyev <andy@altlinux.org> 3.15.2.5-alt1
- 3.15.2.5

* Fri Jun 04 2021 Andrew A. Vasilyev <andy@altlinux.org> 3.15.2.2-alt1
- 3.15.2.2

* Tue Apr 13 2021 Andrew A. Vasilyev <andy@altlinux.org> 3.15.1.27-alt1
- 3.15.1.27

* Thu Apr 08 2021 Andrew A. Vasilyev <andy@altlinux.org> 3.15.1.26-alt1
- 3.15.1.26

* Mon Mar 08 2021 Andrew A. Vasilyev <andy@altlinux.org> 3.15.1.23-alt1
- 3.15.1.23

* Fri Feb 19 2021 Andrew A. Vasilyev <andy@altlinux.org> 3.15.1.22-alt1
- 3.15.1.22

* Mon Feb 01 2021 Andrew A. Vasilyev <andy@altlinux.org> 3.15.1.15-alt1
- 3.15.1.15

* Sat Jan 02 2021 Andrew A. Vasilyev <andy@altlinux.org> 3.15.0.15-alt1
- 3.15.0.15

* Fri Dec 25 2020 Andrew A. Vasilyev <andy@altlinux.org> 3.15.0.14-alt1
- 3.15.0.14

* Tue Dec 08 2020 Andrew A. Vasilyev <andy@altlinux.org> 3.15.0.9-alt1
- 3.15.0.9

* Mon Nov 09 2020 Andrew A. Vasilyev <andy@altlinux.org> 3.12.5.52-alt1
- 3.12.5.52
- cherry-picked commit 86a386a0171eb553d5d3bcb5db92ff13b1f60ad4
  from criu real upstream: "Update test_bit() and test_and_set_bit()
  implementation with recent version from the Linux kernel to fix the warning."

* Fri Oct 30 2020 Andrew A. Vasilyev <andy@altlinux.org> 3.12.5.50-alt1
- 3.12.5.50

* Mon Oct 12 2020 Andrew A. Vasilyev <andy@altlinux.org> 3.12.5.46-alt1
- 3.12.5.46

* Mon Oct 05 2020 Andrew A. Vasilyev <andy@altlinux.org> 3.12.5.44-alt1
- 3.12.5.44

* Fri Oct 02 2020 Andrew A. Vasilyev <andy@altlinux.org> 3.12.5.43-alt1
- 3.12.5.43

* Wed Sep 30 2020 Andrew A. Vasilyev <andy@altlinux.org> 3.12.5.41-alt1
- 3.12.5.41
- remove all extra packages not needed for OpenVZ

* Mon Sep 14 2020 Andrew A. Vasilyev <andy@altlinux.org> 3.12.5.40-alt1
- 3.12.5.40

* Fri Sep 11 2020 Andrew A. Vasilyev <andy@altlinux.org> 3.12.5.38-alt1
- Initial build for ALT from Virtuozzo fork of criu, spec based on crtool.


%def_with rdma
%ifarch armh
%def_without glfs
%else
%def_with glfs
%endif
%ifarch x86_64 aarch64 ppc64el
%def_with rbd
%else
%def_without rbd
%endif

Name: scsitarget-utils
Version: 1.0.92
Release: alt1

Summary: The SCSI target daemon and utility programs
License: GPLv2
Group: System/Configuration/Hardware

URL: https://github.com/fujita/tgt
Vcs: https://github.com/fujita/tgt.git

Source0: %name-%version.tar
Source1: tgt.service
Source2: sysconfig.tgtd
Source3: targets.conf
Source4: sample.conf
Source5: tgtd.conf
Source6: tgt.init

# fedora patches
Patch1: 0002-remove-check-for-xsltproc.patch
Patch2: 0003-default-config.patch
Patch3: tgt-1.0.79-Adapt-to-glusterfs-api-7.6.3.patch

BuildRequires: libxslt docbook-style-xsl xsltproc
BuildRequires: glibc-devel
BuildRequires: libaio-devel
BuildRequires: glibc-kernheaders
BuildRequires: systemd-devel
BuildRequires: perl-Config-General
%{?_with_rdma:BuildRequires: libibverbs-devel librdmacm-devel}
%{?_with_rbd:BuildRequires: ceph-devel}
%{?_with_glfs:BuildRequires: libglusterfs-devel >= 7.6}

Requires: lsof
Requires: sg3_utils

Provides: scsi-target-utils = %version-%release
Provides: tgt = %version-%release
Obsoletes: tgt < %version-%release
Provides: iscsitarget = 1.4.20.2-alt2.1
Obsoletes: iscsitarget < 1.4.20.2-alt2.1

%description
The SCSI target package contains the daemon and tools to setup
a SCSI target. Software iSCSI targets are currently supported.

%package rbd
Summary: Support for the Ceph rbd backstore to scsi-target-utils
Group: System/Configuration/Hardware
Requires: %name = %version-%release

%description rbd
Adds support for the Ceph rbd backstore to scsi-target-utils.

%package gluster
Summary: Support for the Gluster backstore to scsi-target-utils
Group: System/Configuration/Hardware
Requires: %name = %version-%release

%description gluster
Adds support for the Gluster glfs backstore to scsi-target-utils.

%prep
%setup
# %%patch10 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

### FIXME: aarch64 ftbfs workaround with gcc12-12.2.1-alt2 (#322140)
%ifarch aarch64
#sed -i "s/(char \*)siginfo/siginfo/" usr/bs.c
sed -i "s/-Werror/-Wno-error/" usr/Makefile
%endif

%build
sed -i 's|-g -O2 -Wall|%optflags|' Makefile
# to prevent race with mkdir() in xsltproc:
mkdir -p doc/htmlpages
%make_build \
	%{?_with_rdma:ISCSI_RDMA=1} \
	%{?_with_rbd:CEPH_RBD=1} \
	%{?_with_glfs:GLFS_BD=1} \
	SD_NOTIFY=1 \
	libdir=%_libdir/tgt

%install
mkdir -p %buildroot{%_sbindir,%_initdir,%_unitdir,%_sysconfdir/tgt/conf.d,%_sysconfdir/sysconfig,%_man5dir,%_man8dir}
mkdir -p %buildroot%_sysconfdir/tgt/include.d %buildroot%_sysconfdir/tgt/examples

install -p -m 0755 scripts/tgt-setup-lun %buildroot%_sbindir
install -p -m 0644 %SOURCE1 %buildroot%_unitdir
install -p -m 0755 scripts/tgt-admin %buildroot/%_sbindir/tgt-admin
install -p -m 0644 doc/manpages/targets.conf.5 %buildroot/%_man5dir
install -pD -m 0644 doc/manpages/*.8 %buildroot/%_man8dir
install -pD -m 0644 conf/examples/* %buildroot%_sysconfdir/tgt/examples
install -p -m 0600 %SOURCE2 %buildroot%_sysconfdir/sysconfig/tgtd
install -p -m 0600 %SOURCE3 %buildroot%_sysconfdir/tgt
install -p -m 0600 %SOURCE4 %buildroot%_sysconfdir/tgt/conf.d
install -p -m 0600 %SOURCE5 %buildroot%_sysconfdir/tgt
install -p -m 0755 %SOURCE6 %buildroot%_initdir/tgt

pushd usr
%makeinstall_std \
	%{?_with_rdma:ISCSI_RDMA=1} \
	%{?_with_rbd:CEPH_RBD=1} \
	%{?_with_glfs:GLFS_BD=1} \
	SD_NOTIFY=1 \
	sbindir=%_sbindir \
	libdir=%_libdir/tgt

# create and pack in any case
mkdir -p %buildroot%_libdir/tgt/backing-store

%post
%post_service tgt

%preun
%preun_service tgt

%files
%doc LICENSE README.md doc/README.* doc/*.txt doc/htmlpages
%_sbindir/tgtd
%_sbindir/tgtadm
%_sbindir/tgt-setup-lun
%_sbindir/tgt-admin
%_sbindir/tgtimg
%_man5dir/*
%_man8dir/*
%_unitdir/tgt.service
%_initdir/tgt
%dir %_libdir/tgt
%dir %_libdir/tgt/backing-store
%dir %_sysconfdir/tgt
%dir %_sysconfdir/tgt/conf.d
%dir %_sysconfdir/tgt/include.d
%_sysconfdir/tgt/examples
%attr(0600,root,root) %config(noreplace) %_sysconfdir/sysconfig/tgtd
%attr(0600,root,root) %config(noreplace) %_sysconfdir/tgt/targets.conf
%attr(0600,root,root) %config(noreplace) %_sysconfdir/tgt/tgtd.conf
%attr(0600,root,root) %config(noreplace) %_sysconfdir/tgt/conf.d/sample.conf

%if_with rbd
%files rbd
%_libdir/tgt/backing-store/bs_rbd.so
%doc doc/README.rbd
%endif

%if_with glfs
%files gluster
%_libdir/tgt/backing-store/bs_glfs.so
%doc doc/README.glfs
%endif

%changelog
* Mon Sep 02 2024 Andrew A. Vasilyev <andy@altlinux.org> 1.0.92-alt1
- 1.0.92

* Wed Mar 06 2024 Andrew A. Vasilyev <andy@altlinux.org> 1.0.91-alt1
- 1.0.91
- drop tgt-signalfd-via-glibc broken patch:
  https://github.com/fujita/tgt/commit/7ea55975

* Tue Oct 24 2023 Alexey Sheplyakov <asheplyakov@altlinux.org> 1.0.87-alt2
- NMU: use signalfd via glibc wrapper. Fixes FTBFS on LoongArch and riscv64

* Fri Sep 08 2023 Andrew A. Vasilyev <andy@altlinux.org> 1.0.87-alt1
- 1.0.87
- drop GlusterFS support for armh

* Wed Jun 28 2023 Andrew A. Vasilyev <andy@altlinux.org> 1.0.86-alt1
- 1.0.86
- drop use-after-free patch, fixed by upstream:
  https://github.com/fujita/tgt/commit/646aa7329

* Tue May 30 2023 Michael Shigorin <mike@altlinux.org> 1.0.83-alt2
- fix rbd arch condition
- minor spec cleanup
- aarch64 ftbfs workaround (ilyakurdyukov@)

* Mon Jul 18 2022 Andrew A. Vasilyev <andy@altlinux.org> 1.0.83-alt1
- 1.0.83
- fix use-after-free bug

* Wed Mar 09 2022 Andrew A. Vasilyev <andy@altlinux.org> 1.0.81-alt1
- 1.0.81

* Mon Feb 15 2021 Andrew A. Vasilyev <andy@altlinux.org> 1.0.80-alt1
- 1.0.80

* Thu Sep 17 2020 Andrew A. Vasilyev <andy@altlinux.org> 1.0.79-alt1
- 1.0.79
- enable build with glusterfs

* Thu Feb 06 2020 Vitaly Lipatov <lav@altlinux.ru> 1.0.78-alt2
- NMU: disable build with glusterfs (use pre 4.0 obsoleted glfs_pread)

* Tue Jun 04 2019 Alexey Shabalin <shaba@altlinux.org> 1.0.78-alt1
- 1.0.78
- obsoletes for iscsitarget

* Sat Feb 23 2019 Alexey Shabalin <shaba@altlinux.org> 1.0.74-alt1
- new version 1.0.74
- disable support ceph on 32-bit arch

* Mon Jan 11 2016 Alexey Shabalin <shaba@altlinux.ru> 1.0.62-alt1
- 1.0.62

* Fri Mar 20 2015 Alexey Shabalin <shaba@altlinux.ru> 1.0.55-alt3
- Obsoletes tgt

* Fri Mar 06 2015 Alexey Shabalin <shaba@altlinux.ru> 1.0.55-alt2
- fix unit perm

* Fri Mar 06 2015 Alexey Shabalin <shaba@altlinux.ru> 1.0.55-alt1
- 1.0.55

* Tue Sep 03 2013 Pavel Shilovsky <piastry@altlinux.org> 1.0.30-alt6
- Rename tgtd.{init,service} files to tgt.{init,service}

* Mon Aug 26 2013 Vitaly Lipatov <lav@altlinux.ru> 1.0.30-alt5
- cleanup spec

* Sat Mar 30 2013 Pavel Shilovsky <piastry@altlinux.org> 1.0.30-alt4.1
- Add SysVinit support

* Wed Mar 06 2013 Pavel Shilovsky <piastry@altlinux.org> 1.0.30-alt4
- Fix unowned files

* Wed Mar 06 2013 Pavel Shilovsky <piastry@altlinux.org> 1.0.30-alt3
- Use post/preun_service scripts in spec

* Tue Jan 29 2013 Pavel Shilovsky <piastry@altlinux.org> 1.0.30-alt2
- Fix build with new docbook-style-xsl

* Wed Oct 03 2012 Pavel Shilovsky <piastry@altlinux.org> 1.0.30-alt1
- Initial release for Sisyphus

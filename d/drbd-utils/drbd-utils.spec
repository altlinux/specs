%def_without xen
%define githash 4f7d26a69e20e826bc8eb70822a61fb476c020aa
%define gitdiff c6e62702d5e4fb2cf6b3fa27e67cb0d4b399a30b
%define _localstatedir %_var
%global optflags_lto %optflags_lto -ffat-lto-objects

Name: drbd-utils
Version: 9.23.0
Release: alt1

Summary: DRBD user-land tools and scripts
License: GPLv2+
Group: System/Kernel and hardware

Url: http://www.drbd.org/
Source0: %name-%version.tar
Source1: %name-headers-%version.tar
Patch0: %name-%version-%release.patch

%define check_arches x86_64 %ix86
%ifarch %check_arches
%def_with check
%else
%def_without check
%endif


BuildRequires: docbook-style-xsl flex xsltproc
BuildRequires: gcc-c++ po4a udev libudev-devel libsystemd-devel
BuildRequires: asciidoctor resource-agents
%{?!_without_check:%{?!_disable_check:BuildRequires: /proc clitest}}

Requires: linux-ha-common

Conflicts: drbd-tools drbd83-tools
Provides: %name-bash-completion = %EVR
Obsoletes: %name-bash-completion < %EVR

%description
DRBD refers to block devices designed as a building block to form high
availability (HA) clusters. This is done by mirroring a whole block device
via an assigned network. DRBD can be understood as network based raid-1.

This packages includes the DRBD administration tools.

%package xen
Summary: Xen block device management script for DRBD
Group: System/Kernel and hardware
Requires: %name = %version-%release
Requires: xen
BuildArch: noarch

%description xen
This package contains a Xen block device helper script for DRBD, capable of
promoting and demoting DRBD resources as necessary.

%package pacemaker
Summary: Pacemaker resource agent for DRBD
Group: System/Kernel and hardware
Requires: %name = %version-%release
Requires: pacemaker
License: GPLv2
BuildArch: noarch

%description pacemaker
This package contains the master/slave DRBD resource agent for the
Pacemaker High Availability cluster manager.

%package rgmanager
Summary: Red Hat Cluster Suite agent for DRBD
Group: System/Kernel and hardware
Requires: %name = %version-%release
BuildArch: noarch

%description rgmanager
This package contains the DRBD resource agent for the Red Hat Cluster Suite
resource manager.

%prep
%setup -a1
tar -xf %SOURCE1 -C drbd-headers
%patch0 -p1
(echo -e "#define GITHASH \"%githash\""; \
 echo -e "#define GITDIFF \"%gitdiff\"") > user/shared/drbd_buildtag.h
%ifarch %e2k
# lcc 1.25.15 barfs at DrbdRole.cpp:36, DrbdVolume.cpp:748
sed -i 's,-Wshadow,,' user/drbdmon/Makefile*
%endif

%build
%autoreconf
%configure \
    %{subst_with xen} \
    --with-udev \
    --with-pacemaker \
    --with-rgmanager \
    --with-heartbeat \
    --with-distro=generic

# Bug in configure.ac, enabling WITH_DRBDMON anyway:
sed -i "s|WITH_DRBDMON[[:space:]]*=[[:space:]]*no|WITH_DRBDMON = yes|" \
  Makefile user/drbdmon/Makefile documentation/common/Makefile_v9_com
# Bug in compiler option:
sed -i "s|--pedantic-errors|-pedantic-errors|" user/drbdmon/Makefile

%make_build

%install
%makeinstall_std

rm -rf %buildroot%_mandir/ja
rm -f  %buildroot/etc/init.d/drbd	# NB: _not_ %%_initdir here
pushd scripts
install -pDm644 -t %buildroot%_unitdir *.service
install -pDm644 -t %buildroot%_unitdir *.target
install -pDm755 -t %buildroot/lib/drbd/scripts drbd drbd-service-shim.sh drbd-wait-promotable.sh ocf.ra.wrapper.sh
install -pDm755 drbd %buildroot%_initdir/drbd
popd

%post
%post_service drbd

%preun
%preun_service drbd

%check
make test

%files
%doc scripts/drbd.conf.example COPYING ChangeLog README.md
%config(noreplace) %_sysconfdir/drbd.conf
%dir %_sysconfdir/drbd.d
%config(noreplace) %_sysconfdir/drbd.d/global_common.conf
%config(noreplace) %_sysconfdir/multipath/conf.d/drbd.conf
%_sysconfdir/ha.d/resource.d/*
%_initdir/drbd
%_unitdir/drbd.service
%_unitdir/drbd-lvchange@.service
%_unitdir/drbd-promote@.service
%_unitdir/drbd-reconfigure-suspend-or-error@.service
%_unitdir/drbd-demote-or-escalate@.service
%_unitdir/drbd-services@.target
%_unitdir/drbd-wait-promotable@.service
%_unitdir/drbd@.service
%_unitdir/drbd@.target
%_unitdir/ocf.ra@.service
%_sbindir/drbdsetup
%_sbindir/drbdadm
%_sbindir/drbdmeta
%_sbindir/drbdmon
%dir /lib/drbd
/lib/drbd/drbdadm-*
/lib/drbd/drbdsetup-*
%dir /lib/drbd/scripts
/lib/drbd/scripts/drbd
/lib/drbd/scripts/drbd-service-shim.sh
/lib/drbd/scripts/drbd-wait-promotable.sh
/lib/drbd/scripts/ocf.ra.wrapper.sh
/lib/udev/rules.d/65-drbd.rules
%exclude /usr/lib/drbd/crm-*fence-peer.sh
%exclude /usr/lib/drbd/stonith_admin-fence-peer.sh
%dir /usr/lib/drbd
/usr/lib/drbd/*.sh
/usr/lib/drbd/rhcs_fence
%dir %_var/lib/drbd
%_man8dir/drbd*
%_man7dir/*
%_man5dir/drbd*
%_sysconfdir/bash_completion.d/*

%if_with xen
%files xen
%_sysconfdir/xen/scripts/block-drbd
%endif

%files pacemaker
%dir /usr/lib/ocf/resource.d/linbit
/usr/lib/ocf/resource.d/linbit/drbd
/usr/lib/ocf/resource.d/linbit/drbd.shellfuncs.sh
/usr/lib/ocf/resource.d/linbit/drbd-attr
/usr/lib/drbd/crm-*fence-peer.sh
/usr/lib/drbd/stonith_admin-fence-peer.sh

%files rgmanager
%_datadir/cluster/drbd.sh
%_datadir/cluster/drbd.metadata

%changelog
* Wed Jan 25 2023 Andrew A. Vasilyev <andy@altlinux.org> 9.23.0-alt1
- 9.23.0

* Wed Sep 21 2022 Andrew A. Vasilyev <andy@altlinux.org> 9.22.0-alt1
- 9.22.0

* Mon Jul 18 2022 Andrew A. Vasilyev <andy@altlinux.org> 9.21.4-alt1
- 9.21.4

* Tue Jul 12 2022 Andrew A. Vasilyev <andy@altlinux.org> 9.21.3-alt1
- 9.21.3

* Wed Jun 08 2022 Andrew A. Vasilyev <andy@altlinux.org> 9.21.2-alt1
- 9.21.2

* Thu Apr 28 2022 Andrew A. Vasilyev <andy@altlinux.org> 9.21.1-alt1
- 9.21.1

* Tue Apr 26 2022 Andrew A. Vasilyev <andy@altlinux.org> 9.21.0-alt1
- 9.21.0

* Mon Jan 31 2022 Andrew A. Vasilyev <andy@altlinux.org> 9.20.2-alt1
- 9.20.2

* Thu Jan 13 2022 Andrew A. Vasilyev <andy@altlinux.org> 9.20.0-alt1
- 9.20.0

* Fri Dec 03 2021 Egor Ignatov <egori@altlinux.org> 9.19.1-alt4
- drbd.ocf: change type name 'numeric' to 'integer'

* Mon Nov 29 2021 Andrew A. Vasilyev <andy@altlinux.org> 9.19.1-alt3
- add Provides and Obsoletes for bash-completion package

* Mon Nov 29 2021 Andrew A. Vasilyev <andy@altlinux.org> 9.19.1-alt2
- remove journalctl and systemctl direct requirements (closes: #41454)
- move bash completion to main package

* Mon Nov 22 2021 Andrew A. Vasilyev <andy@altlinux.org> 9.19.1-alt1
- 9.19.1

* Mon Oct 04 2021 Andrew A. Vasilyev <andy@altlinux.org> 9.19.0-alt1
- 9.19.0
- add %%check for x86_64 and %%ix86

* Thu Aug 05 2021 Andrew A. Vasilyev <andy@altlinux.org> 9.18.2-alt1
- 9.18.2

* Wed Jul 21 2021 Andrew A. Vasilyev <andy@altlinux.org> 9.18.1-alt1
- 9.18.1
- add systemd templates and ocf RA wrapper script

* Fri Jun 18 2021 Michael Shigorin <mike@altlinux.org> 9.17.0-alt1.1
- E2K: ftbfs workaround

* Thu Apr 29 2021 Andrew A. Vasilyev <andy@altlinux.org> 9.17.0-alt1
- 9.17.0

* Fri Feb 19 2021 Andrew A. Vasilyev <andy@altlinux.org> 9.16.0-alt1
- 9.16.0

* Wed Dec 30 2020 Andrew A. Vasilyev <andy@altlinux.org> 9.15.1-alt1
- 9.15.1

* Thu May 14 2020 Andrew A. Vasilyev <andy@altlinux.org> 9.13.1-alt1
- 9.13.1

* Mon Apr 20 2020 Andrew A. Vasilyev <andy@altlinux.org> 9.12.2-alt1
- 9.12.2

* Tue Mar 24 2020 Andrew A. Vasilyev <andy@altlinux.org> 9.12.1-alt1
- 9.12.1

* Sat Mar 07 2020 Andrew A. Vasilyev <andy@altlinux.org> 9.12.0-alt1.1
- Avoid undocumented option form (for lcc on e2k actually) (mike@)
- Minor spec cleanup (mike@)

* Wed Feb 19 2020 Andrew A. Vasilyev <andy@altlinux.org> 9.12.0-alt1
- 9.12.0

* Tue Apr 04 2017 Valery Inozemtsev <shrek@altlinux.ru> 8.9.6-alt1
- 8.9.6

* Fri May 27 2016 Mikhail Efremov <sem@altlinux.org> 8.9.0-alt3
- Disable xen support.

* Tue Jan 26 2016 Lenar Shakirov <snejok@altlinux.ru> 8.9.0-alt2
- Fixed build (man page packaging)

* Mon Sep 01 2014 Lenar Shakirov <snejok@altlinux.ru> 8.9.0-alt1
- First build for ALT as separate package "%name" (based on Fedora 8.9.0-8.fc21.src)


%define _localstatedir %_var
%def_without xen

Name: drbd-utils
Version: 8.9.6
Release: alt1
Summary: DRBD user-land tools and scripts
License: GPLv2+
Group: System/Kernel and hardware
URL: http://www.drbd.org/

Conflicts: drbd-tools drbd83-tools

Source0: %name-%version.tar
Source1: drbd-headers.tar
Patch0: %name-%version-%release.patch

BuildRequires: docbook-style-xsl flex xsltproc

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

%package bash-completion
Summary: Programmable bash completion support for drbdadm
Group: System/Kernel and hardware
Requires: %name = %version-%release
BuildArch: noarch

%description bash-completion
This package contains programmable bash completion support for the drbdadm
management utility.

%prep
%setup -q -a1
%patch0 -p1

%build
%autoreconf
%configure \
    --with-udev \
    %{subst_with xen} \
    --with-pacemaker \
    --with-rgmanager \
    --with-distro=generic
%make_build

%install
%make DESTDIR=%buildroot install

install -Dp -m644 drbd.service %buildroot%_unitdir/drbd.service
rm -f %buildroot%_man8dir/drbd-overview.8

%post
%post_service drbd

%preun
%preun_service drbd

%files
%doc scripts/drbd.conf.example COPYING ChangeLog README
%config(noreplace) %_sysconfdir/drbd.conf
%dir %_sysconfdir/drbd.d
%config(noreplace) %_sysconfdir/drbd.d/global_common.conf
%_unitdir/drbd.service
%_sbindir/drbdsetup
%_sbindir/drbdadm
%_sbindir/drbdmeta
%_sbindir/drbd-overview
/lib/drbd/drbdadm-*
/lib/drbd/drbdsetup-*
%exclude /usr/lib/drbd/crm-*fence-peer.sh
%exclude /usr/lib/drbd/stonith_admin-fence-peer.sh
/usr/lib/drbd/*.sh
/usr/lib/drbd/rhcs_fence
%dir %_var/lib/drbd
%_man8dir/drbd*
%_man5dir/drbd*

%if_with xen
%files xen
%_sysconfdir/xen/scripts/block-drbd
%endif

%files pacemaker
/usr/lib/ocf/resource.d/linbit/drbd
/usr/lib/drbd/crm-*fence-peer.sh
/usr/lib/drbd/stonith_admin-fence-peer.sh

%files rgmanager
%_datadir/cluster/drbd.sh
%_datadir/cluster/drbd.metadata

%files bash-completion
%_sysconfdir/bash_completion.d/drbdadm*

%changelog
* Tue Apr 04 2017 Valery Inozemtsev <shrek@altlinux.ru> 8.9.6-alt1
- 8.9.6

* Fri May 27 2016 Mikhail Efremov <sem@altlinux.org> 8.9.0-alt3
- Disable xen support.

* Tue Jan 26 2016 Lenar Shakirov <snejok@altlinux.ru> 8.9.0-alt2
- Fixed build (man page packaging)

* Mon Sep 01 2014 Lenar Shakirov <snejok@altlinux.ru> 8.9.0-alt1
- First build for ALT as separate package "%name" (based on Fedora 8.9.0-8.fc21.src)


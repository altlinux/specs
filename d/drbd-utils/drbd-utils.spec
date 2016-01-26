%define _localstatedir %_var
Name: drbd-utils
Summary: DRBD user-land tools and scripts
Version: 8.9.0
Release: alt2
Source0: http://oss.linbit.com/%{name}/%{name}-%{version}.tar.gz
Source1: drbd.service
Patch0: disable_drbd_checkin.patch
License: GPLv2+
Group: System/Kernel and hardware
URL: http://www.drbd.org/
BuildRequires: udev flex
Conflicts: drbd-tools
Conflicts: drbd83-tools

%description
DRBD refers to block devices designed as a building block to form high 
availability (HA) clusters. This is done by mirroring a whole block device 
via an assigned network. DRBD can be understood as network based raid-1.

This packages includes the DRBD administration tools.

%prep
%setup

# Disable the automatic checkin with drbd starts
%patch0 -p0

%build
%configure \
    --with-utils \
    --without-km \
    --with-udev \
%ifarch %{ix86} x86_64
    --with-xen \
%else
    --without-xen \
%endif
    --with-pacemaker \
    --with-rgmanager \
    --with-distro=generic \
    --with-initdir=%{_initddir}
make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT

# Remove old init script, replace with systemd unit file
rm -f $RPM_BUILD_ROOT/%{_initddir}/drbd
install -d -m755 $RPM_BUILD_ROOT/%{_unitdir}
install -m644 %{SOURCE1} $RPM_BUILD_ROOT/%{_unitdir}/drbd.service

# Relocate udev rules to the location systemd expects to find them
install -d -m755 $RPM_BUILD_ROOT/%{_udevrulesdir}
mv $RPM_BUILD_ROOT/etc/udev/rules.d/* $RPM_BUILD_ROOT/%{_udevrulesdir}/

%files
%{_sbindir}/drbdsetup
%{_sbindir}/drbdadm
%{_sbindir}/drbdmeta
%{_sbindir}/drbd-overview

%attr(0644,root,root) %{_unitdir}/drbd.service

# Yes, these paths are peculiar. Upstream is peculiar.
# Be forewarned: rpmlint hates this stuff.
/lib/drbd/drbdadm-*
/lib/drbd/drbdsetup-*
%exclude /usr/lib/drbd/crm-*fence-peer.sh
%exclude /usr/lib/drbd/stonith_admin-fence-peer.sh
/usr/lib/drbd/*.sh
/usr/lib/drbd/rhcs_fence

%dir %{_var}/lib/drbd
%config %{_udevrulesdir}/65-drbd.rules*
%config(noreplace) %{_sysconfdir}/drbd.conf
%dir %{_sysconfdir}/drbd.d
%config(noreplace) %{_sysconfdir}/drbd.d/global_common.conf
%{_mandir}/man8/drbd*
%{_mandir}/man5/drbd*
%doc scripts/drbd.conf.example
%doc COPYING
%doc ChangeLog
%doc README

# armv7hl/aarch64 doesn't have Xen packages
%ifarch %{ix86} x86_64
%package xen
Summary: Xen block device management script for DRBD
Group: System/Kernel and hardware
Requires: %{name} = %{version}-%{release}
Requires: xen
BuildArch: noarch

%description xen
This package contains a Xen block device helper script for DRBD, capable of
promoting and demoting DRBD resources as necessary.

%files xen
%{_sysconfdir}/xen/scripts/block-drbd
%endif

%package pacemaker
Summary: Pacemaker resource agent for DRBD
Group: System/Kernel and hardware
Requires: %{name} = %{version}-%{release}
Requires: pacemaker
License: GPLv2
BuildArch: noarch

%description pacemaker
This package contains the master/slave DRBD resource agent for the
Pacemaker High Availability cluster manager.

%files pacemaker
%{_prefix}/lib/ocf/resource.d/linbit/drbd
/usr/lib/drbd/crm-*fence-peer.sh
/usr/lib/drbd/stonith_admin-fence-peer.sh

%package rgmanager
Summary: Red Hat Cluster Suite agent for DRBD
Group: System/Kernel and hardware
Requires: %{name} = %{version}-%{release}
##Conflicts: resource-agents >= 3
BuildArch: noarch

%description rgmanager
This package contains the DRBD resource agent for the Red Hat Cluster Suite
resource manager.

As of Red Hat Cluster Suite 3.0.1, the DRBD resource agent is included
in the Cluster distribution.

%files rgmanager
%{_datadir}/cluster/drbd.sh

%{_datadir}/cluster/drbd.metadata

%package bash-completion
Summary: Programmable bash completion support for drbdadm
Group: System/Kernel and hardware
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description bash-completion
This package contains programmable bash completion support for the drbdadm
management utility.

%files bash-completion
%config %{_sysconfdir}/bash_completion.d/drbdadm*

%post
%post_service drbd

%preun
%preun_service drbd

%changelog
* Tue Jan 26 2016 Lenar Shakirov <snejok@altlinux.ru> 8.9.0-alt2
- Fixed build (man page packaging)

* Mon Sep 01 2014 Lenar Shakirov <snejok@altlinux.ru> 8.9.0-alt1
- First build for ALT as separate package "%name" (based on Fedora 8.9.0-8.fc21.src)


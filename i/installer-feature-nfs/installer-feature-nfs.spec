Name: installer-feature-nfs
Version: 0.3
Release: alt1

Summary: Installer stage3 NFS hooks
License: GPL
Group: System/Configuration/Other
Url: http://www.altlinux.org/Installer/beans
Packager: Dmitry V. Levin <ldv@altlinux.org>
BuildArch: noarch

%description
Installer stage3 NFS client and server tuning hooks.

%package client-stage3
Summary: Installer stage3 NFS client tuning hook
License: GPL
Group: System/Configuration/Other
Requires: installer-common-stage3, rpcbind

%description client-stage3
This package contains NFS client tuning hook for installer stage3.

%package server-stage3
Summary: Installer stage3 NFS server tuning hook
License: GPL
Group: System/Configuration/Other
Requires: installer-common-stage3, rpcbind, nfs-clients

%description server-stage3
This package contains NFS server tuning hook for installer stage3.

%install
mkdir -p %buildroot

%post client-stage3
control rpcbind local
chkconfig rpcbind on

%post server-stage3
control rpcbind server
chkconfig rpcbind on
chkconfig nfslock on

%files client-stage3

%files server-stage3

%changelog
* Sun Nov 07 2010 Michael Shigorin <mike@altlinux.org> 0.3-alt1
- NMU: use rpcbind instead of portmap as per maintainer's advice

* Wed Apr 01 2009 Dmitry V. Levin <ldv@altlinux.org> 0.2-alt1
- Rewritten from stage2 to stage3.

* Tue Mar 17 2009 Dmitry V. Levin <ldv@altlinux.org> 0.1-alt1
- Initial revision based on installer/preinstall.d/60-nfs.sh.


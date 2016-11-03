Name: installer-feature-pve
Version: 0.4
Release: alt1

Summary: Prevonfigures PVE cluster node
License: GPL
Group: System/Configuration/Other
Url: http://www.altlinux.org/Installer/beans
BuildArch: noarch
Source: %name-%version.tar

%description
Prevonfigures PVE cluster node
See https://www.altlinux.org/PVE

%prep
%setup

%install
%define hookdir %_datadir/install2/postinstall.d
mkdir -p %buildroot%hookdir
install -pm755 *.sh %buildroot%hookdir/

%files
%hookdir/*

%changelog
* Thu Nov 03 2016 Anton V. Boyarshinov <boyarsh@altlinux.org> 0.4-alt1
- rrdcache config location changed

* Wed Oct 12 2016 Anton V. Boyarshinov <boyarsh@altlinux.org> 0.3-alt1
- properly start nfs-client and pre-enable pve-cluster & pve-manager

* Wed Oct 12 2016 Anton V. Boyarshinov <boyarsh@altlinux.org> 0.2-alt1
- it was The Real Killer Feature! Fixed

* Wed Oct 12 2016 Anton V. Boyarshinov <boyarsh@altlinux.org> 0.1-alt1
- initial version



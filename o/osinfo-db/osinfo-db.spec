
Summary: osinfo database files
Name: osinfo-db
Version: 20161026
Release: alt1
License: LGPLv2+
Group: System/Libraries
Url: http://libosinfo.org/
Source: https://fedorahosted.org/releases/l/i/libosinfo/%name-%version.tar.xz
BuildArch: noarch

BuildRequires: intltool >= 0.40.0
BuildRequires: osinfo-db-tools
Conflicts: libosinfo < 1.0.0

%description
The osinfo database provides information about operating systems and
hypervisor platforms to facilitate the automated configuration and
provisioning of new virtual machines

%install
osinfo-db-import --root %buildroot --system %SOURCE0

%files
%dir %_datadir/osinfo
%_datadir/osinfo/*

%changelog
* Fri Dec 30 2016 Alexey Shabalin <shaba@altlinux.ru> 20161026-alt1
- 20161026

* Mon Oct 17 2016 Alexey Shabalin <shaba@altlinux.ru> 20160728-alt1
- 20160728


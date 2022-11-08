
Name: pve-storage-linstor
Version: 6.1.0
Release: alt2

Summary: LINSTOR Proxmox Plugin
Group: System/Servers
License: GPLv2+

Packager: Andrew A. Vasilyev <andy@altlinux.org>

Url: https://github.com/LINBIT/linstor-proxmox
Vcs: https://github.com/LINBIT/linstor-proxmox.git

Source: %name-%version.tar

ExclusiveArch: x86_64 aarch64

BuildRequires(pre): rpm-build-perl
BuildRequires: pve-storage
BuildRequires: perl-JSON-XS
BuildRequires: perl(REST/Client.pm)
Requires: linstor-controller pve-manager

%add_perl_lib_path %buildroot%perl_vendor_privlib

%description
LINSTOR Proxmox Plugin.

%prep
%setup

%build
#Empty build

%install
	install -D -m 0644 ./LINSTORPlugin.pm %buildroot%perl_vendor_privlib/PVE/Storage/Custom/LINSTORPlugin.pm
	install -D -m 0644 ./LINBIT/Linstor.pm %buildroot%perl_vendor_privlib/LINBIT/Linstor.pm
	install -D -m 0644 ./LINBIT/PluginHelper.pm %buildroot%perl_vendor_privlib/LINBIT/PluginHelper.pm
	mkdir -p %buildroot%_cachedir/linstor-proxmox

%post
/sbin/service pvedaemon condrestart ||:

%postun
if [ $1 = 0 ]; then
    /sbin/service pvedaemon condrestart ||:
fi

%files
%doc README.md
%dir %perl_vendor_privlib/PVE/Storage/Custom
%perl_vendor_privlib/PVE/Storage/Custom/LINSTORPlugin.pm
%dir %perl_vendor_privlib/LINBIT
%perl_vendor_privlib/LINBIT/Linstor.pm
%perl_vendor_privlib/LINBIT/PluginHelper.pm
%_cachedir/linstor-proxmox/

%changelog
* Tue Nov 08 2022 Andrew A. Vasilyev <andy@altlinux.org> 6.1.0-alt2
- pack /var/cache/linstor-proxmox directory

* Fri Oct 14 2022 Andrew A. Vasilyev <andy@altlinux.org> 6.1.0-alt1
- 6.1.0

* Wed Jul 13 2022 Andrew A. Vasilyev <andy@altlinux.org> 6.0.1-alt1
- 6.0.1

* Tue Jun 28 2022 Andrew A. Vasilyev <andy@altlinux.org> 6.0.0-alt1
- 6.0.0

* Wed Jan 05 2022 Andrew A. Vasilyev <andy@altlinux.org> 5.2.2-alt1
- 5.2.2

* Tue Nov 09 2021 Andrew A. Vasilyev <andy@altlinux.org> 5.2.1-alt1
- 5.2.1

* Mon Jul 12 2021 Andrew A. Vasilyev <andy@altlinux.org> 5.2.0-alt1
- 5.2.0

* Wed Jun 16 2021 Andrew A. Vasilyev <andy@altlinux.org> 5.1.5-alt2
- rebuild with new perl 5.34.0

* Tue Jun 08 2021 Andrew A. Vasilyev <andy@altlinux.org> 5.1.5-alt1
- 5.1.5

* Fri Nov 27 2020 Andrew A. Vasilyev <andy@altlinux.org> 5.1.4-alt1
- 5.1.4

* Mon Sep 28 2020 Andrew A. Vasilyev <andy@altlinux.org> 5.1.3-alt1
- 5.1.3

* Tue Jun 23 2020 Andrew A. Vasilyev <andy@altlinux.org> 5.1.2-alt1
- 5.1.2

* Tue Mar 17 2020 Andrew A. Vasilyev <andy@altlinux.org> 4.1.2-alt1
- initial build for ALT


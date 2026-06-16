%def_without check

Name: pve-network
Summary: PVE SDN package
Version: 1.6.6
Release: alt1
License: AGPL-3.0+
Group: Development/Perl
Url: https://git.proxmox.com/

Source: %name-%version.tar
Patch: alt-dnsmasq.patch

ExclusiveArch: x86_64 aarch64 loongarch64

Provides: libpve-network-perl = %EVR
Requires: ifupdown2
Requires: pve-common >= 9.1.1
Requires: pve-cluster >= 9.0.1
Requires: pve-firewall >= 5.1.0
Requires: frr frr-pythontools
Requires: dnsmasq

BuildRequires: pve-cluster
BuildRequires: pve-firewall
BuildRequires: pve-doc-generator
BuildRequires: pve-common >= 9.1.1
BuildRequires: perl
BuildRequires: perl(CPAN/Meta/YAML.pm)
BuildRequires: perl(Data/Dumper.pm)
BuildRequires: perl(Digest/SHA.pm)
BuildRequires: perl(Encode.pm)
BuildRequires: perl(File/Basename.pm)
BuildRequires: perl(File/Copy.pm)
BuildRequires: perl(File/Path.pm)
BuildRequires: perl(File/Slurp.pm)
BuildRequires: perl(HTTP/Request.pm)
BuildRequires: perl(JSON.pm)
BuildRequires: perl(LWP/UserAgent.pm)
BuildRequires: perl(NetAddr/IP.pm)
BuildRequires: perl(Net/IP.pm)
BuildRequires: perl(Net/Subnet.pm)
BuildRequires: perl(PVE/Cluster.pm)
BuildRequires: perl(PVE/Exception.pm)
BuildRequires: perl(PVE/INotify.pm)
BuildRequires: perl(PVE/JSONSchema.pm)
BuildRequires: perl(PVE/RESTHandler.pm)
BuildRequires: perl(PVE/RPCEnvironment.pm)
BuildRequires: perl(PVE/SafeSyslog.pm)
BuildRequires: perl(PVE/SectionConfig.pm)
BuildRequires: perl(PVE/Tools.pm)
BuildRequires: perl(Test/MockModule.pm)
BuildRequires: perl(Test/More.pm)

%define __spec_autodep_custom_pre export PERL5OPT='-I%buildroot%perl_vendor_privlib -MPVE::Network::SDN'; export TZ=UTC
%set_perl_req_method relaxed

%description
Proxmox VE's experimental SDN (Software Defined Network)
This package contains the experimental SDN library used by Proxmox VE.

%prep
%setup -q -n %name-%version
%patch -p1
sed -i 's!)/lib/systemd/system!)/usr/lib/systemd/system!' src/services/Makefile

%install
%make -C src DESTDIR=%buildroot install

%check
make -C src test

%files
%doc debian/copyright
%perl_vendor_privlib/PVE/*
%_unitdir/dnsmasq@.service.d/00-dnsmasq-after-networking.conf

%changelog
* Tue Jun 09 2026 Sergey Konev <darisishe@altlinux.org> 1.6.6-alt1
- 1.6.6

* Thu Jan 22 2026 Sergey Konev <darisishe@altlinux.org> 1.2.4-alt1
- 1.2.4

* Sat Aug 09 2025 Sergey Konev <darisishe@altlinux.org> 1.1.6-alt1
- 1.1.6

* Fri Jul 11 2025 Ivan A. Melnikov <iv@altlinux.org> 0.11.2-alt2
- NMU: build on loongarch64

* Wed May 21 2025 Alexey Shabalin <shaba@altlinux.org> 0.11.2-alt1
- 0.11.2
- Requires frr-pythontools for frr-reload.py
- Enable bgpd and bfdd in frr daemon config

* Mon Jan 27 2025 Alexey Shabalin <shaba@altlinux.org> 0.10.0-alt2
- Fixed dnsmasq dbus config, allow policy user _dnsmasq.

* Wed Dec 18 2024 Sergey Konev <darisishe@altlinux.org> 0.10.0-alt1
- 0.10.0
- Fixed config path for dnsmasq

* Thu Aug 29 2024 Andrew A. Vasilyev <andy@altlinux.org> 0.9.8-alt1
- 0.9.8

* Mon Jun 24 2024 Andrew A. Vasilyev <andy@altlinux.org> 0.9.6-alt1.1
- FTBFS: fix systemd path

* Fri Mar 29 2024 Andrew A. Vasilyev <andy@altlinux.org> 0.9.6-alt1
- 0.9.6

* Thu Mar 14 2024 Andrew A. Vasilyev <andy@altlinux.org> 0.9.5-alt1
- 0.9.5
- add copyright file

* Fri Mar 24 2023 Andrew A. Vasilyev <andy@altlinux.org> 0.7.3-alt1
- 0.7.3

* Fri Mar 10 2023 Andrew A. Vasilyev <andy@altlinux.org> 0.7.2-alt1
- 0.7.2

* Thu Oct 06 2022 Andrew A. Vasilyev <andy@altlinux.org> 0.7.1-alt1
- Initial build for ALT


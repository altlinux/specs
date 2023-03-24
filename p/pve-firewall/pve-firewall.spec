%global _unpackaged_files_terminate_build 1

Name: pve-firewall
Summary: Proxmox VE Firewall
Version: 4.3.1
Release: alt1
License: AGPL-3.0+
Group: System/Servers
Url: https://www.proxmox.com
Vcs: git://git.proxmox.com/git/pve-firewall.git
Source: %name-%version.tar

ExclusiveArch: x86_64 aarch64

# from debian/control
#Conflicts: ulogd

Requires: ebtables ipset iptables iptables-ipv6 iproute2 

BuildRequires: pve-access-control libpve-cluster-perl pve-common pve-cluster pve-doc-generator
BuildRequires: pkgconfig(libnetfilter_log) pkgconfig(libnetfilter_conntrack) pkgconfig(glib-2.0)
BuildRequires: perl(IO/Zlib.pm)

%description
%summary.
This package contains the Proxmox VE Firewall.

%prep
%setup

%build
%make_build -C src

%install
%makeinstall_std -C src
mkdir -p %buildroot{%_unitdir,%_logrotatedir,%_tmpfilesdir,%_modulesloaddir,%_localstatedir/%name}

install -m0644 debian/*.service %buildroot%_unitdir/
install -m0644 debian/pve-firewall.logrotate %buildroot%_logrotatedir/%name

cat << __EOF__ > %buildroot%_tmpfilesdir/%name.conf
f /var/lock/pvefw-logger.lck 0644 root root
__EOF__

cat << __EOF__ > %buildroot%_modulesloaddir/%name.conf
br_netfilter
__EOF__

%post
#%%post_service pve-firewall
%post_service pvefw-logger

%preun
#%%preun_service pve-firewall
%preun_service pvefw-logger

%files
%_tmpfilesdir/%name.conf
%_datadir/bash-completion/completions/*
%_datadir/zsh/vendor-completions/*
%_logrotatedir/%name
%config(noreplace) %_sysctldir/%name.conf
%_modulesloaddir/pve-firewall.conf
%_unitdir/*
%_sbindir/*
%perl_vendor_privlib/PVE/*.pm
%perl_vendor_privlib/PVE/API2/Firewall
%perl_vendor_privlib/PVE/Firewall
%perl_vendor_privlib/PVE/Service/*.pm
%_localstatedir/%name
%_man8dir/*

%changelog
* Mon Mar 20 2023 Andrew A. Vasilyev <andy@altlinux.org> 4.3.1-alt1
- 4.3-1

* Tue Feb 28 2023 Andrew A. Vasilyev <andy@altlinux.org> 4.2.6-alt3
- ipset: support old 5.10 kernel too, no bucketsize

* Mon Oct 24 2022 Alexey Shabalin <shaba@altlinux.org> 4.2.6-alt2
- delete conflicts with ulogd

* Mon Oct 03 2022 Alexey Shabalin <shaba@altlinux.org> 4.2.6-alt1
- 4.2-6

* Wed Mar 09 2022 Alexey Shabalin <shaba@altlinux.org> 4.2.5-alt1
- 4.2-5
- build as separate package


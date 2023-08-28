%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

Name: iptraf-ng
Version: 1.2.1
Release: alt3

Summary: IPTraf-ng is a console-based network monitoring program for Linux
License: GPL-2.0
Url: https://github.com/iptraf-ng/iptraf-ng
Group: Monitoring

Source: %name-%version.tar
Patch0: iptraf-ng-1.2.1-alt-fix-non-lfs-functions.patch

BuildRequires: libncursesw-devel

%description
IPTraf-ng is a console-based network monitoring program for Linux that
displays information about IP traffic.  It returns such information as:

        Current TCP connections
        UDP, ICMP, OSPF, and other types of IP packets
        Packet and byte counts on TCP connections
        IP, TCP, UDP, ICMP, non-IP, and other packet and byte counts
        TCP/UDP counts by ports
        Packet counts by packet sizes
        Packet and byte counts by IP address
        Interface activity
        Flag statuses on TCP packets
        LAN station statistics

This program can be used to determine the type of traffic on your network,
and what kind of service is the most heavily used on what machines, among
others.

IPTraf-ng works on Ethernet, FDDI, PLIP, loopback, and SLIP/PPP
interfaces. Also supports GRE-over-IP tunnels, 802.1ad and QinQ VLAN,
and SIT tunnels.

%prep
%setup
%patch0 -p1

%build
%make_build

%install
%makeinstall

mkdir -p %buildroot%_logdir/%name
mkdir -p %buildroot%_logrotatedir
install -pD -m644 iptraf-ng-logrotate.conf %buildroot%_logrotatedir/%name.conf

%files
%doc AUTHORS CHANGES FAQ LICENSE README* Documentation
%_sbindir/*
%_man8dir/*
%attr(750, root, root) %dir %_logdir/*
%config(noreplace) %_logrotatedir/*


%changelog
* Mon Aug 28 2023 Anton Zhukharev <ancieg@altlinux.org> 1.2.1-alt3
- Fixed FTBFS: built with libncursesw.

* Sat Jun 04 2022 Anton Zhukharev <ancieg@altlinux.org> 1.2.1-alt2
- bump release to override autoimports package

* Tue May 31 2022 Anton Zhukharev <ancieg@altlinux.org> 1.2.1-alt1
- initial build for Sisyphus

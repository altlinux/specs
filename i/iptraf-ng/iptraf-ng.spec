%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

Name: iptraf-ng
Version: 1.2.2
Release: alt1

Summary: IPTraf-ng is a console-based network monitoring program for Linux
License: GPL-2.0
Group: Monitoring
Url: https://github.com/iptraf-ng/iptraf-ng
Vcs: https://github.com/iptraf-ng/iptraf-ng

Source: %name-%version.tar
Patch: %name-%version-alt.patch

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
%autopatch0 -p1

%build
%make_build

%install
%makeinstall

mkdir -p %buildroot%_logdir/%name
install -pD -m644 iptraf-ng-logrotate.conf %buildroot%_logrotatedir/%name.conf

%files
%doc AUTHORS CHANGES FAQ LICENSE README* Documentation
%_sbindir/iptraf-ng
%_man8dir/iptraf-ng.8*
%attr(750, root, root) %dir %_logdir/%name
%config(noreplace) %_logrotatedir/%name.conf

%changelog
* Mon Nov 25 2024 Anton Zhukharev <ancieg@altlinux.org> 1.2.2-alt1
- Updated to 1.2.2 (fixes CVE-2024-52949).

* Mon Aug 28 2023 Anton Zhukharev <ancieg@altlinux.org> 1.2.1-alt3
- Fixed FTBFS: built with libncursesw.

* Sat Jun 04 2022 Anton Zhukharev <ancieg@altlinux.org> 1.2.1-alt2
- bump release to override autoimports package

* Tue May 31 2022 Anton Zhukharev <ancieg@altlinux.org> 1.2.1-alt1
- initial build for Sisyphus

%define dist NetPacket

Name: perl-%dist
Version: 1.2.0
Release: alt1

Summary: A cluster of modules related to decoding and encoding of network protocols.
License: %artistic_license_v2
Group: Development/Perl

Url: %CPAN %dist
Source: http://www.cpan.org/authors/id/Y/YA/YANICK/NetPacket-%{version}.tar.gz

Patch1: NetPacket-IPv6.diff
Patch2: NetPacket-1.1.0-LinuxSLL.pm.patch

BuildArch: noarch

BuildPreReq: /proc rpm-build-licenses

# Automatically added by buildreq on Sat Jan 15 2011
BuildRequires: perl-Module-Build

%description
NetPacket provides a base class for a cluster of modules related to
decoding and encoding of network protocols. Each NetPacket descendent
module knows how to encode and decode packets for the network protocol
it implements. Consult the documentation for the module in question
for protocol-specific implementation.

%package -n perl-NetPacket-IPv6
Summary: IPv6 modules (v0.020) for NetPacket
Group: Development/Perl
License: %bsd
Url: http://www.packetmischief.ca/code/netpacket/

%description -n perl-NetPacket-IPv6
perl-NetPacket-IPv6 contain IPv6 modules for perl-NetPacket
(ICMPv6.pm and IPv6.pm). OpenBSD Packet Filter Module (PFLog.pm)
included also becouse it is a part of original netpacket.diff.
Version of modules 0.020

%prep
%setup -q -n %dist-%version

%patch1 -p1
%patch2 -p1

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes

%exclude %perl_vendor_privlib/NetPacket/ICMPv6.pm
%exclude %perl_vendor_privlib/NetPacket/IPv6.pm
%exclude %perl_vendor_privlib/NetPacket/PFLog.pm
%perl_vendor_privlib/NetPacket*

%files -n perl-NetPacket-IPv6
%perl_vendor_privlib/NetPacket/ICMPv6.pm
%perl_vendor_privlib/NetPacket/IPv6.pm
%perl_vendor_privlib/NetPacket/PFLog.pm

%changelog
* Sun Sep 25 2011 Igor Vlasenko <viy@altlinux.ru> 1.2.0-alt1
- automated CPAN update

* Tue Mar 01 2011 Sergey Y. Afonin <asy@altlinux.ru> 1.1.1-alt1
- New wersion
- removed Ethernet.pm.patch (fixed in new version)

* Tue Mar 01 2011 Sergey Y. Afonin <asy@altlinux.ru> 1.1.0-alt4
- rewrote LinuxSLL.pm in new style of NetPacket (object oriented)

* Tue Feb 15 2011 Sergey Y. Afonin <asy@altlinux.ru> 1.1.0-alt3
- added LinuxSLL.pm

* Mon Feb 07 2011 Sergey Y. Afonin <asy@altlinux.ru> 1.1.0-alt2
- fixed export of new variables in Ethernet.pm

* Sat Jan 15 2011 Sergey Y. Afonin <asy@altlinux.ru> 1.1.0-alt1
- Initial build for ALTLinux
- added netpacket.diff: http://www.packetmischief.ca/code/netpacket/
  Some parts removed, file remamed to NetPacket-IPv6.diff.
  Warning: perl-NetPacket and perl-NetPacket-IPv6 have different licenses.

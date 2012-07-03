%define dist Net-ARP
Name: perl-%dist
Version: 1.0.6
Release: alt2

Summary: Perl extension for creating ARP packets
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tgz

# from Fedora
Patch: Net-Arp-1.0.6-tests.patch

# Automatically added by buildreq on Sun Oct 09 2011
BuildRequires: perl-devel

%description
This module is a Perl extension to create and send ARP packets and lookup
local or remote mac addresses.

%prep
%setup -n %dist
%patch -p1

# need root
mv t/send_packet.t t/send_packet.t.orig

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_archlib/Net
%perl_vendor_autolib/Net

%changelog
* Sun Oct 09 2011 Alexey Tourbin <at@altlinux.ru> 1.0.6-alt2
- rebuilt for perl-5.14

* Sat Jul 30 2011 Slava Dubrovskiy <dubrsl@altlinux.org> 1.0.6-alt1
- initial build for ALT Linux Sisyphus

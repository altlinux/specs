%define dist Net-Packet
Name: perl-%dist
Version: 3.27
Release: alt1

Summary: A framework to easily send and receive frames from layer 2 to layer 7
License: Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz
Patch: Net-Packet-3.27-alt-no-warn.patch

BuildArch: noarch

# Automatically added by buildreq on Fri Nov 11 2011
BuildRequires: net-tools perl-Bit-Vector perl-Net-IPv6Addr perl-Net-Libdnet perl-Net-Write perl-Test-Pod perl-Test-Pod-Coverage

%description
This module is a unified framework to craft, send and receive packets at
layers 2, 3, 4 and 7.

Basically, you forge each layer of a frame (Net::Packet::IPv4 for layer 3,
Net::Packet::TCP for layer 4 ; for example), and pack all of this into a
Net::Packet::Frame object. Then, you can send the frame to the network,
and receive it easily, since the response is automatically searched for
and matched against the request.

*** This framework is obsolete. Use Net::Frame::* now.

%prep
%setup -q -n %dist-%version
%patch -p1

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/Net

%changelog
* Fri Nov 11 2011 Alexey Tourbin <at@altlinux.ru> 3.27-alt1
- 3.26 -> 3.27

* Sat Nov 07 2009 Denis Smirnov <mithraen@altlinux.ru> 3.26-alt1
- initial build for ALT Linux Sisyphus

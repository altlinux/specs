%define module Net-RTP
%define m_distro Net-RTP
%define m_name Net::RTP
%define m_author_id NJH
%define _enable_test 1

Name: perl-Net-RTP
Version: 0.09
Release: alt1

Summary: Net-RTP - Send and receive RTP packets

License: Artistic
Group: Development/Perl
Url: http://search.cpan.org/dist/Net-RTP/

Packager: Michael Bochkaryov <misha@altlinux.ru>

BuildArch: noarch
Source: %m_distro-%version.tar.gz

# Automatically added by buildreq on Sat Oct 17 2009 (-bi)
BuildRequires: perl-IO-Interface perl-IO-Socket-INET6 perl-IO-Socket-Multicast perl-Module-Build perl-Test-Pod

%description
This is a pure perl implementation of
Real-time Transport (RTP) Protocol (RFC3550).

The Net::RTP module is used to send a receive RTP packets.

The Net::RTP::Packet module is used to parse the RTP packet headers.
It may be used totally independently of Net::RTP if you want to handle
sending and receiving packets yourself.


%prep
%setup -q -n %m_distro-%version
%build
%perl_vendor_build

%install
%perl_vendor_install
rm -rf %buildroot%perl_vendor_man3dir/

%files
%perl_vendor_privlib/Net/*
%doc README Changes tools/*.pl

%changelog
* Fri Jul 24 2009 Michael Bochkaryov <misha@altlinux.ru> 0.09-alt1
- initial build for ALT Linux Sisyphus


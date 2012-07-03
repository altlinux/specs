%define dist Net-Pcap-Easy

%ifdef __BTE
%def_without test
%endif

Name: perl-%dist
Version: 1.4207
Release: alt1

Summary: Net::Pcap is awesome, but it's difficult to bootstrap
Group: Development/Perl
License: GPL or Artistic
BuildArch: noarch

Url: %CPAN %dist
Source: %dist-%version.tar.gz

BuildRequires: perl-devel perl-Net-Pcap perl-NetPacket perl-Net-Netmask

%description
This module is little more than a collection of macros and convenience functions. Net::Pcap does all the real work (of lifting libpcap into perl anyway).

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/Net*
%doc README

%changelog
* Mon Dec 12 2011 Eugene Prokopiev <enp@altlinux.ru> 1.4207-alt1
- First build for Sisyphus

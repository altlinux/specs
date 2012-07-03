%define dist Net-CIDR
Name: perl-Net-CIDR
Version: 0.14
Release: alt2

Summary: Manipulate IPv4/IPv6 netblocks in CIDR notation
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Wed Apr 27 2011
BuildRequires: perl-devel

%description
The Net::CIDR package contains functions that manipulate lists of IP
netblocks expressed in CIDR notation.
The Net::CIDR functions handle both IPv4 and IPv6 addresses.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/Net

%changelog
* Wed Apr 27 2011 Alexey Tourbin <at@altlinux.ru> 0.14-alt2
- fixed unpackaged directory

* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 0.14-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Tue Jul 13 2010 Igor Vlasenko <viy@altlinux.ru> 0.14-alt1
- automated CPAN update

* Mon Apr 20 2009 Alexey Shabalin <shaba@altlinux.ru> 0.13-alt1
- 0.13

* Mon Oct 06 2008 Alexey Shabalin <shaba@altlinux.ru> 0.11-alt2
- fixed files list for sisyphus_check

* Thu Aug 18 2005 Alexey Shabalin <shaba@altlinux.ru> 0.11-alt1
- update 0.11

* Mon Jun 27 2005 Alexey Shabalin <shaba@altlinux.ru> 0.10-alt1
- first build for ALT Linux Sisyphus

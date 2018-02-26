%define dist Net-SNPP
Name: perl-%dist
Version: 1.17
Release: alt1.1.1

Summary: Simple Network Pager Protocol Client
License: GPL or Artistic
Group: Development/Perl

Url: %CPAN %dist
Source: %dist-%version.tar.bz2

BuildArch: noarch

# Automatically added by buildreq on Sat Apr 17 2004
BuildRequires: perl-devel perl-libnet

%description
This module implements a client interface to the SNPP protocol (Simple
Network Pager Protocol, RFC1861), enabling a perl5 application to talk
to SNPP servers.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README
%perl_vendor_privlib/Net

%changelog
* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 1.17-alt1.1.1
- repair after perl 5.12 upgrade using girar-nmu

* Sat Feb 19 2005 ALT QA Team Robot <qa-robot@altlinux.org> 1.17-alt1.1
- Rebuilt with rpm-build-perl-0.5.1.

* Sat Apr 17 2004 Alexey Tourbin <at@altlinux.ru> 1.17-alt1
- 1.15a -> 1.17

* Fri Oct 24 2003 Alexey Tourbin <at@altlinux.ru> 1.15a-alt1
- initial revision (this module is required by mon)

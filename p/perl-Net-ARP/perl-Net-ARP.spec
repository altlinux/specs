# tests require network
%define _without_test 1
%define _unpackaged_files_terminate_build 1
%define dist Net-ARP
Name: perl-%dist
Version: 1.0.12
Release: alt1

Summary: Perl extension for creating ARP packets
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source0: http://www.cpan.org/authors/id/C/CR/CRAZYDJ/%{dist}-%{version}.tar.gz

# Automatically added by buildreq on Sun Oct 09 2011
BuildRequires: perl-devel

%description
This module is a Perl extension to create and send ARP packets and lookup
local or remote mac addresses.

%prep
%setup -q -n %{dist}-%{version}

# need root
# mv t/send_packet.t t/send_packet.t.orig

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_archlib/Net
%perl_vendor_autolib/Net

%changelog
* Thu May 12 2022 Igor Vlasenko <viy@altlinux.org> 1.0.12-alt1
- automated CPAN update

* Thu Jun 25 2020 Igor Vlasenko <viy@altlinux.ru> 1.0.11-alt1
- automated CPAN update

* Thu Jan 24 2019 Igor Vlasenko <viy@altlinux.ru> 1.0.9-alt1.2
- rebuild with new perl 5.28.1

* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 1.0.9-alt1.1.1.1
- rebuild with new perl 5.26.1

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 1.0.9-alt1.1.1
- rebuild with new perl 5.24.1

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 1.0.9-alt1.1
- rebuild with new perl 5.22.0

* Tue Dec 16 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.9-alt1
- automated CPAN update

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.8-alt2.1
- rebuild with new perl 5.20.1

* Wed Aug 28 2013 Vladimir Lettiev <crux@altlinux.ru> 1.0.8-alt2
- built for perl 5.18

* Sat Jul 27 2013 Igor Vlasenko <viy@altlinux.ru> 1.0.8-alt1
- automated CPAN update

* Sat Sep 01 2012 Vladimir Lettiev <crux@altlinux.ru> 1.0.6-alt3
- rebuilt for perl-5.16

* Sun Oct 09 2011 Alexey Tourbin <at@altlinux.ru> 1.0.6-alt2
- rebuilt for perl-5.14

* Sat Jul 30 2011 Slava Dubrovskiy <dubrsl@altlinux.org> 1.0.6-alt1
- initial build for ALT Linux Sisyphus

%define dist Net-Libdnet
Name: perl-%dist
Version: 0.98
Release: alt2.1.1.1.1

Summary: Binding for Dug Song's libdnet
License: BSD
Group: Development/Perl

URL: %CPAN %dist
Source: http://www.cpan.org/authors/id/G/GO/GOMOR/Net-Libdnet-%{version}.tar.gz

# Automatically added by buildreq on Tue Oct 11 2011
BuildRequires: libdnet-devel perl-Class-Gomor perl-Test-Pod perl-Test-Pod-Coverage

%description
Net::Libdnet provides a simplified, portable interface to several low-level
networking routines, including network address manipulation, kernel arp cache
and route table lookup and manipulation, network firewalling, network interface
lookup and manipulation, network traffic interception via tunnel interfaces,
and raw IP packet and Ethernet frame transmission. It is intended to complement
the functionality provided by libpcap.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_archlib/Net
%perl_vendor_autolib/Net

%changelog
* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 0.98-alt2.1.1.1.1
- rebuild with new perl 5.26.1

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.98-alt2.1.1.1
- rebuild with new perl 5.24.1

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 0.98-alt2.1.1
- rebuild with new perl 5.22.0

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 0.98-alt2.1
- rebuild with new perl 5.20.1

* Thu Aug 29 2013 Vladimir Lettiev <crux@altlinux.ru> 0.98-alt2
- built for perl 5.18

* Wed Jul 24 2013 Igor Vlasenko <viy@altlinux.ru> 0.98-alt1
- automated CPAN update

* Sun Sep 02 2012 Vladimir Lettiev <crux@altlinux.ru> 0.96-alt1
- 0.92 -> 0.96
- built for perl-5.16

* Tue Oct 11 2011 Alexey Tourbin <at@altlinux.ru> 0.92-alt1.2
- rebuilt for perl-5.14

* Thu Nov 04 2010 Vladimir Lettiev <crux@altlinux.ru> 0.92-alt1.1
- rebuilt with perl 5.12

* Sat Nov 07 2009 Denis Smirnov <mithraen@altlinux.ru> 0.92-alt1
- initial build for ALT Linux Sisyphus


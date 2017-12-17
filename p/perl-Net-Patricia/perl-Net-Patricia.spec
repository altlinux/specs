%define _unpackaged_files_terminate_build 1
%define module Net-Patricia
Name: perl-%module
Version: 1.22
Release: alt1.1.1.1.1

Summary: Patricia Trie perl module for fast IP address lookups
License: GPL
Group: Development/Perl

URL: %CPAN %module
Source: http://www.cpan.org/authors/id/G/GR/GRUBER/Net-Patricia-%{version}.tar.gz

# Automatically added by buildreq on Tue Oct 11 2011
BuildRequires: perl-Net-CIDR-Lite perl-Socket6 perl-devel

%description
This module uses a Patricia Trie data structure to quickly
perform IP address prefix matching for applications such as
IP subnet, network or routing table lookups.

%prep
%setup -q -n %module-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README demo
%perl_vendor_archlib/Net
%perl_vendor_autolib/Net

%changelog
* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 1.22-alt1.1.1.1.1
- rebuild with new perl 5.26.1

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 1.22-alt1.1.1.1
- rebuild with new perl 5.24.1

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 1.22-alt1.1.1
- rebuild with new perl 5.22.0

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 1.22-alt1.1
- rebuild with new perl 5.20.1

* Mon Oct 21 2013 Igor Vlasenko <viy@altlinux.ru> 1.22-alt1
- automated CPAN update

* Mon Sep 30 2013 Igor Vlasenko <viy@altlinux.ru> 1.21-alt1
- automated CPAN update

* Thu Aug 29 2013 Vladimir Lettiev <crux@altlinux.ru> 1.20-alt2
- built for perl 5.18

* Wed Jul 24 2013 Igor Vlasenko <viy@altlinux.ru> 1.20-alt1
- automated CPAN update

* Sun Sep 02 2012 Vladimir Lettiev <crux@altlinux.ru> 1.19-alt3
- rebuilt for perl-5.16

* Tue Oct 11 2011 Alexey Tourbin <at@altlinux.ru> 1.19-alt2
- rebuilt for perl-5.14

* Sun Dec 12 2010 Vladimir Lettiev <crux@altlinux.ru> 1.19-alt1
- New version 1.19
- Updated buildrequires
- Fixed files section

* Sat Nov 06 2010 Vladimir Lettiev <crux@altlinux.ru> 1.014-alt2.1
- rebuilt with perl 5.12

* Fri Sep 05 2008 Dmitry Lebkov <dlebkov@altlinux.ru> 1.014-alt2
- list of packaged directories fixed

* Fri Jan 12 2007 Dmitry Lebkov <dlebkov@altlinux.ru> 1.014-alt1
- 1.014

* Fri Sep 03 2004 Dmitry Lebkov <dlebkov@altlinux.ru> 1.010-alt1
- initial package for ALT Linux

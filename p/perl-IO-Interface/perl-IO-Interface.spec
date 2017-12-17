%define _unpackaged_files_terminate_build 1
BuildRequires: perl(Module/Build.pm)
%define dist IO-Interface
Name: perl-%dist
Version: 1.09
Release: alt1.1.1.1

Summary: extention for IO::Socket
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: http://www.cpan.org/authors/id/L/LD/LDS/IO-Interface-%{version}.tar.gz

# Automatically added by buildreq on Sat Oct 08 2011
BuildRequires: perl-devel

%description
IO::Interface adds object-methods to IO::Socket objects to allow them
to get and set operational characteristics of network interface cards,
such as IP addresses, net masks, and so forth.  It is useful for
identifying runtime characteristics of cards, such as broadcast
addresses, and finding interfaces that satisfy certain criteria, such
as the ability to multicast.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README.md
%perl_vendor_archlib/IO
%perl_vendor_autolib/IO

%changelog
* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 1.09-alt1.1.1.1
- rebuild with new perl 5.26.1

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 1.09-alt1.1.1
- rebuild with new perl 5.24.1

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 1.09-alt1.1
- rebuild with new perl 5.22.0

* Tue Dec 16 2014 Igor Vlasenko <viy@altlinux.ru> 1.09-alt1
- automated CPAN update

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 1.07-alt1.1
- rebuild with new perl 5.20.1

* Tue Jun 10 2014 Igor Vlasenko <viy@altlinux.ru> 1.07-alt1
- automated CPAN update

* Wed Aug 28 2013 Vladimir Lettiev <crux@altlinux.ru> 1.06-alt4
- built for perl 5.18

* Fri Aug 31 2012 Vladimir Lettiev <crux@altlinux.ru> 1.06-alt3
- rebuilt for perl-5.16

* Sat Oct 08 2011 Alexey Tourbin <at@altlinux.ru> 1.06-alt2
- rebuilt for perl-5.14

* Mon Sep 19 2011 Igor Vlasenko <viy@altlinux.ru> 1.06-alt1
- automated CPAN update

* Sat Nov 06 2010 Vladimir Lettiev <crux@altlinux.ru> 1.05-alt1.1
- rebuilt with perl 5.12

* Tue Sep 02 2008 Sergey Y. Afonin <asy@altlinux.ru> 1.05-alt1
- New version
- fixed directory ownership viloation

* Wed Mar 05 2008 Sergey Y. Afonin <asy@altlinux.ru> 1.04-alt1
- new version

* Mon May 07 2007 Sergey Y. Afonin <asy@altlinux.ru> 1.03-alt1
- Initial build for ALTLinux

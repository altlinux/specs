%define dist Acme-Damn
Name: perl-%dist
Version: 0.08
Release: alt1.1.1

Summary: 'Unbless' Perl objects
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: http://www.cpan.org/authors/id/I/IB/IBB/Acme-Damn-%{version}.tar.gz

# Automatically added by buildreq on Sat Oct 08 2011
BuildRequires: perl-Test-Exception

%description
Acme::Damn provides a single routine, damn(), which takes a blessed
reference (a Perl object), and *unblesses* it, to return the original
reference. I can't think of any reason why you might want to do this, but
just because it's of no use doesn't mean that you shouldn't be able to do
it.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_archlib/Acme
%perl_vendor_autolib/Acme

%changelog
* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 0.08-alt1.1.1
- rebuild with new perl 5.26.1

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.08-alt1.1
- rebuild with new perl 5.24.1

* Sun Dec 18 2016 Igor Vlasenko <viy@altlinux.ru> 0.08-alt1
- automated CPAN update

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 0.06-alt1.1.1
- rebuild with new perl 5.22.0

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 0.06-alt1.1
- rebuild with new perl 5.20.1

* Mon Oct 27 2014 Igor Vlasenko <viy@altlinux.ru> 0.06-alt1
- automated CPAN update

* Wed Aug 28 2013 Vladimir Lettiev <crux@altlinux.ru> 0.05-alt2
- built for perl 5.18

* Fri Aug 31 2012 Vladimir Lettiev <crux@altlinux.ru> 0.05-alt1
- 0.04 -> 0.05
- built for perl-5.16

* Sat Oct 08 2011 Alexey Tourbin <at@altlinux.ru> 0.04-alt1.2
- rebuilt for perl-5.14

* Thu Nov 04 2010 Vladimir Lettiev <crux@altlinux.ru> 0.04-alt1.1
- rebuilt with perl 5.12

* Sun Sep 20 2009 Vitaly Lipatov <lav@altlinux.ru> 0.04-alt1
- initial build for ALT Linux Sisyphus


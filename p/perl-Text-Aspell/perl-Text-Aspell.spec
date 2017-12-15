%define dist Text-Aspell
Name: perl-%dist
Version: 0.09
Release: alt3.1.1.1.1

Summary: Perl interface to the GNU Aspell library
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

# Automatically added by buildreq on Fri Oct 07 2011
BuildRequires: aspell-en libaspell-devel perl-Test-Pod

%description
This module provides a Perl interface to the GNU Aspell library.
The GNU Aspell library provides access to system spelling libraries,
including a spell checker.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_archlib/Text
%perl_vendor_autolib/Text

%changelog
* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 0.09-alt3.1.1.1.1
- rebuild with new perl 5.26.1

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.09-alt3.1.1.1
- rebuild with new perl 5.24.1

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 0.09-alt3.1.1
- rebuild with new perl 5.22.0

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 0.09-alt3.1
- rebuild with new perl 5.20.1

* Wed Aug 28 2013 Vladimir Lettiev <crux@altlinux.ru> 0.09-alt3
- built for perl 5.18

* Thu Aug 30 2012 Vladimir Lettiev <crux@altlinux.ru> 0.09-alt2
- rebuilt for perl-5.16

* Fri Oct 07 2011 Alexey Tourbin <at@altlinux.ru> 0.09-alt1.2
- rebuilt for perl-5.14

* Fri Nov 05 2010 Vladimir Lettiev <crux@altlinux.ru> 0.09-alt1.1
- rebuilt with perl 5.12

* Thu Apr 29 2010 Alexey Tourbin <at@altlinux.ru> 0.09-alt1
- 0.04 -> 0.09

* Sat Feb 19 2005 ALT QA Team Robot <qa-robot@altlinux.org> 0.04-alt1.1
- Rebuilt with rpm-build-perl-0.5.1.

* Sun Nov 28 2004 Alexey Tourbin <at@altlinux.ru> 0.04-alt1
- initial revision
- alt-sigsegv.patch: fixed null dereferencing (cpan #8633)
- alt-static.patch: made C functions static (cpan #8634)
- clear_session not implemented as of aspell-0.60 (cpan #8635)

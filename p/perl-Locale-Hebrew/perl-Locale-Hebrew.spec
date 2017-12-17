%define dist Locale-Hebrew
Name: perl-%dist
Version: 1.05
Release: alt5.1.1.1.1

Summary: Bidirectional Hebrew support
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

# Automatically added by buildreq on Wed Nov 16 2011
BuildRequires: perl-Encode perl-Pod-Escapes perl-devel

%description
This module is based on code from the Unicode Consortium.
The charset on their code was bogus, therefore this module had to work
the real charset from scratch.  There might have some mistakes, though.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_archlib/Locale
%perl_vendor_autolib/Locale

%changelog
* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 1.05-alt5.1.1.1.1
- rebuild with new perl 5.26.1

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 1.05-alt5.1.1.1
- rebuild with new perl 5.24.1

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 1.05-alt5.1.1
- rebuild with new perl 5.22.0

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 1.05-alt5.1
- rebuild with new perl 5.20.1

* Thu Aug 29 2013 Vladimir Lettiev <crux@altlinux.ru> 1.05-alt5
- built for perl 5.18

* Sun Sep 02 2012 Vladimir Lettiev <crux@altlinux.ru> 1.05-alt4
- rebuilt for perl-5.16

* Wed Nov 16 2011 Alexey Tourbin <at@altlinux.ru> 1.05-alt3
- disabled build dependency on perl-Module-Install

* Tue Oct 11 2011 Alexey Tourbin <at@altlinux.ru> 1.05-alt2
- rebuilt for perl-5.14

* Mon Sep 19 2011 Igor Vlasenko <viy@altlinux.ru> 1.05-alt1
- automated CPAN update

* Sat Nov 06 2010 Vladimir Lettiev <crux@altlinux.ru> 1.04-alt1.1
- rebuilt with perl 5.12

* Sat Sep 09 2006 Vyacheslav Dikonov <slava@altlinux.ru> 1.04-alt1
- Initial build

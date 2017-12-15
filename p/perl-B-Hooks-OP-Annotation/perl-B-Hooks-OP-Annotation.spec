%define dist B-Hooks-OP-Annotation
Name: perl-%dist
Version: 0.44
Release: alt4.1.1.1.1

Summary: Annotate and delegate hooked OPs
License: Perl
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

# Automatically added by buildreq on Tue Oct 11 2011
BuildRequires: perl-ExtUtils-Depends perl-Test-Pod

%description
This module provides a way for XS code that hijacks OP op_ppaddr
functions to delegate to (or restore) the previous functions,
whether assigned by perl or by another module.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README 
%perl_vendor_archlib/B
%perl_vendor_autolib/B

%changelog
* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 0.44-alt4.1.1.1.1
- rebuild with new perl 5.26.1

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.44-alt4.1.1.1
- rebuild with new perl 5.24.1

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 0.44-alt4.1.1
- rebuild with new perl 5.22.0

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 0.44-alt4.1
- rebuild with new perl 5.20.1

* Thu Aug 29 2013 Vladimir Lettiev <crux@altlinux.ru> 0.44-alt4
- built for perl 5.18

* Sun Sep 02 2012 Vladimir Lettiev <crux@altlinux.ru> 0.44-alt3
- rebuilt for perl-5.16

* Tue Oct 11 2011 Alexey Tourbin <at@altlinux.ru> 0.44-alt2
- rebuilt for perl-5.14

* Thu Sep 22 2011 Igor Vlasenko <viy@altlinux.ru> 0.44-alt1
- automated CPAN update

* Thu Feb 17 2011 Vladimir Lettiev <crux@altlinux.ru> 0.43-alt1
- initial build

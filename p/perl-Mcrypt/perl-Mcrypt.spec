Name: perl-Mcrypt
Version: 2.5.7.0
Release: alt2.1.1.1.1

Summary: Mcrypt - Perl extension for the Mcrypt cryptography library
Group: Development/Perl
License: Perl

Url: %CPAN Mcrypt
Source: %name-%version.tar

BuildRequires: libmcrypt-devel perl-devel

%description
%summary

%prep
%setup -q

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_archlib/Mcrypt*
%perl_vendor_autolib/Mcrypt*
%doc ChangeLog README 

%changelog
* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 2.5.7.0-alt2.1.1.1.1
- rebuild with new perl 5.26.1

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 2.5.7.0-alt2.1.1.1
- rebuild with new perl 5.24.1

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 2.5.7.0-alt2.1.1
- rebuild with new perl 5.22.0

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 2.5.7.0-alt2.1
- rebuild with new perl 5.20.1

* Mon Sep 02 2013 Vladimir Lettiev <crux@altlinux.ru> 2.5.7.0-alt2
- built for perl 5.18

* Thu Sep 20 2012 Vladimir Lettiev <crux@altlinux.ru> 2.5.7.0-alt1
- initial build

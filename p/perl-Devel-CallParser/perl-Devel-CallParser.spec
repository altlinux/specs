Name: perl-Devel-CallParser
Version: 0.002
Release: alt1.1.1.1.1

Summary: custom parsing attached to subroutines
Group: Development/Perl
License: perl

Url: %CPAN Devel-CallParser
Source: %name-%version.tar

BuildRequires: perl-base perl(parent.pm) perl-devel perl(DynaLoader/Functions.pm) perl(Devel/CallChecker.pm) perl(Module/Build.pm) perl(ExtUtils/CBuilder.pm)

%description
%summary

%prep
%setup -q

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_autolib/Devel/CallParser*
%perl_vendor_archlib/Devel/CallParser*
%doc Changes README

%changelog
* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 0.002-alt1.1.1.1.1
- rebuild with new perl 5.26.1

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.002-alt1.1.1.1
- rebuild with new perl 5.24.1

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 0.002-alt1.1.1
- rebuild with new perl 5.22.0

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 0.002-alt1.1
- rebuild with new perl 5.20.1

* Fri Dec 06 2013 Vladimir Lettiev <crux@altlinux.ru> 0.002-alt1
- initial build for ALTLinux


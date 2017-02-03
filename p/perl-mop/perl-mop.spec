%def_without test
Name: perl-mop
Version: 0.02
Release: alt2.1

Summary: A new object system for Perl 5
Group: Development/Perl
License: perl_5

Url: %CPAN mop
Source: %name-%version.tar

BuildRequires: perl-devel perl(Devel/CallParser.pm) perl(parent.pm)

%description
%summary

%prep
%setup -q

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_autolib/mop*
%perl_vendor_archlib/mop*
%perl_vendor_archlib/op.pm
%doc Changes README.md

%changelog
* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.02-alt2.1
- rebuild with new perl 5.24.1

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.02-alt2
- disabled tests to upgrade perl smoothly.

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 0.02-alt1.1.1
- rebuild with new perl 5.22.0

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 0.02-alt1.1
- rebuild with new perl 5.20.1

* Fri Dec 06 2013 Vladimir Lettiev <crux@altlinux.ru> 0.02-alt1
- initial build for ALTLinux


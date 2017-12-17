Name: perl-Class-Load-XS
Version: 0.10
Release: alt1.1

Summary: XS implementation of parts of Class::Load
Group: Development/Perl
License: artistic_2

Url: %CPAN Class-Load-XS
Source: %name-%version.tar

BuildRequires: perl(Test/Requires.pm) perl(Class/Load.pm) perl(Test/Fatal.pm) perl-devel perl(Module/Implementation.pm) perl(Module/Build.pm) perl(Test/Needs.pm)

%description
%summary

%prep
%setup -q

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_autolib/Class/Load/XS*
%perl_vendor_archlib/Class/Load/XS*
%doc Changes LICENSE README

%changelog
* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 0.10-alt1.1
- rebuild with new perl 5.26.1

* Wed May 10 2017 Igor Vlasenko <viy@altlinux.ru> 0.10-alt1
- automated CPAN update

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.09-alt1.1.1
- rebuild with new perl 5.24.1

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 0.09-alt1.1
- rebuild with new perl 5.22.0

* Wed Dec 17 2014 Igor Vlasenko <viy@altlinux.ru> 0.09-alt1
- automated CPAN update

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 0.08-alt1.1
- rebuild with new perl 5.20.1

* Tue Jun 24 2014 Igor Vlasenko <viy@altlinux.ru> 0.08-alt1
- automated CPAN update

* Wed Aug 28 2013 Vladimir Lettiev <crux@altlinux.ru> 0.06-alt1
- initial build for ALTLinux


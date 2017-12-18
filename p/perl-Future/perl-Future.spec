Name: perl-Future
Version: 0.38
Release: alt1

Summary: represent an operation awaiting completion
Group: Development/Perl
License: perl

Url: %CPAN Future
Source: %name-%version.tar

BuildArch: noarch
BuildRequires: perl-devel perl(Module/Build.pm) perl(Test/Refcount.pm) perl(Test/Fatal.pm) perl(Test/Identity.pm)

%description
%summary

%prep
%setup -q

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes LICENSE README examples
%perl_vendor_privlib/Future*
%perl_vendor_privlib/Test/Future*
%doc Changes LICENSE README

%changelog
* Mon Dec 18 2017 Igor Vlasenko <viy@altlinux.ru> 0.38-alt1
- automated CPAN update

* Sun Oct 01 2017 Igor Vlasenko <viy@altlinux.ru> 0.35-alt1
- automated CPAN update

* Fri Nov 18 2016 Igor Vlasenko <viy@altlinux.ru> 0.34-alt1
- automated CPAN update

* Thu Oct 15 2015 Igor Vlasenko <viy@altlinux.ru> 0.33-alt1
- automated CPAN update

* Wed Dec 17 2014 Igor Vlasenko <viy@altlinux.ru> 0.30-alt1
- automated CPAN update

* Fri Jul 25 2014 Igor Vlasenko <viy@altlinux.ru> 0.29-alt1
- automated CPAN update

* Tue Jun 24 2014 Igor Vlasenko <viy@altlinux.ru> 0.28-alt1
- automated CPAN update

* Sat Dec 14 2013 Vladimir Lettiev <crux@altlinux.ru> 0.20-alt1
- initial build for ALTLinux


Name: perl-CPAN-Perl-Releases
Version: 2.58
Release: alt1

Summary: Mapping Perl releases on CPAN to the location of the tarballs
Group: Development/Perl
License: perl

Url: %CPAN CPAN-Perl-Releases
Source: %name-%version.tar

BuildArch: noarch
BuildRequires: perl-devel

%description
%summary

%prep
%setup -q

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/CPAN/Perl/Releases*
%doc Changes LICENSE README

%changelog
* Thu Mar 03 2016 Igor Vlasenko <viy@altlinux.ru> 2.58-alt1
- automated CPAN update

* Mon Dec 07 2015 Igor Vlasenko <viy@altlinux.ru> 2.48-alt1
- automated CPAN update

* Wed Nov 11 2015 Igor Vlasenko <viy@altlinux.ru> 2.42-alt1
- automated CPAN update

* Thu Oct 15 2015 Igor Vlasenko <viy@altlinux.ru> 2.38-alt1
- automated CPAN update

* Mon Dec 22 2014 Igor Vlasenko <viy@altlinux.ru> 2.02-alt1
- automated CPAN update

* Wed Dec 17 2014 Igor Vlasenko <viy@altlinux.ru> 2.00-alt1
- automated CPAN update

* Fri Jul 25 2014 Igor Vlasenko <viy@altlinux.ru> 1.78-alt1
- automated CPAN update

* Thu Jun 26 2014 Igor Vlasenko <viy@altlinux.ru> 1.76-alt1
- automated CPAN update

* Tue Sep 10 2013 Vladimir Lettiev <crux@altlinux.ru> 1.42-alt1
- 0.72 -> 1.42

* Wed Oct 10 2012 Vladimir Lettiev <crux@altlinux.ru> 0.72-alt1
- initial build for ALTLinux


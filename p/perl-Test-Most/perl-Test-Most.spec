Name: perl-Test-Most
Version: 0.35
Release: alt1

Summary: Test::Most - Most commonly needed test functions and features
Group: Development/Perl
License: Perl

Url: %CPAN Test-Most
Source: %name-%version.tar

BuildArch: noarch
BuildRequires: perl-devel perl-Test-Deep perl-Test-Warn perl-Exception-Class perl-Test-Differences perl-Test-Exception perl-Module-Build
Requires: perl-Test-Warn perl-Test-Exception perl-Test-Differences perl-Test-Deep

%description
%summary

%prep
%setup -q

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/Test/Most*
%doc Changes README

%changelog
* Tue Dec 19 2017 Igor Vlasenko <viy@altlinux.ru> 0.35-alt1
- automated CPAN update

* Wed Dec 17 2014 Igor Vlasenko <viy@altlinux.ru> 0.34-alt1
- automated CPAN update

* Mon Jun 30 2014 Igor Vlasenko <viy@altlinux.ru> 0.33-alt1
- automated CPAN update

* Mon Oct 01 2012 Vladimir Lettiev <crux@altlinux.ru> 0.31-alt1
- 0.25 -> 0.31
- sources cloned from upstream git

* Thu May 31 2012 Vladimir Lettiev <crux@altlinux.ru> 0.25-alt3
- fixed requires (reported by viy@)

* Sat Nov 05 2011 Vladimir Lettiev <crux@altlinux.ru> 0.25-alt2
- fixed builddeps

* Thu Sep 22 2011 Igor Vlasenko <viy@altlinux.ru> 0.25-alt1
- automated CPAN update

* Fri Dec 03 2010 Vladimir Lettiev <crux@altlinux.ru> 0.23-alt1
- initial build

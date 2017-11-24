Name: perl-Test-Spec
Version: 0.54
Release: alt1

Summary: Write tests in a declarative specification style
Group: Development/Perl
License: perl

Url: %CPAN Test-Spec
Source: %name-%version.tar

BuildArch: noarch
BuildRequires: perl-Tie-IxHash perl-Package-Stash perl-devel perl-Test-Trap perl-Test-Deep

%description
%summary

%prep
%setup -q

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/Test/Spec*
%doc Changes README*

%changelog
* Sat Nov 25 2017 Igor Vlasenko <viy@altlinux.ru> 0.54-alt1
- automated CPAN update

* Sun Oct 01 2017 Igor Vlasenko <viy@altlinux.ru> 0.53-alt1
- automated CPAN update

* Thu Oct 15 2015 Igor Vlasenko <viy@altlinux.ru> 0.51-alt1
- automated CPAN update

* Tue Jun 24 2014 Igor Vlasenko <viy@altlinux.ru> 0.47-alt1
- automated CPAN update

* Wed Oct 10 2012 Vladimir Lettiev <crux@altlinux.ru> 0.46-alt1
- initial build for ALTLinux


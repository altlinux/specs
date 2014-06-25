Name: perl-Test-Spec
Version: 0.47
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
%doc Changes README

%changelog
* Tue Jun 24 2014 Igor Vlasenko <viy@altlinux.ru> 0.47-alt1
- automated CPAN update

* Wed Oct 10 2012 Vladimir Lettiev <crux@altlinux.ru> 0.46-alt1
- initial build for ALTLinux


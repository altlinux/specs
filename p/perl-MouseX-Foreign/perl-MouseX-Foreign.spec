Name: perl-MouseX-Foreign
Version: 1.000
Release: alt1.1
Summary: MouseX::Foreign - Extends non-Mouse classes as well as Mouse classes

Group: Development/Perl
License: Perl
Url: %CPAN MouseX-Foreign

BuildArch: noarch
Source: %name-%version.tar
BuildRequires: perl-devel perl-Mouse perl-Test-Exception perl-Test-Requires perl-Module-Build perl-Math-BigInt perl-Any-Moose

%description
%summary

%prep
%setup -q

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/MouseX/Foreign*
%perl_vendor_privlib/MouseX/NonMoose*
%doc Changes README.md

%changelog
* Wed Apr 22 2020 Igor Vlasenko <viy@altlinux.ru> 1.000-alt1.1
- dropped BR: perl-Module-Install

* Sat Jun 28 2014 Igor Vlasenko <viy@altlinux.ru> 1.000-alt1
- automated CPAN update

* Fri Apr 13 2012 Vladimir Lettiev <crux@altlinux.ru> 0.007-alt1
- 0.007

* Fri Aug 12 2011 Vladimir Lettiev <crux@altlinux.ru> 0.004-alt1
- initial build

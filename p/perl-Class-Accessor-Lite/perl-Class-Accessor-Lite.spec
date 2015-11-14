%define dist Class-Accessor-Lite
Name: perl-Class-Accessor-Lite
Version: 0.08
Release: alt1
Summary: Class::Accessor::Lite - a minimalistic variant of Class::Accessor

Group: Development/Perl
License: Perl
Url: %CPAN %dist

BuildArch: noarch
Source: %dist-%version.tar.gz
BuildRequires: perl-Module-Install

%description
%summary

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/Class/Accessor/Lite*
%doc Changes README 

%changelog
* Fri Nov 13 2015 Vladimir Lettiev <crux@altlinux.ru> 0.08-alt1
- 0.08
- switch to srpm update

* Wed Dec 17 2014 Igor Vlasenko <viy@altlinux.ru> 0.06-alt1
- automated CPAN update

* Sat Jul 30 2011 Vladimir Lettiev <crux@altlinux.ru> 0.05-alt1
- initial build

Name: perl-Router-Boom
Version: 1.03
Release: alt1

Summary: Fast routing engine for web applications
Group: Development/Perl
License: perl

Url: %CPAN Router-Boom
Source: %name-%version.tar

BuildArch: noarch
BuildRequires: perl-devel perl(CPAN/Meta.pm) perl(Module/Build/Tiny.pm) perl(Class/Accessor/Lite.pm) perl(CPAN/Meta/Prereqs.pm) perl(Test/Deep.pm)

%description
%summary

%prep
%setup -q

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/Router/Boom*
%doc Changes LICENSE README.md

%changelog
* Thu May 26 2016 Igor Vlasenko <viy@altlinux.ru> 1.03-alt1
- automated CPAN update

* Thu Oct 15 2015 Igor Vlasenko <viy@altlinux.ru> 1.02-alt1
- automated CPAN update

* Tue Jun 24 2014 Igor Vlasenko <viy@altlinux.ru> 1.01-alt1
- automated CPAN update

* Mon Dec 09 2013 Vladimir Lettiev <crux@altlinux.ru> 1.00-alt1
- initial build for ALTLinux


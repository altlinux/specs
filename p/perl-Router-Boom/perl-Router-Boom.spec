Name: perl-Router-Boom
Version: 1.01
Release: alt1

Summary: Fast routing engine for web applications
Group: Development/Perl
License: perl

Url: %CPAN Router-Boom
Source: %name-%version.tar

BuildArch: noarch
BuildRequires: perl-devel perl(CPAN/Meta.pm) perl(Module/Build.pm) perl(Class/Accessor/Lite.pm) perl(CPAN/Meta/Prereqs.pm)

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
* Tue Jun 24 2014 Igor Vlasenko <viy@altlinux.ru> 1.01-alt1
- automated CPAN update

* Mon Dec 09 2013 Vladimir Lettiev <crux@altlinux.ru> 1.00-alt1
- initial build for ALTLinux


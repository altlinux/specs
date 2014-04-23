Name: perl-ExtUtils-CChecker
Version: 0.09
Release: alt1

Summary: configure-time utilities for using C headers, libraries, or OS features
Group: Development/Perl
License: perl

Url: %CPAN ExtUtils-CChecker
Source: %name-%version.tar

BuildArch: noarch
BuildRequires: perl-devel perl(Test/Fatal.pm) perl(Module/Build.pm) perl(ExtUtils/CBuilder.pm)

%description
%summary

%prep
%setup -q

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/ExtUtils/CChecker*
%doc Changes LICENSE README

%changelog
* Wed Apr 23 2014 Vladimir Lettiev <crux@altlinux.ru> 0.09-alt1
- 0.09

* Tue Sep 10 2013 Vladimir Lettiev <crux@altlinux.ru> 0.08-alt1
- initial build for ALTLinux


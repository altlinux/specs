Name: perl-Apache-LogFormat-Compiler
Version: 0.33
Release: alt1

Summary: Compile a log format string to perl-code 
Group: Development/Perl
License: perl

Url: %CPAN Apache-LogFormat-Compiler
Source: %name-%version.tar

BuildArch: noarch
BuildRequires: perl(Test/Requires.pm) perl(Try/Tiny.pm) perl(URI/Escape.pm) perl(HTTP/Request/Common.pm) perl-devel perl(CPAN/Meta.pm) perl(Module/Build.pm) perl(CPAN/Meta/Prereqs.pm) perl(Test/MockTime.pm) perl(POSIX/strftime/Compiler.pm)

%description
%summary

%prep
%setup -q

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/Apache/LogFormat/Compiler*
%doc Changes LICENSE README.md

%changelog
* Thu Mar 03 2016 Igor Vlasenko <viy@altlinux.ru> 0.33-alt1
- automated CPAN update

* Tue Jun 24 2014 Igor Vlasenko <viy@altlinux.ru> 0.32-alt1
- automated CPAN update

* Mon Sep 30 2013 Vladimir Lettiev <crux@altlinux.ru> 0.13-alt1
- initial build for ALTLinux


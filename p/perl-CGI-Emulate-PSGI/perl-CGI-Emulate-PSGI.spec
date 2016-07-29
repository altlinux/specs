Name: perl-CGI-Emulate-PSGI
Version: 0.22
Release: alt1

Summary: CGI::Emulate::PSGI - PSGI adapter for CGI
Group: Development/Perl
License: Perl

Url: %CPAN CGI-Emulate-PSGI
Source: %name-%version.tar

BuildArch: noarch
BuildRequires: perl-devel perl-libwww perl-CGI perl(Test/Requires.pm)

%description
This module allows an application designed for the CGI environment to
run in a PSGI environment, and thus on any of the backends that PSGI
supports.
It works by translating the environment provided by the PSGI
specification to one expected by the CGI specification. Likewise, it
captures output as it would be prepared for the CGI standard, and
translates it to the format expected for the PSGI standard using
CGI::Parse::PSGI module

%prep
%setup -q

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/CGI/Emulate/PSGI.pm
%perl_vendor_privlib/CGI/Parse/PSGI.pm
%doc Changes README

%changelog
* Fri Jul 29 2016 Igor Vlasenko <viy@altlinux.ru> 0.22-alt1
- automated CPAN update

* Thu Oct 15 2015 Igor Vlasenko <viy@altlinux.ru> 0.21-alt1
- automated CPAN update

* Wed Dec 17 2014 Igor Vlasenko <viy@altlinux.ru> 0.20-alt1
- automated CPAN update

* Mon Sep 30 2013 Vladimir Lettiev <crux@altlinux.ru> 0.15-alt1
- New version 0.15

* Mon Dec 05 2011 Vladimir Lettiev <crux@altlinux.ru> 0.14-alt1
- New version 0.14

* Thu Sep 22 2011 Igor Vlasenko <viy@altlinux.ru> 0.13-alt1
- automated CPAN update

* Thu Mar 03 2011 Vladimir Lettiev <crux@altlinux.ru> 0.11-alt1
- New version 0.11

* Mon Aug 30 2010 Vladimir Lettiev <crux@altlinux.ru> 0.10-alt1
- initial build

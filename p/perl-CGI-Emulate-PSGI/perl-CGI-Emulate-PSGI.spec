Name: perl-CGI-Emulate-PSGI
Version: 0.14
Release: alt1
Summary: CGI::Emulate::PSGI - PSGI adapter for CGI

Group: Development/Perl
License: Perl
Url: %CPAN CGI-Emulate-PSGI

BuildArch: noarch
Source: %name-%version.tar
BuildRequires: perl-devel perl-libwww perl-CGI

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
%setup -q -n %name-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/CGI/Emulate/PSGI.pm
%perl_vendor_privlib/CGI/Parse/PSGI.pm
%doc Changes README 

%changelog
* Mon Dec 05 2011 Vladimir Lettiev <crux@altlinux.ru> 0.14-alt1
- New version 0.14

* Thu Sep 22 2011 Igor Vlasenko <viy@altlinux.ru> 0.13-alt1
- automated CPAN update

* Thu Mar 03 2011 Vladimir Lettiev <crux@altlinux.ru> 0.11-alt1
- New version 0.11

* Mon Aug 30 2010 Vladimir Lettiev <crux@altlinux.ru> 0.10-alt1
- initial build

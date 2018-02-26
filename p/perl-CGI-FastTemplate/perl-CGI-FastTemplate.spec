## SPEC file for Perl module CGI::FastTemplate
## Used in perl-CGI-FormTemplate

%define version    1.09
%define release    alt1

Name: perl-CGI-FastTemplate
Version: %version
Release: alt1.1

Summary: Perl extension for managing templates, and performing variable interpolation

License: %perl_license
Group: Development/Perl
URL: http://search.cpan.org/~jmoore/CGI-FastTemplate/

Packager: Nikolay A. Fetisov <naf@altlinux.ru>
BuildArch: noarch

%define real_name CGI-FastTemplate
Source: %real_name-%version.tar.bz2

AutoReqProv: perl, yes
BuildPreReq: rpm-build-licenses perl-devel

%description
Perl module CGI::FastTemplate manages templates and parses
templates replacing variable names with values. It was designed
for mid to large scale web applications (CGI, mod_perl) where
there are great benefits to separating the logic of an 
application from the specific implementation details.

%prep
%setup  -n %real_name-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README
%perl_vendor_privlib/CGI/FastTemplate*

%changelog
* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 1.09-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Sat Feb 23 2008 Nikolay A. Fetisov <naf@altlinux.ru> 1.09-alt1
- Initial build for ALT Linux Sisyphus

* Mon Feb 18 2008 Nikolay A. Fetisov <naf@altlinux.ru> 1.09-alt0.1
- Initial build

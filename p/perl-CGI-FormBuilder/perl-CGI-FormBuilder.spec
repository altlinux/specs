## SPEC file for Perl module CGI::FormBuilder
## Used in ikiwiki

%define version    3.0501
%define release    alt2

Name: perl-CGI-FormBuilder
Version: %version
Release: alt2.1

Summary: Perl module for easily generation and processing stateful forms

License: %perl_license
Group: Development/Perl
URL: http://search.cpan.org/~nwiger/CGI-FormBuilder/

Packager: Nikolay A. Fetisov <naf@altlinux.ru>
BuildArch: noarch

%define real_name CGI-FormBuilder
Source: %real_name-%version.tar

AutoReqProv: perl, yes
BuildRequires(pre): rpm-build-licenses perl-devel

# Automatically added by buildreq on Tue Feb 24 2009
BuildRequires: perl-CGI-FastTemplate perl-CGI-Session perl-HTML-Template perl-Template perl-Text-Template

%description
Perl module CGI::FormBuilder (FormBuilder) provides an easy way
for you to generate and process entire CGI form-based applications.
Its main features are:
- Field Abstraction
- DWIMmery
- Built-in Validation
- Template Support
The native HTML generated is valid XHTML 1.0 Transitional.

%prep
%setup  -n %real_name-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes
%exclude /.perl.req
%perl_vendor_privlib/CGI/FormBuilder*

%changelog
* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 3.0501-alt2.1
- repair after perl 5.12 upgrade using girar-nmu

* Tue Feb 24 2009 Nikolay A. Fetisov <naf@altlinux.ru> 3.0501-alt2
- Update BuildRequires

* Sat Feb 23 2008 Nikolay A. Fetisov <naf@altlinux.ru> 3.0501-alt1
- Initial build for ALT Linux Sisyphus

* Mon Feb 18 2008 Nikolay A. Fetisov <naf@altlinux.ru> 3.0501-alt0.1
- Initial build

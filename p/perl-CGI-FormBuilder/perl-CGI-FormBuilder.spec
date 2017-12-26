## SPEC file for Perl module CGI::FormBuilder
## Used in ikiwiki

Name: perl-CGI-FormBuilder
Epoch:   1
Version: 3.10
Release: alt2

Summary: Perl module for easily generation and processing stateful forms

License: %perl_license
Group: Development/Perl
URL: http://search.cpan.org/dist/CGI-FormBuilder/

Packager: Nikolay A. Fetisov <naf@altlinux.ru>
BuildArch: noarch

%define real_name CGI-FormBuilder
Source: %real_name-%version.tar
Patch0: %name-3.90-alt-test_fix.patch
Patch1: %name-3.10-alt-fix_encoding.patch

AutoReqProv: perl, yes
BuildRequires(pre): rpm-build-licenses perl-devel

# Automatically added by buildreq on Thu Oct 18 2012
# optimized out: perl-CGI perl-HTML-SimpleParse perl-HTTP-Cookies perl-HTTP-Date perl-HTTP-Message perl-TimeDate perl-URI perl-libwww
BuildRequires: perl-CGI-FastTemplate perl-CGI-SSI perl-CGI-Session perl-HTML-Template perl-Template perl-Text-Template perl-devel

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
%patch0
%patch1

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes
%exclude /.perl.req
%perl_vendor_privlib/CGI/FormBuilder*

%changelog
* Tue Dec 26 2017 Nikolay A. Fetisov <naf@altlinux.org> 1:3.10-alt2
- Fix build: convert Spanish message files to UTF-8

* Fri Sep 09 2016 Nikolay A. Fetisov <naf@altlinux.ru> 1:3.10-alt1
- New version

* Sun Dec 01 2013 Nikolay A. Fetisov <naf@altlinux.ru> 3.0900-alt1
- New version

* Tue Oct 18 2012 Nikolay A. Fetisov <naf@altlinux.ru> 3.0800-alt1
- New version

* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 3.0501-alt2.1
- repair after perl 5.12 upgrade using girar-nmu

* Tue Feb 24 2009 Nikolay A. Fetisov <naf@altlinux.ru> 3.0501-alt2
- Update BuildRequires

* Sat Feb 23 2008 Nikolay A. Fetisov <naf@altlinux.ru> 3.0501-alt1
- Initial build for ALT Linux Sisyphus

* Mon Feb 18 2008 Nikolay A. Fetisov <naf@altlinux.ru> 3.0501-alt0.1
- Initial build
